import numpy as np
import cv2


def get_image(image_name):
    image = cv2.imread(image_name)

    if(isinstance(image, np.ndarray)):
        return image
    raise FileNotFoundError("Imagem não encontrada")


def convert_to_binary(message):
    if type(message) == str:
        return ''.join([format(ord(letter), "08b") for letter in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Tipo de dado não aceito")


def convert_to_ascii(value):
    if type(value) == int:
        return chr(value)
    elif type(value) == str:
        return chr(int(value, 2))


def show_images(name1, image1, name2, image2):
    cv2.imshow(name1, image1)
    cv2.imshow(name2, image2)

    while cv2.getWindowProperty(name1, cv2.WND_PROP_VISIBLE) >= 1 and cv2.getWindowProperty(name2, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(50)
        if (keyCode & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break


def save_image(out_image_name, new_image):
    cv2.imwrite(out_image_name, new_image)
