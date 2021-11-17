import math
from cv2 import mean

from numpy import number
from utils import *
from quality_metrics import quality_metrics

if __name__ == "__main__":
    # 1- Utilizar a imagem da lena.jpg disponí­vel;
    og_image = get_image("lena.jpg", 0)

    # 2- Realizar operações aritméticas;
    # 3- Calcular histograma de cada operação aritmética;
    # 4- Plotar um gráfico para cada uma;
    # 5- Calcular métricas de qualidade (visto em sala) para cada imagem resultante;

    # soma 30
    # mod_image = cv2.add(og_image, (30, 0, 0, 0))
    # show_images("Original", og_image, "Soma 30", mod_image)
    # plot_histogram("Soma 30", mod_image)
    # print(quality_metrics(og_image, mod_image))

    # subtração 70
    # mod_image = cv2.subtract(og_image, (70, 0, 0, 0))
    # show_images("Original", og_image, "Subtrai 70", mod_image)
    # plot_histogram("Subtração 70", mod_image)
    # print(quality_metrics(og_image, mod_image))

    # multiplicação 1.2
    # mod_image = cv2.multiply(og_image, (1.2, 0, 0, 0))
    # show_images("Original", og_image, "Multiplica 1.2", mod_image)
    # plot_histogram("Multiplicação 1.2", mod_image)
    # print(quality_metrics(og_image, mod_image))

    # divisão 4
    # mod_image = cv2.divide(og_image, (4, 0, 0, 0))
    # show_images("Original", og_image, "Divide 4", mod_image)
    # plot_histogram("Divisão 4", mod_image)
    # print(quality_metrics(og_image, mod_image))

    # 6- Realizar redimensionamento piramidal por meio de média aritmética de janela 2x2 pixels (vide slides) para N/2, N/4 e N/8.
    def pyramid_resize(image: np.ndarray) -> np.ndarray:
        row, col = image.shape

        if row % 2 != 0:
            row -= 1

        if col % 2 != 0:
            col -= 1

        final_image = list()

        for x in range(0, row, 2):
            final_image_row = list()
            for y in range(0, col, 2):
                a = int(image[x][y])
                b = int(image[x + 1][y])
                c = int(image[x][y + 1])
                d = int(image[x + 1][y + 1])

                local_mean = (a + b + c + d) // 4
                if local_mean > 255:
                    local_mean = 255
                final_image_row.append(local_mean)
            final_image.append(final_image_row)

        return np.array(final_image, dtype="uint8")

    # n2_image = pyramid_resize(og_image)
    # n4_image = pyramid_resize(n2_image)
    # n8_image = pyramid_resize(n4_image)
    # show_images(["Original", "Redimensionamento Piramidal N/2", "Redimensionamento Piramidal N/4", "Redimensionamento Piramidal N/8"], [
    #             og_image, n2_image, n4_image, n8_image])

    # 7- Criar ruído gaussiano na lena;
    def gaussian_noise(image: np.ndarray, mean: float = 0, sigma: float = 2) -> np.ndarray:
        row, col = image.shape

        rng = np.random.default_rng()
        gauss = mean + sigma * rng.standard_normal(size=(row, col))
        gauss = np.array(gauss.reshape(row, col), dtype="uint8")
        noisy_image = np.add(image, np.abs(gauss))

        return noisy_image

    noisy_image = gaussian_noise(og_image, mean=0, sigma=5)
    cv2.imwrite("lena_com_ruido.jpg", noisy_image)

    # 8- Calcular entropia da lena original e lena com ruí­do;
    def entropy(image: np.ndarray) -> float:
        p = np.histogramdd(np.ravel(image), bins=256)[0]/image.size
        p = list(filter(lambda p: p > 0, np.ravel(p)))
        return -np.sum(np.multiply(p, np.log2(p)))

    print(f"Entropia da imagem original: {entropy(og_image)}")
    print(f"Entropia da imagem com ruído: {entropy(noisy_image)}")

    # 9- Achar diferença entre lena original e lena modificada, criando uma outra imagem binária (preto = 0 e branco = 255) em que branco estão os pixels diferentes entre as "lenas";
    def dif_binary_image(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
        res = np.zeros(image1.shape, dtype="uint8")

        for x, (line1, line2) in enumerate(zip(image1, image2)):
            for y, (pixel1, pixel2) in enumerate(zip(line1, line2)):
                res[x][y] = 255 if pixel1 == pixel2 else 0
        return res

    dif = dif_binary_image(og_image, noisy_image)
    cv2.imwrite("diferenca_lenas_ruido.jpg", dif)

    mod_image = cv2.imread("lena_modificada.jpg", 0)
    dif = dif_binary_image(og_image, mod_image)
    cv2.imwrite("diferenca_lenas_modificada.jpg", dif)

    # 10- Contar quantos objetos conexos existem na nova imagem utilizando vizinhança-4 e vizinhança-8;
    res = cv2.connectedComponentsWithStats(dif, 4, cv2.CV_32S)
    print(f"Quantidade de objetos conexos em vizinhança-4: {res[0]}")

    res = cv2.connectedComponentsWithStats(dif, 8, cv2.CV_32S)
    print(f"Quantidade de objetos conexos em vizinhança-8: {res[0]}")
