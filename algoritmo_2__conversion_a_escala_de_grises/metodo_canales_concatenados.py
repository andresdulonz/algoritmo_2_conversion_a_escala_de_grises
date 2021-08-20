# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Abrir imagen
img = cv2.imread('imagen.jpg')

#Separación y conversión de cada canal a escala de grises
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Concatenación de canales
img0 = np.hstack((R,G,B))

# Mostrar imagen original
cv2.imshow('Imagen original', img)

# Mostrar imagen con método del promedio
cv2.imshow('Imagen con canales concatenados', img0)

# Mantener la ejecución del programa
cv2.waitKey(0)