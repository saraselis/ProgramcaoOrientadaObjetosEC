# -*- coding: utf-8 -*-
"""prova_poo_questao_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TLcj9eRkJ7sKyTosDs15mHKCPXQC3Hxj

# Primeria prova POO

> Importando bibliotecas
"""

import cmath

"""> Classes"""

class Numero:
    '''
        Essa classe instancia um numero complexo em forma retangular
        e realizar conversoes para polar, exponencial e retorna o teta do numero.
    '''
    
    def __init__(self, number:complex):
        self._number = number
    
    @property
    def number(self) -> complex:
        return self._number
    
    @number.setter
    def number(self, number_:complex) -> complex:
        self._number = number_
        return self._number

    def polar(self) -> complex:
        polar = cmath.polar(self._number)
        return polar
    
    def expo(self) -> complex:
        expo = cmath.exp(self._number)
        return expo
    
    def teta(self) -> complex:
        tetao = cmath.atan(self._number)
        return tetao
    
    def __str__(self):
        return f"O número complexo {self._number} foi instanciado!"

class CalculadoraComplexa:
    '''
       Essa classe realiza operacoes entre numeros complexos. 
    '''
    def __init__(self, resultados=0):
        self._resultados = resultados
        
    def somar(self, numero_1:Numero, numero_2:Numero) -> complex:
        '''
            Params
            -----
            numero_1: primeiro numero complexo das operacoes
            numero_2: segundo numero complexo das operacoes
            
            Return
            -----
            resultados: resultado da operacoes realizadas
        '''
        self._resultados = numero_1.number + numero_2.number
        return self._resultados
    
    def sub(self, numero_1:Numero, numero_2:Numero) -> complex:
        '''
            Params
            -----
            numero_1: primeiro numero complexo das operacoes
            numero_2: segundo numero complexo das operacoes
            
            Return
            -----
            resultados: resultado da operacoes realizadas
        '''
        self._resultados = numero_1.number - numero_2.number
        return self._resultados
    
    def multi(self, numero_1:Numero, numero_2:Numero) -> complex:
        '''
            Params
            -----
            numero_1: primeiro numero complexo das operacoes
            numero_2: segundo numero complexo das operacoes
            
            Return
            -----
            resultados: resultado da operacoes realizadas
        '''
        self._resultados = numero_1.number * numero_2.number
        return self._resultados
    
    def div(self, numero_1:Numero, numero_2:Numero) -> complex:
        '''
            Params
            -----
            numero_1: primeiro numero complexo das operacoes
            numero_2: segundo numero complexo das operacoes
            
            Return
            -----
            resultados: resultado da operacoes realizadas
        '''
        self._resultados = numero_1.number / numero_2.number
        return self._resultados

"""------"""

z1 = Numero(4+4j)

print(z1)

z1.polar()

z1.expo()

z1.teta()

"""------"""

z2 = Numero(1+2j)

print(z2)

z2.polar()

z2.expo()

z2.teta()

"""-----"""

calc = CalculadoraComplexa()

calc.somar(z1, z2)

calc.sub(z1, z2)

calc.multi(z1, z2)

calc.div(z1, z2)







