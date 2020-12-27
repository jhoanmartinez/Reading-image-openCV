import numpy as np

# Pixeles son tipos enteros sin signos de 8 bits
#los cuales van de 0 a 255, los mismos valores
#de color en las imagenes
#np.uint8

a = np.zeros((5, 6))
print(a)
print(a.dtype)
print(a.shape)

print("numero de filas {}".format(a.shape[0]))
print("numero de columnas {}".format(a.shape[1]))

b = np.zeros((5,6), dtype=np.uint8)
print(b)
print(b.dtype)
print(a.shape)
print("numero de filas {}".format(b.shape[0]))
print("numero de columnas {}".format(a.shape[1]))

c = np.random.rand(5,6)
print(c)
print(c.dtype)
print(c.shape)
print("numero de filas (height) {}".format(c.shape[0]))
print("numero de columnas (width) {}".format(c.shape[1]))

d = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [12,13,14,15,16,17]
])
print(d)
print(d.shape)
print(d.dtype)
print("numero de filas {}".format(d.shape[0]))
print("numero de columnas {}".format(d.shape[1]))

"""
        Definir la ubicacion de los piexeles en la imagen
    centro de imagen es (W/2, H/2)

    para bordes HSV es mejor

"""
