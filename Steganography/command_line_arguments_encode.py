import getopt
import sys


def print_help():
    print("Uso:")
    print("\tencode.py <comando> [valor]")
    print("Comandos:")
    print("\t-e, --imagem-entrada       Nome da imagem de entrada. Deve estar no mesmo diretório que o programa")
    print("\t-s, --imagem-saida         Nome da imagem de saída")
    print("\t-m, --mensagem             Nome do arquivo .txt contendo a mensagem a ser escondida")
    print("\t-b, --plano-bits           Plano de bits a ser alterado. 0 -> R, 1 -> G, 2 -> B, 3 -> RGB")
    print("\t-h, --help                 Ajuda. Gera essa tela")


def get_args(argv):
    og_image = ''
    text_file = ''
    bits_plan = 0
    out_image = ''
    try:
        opts, _ = getopt.getopt(argv, "he:s:m:b:", [
                                "help", "imagem-entrada=", "imagem-saida=", "mensagem=", "plano-bits="])
    except getopt.GetoptError:
        raise SystemExit(print_help())
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-e", "--imagem-entrada"):
            og_image = arg
        elif opt in ("-s", "--imagem-saida"):
            out_image = arg
        elif opt in ("-m", "--mensagem"):
            text_file = arg
        elif opt in ("-b", "--plano-bits"):
            bits_plan = int(arg)
    # print(get_args)
    # print(og_image, text_file, bits_plan, out_image)
    return [og_image, text_file, bits_plan, out_image]
