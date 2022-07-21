import cv2
inport numpy as np
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
altura = 400
largura = 1800

image_file = get_pkg_data_filename('UIRAPURU_20220709_002000_59.fit')
image_data = fits.getdata(image_file, ext=0)

matriz = np.zeros((400, 1800, 3))

print("ok")
x = input()
for i in range(altura):
	for j in range(largura):
		print("ok")
		x = input()
		matriz[i][j] = [0, 0, image_data[i][j]]

print("ok")
x = input()

cv2.imshow('imagem base printada', image_data)
cv2.imwrite('imagem base printada.jpg',image_data)
cv2.waitKey()
