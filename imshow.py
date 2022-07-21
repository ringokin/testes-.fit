import cv2

altura = 256
largura = 256

arquivo = open("matriz saida.txt", "r")
matriz = []



aux = arquivo.readlines(2)
#aux.append(arquivo.readline(3)+arquivo.readline(4))
for j in range(2, largura):
		aux.append(arquivo.readline(j + 1))
matriz.append(aux)

for i in range(1, altura):
	aux = []
	for j in range(largura):
		aux.append(arquivo.readline(256*i + j + 1))
	matriz.append(aux)



#print(matriz)
#print(len(matriz))
#print(len(matriz[0]))
#x = input()
#for i in range(altura):
#	for j in range(largura):
#		matriz[i][j] = int(matriz[i][j])
#print(matriz)
#x = input()
imagem = cv2.imread('exemplo salt and pepper.jpg', cv2.IMREAD_GRAYSCALE)
#print("teste")
#x = input()
for i in range(altura):
	for j in range(largura):
		imagem[i][j] = matriz[i][j]


print("feito tbm")
#xx = input()
cv2.imshow('exemplo salt and pepper filtrado', imagem)
cv2.imwrite('exemplo salt and pepper filtrado.jpg',imagem)
cv2.waitKey()