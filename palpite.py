#!/usr/bin/env python
# -*- coding: utf-8 - -*-

from res_anteriores import dados
import random
import math

def fo(palpite):
	""" Funcao responsavel por avaliar a qualidade de um palpite """
	resultados = [0,0,0,0,0,0]
	for i in dados:
		indice=len(palpite & i)
		if indice > 0:
			resultados[6-indice]+=1
	return resultados

def move(palpite):
	""" Funcao responsavel por gerar um palpite 'vizinho' do palpite atual """
	novo_palpite=[x for x in palpite]
	numero_antigo=numero=random.choice(novo_palpite)
	while numero in novo_palpite:
		numero_antigo=numero
		if random.random() > 0.5:	#sorteia se vai modificar a dezena ou a unidade
			#modifica a unidade
			r=int(random.random()*100)%9+1
			numero=numero-numero%10+(r+numero%10)%10
		else:
			#modifica a dezena
			r=int(random.random()*100)%5+1
			numero=numero%10+r*10
		if numero == 0:
			numero = 60
		elif numero > 60:
			numero%=60

	novo_palpite.remove(numero_antigo)
	novo_palpite.append(numero)
	return set(novo_palpite)

def solucao_inicial(n=6):
	""" funcao que gera um palpite qualquer """
	s=set()
	while len(s)<n:
		i=random.choice(range(60))+1
		while i in s:
			i=random.choice(range(60))+1
		s.add(i)
	return s
	
def sa(alfa,t,samax,s=solucao_inicial()):
	"""implementacao do simulated annealing para o problema de encontrar um bom palpite"""
	vfo=fo(s)
	s_star=s	
	vfo_star=vfo
	
	while t >= 1:		
		i=0
		while i < samax:
			i+=1
			s_=move(s)
			vfo_=fo(s_)
			#print s, vfo
			delta=vfo_-vfo			
			if(delta>0):	#se houve melhora
				s=s_
				vfo=vfo_
				if vfo > vfo_star:
					s_star=s
					vfo=vfo_star
			elif random.random()< math.exp(-delta/t):
				s=s_
				vfo=vfo_
		t*=alfa
	return s_star			
				
def bt(tam_busca,tam_lista,btmax,s=solucao_inicial()):
	""" implementacao da busca tabu para o problema problema de encontrar um bom palpite"""
	fo_s=fo(s)
	s_star=s
	fo_s_star=fo_s
	sem_melhora=0
	T=[0 for x in range(tam_lista)]
	while sem_melhora < btmax:
		sem_melhora+=1
		i=0
		melhor_vizinho=move(s)
		fo_melhor_vizinho=fo(melhor_vizinho)
		while i < tam_busca:
			i+=1
			s_=move(s)
			fo_s_=fo(s_)
			while ((s_-s) in T) and (fo_s_<fo_s_star):
				s_=move(s)
				fo_s_=fo(s_)
			if(fo_s_>fo_melhor_vizinho):
				melhor_vizinho=s_
				fo_melhor_vizinho=fo_s_
		T.pop(0)
		T.append(s-melhor_vizinho)		
		s=melhor_vizinho
		fo_s=fo_melhor_vizinho
		if fo_s > fo_s_star:
			fo_s_star = fo_s
			s_star = s
			sem_melhora=0
	return s_star

def pathrelinking(s1,s2):
	fo_alvo=fo(s2)
	fo_s1=fo(s1)
	if fo_s1 > fo_alvo: fo_alvo=fo_s1
	diferenca = s1-s2
	melhor=[]
	while (len(diferenca)>0):
		#tira um cara de s1		
		diferenca = s1-s2
	return melhor



if __name__ == "__main__":
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
	