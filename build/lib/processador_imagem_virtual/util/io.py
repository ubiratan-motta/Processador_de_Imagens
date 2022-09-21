from skimage.io import imread, imsave


def ler_imagem(path, is_gray=False):
    imagem = imread(path, as_gray = is_gray)
    return imagem


def salvar_imagem(imagem, path):
    imsave(path, imagem)
