import cv2
import numpy as np

# Abrir imagen
img = cv2.imread('imagen.jpg')

# Transformación de formato a escala de grises con el método cvtcolor (openCV)
img_b = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Mostrar imagen original
cv2.imshow('Imagen original', img)
# Mostramos imagen con canales RGB con el método cvtcolor (openCV)
cv2.imshow('Imagen con el metodo de cvtColor (openCV) en estandar BT.601', img_b)

# Mantener la ejecución del programa
cv2.waitKey(0)