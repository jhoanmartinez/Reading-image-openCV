"""Using matplotlib to display images

matplotlib asume que la imagen esta en RGB, pero en
openCV la imagen esta en BGR, por eso se debe converitr
de BGR a RGB para leer en matplotlib

BGR to RGB ==> cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

El otro metodo consiste en voltear los ordenes de los canales
usando la maniulacion del array en matplotlib
img[:,:,::-1]
donde ::-1 en la ultima posicion es responsable por voltear
el orden de los canales
"""

import matplotlib.pyplot as plt
import cv2

img = cv2.imread("images/a_image.jpg")
plt.imshow(img, cmap="gray")
plt.show()
