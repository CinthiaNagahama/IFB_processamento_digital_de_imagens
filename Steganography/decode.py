import sys

import cv2
from command_line_arguments_decode import get_args, print_help
from utils import convert_to_binary, convert_to_ascii, get_image

# Para teste, use:
# python3 decode.py -i butterfly_modificado.png -a decodified_text.txt -b 0
# python3 decode.py -i stinkbug_modificado.png -a decodified_text.txt -b 0


def find_message(image, bits_plan):
    binary_data = ""

    if(bits_plan < 3):
        for values in image:
            for pixel in values:
                rgb = dict(zip(["0", "1", "2"], convert_to_binary(pixel)))

                binary_data += rgb[str(bits_plan)][-1]
    else:
        for values in image:
            for pixel in values:
                rgb = dict(zip(["0", "1", "2"], convert_to_binary(pixel)))

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

    return message[:-5]


def decode():
    [image_name, text_file_name, bits_plan] = get_args(sys.argv[1:])

    mod_image = get_image(image_name)
    mod_image = cv2.cvtColor(mod_image, cv2.COLOR_BGR2RGB)

    message = find_message(mod_image, bits_plan)

    with open(text_file_name, "w") as f:
        f.write(message)


if __name__ == "__main__":
    try:
        sys.argv[1]
        decode()
    except IndexError:
        raise SystemExit(print_help())
