import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from command_line_arguments import get_args, print_help


def encode():
    [og_image_name, text_file_name, bits_plan,
        out_image_name] = get_args(sys.argv[1:])

    file = open(text_file_name)
    og_image = mpimg.imread(og_image_name)

    file.close()
    return


if __name__ == "__main__":
    try:
        sys.argv[1]
        encode()
    except IndexError:
        raise SystemExit(print_help())
