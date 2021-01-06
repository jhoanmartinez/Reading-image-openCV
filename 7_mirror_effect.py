import numpy as np
import cv2
import matplotlib.pyplot as plt

"""3D plot """
from mpl_toolkits.mplot3d.axes3d import get_test_data
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

img = cv2.imread("images/b_lion.jpg")
# cv2.imshow("tesla", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""Imagen siempre esta en bgr """
print(img.shape)

""" covertir la imagen al espacio de color HSV """
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
plt.imshow(hsv_image[:, :, ::-1])
print(hsv_image.shape)
#plt.show()
print(hsv_image.shape)

"""Obtener el canal HUE """
hue, sat, val = cv2.split(hsv_image)
plt.imshow(val, cmap="gray")
#plt.show()
print(hsv_image.shape)

"""Obtener imagen a negativo"""
val = 255-val
plt.imshow(val, cmap="gray")
#plt.show()
print(hsv_image.shape)

""" combinar el valor val en si mismo"""
hsv_image = cv2.merge((val, val, val))
plt.imshow(hsv_image[:,:,::-1])
#plt.show()
print(hsv_image.shape)

"""girar la imagen de manera horizontal"""
hsv_image = hsv_image[:, ::-1, :]
plt.imshow(hsv_image)
#plt.show()

""" Pasar a RGB """
#img = (img[:,:,::-1])
# plt.imshow(img)
# plt.show()

"""Crear imagen vacia """
empty = np.zeros((407, 1280, 3), dtype=np.uint8)


""" añadir imagen original a la imagen vacia """
empty[:, 0:640, :] = img
empty[:, 640:1280, :] = hsv_image
plt.imshow(empty[:, :, ::-1])
plt.show()
print(empty.shape)

"""Escribir y guardar la imagen"""
cv2.imwrite("images/d_mirror.png", empty)
