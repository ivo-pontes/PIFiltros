#!/usr/bin/env python3
# -*- coding: utf-8 -*

import numpy as np

if __name__ == '__main__':
	print("Processamento de Imagens.")

	#Questão #5
	m = [[0,0,0,0,0,0,0,0],
		[0,40,0,0,0,100,100,0],
		[0,40,0,100,100,0,50,0],
		[0,20,100,0,0,100,20,0],
		[0,20,20,80,0,0,0,0],
		[0,60,100,130,40,100,20,0],
		[0,100,130,30,130,120,120,0],
		[0,0,0,0,0,0,0,0]]

	n = np.zeros([8,8], dtype=int)

	mascara = [[-1, -1, -1],
			  [-1, 8, -1],
			  [-1, -1, -1]]
			
	#for i in range(len(m)):
	#	for j in range(len(m)):
	#		print(m[i][j], end='\t')
	#	print('')
		
	for i in range(len(m)):
		for j in range(len(m)):	
			if i != 0 and j != 0 and i != (len(m)-1) and j != (len(m)-1):
				#print(m[i][j], end='\t')
				n[i][j] = m[i-1][j-1]*mascara[0][0] + m[i-1][j]*mascara[0][1] + m[i-1][j+1]*mascara[0][2]
				n[i][j] += m[i][j-1]*mascara[1][0] + m[i][j]*mascara[1][1] + m[i][j+1]*mascara[1][2]
				n[i][j] += m[i+1][j-1]*mascara[2][0] + m[i+1][j]*mascara[2][1] + m[i+1][j+1]*mascara[2][2]
				n[i][j] = int(n[i][j]/9)
				if n[i][j] < 0:
					n[i][j] = 0
			#print('')
	
	for i in range(len(n)):
		for j in range(len(n)):
			print(n[i][j], end='\t')
		print('')
			
	print("Fim execução!!")

