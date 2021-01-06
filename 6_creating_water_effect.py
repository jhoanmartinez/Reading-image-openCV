"""
1. Leer la imagen
2. Voltea rla imagen horizontal
3. Unir a la imagen original
4. Mostrar y guardar la imagen """

import cv2
import numpy as np
import matplotlib.pyplot as plt

""" Leer imagen """
img = cv2.imread("images/b_lion.jpg")

""" mostrar imagen """
#plt.imshow(img[:, :, ::-1])
#plt.show()

""" Ver la shape para ver que estamos viendo """
print(img.shape) #(filas, columnas, canales)

"""Se tiene que crear una imagen el doble de
filas (o columnas), pero el mismo numero de
columnas (width) y el mismo numero de canales
esto para agregar el espejo de la foto en la parte
inferior de la imagen original
"""

"""
    -Crear array con el tamaño doble
    -Height se convertira al doble
    -Width y channels estaran igual
"""

""" create image """
imgNew = np.zeros((814, 640, 3), dtype=np.uint8)

""" Display imagen """
#plt.imshow(imgNew[:, :, ::-1])
#plt.show()
print(imgNew.shape)

"""" Copiar la imagen original encima de la
    mitad de la imagen negra"""
imgNew[:407, :, :] = img

""" ver imagenes """
plt.imshow(imgNew[:, :, ::-1])
plt.show()
print(imgNew.shape)

"""" Voltear la imagen original
Invertir las filas de la imagen es voltearla
de forma horizontal
"""
imgInverted = img[::-1, :, :]
#plt.imshow(imgInverted[:, :, ::-1])
#plt.show()
print(imgInverted.shape)

"""
    Lo que resta hacer es copiar la imagen
    volteada a la imagen que no esta volteada
"""
imgNew[407:][:] = imgInverted
plt.imshow(imgNew[:, :, ::-1])
plt.show()
print(imgNew.shape)

"""guardar imagen """
#cv2.imwrite("images/c_Water effect.png",imgNew )
