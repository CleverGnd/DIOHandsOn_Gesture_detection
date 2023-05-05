# DIO Hands On #1 – Criando um Sistema de Interpretação de Gestos com Python e Machine Learning
Este é um projeto de reconhecimento de gestos da mão em tempo real utilizando a biblioteca OpenCV e Python. O objetivo deste projeto é identificar gestos específicos da mão e associá-los a determinadas ações. Esse projeto foi desenvolvido durante o evento DIO Hands On, provido pela DIO em 19 de abr. de 2023.

O projeto é composto por dois arquivos principais:

- [hand_gesture_recognition.py](./hand_gesture_recognition.py): este arquivo contém a implementação do algoritmo de reconhecimento de gestos da mão.

- [main.py](./main.py): este arquivo contém o código principal para capturar imagens da câmera e processá-las com o algoritmo de reconhecimento de gestos.

Professor: [Diego Renan Bruno](https://github.com/diegobrunoDIO)

<a href="https://www.dio.me/"><img src="https://hermes.digitalinnovation.one/assets/diome/logo-full.svg" align="center" height="120" width="120" ></a> <br>

## Funcionamento
O programa utiliza a câmera do dispositivo para capturar imagens em tempo real. A imagem capturada é processada pelo algoritmo de reconhecimento de gestos, que identifica a região da mão na imagem e os gestos realizados. O programa exibe a imagem processada e o número do gesto identificado.

## Instalação

Para executar o projeto, é necessário ter Python e OpenCV instalados no sistema. Além disso, é necessário instalar as seguintes bibliotecas Python: numpy e math.

Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:
~~~python
pip install numpy math opencv-python
~~~

### Uso
Para executar o programa, execute o arquivo main.py no terminal:
~~~python
python main.py
~~~
O programa irá iniciar a captura da câmera e exibir a imagem processada em uma janela. Para encerrar o programa, pressione a tecla 'q'.

## Contribuição
Este é um projeto de código aberto. Sinta-se à vontade para contribuir com correções, melhorias e novas funcionalidades. Para contribuir, basta fazer um fork deste repositório, fazer as alterações desejadas e enviar um pull request.
## Agradecimentos
Agradecemos à DIO e a ao professor Diego Renan por disponibilizar o conteúdo do evento DIO Hands On e por fornecer o código inicial para este projeto.