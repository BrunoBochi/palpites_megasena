#!/usr/bin/python
from res_anteriores import dados
from palpite import *
import random

random.seed()
#s=set([2, 4, 16, 21, 32, 37, 43, 57, 58])
#s=set([14, 23, 24, 25, 26, 27, 41, 51, 53])
#s=set([11, 13, 21, 33, 38, 39, 45, 54, 57])
#s=set([2, 4, 16, 21, 37, 43, 55, 57, 58])
#s=set([2, 16, 21, 32, 37, 43, 52, 57, 58])
#s=set([4, 12, 13, 14, 30, 42, 47, 49, 59])

qtde=50
tam_palpite=6
tam_busca=50
tam_lista=27
btmax=4*tam_lista
resultados=[]

for i in range(qtde):
	s=solucao_inicial(tam_palpite)
	s=bt(tam_busca=tam_busca,tam_lista=tam_lista,btmax=btmax,s=s)
	resultados.append(s)
	
resultados.sort()

for i in resultados:
	s_sorted=[x for x in i]	
	s_sorted.sort()
	print s_sorted, fo(i)

#s=bt(tam_busca=tam_busca,tam_lista=tam_lista,btmax=btmax,s=s)
#s=sa(0.95, 100.0, 200,s)
