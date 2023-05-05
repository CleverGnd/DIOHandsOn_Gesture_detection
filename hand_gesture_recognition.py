import cv2
import numpy as np
import math

# Define os limites de cor da pele em HSV
LOWER_SKIN = np.array([0,20,70], dtype=np.uint8)
UPPER_SKIN = np.array([20,255,255], dtype=np.uint8)

# Define o tamanho da região de interesse (ROI) para análise da mão
ROI_SIZE = (200, 200)

def process_frame(frame):
    """
    Processa um frame de vídeo para identificar a mão e seus gestos.

    Args:
        frame: Um frame de vídeo capturado pela câmera.

    Returns:
        Um tuple contendo a imagem processada e o número do gesto identificado.
    """
    # Inverte o frame horizontalmente
    frame = cv2.flip(frame, 1)

    # Define a ROI para análise da mão
    roi = frame[100:100+ROI_SIZE[1], 100:100+ROI_SIZE[0]]

    # Aplica o filtro de cor para identificar a região da mão em HSV
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_SKIN, UPPER_SKIN)

    # Realiza operações morfológicas para melhorar a segmentação da mão
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=4)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    # Encontra o contorno da mão
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return frame, None
    cnt = max(contours, key=lambda x: cv2.contourArea(x))

    # Realiza aproximação do contorno da mão e cria um objeto convexo em torno dela
    epsilon = 0.0005 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    hull = cv2.convexHull(approx)

    # Calcula a razão entre a área do objeto convexo e a área da mão
    areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)
    arearatio = ((areahull - areacnt) / areacnt) * 100

    # Encontra os defeitos de convexidade da mão em relação ao objeto convexo
    hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, hull)

    # Verifica se foram encontrados defeitos de convexidade
    if defects is None:
        return frame, None

    # Identifica o número do gesto baseado nos defeitos de convexidade
    gesture = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(approx[s][0])
        end = tuple(approx[e][0])
        far = tuple(approx[f][0])

        # Calcula os comprimentos dos lados do triângulo formado pelos pontos
        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        s = (a + b + c) / 2
        ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Calcula a distância entre o ponto e o objeto convexo
        d = (2 * ar) / a

        # Calcula o ângulo entre os lados do triângulo
        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

        # Ignora ângulos > 90 e pontos muito próximos ao objeto convexo (ruído)
        if angle <= 90 and d > 30:
            gesture += 1
            cv2.circle(roi, far, 3, [255,0,0], -1)
        cv2.line(roi, start, end, [0,255,0], 2)

    # Identifica o gesto correspondente ao número de defeitos de convexidade
    if gesture == 0:
        if areacnt < 2000:
            text = 'Esperando dados'
        elif arearatio < 12:
            text = '0 = Navegador'
        elif arearatio < 17.5:
            text = ''
        else:
            text = '1 = Word'
        gesture_num = gesture
    elif gesture == 1:
        text = '2 = Excel'
        gesture_num = gesture
    elif gesture == 2 and arearatio < 27:
        text = '3 = Power Point'
        gesture_num = gesture
    elif gesture == 3:
        text = '4 = ????'
        gesture_num = gesture
    elif gesture == 4:
        text = '5 = Sair'
        gesture_num = gesture
    else:
        text = 'Esperando dados'
        gesture_num = None

    # Desenha a ROI e o texto com o número do gesto identificado
    cv2.rectangle(frame, (100, 100), (100+ROI_SIZE[0], 100+ROI_SIZE[1]), (0, 255, 0), 2)
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return frame, gesture_num