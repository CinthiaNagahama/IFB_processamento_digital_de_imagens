import sys
import cv2
import numpy as np
from command_line_arguments_encode import get_args, print_help

# python3 encode.py -e butterfly.png -s butterfly_modificado.png -m secret_text.txt -b 0
# python3 encode.py -e stinkbug.png -s stinkbug_modificado.png -m secret_text.txt -b 0


def get_image(image_name):
    image = cv2.imread(image_name)

    if(image.all() != None):
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
        raise TypeError("Tipo de dados não aceito")


def hide_message(image, bits_plan, message):
    max_size = image.shape[0] * image.shape[1]

    if (bits_plan < 3) & (len(message) > max_size):
        raise ValueError(
            "A mensagem é grande demais para o plando de bits escolhido")
    elif len(message) > (max_size * 3):
        raise ValueError("A mensagem é grande demais para a imagem escolhida")

    index = 0
    for values in image[0]:
        for pixel in image[1]:
            rgb = dict(zip(["0", "1", "2"], convert_to_binary(pixel)))

            if(bits_plan < 3):
                pixel[bits_plan] = int(
                    rgb[str(bits_plan)][:-1] + message[index], 2)
                index += 1
            else:
                if(index < len(message)):
                    pixel[0] = int(rgb["0"][:-1] + message[index], 2)
                    index += 1
                if(index < len(message)):
                    pixel[1] = int(rgb["1"][:-1] + message[index], 2)
                    index += 1
                if(index < len(message)):
                    pixel[2] = int(rgb["2"][:-1] + message[index], 2)
                    index += 1

            if(index >= len(message)):
                break
    return image


def encode():
    [og_image_name, text_file_name, bits_plan,
        out_image_name] = get_args(sys.argv[1:])

    og_image = get_image(og_image_name)

    file = open(text_file_name)
    message = convert_to_binary(file.read() + ";;;;;")
    file.close()

    new_image = hide_message(og_image, bits_plan, message)

    cv2.imwrite(out_image_name, new_image)

    return


if __name__ == "__main__":
    try:
        sys.argv[1]
        encode()
    except IndexError:
        raise SystemExit(print_help())
