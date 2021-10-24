import sys
from command_line_arguments_encode import get_args, print_help
from utils import get_image, convert_to_binary, save_image

# Para teste, use:
# python3 encode.py -e butterfly.png -s butterfly_modificado.png -m secret_text.txt -b 0
# python3 encode.py -e stinkbug.png -s stinkbug_modificado.png -m secret_text.txt -b 0


def hide_message(image, bits_plan, message):
    max_size = image.shape[0] * image.shape[1]

    if (bits_plan < 3) & (len(message) > max_size):
        raise ValueError(
            "A mensagem é grande demais para o plando de bits escolhido")
    elif len(message) > (max_size * 3):
        raise ValueError("A mensagem é grande demais para a imagem escolhida")

    index = 0
    len_message = len(message)
    for values in image:
        for pixel in values:
            rgb = dict(zip(["0", "1", "2"], convert_to_binary(pixel)))

            if bits_plan < 3:
                pixel[bits_plan] = int(
                    rgb[str(bits_plan)][:-1] + message[index], 2)
                index += 1
            else:
                if index < len(message):
                    pixel[0] = int(rgb["0"][:-1] + message[index], 2)
                    index += 1
                if index < len(message):
                    pixel[1] = int(rgb["1"][:-1] + message[index], 2)
                    index += 1
                if index < len(message):
                    pixel[2] = int(rgb["2"][:-1] + message[index], 2)
                    index += 1

            if index >= len_message:
                return image


def encode():
    [og_image_name, text_file_name, bits_plan,
        out_image_name] = get_args(sys.argv[1:])

    og_image = get_image(og_image_name)

    with open(text_file_name) as f:
        message = convert_to_binary(f.read() + ";;;;;")

    new_image = hide_message(og_image, bits_plan, message)

    save_image(out_image_name, new_image)


if __name__ == "__main__":
    try:
        sys.argv[1]
        encode()
    except IndexError:
        raise SystemExit(print_help())
