<h1 align="center">
  Trabalho 1 - Estaganografia
</h1>

<br>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/CinthiaNagahama/processamento_digital_de_imagens">

  <a href=#>
    <img alt="Made by" src="https://img.shields.io/badge/made%20by-Cinthia%20Nagahama-gree">
  </a>
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/CinthiaNagahama/processamento_digital_de_imagens">
  
  <a href=#>
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CinthiaNagahama/processamento_digital_de_imagens">
  </a>
</p>

<p align="center">
  <a href="#about">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how_to">Como usar</a>
</p>

<br>

## 👨🏻‍💻 Sobre

<br>

<p style="text-align: justify">
  A técnica de esteganografia consiste em ocultar uma mensagem dentro de uma imagem. 
  Neste trabalho, a esteganografia deve alterar os bits da mensagem a ser oculta nos bits menos significativos de cada um dos três canais de cor da imagem. Dessa forma, cada pixel da imagem pode armazenar 3 bits de informação, tal que a imagem pode comportar três vezes o número de pixels que ela possui.
</p>

<br>

## 💻 Como usar

<br>

Antes de qualquer coisa, baixe os arquivos na sua máquina. Junto com os códigos estão: duas imagens .png e um arquivo de texto de teste.

<br>

### Codificando uma imagem:

<br>

Com uma imagem .png no mesmo diretório que o programa e uma mensagem secreta escrita em um arquivo .txt, rode em seu terminal:

```
  python3 encode.py -e <nome da imagem de entrada> -s <nome da imagem de saída> -m <arquivo com a mensagem secreta> -b <valor do plano de bits>
```

Obs. O plano de bits representa o canal de cor que será modificado, escolha: <br>

- 0 -> Vermelho
- 1 -> Verde
- 2 -> Azul
- 3 -> Todos os canais

<br>

### Decodificando uma imagem:

<br>

Com a imagem .png codificada no mesmo diretório, rode em seu terminal:

```
  python3 decode.py -i <nome da imagem de entrada> -a <nome do arquivo de saída> -b <valor do plano de bits>
```

Feito com 💜&nbsp;por Cinthia M. N. Ungefehr &nbsp;
