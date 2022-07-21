import cv2

altura = 256
largura = 256

matriz = cv2.imread('exemplo salt and pepper.jpg', cv2.IMREAD_GRAYSCALE)


arquivo = open("matriz imagem.txt", "w")

for i in range(altura):
	for j in range(largura):
		arquivo.write(str(matriz[i][j]) + "\n")

print("feito")
x = input()
print("altura: "+str(matriz.len()) +"\nlargura: "+str(matriz[0].len()))
x = input()

#print(matriz)

#y = input()
#cv2.waitKey()