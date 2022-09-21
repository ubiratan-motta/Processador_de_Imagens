import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def encontrando_diferencas_dupla(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Specify 2 images with de same shape."
    imagem1_cinza = rgb2gray(imagem1)
    imagem2_cinza = rgb2gray(imagem2)
    (score, imagem_diferente) = structural_similarity(imagem1_cinza, imagem2_cinza, full=True)
    print("Similarity of the image: ", score)
    diferenca_imagem_normalizada = (imagem_diferente-np.min(imagem_diferente))/(np.max(imagem_diferente)-np.min(imagem_diferente))
    return diferenca_imagem_normalizada


def encontrando_diferencas_tripla(imagem1, imagem2, imagem3):
    assert imagem1.shape == imagem2.shape and imagem2.shape == imagem3.shape, "Specify 3 images with de same shape."
    imagem1_cinza = rgb2gray(imagem1)
    imagem2_cinza = rgb2gray(imagem2)
    imagem3_cinza = rgb2gray(imagem3)
    (score, imagem_diferente) = structural_similarity(imagem1_cinza, imagem2_cinza, imagem3_cinza, full=True)
    print("Similarity of the image: ", score)
    diferenca_imagem_normalizada = (imagem_diferente-np.min(imagem_diferente))/(np.max(imagem_diferente)-np.min(imagem_diferente))
    return diferenca_imagem_normalizada


def transferindo_histograma_dupla(imagem1, imagem2):
    imagem_correspondente = match_histograms(imagem1, imagem2, multichannel=True)
    return imagem_correspondente


def transferindo_histograma_tripla(imagem1, imagem2, imagem3):
    imagem_correspondente = match_histograms(imagem1, imagem2, imagem3, multichannel=True)
    return imagem_correspondente
