from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processador_imagem_virtual",
    version="0.0.5",
    author="Ubiratan Motta",
    author_email="mottaubiratan@gmail.com",
    description="Pacote de processamento de imagem usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ubiratan-motta/Processador_de_Imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
