#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Filtros import Filtros

if __name__ == '__main__':
	print("Processamento de Imagens.")

	op = -1

	while op != 0:
		menuStr = "\n-------Menu-------\nFiltro Laplaciano:\n1 - Tipo #1\n2 - Tipo #2\n3 - Tipo #3\n4 - Tipo #4"
		menuStr += "\n5 - Filtro de Média:\nFiltro de Sobel:\n6 - Tipo Linhas\n7 - Tipo Colunas\n0 - Sair\n"

		op = input(menuStr)
		op = int(op)

		if op == 0:
			pass
		elif op < 6:
			filtros = Filtros("img/p.png")
			filtros.carregarImagem()
			filtros.filtroLaplaciano(op)
		else:
			filtros = Filtros("img/sobel-fruits.png")
			filtros.carregarImagem()
			filtros.filtroSobel(op)

			
	print("Fim execução!!")
