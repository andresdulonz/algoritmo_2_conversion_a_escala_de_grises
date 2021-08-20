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

# Metódo del promedio ponderado estándar BT.601 --> Y=(0.229R+0.587G+0.114B)/3
img2 = (R*0.229 + G*0.587 + B*0.114)

# Método del promedio ponderado estándar BT.709 --> Y=(0.2126R+0.7152G+0.0722B)
img3 = (R*0.2126 + G*0.7152 + B*0.0722)

# Concatenación de los tres métodos
img0 = np.hstack((img1,img2, img3))

# la imagen resultante es tipo flotante, convertir a tipo uint-8
img_a = img0.astype(np.uint8)

# Transformación de formato a escala de grises con el método cvtcolor (openCV)
img_b = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Mostrar imagen original
cv2.imshow('Imagen original', img)
# Mostrar imagen con canales RGB concatenados
cv2.imshow('Imagen con metodos de promedio, estandar BT.601 y estandar BT.709', img_a)
# Mostramos imagen con canales RGB con el método cvtcolor (openCV)
cv2.imshow('Imagen con el metodo de cvtColor (openCV) en estandar BT.601', img_b)


# Mantener la ejecución del programa
cv2.waitKey(0)