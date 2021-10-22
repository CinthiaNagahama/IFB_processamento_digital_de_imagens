import getopt
import sys


def print_help():
    print("Uso:")
    print("\tdecode.py <comando> [valor]")
    print("Comandos:")
    print("\t-i, --imagem               Nome da imagem a ser decodificada. Deve estar no mesmo diretório que o programa")
    print("\t-m, --mensagem             Nome do arquivo .txt onde a mensagem será escrita")
    print("\t-b, --plano-bits           Plano de bits que foi alterado. 0 -> R, 1 -> G, 2 -> B, 3 -> RGB")
    print("\t-h, --help                 Ajuda. Gera essa tela")


def get_args(argv):
    image = ''
    text_file = ''
    bits_plan = 0
    try:
        opts, _ = getopt.getopt(argv, "he:s:m:b:", [
                                "help", "imagem=", "mensagem=", "plano-bits="])
    except getopt.GetoptError:
        raise SystemExit(print_help())
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--imagem"):
            image = arg
        elif opt in ("-m", "--mensagem"):
            text_file = arg
        elif opt in ("-b", "--plano-bits"):
            bits_plan = arg
    return [image, text_file, bits_plan]
