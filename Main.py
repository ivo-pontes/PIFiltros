#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Filtros import Filtros

if __name__ == '__main__':
	print("Processamento de Imagens.")

	#filtros = Filtros("img/lena-gray.png")
	filtros = Filtros("img/sobel-fruits.png")
	filtros.carregarImagem()

	#filtros.filtroLaplaciano()
	filtros.filtroSobel()
			
	print("Fim execução!!")
