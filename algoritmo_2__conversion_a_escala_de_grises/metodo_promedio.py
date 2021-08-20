# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Abrir imagen
img = cv2.imread('imagen.jpg')

#Separación y conversión de cada canal a escala de grises
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Metódo del promedio --> Y=(R+G+B)/3
img1 = (R*0.33 + G*0.33 + B*0.33)

# Conversión de tipo flotante a unit-8
img1 = img1.astype(np.uint8)

# Mostrar imagen original
cv2.imshow('Imagen original', img)

# Mostrar imagen con método del promedio
cv2.imshow('Imagen con metodo del promedio', img1)

# Mantener la ejecución del programa
cv2.waitKey(0)