#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np

class Filtros():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []
		self.img = []

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 0)
		#Dimensão N
		self.n = np.size(self.matriz, 1)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)


	'''
	Interpolação Bilinear para Redução
	'''
	def filtroLaplaciano(self, op):
		saida = np.zeros([self.m,self.n], dtype=np.uint8)
		m1 = np.size(saida, 0)
		n1 = np.size(saida, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#Ternário em Python
		tamM = self.m-1 if self.m != 0 else self.m
		tamN = self.n-1 if self.n != 0 else self.n

		#Laplaciano

		if op == 1:
			#'''
			mascara = [[-1, -1, -1],
					  [-1, 8, -1],
					  [-1, -1, -1]]
			#'''
		elif op == 2:
			#'''
			mascara = [[1, 1, 1],
					  [1, -8, 1],
					  [1, 1, 1]]
			#'''
		elif op == 3:	
			#'''
			mascara = [[0, -1, 0],
					  [-1, 4, -1],
					  [0, -1, 0]]
			#'''
		elif op == 4:		
			#'''
			mascara = [[0, 1, 0],
					  [1, -4, 1],
					  [0, 1, 0]]
			#'''
		elif op == 5:	
			#Média
			#'''
			mascara = [[1, 1, 1],
					  [1, 1, 1],
					  [1, 1, 1]]		
			#'''


		#Tratando 
		for i in range(0,tamM):
			for j in range(0,tamN):
				if i != 0 and j != 0 and i != (tamM-1) and j != (tamN-1):
					#print(self.matriz[i][j], end='\t')
					saida[i][j] = int((self.matriz[i-1][j-1]*mascara[0][0] + self.matriz[i-1][j]*mascara[0][1] + self.matriz[i-1][j+1]*mascara[0][2] + \
					self.matriz[i][j-1]*mascara[1][0] + self.matriz[i][j]*mascara[1][1] + self.matriz[i][j+1]*mascara[1][2] + \
					self.matriz[i+1][j-1]*mascara[2][0] + self.matriz[i+1][j]*mascara[2][1] + self.matriz[i+1][j+1]*mascara[2][2])/9)

					if saida[i][j] < 0:
						saida[i][j] = 0

					#saida[i][j] = 255 - saida[i][j]


		for i in range(tamM):
			for j in range(tamN):
				print(saida[i][j], end='\t')
			print('')	

										
		print(saida)
		imagem = Image.fromarray(saida)		
		self.img.show()
		imagem.show()

	'''
	Aplicação do Filtro de Sobel
	'''
	def filtroSobel(self, op):
		saida = np.zeros([self.m,self.n], dtype=np.uint8)
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#Ternário em Python
		tamM = self.m-1 if self.m != 0 else self.m
		tamN = self.n-1 if self.n != 0 else self.n

		#Máscara #1
		if op == 6:
			#'''
			mascara = [[-1, -2, -1],
					  [0, 0, 0],
					  [1, 2, 1]]
			#'''
		elif op == 7:
			#Máscara #2
			#'''
			mascara = [[-1, 0, 1],
					  [-2, 0, 2],
					  [-1, 0, 1]]
			#'''

		#Tratando 
		for i in range(0,tamM):
			for j in range(0,tamN):
				if i != 0 and j != 0 and i != (tamM-1) and j != (tamN-1):
					#print(self.matriz[i][j], end='\t')
					saida[i][j] = int((self.matriz[i-1][j-1]*mascara[0][0] + self.matriz[i-1][j]*mascara[0][1] + self.matriz[i-1][j+1]*mascara[0][2] + \
					self.matriz[i][j-1]*mascara[1][0] + self.matriz[i][j]*mascara[1][1] + self.matriz[i][j+1]*mascara[1][2] + \
					self.matriz[i+1][j-1]*mascara[2][0] + self.matriz[i+1][j]*mascara[2][1] + self.matriz[i+1][j+1]*mascara[2][2])/9)

					if saida[i][j] < 0:
						saida[i][j] = 0

					saida[i][j] = 255 - saida[i][j]

		for i in range(tamM):
			for j in range(tamN):
				print(saida[i][j], end='\t')
			print('')	

										
		print(saida)
		imagem = Image.fromarray(saida)		
		self.img.show()
		imagem.show()
		