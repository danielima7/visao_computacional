
# Como abrir camera com o Open CV e Python
import cv2 # pip install cv2

# Inicializa captura de video
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) - Usado caso a camera de erro
# cap = cv2.VideoCapture("https://concer.com.br/cameras/proximidade-viaduto-bonsucesso-ii.aspx") 

# Condição 1
if not cap.isOpened():
    print("Câmera não abriu!")
    exit()

# Loop para manter a camera operando
while True:
    ret, frame = cap.read() # Captura a imagem da camera por frames

    if not ret:
        print("Não tem frame!")
        break

    windowName = cv2.imshow("Robson", frame) # Nomeando a janela
    
    k = cv2.waitKey(1) # Variavel para condição de parada.

    if k == ord("q"): # Pressione 'q' para sair.
        break
