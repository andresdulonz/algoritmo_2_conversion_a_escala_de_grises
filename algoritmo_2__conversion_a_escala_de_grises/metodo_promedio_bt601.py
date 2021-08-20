# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Abrir imagen
img = cv2.imread('imagen.jpg')

#Separación y conversión de cada canal a escala de grises
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Metódo del promedio ponderado estándar BT.601 --> Y=(0.229R+0.587G+0.114B)/3
img2 = (R*0.229 + G*0.587 + B*0.114)

# Conversión de tipo flotante a unit-8
img2 = img2.astype(np.uint8)

# Mostrar imagen original
cv2.imshow('Imagen original', img)

# Mostrar imagen con método del promedio ponderado BT.601
cv2.imshow('Imagen con metodo del promedio ponderado estandar BT.601', img2)

# Mantener la ejecución del programa
cv2.waitKey(0)