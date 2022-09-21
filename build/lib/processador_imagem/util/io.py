from email.mime import image
from skimage.io import imread, imsave


def ler_imagem(path, cinza=False):
    imagem = imread(path, cinza=cinza)
    return imagem


def salvar_imagem(imagem, path):
    imsave(path, imagem)
