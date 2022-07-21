import cv2
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

image_file = get_pkg_data_filename('UIRAPURU_20220709_002000_59.fit')
image_data = fits.getdata(image_file, ext=0)

cv2.imshow('imagem base printada', image_data)
cv2.imwrite('imagem base printada.jpg',image_data)
cv2.waitKey()
