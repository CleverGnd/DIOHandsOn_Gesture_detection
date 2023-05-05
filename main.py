import cv2
from hand_gesture_recognition import process_frame

# Inicia a captura de vídeo da câmera padrão
cap = cv2.VideoCapture(0)

# Verifica se a captura de vídeo foi iniciada corretamente
if not cap.isOpened():
    print('Erro ao abrir a câmera')
    exit()

while True:
    # Lê um frame do vídeo
    ret, frame = cap.read()

    # Verifica se o frame foi lido corretamente
    if not ret:
        break

    # Processa o frame com a função process_frame
    processed_frame, gesture_num = process_frame(frame)

    # Exibe a imagem processada
    cv2.imshow('Hand Gesture Recognition', processed_frame)

    # Verifica se a tecla 'q' foi pressionada para encerrar o programa
    if cv2.waitKey(1) == ord('q'):
        break

# Libera a câmera e fecha as janelas abertas
cap.release()
cv2.destroyAllWindows()