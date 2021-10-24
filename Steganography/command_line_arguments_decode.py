import getopt


def print_help():
    print("Uso:")
    print("\tdecode.py <comando> [valor]")
    print("Comandos:")
    print("\t-i, --imagem               Nome da imagem a ser decodificada. Deve estar no mesmo diretório que o programa")
    print("\t-a, --arquivo              Nome do arquivo .txt onde a mensagem será escrita")
    print("\t-b, --plano-bits           Plano de bits que foi alterado. 0 -> R, 1 -> G, 2 -> B, 3 -> RGB")
    print("\t-h, --help                 Ajuda. Gera essa tela")


def get_args(argv):
    image = ''
    text_file = ''
    bits_plan = ''

    try:
        opts, _ = getopt.getopt(argv, "he:i:a:b:", [
                                "help", "imagem=", "arquivo=", "plano-bits="])
    except getopt.GetoptError:
        raise SystemExit(print_help())

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise SystemExit(print_help())
        elif opt in ("-i", "--imagem"):
            image = arg
        elif opt in ("-a", "--arquivo"):
            text_file = arg
        elif opt in ("-b", "--plano-bits"):
            bits_plan = int(arg)

    # print([image, text_file, bits_plan])
    return [image, text_file, bits_plan]
