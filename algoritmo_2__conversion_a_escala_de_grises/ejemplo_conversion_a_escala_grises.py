# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Abrir imagen
im= cv2.imread('imagen.jpg')

# Separar los canales rojo, verde y azul (RGB)
# ---------------------------------------------------------------------
    # Mostrar el canal rojo
    # im[:,:,0]= 0
    # Mostrar el canal verde
    # im[:,:,1]= 0
    # Mostrar el canal azul
    # im[:,:,2]= 0
    # Mostramos imagen
    # cv2.imshow('imagen', im)

# Convertir a escala de grises en un canal
# ---------------------------------------------------------------------
    # R = im[:,:,2]
    # G = im[:,:,1]
    # B = im[:,:,0]
    # Mostramos imagen con un solo canal
    # cv2.imshow('imagen', R)

# Convertir a escala de grises en canales concatenados
# ---------------------------------------------------------------------
    # R = im[:,:,2]
    # G = im[:,:,1]
    # B = im[:,:,0]
    # Concatenación de canales
    # ig = np.hstack((R,G,B))
    # Mostrar imagen original
    # cv2.imshow('imagen0', im)
    # Mostramos imagen con canales RGB concatenados
    # cv2.imshow('imagen', ig)

# Convertir a escala de grises por métodos de promedio
# ---------------------------------------------------------------------
    # R = im[:,:,2]
    # G = im[:,:,1]
    # B = im[:,:,0]
    # Metódo del promedio --> Y=(R+G+B)/3
    # ig1 = (R*0.33 + G*0.33 + B*0.33)
    # Metódo del promedio ponderado estándar BT.601 --> Y=(0.229R+0.587G+0.114B)/3
    # ig2 = (R*0.229 + G*0.587 + B*0.114)
    # Método del promedio ponderado estándar BT.709 --> Y=(0.2126R+0.7152G+0.0722B)
    # ig3 = (R*0.2126 + G*0.7152 + B*0.0722)
    # Concatenación de los tres métodos
    # ig = np.hstack((ig1, ig2, ig3))
    # la imagen resultante es tipo flotante, convertir a tipo uint-8
    # ig = ig.astype(np.uint8)
    # Mostrar imagen original
    # cv2.imshow('Imagen original', im)
    # Mostramos imagen con canales RGB concatenados
    # cv2.imshow('Imagen con metodos de promedio, estandar BT.601 y estandar BT.709', ig)

# Convertir a escala de grises por el método cvtcolor (openCV)
# ---------------------------------------------------------------------
# argumento (im), transformación a modo de color (COLOR_BGR2GRA)
ig = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# Mostrar imagen original
cv2.imshow('Imagen original', im)
# Mostramos imagen con canales RGB con el método cvtcolor (openCV)
cv2.imshow('Imagen con el metodo de cvtColor (openCV) en estandar BT.601', ig)



# Extendemos la ejecución del programa
cv2.waitKey(0)