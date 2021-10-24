import sys
import cv2
import numpy as np
from command_line_arguments_decode import get_args, print_help

# Para teste, use:
# python3 decode.py -i butterfly_modificado.png -a decodified_text.txt -b 0
# python3 decode.py -i stinkbug_modificado.png -a decodified_text.txt -b 0


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
    return chr(int(value, 2))


def find_message(image, bits_plan):
    binary_data = ""

    for values in image:
        for pixel in values:
            rgb = dict(zip(["0", "1", "2"], convert_to_binary(pixel)))

            if(bits_plan < 3):
                binary_data += rgb[str(bits_plan)][-1]
            else:
                binary_data += rgb["0"][-1]
                binary_data += rgb["1"][-1]
                binary_data += rgb["2"][-1]

    binary_data = [binary_data[i: i + 8]
                   for i in range(0, len(binary_data), 8)]

    message = ""
    for word in binary_data:
        message += convert_to_ascii(word)
        if(message[-5:] == ";;;;;"):
            break

    print(message[0:5])

    return message[:-5]


def decode():
    [image_name, text_file_name, bits_plan] = get_args(sys.argv[1:])

    mod_image = get_image(image_name)

    message = find_message(mod_image, bits_plan)
    print("final message: " + message)

    with open(text_file_name, "w") as f:
        f.write(message)

    return


if __name__ == "__main__":
    try:
        sys.argv[1]
        decode()
    except IndexError:
        raise SystemExit(print_help())
