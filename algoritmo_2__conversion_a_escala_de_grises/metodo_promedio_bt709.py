# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Abrir imagen
img = cv2.imread('imagen.jpg')

#Separación y conversión de cada canal a escala de grises
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Método del promedio ponderado estándar BT.709 --> Y=(0.2126R+0.7152G+0.0722B)
img3 = (R*0.2126 + G*0.7152 + B*0.0722)

# Conversión de tipo flotante a unit-8
img3 = img3.astype(np.uint8)

# Mostrar imagen original
cv2.imshow('Imagen original', img)

# Mostrar imagen con método del promedio ponderado BT.709
cv2.imshow('Imagen con metodo del promedio ponderado estandar BT.709', img3)

# Mantener la ejecución del programa
cv2.waitKey(0)