import math

from numpy import number
from utils import *
from quality_mertics import quality_metrics

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

        return np.array(final_image, dtype=np.uint8)

    # n2_image = pyramid_resize(og_image)
    # n4_image = pyramid_resize(n2_image)
    # n8_image = pyramid_resize(n4_image)
    # show_images(["Original", "Redimensionamento Piramidal N/2", "Redimensionamento Piramidal N/4", "Redimensionamento Piramidal N/8"], [
    #             og_image, n2_image, n4_image, n8_image])

    # 7- Criar ruído gaussiano na lena;
    def gaussian_noise(image: np.ndarray, mean: float = 0) -> np.ndarray:
        row, col = image.shape
        sigma = 0.1

        rng = np.random.default_rng()
        gauss = mean + sigma * rng.standard_normal(size=(row, col))
        gauss = gauss.reshape(row, col)
        noisy_image = np.add(image, gauss)

        return noisy_image

    noisy_image = gaussian_noise(og_image)
    noisy_image = cv2.convertScaleAbs(noisy_image)
    show_images(["Original", "Gaussian Noise"], [og_image, noisy_image])

    # 8- Calcular entropia da lena original e lena com ruí­do;
    def entropy(image: np.ndarray) -> float:
        pass

    # 9- Achar diferença entre lena original e lena modificada, criando uma outra imagem binária (preto = 0 e branco = 255) em que branco estão os pixels diferentes entre as "lenas";
    # 10- Contar quantos objetos conexos existem na nova imagem utilizando vizinhança-4 e vizinhança-8;
