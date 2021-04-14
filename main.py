import cv2
import datetime

# La webcam se abre
webcam = cv2.VideoCapture(0)

# La ruta mas el nombre, que es la fecha
fecha =  datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
ruta = f"K:/Capturas/{fecha}.avi"

# Cantidad de fotogramas empleados
fps = 30.0

# La salida de la webcam en forma de video, blanco y negro
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
salida = cv2.VideoWriter(ruta, fourcc, fps, (int(webcam.get(3)), int(webcam.get(4))), False)

# Primer frame sobre el que compara si hay movimiento
success, primerFrame = webcam.read()

# Adaptamos la imagen con la escala de grises y el efecto borroso
primerFrame = cv2.cvtColor(primerFrame, cv2.COLOR_BGR2GRAY)
primerFrame = cv2.GaussianBlur(primerFrame, (21, 21), 0)

# Cantidad de pixeles de area aceptada
area_pixeles = 1.0

while True:
    # Si entran frames de la webcam seguir leyendo
    success, imagen = webcam.read()

    # Convierto el frame actual a un frame gris
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Ahora hacemos borrosa la imagen para que sea mas facil detectar el movimiento
    imagenBorrosa = cv2.GaussianBlur(imagenGris, (21, 21), 0)

    # Comparamos la imagen mediante el algoritmo absdiff y creamos una imagen de pixeles blancos y negros
    imagenComparacion = cv2.absdiff(primerFrame, imagenBorrosa)

    # En una imagen pasada a grises se busca los pixeles más intensos
    pixelesIntensos = cv2.threshold(imagenComparacion, 30, 255, cv2.THRESH_BINARY)[1]
    pixelesIntensos = cv2.dilate(pixelesIntensos, None, iterations=2)

    # Buscamos ahora los bordes
    bordes, _ = cv2.findContours(pixelesIntensos.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Mostrar en una ventana la salida
    cv2.imshow("Webcam Borrosa", imagenGris)
    cv2.imshow("Imagen Borrosa", imagenBorrosa)
    cv2.imshow("Pixeles intensos", pixelesIntensos)

    # Recorremos todas las areas y miramos si superan cierta area mínima
    for borde in bordes:
        if cv2.contourArea(borde) < 100:      # Si el area tiene mas de x píxeles entonces...
            # Se guarda la imagen si el area minima se cumple
            salida.write(imagenGris)
            print("Movimiento detectado")

    # Cuando pulsemos 'q' se terminara el bucle.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
