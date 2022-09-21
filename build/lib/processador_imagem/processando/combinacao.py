import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrando_diferencas(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Specify 2 images with de same shape."
    imagem1_cinza = rgb2gray(imagem1)
    imagem2_cinza = rgb2gray(imagem2)
    (score, imagem_diferente) = structural_similarity(imagem1_cinza, imagem2_cinza, full=True)
    print("Similarity of the image: ", score)
    diferenca_imagem_normalizada = (imagem_diferente-np.min(imagem_diferente)) /\
                                  (np.max(imagem_diferente)-np.min(imagem_diferente))
    return diferenca_imagem_normalizada


def transferindo_histograma(imagem1, imagem2):
    imagem_correspondente = match_histograms(imagem1, imagem2, multichannel=True)
    return imagem_correspondente
