from typing import List
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_image(name: str, flag: np.number = 1) -> np.ndarray:
    image = cv2.imread(name, flag)

    if(isinstance(image, np.ndarray)):
        return image
    raise FileNotFoundError("Imagem não encontrada")


def show_image(name: str, image: np.ndarray) -> None:
    cv2.imshow(name, image)
    while cv2.getWindowProperty(name, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(50)
        if (keyCode & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break


def show_images(names: List[str], images: List[np.ndarray]) -> None:
    is_window_visible = list()
    for name, image in zip(names, images):
        cv2.imshow(name, image)
        is_window_visible.append(cv2.getWindowProperty(
            name, cv2.WND_PROP_VISIBLE))

    while 0 not in is_window_visible:
        keyCode = cv2.waitKey(50)
        if (keyCode & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break

        for i, name in enumerate(names):
            is_window_visible[i] = cv2.getWindowProperty(
                name, cv2.WND_PROP_VISIBLE)


def plot_histogram(name: str, image: np.ndarray) -> None:
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.grid(True)
    plt.title(name)
    plt.show()
