# -*- coding: utf-8 -*-
"""FilaCircular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLLrHAw4aEMuQq3nPaAIXXuo7-vRgJ-8

# Implemtacao Fila Circular
## P2 - POO

Tratamento de excecao para lista vazia
"""

class EmptyLinkedList(Exception):
    def __init__(self):
        super().__init__('Lista vazia para de burrice')

"""Classe aluno que será Inserido na Fila"""

class Aluno:
    def __init__(self, nome: str, nota: float):
        self._nome = nome
        self._nota = nota
        self._prox = None

    def __repr__(self):
        '''Representacao do aluno'''
        return f'{self._nome}:{self._nota}'

    def __lt__(self, outro_aluno):
        return self._nota < outro_aluno._nota
    
    def __gt__(self, outro_aluno):
        return self._nota > outro_aluno._nota

    @property
    def prox(self):
        return self._prox
    
    @prox.setter
    def prox(self, prox):
        self._prox = prox
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
        
    @property
    def nota(self) -> str:
        return self._nota
    
    @nota.setter
    def nota(self, nota:float):
        self._nota = nota

class No:
    def __init__(self, aluno=None, prox = None):
        self.aluno = aluno
        self.prox = prox

"""Implementacao da Fila Circular"""

class Circular:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        
    def show_fila(self):
        '''Printa a fila'''
        # primeiro nó
        atual = self.inicio
        
        # o tamanho maximo que nosso nó deverá ir
        while atual.prox:
            print(atual.aluno)
            atual = atual.prox
            
            # finaliza o percorrimento
            if atual == self.inicio:
                break
    
    def insere_fim(self, aluno:Aluno):
        '''Insere um aluno ao fim da Fila'''
        novo_aluno = No(aluno)
        
        # se a lista estiver vazia
        if self.inicio == None:
            self.inicio = novo_aluno
            self.inicio.prox = novo_aluno
            self.fim = novo_aluno
            
            return 
        
        # se a lista não estiver vazia
        if self.fim != None:
            self.fim.prox = novo_aluno
            novo_aluno.prox = self.inicio
            self.fim = novo_aluno
            return 
        
    def insere_inicio(self, aluno:Aluno):
        '''Insere um aluno no inicio da fila'''
        novo_aluno = No(aluno)
        novo_aluno.prox = self.inicio
        atual = self.inicio
        
        # lista vazia
        if atual == None:
            self.inicio = novo_aluno
            self.fim = novo_aluno
            self.inicio.prox = novo_aluno
            return
        
        # lista não está vazia
        if self.fim != None:
            self.fim.prox = novo_aluno
            novo_aluno.prox = self.inicio
            self.inicio = novo_aluno
            return
    
    def insere_mei(self, ref_aluno, aluno:Aluno):
        '''Insere no meio a partir de uma posicao estipulada'''
        # verifica vazia
        if ref_aluno == None:
            raise EmptyLinkedList
            
        # se o nó é igual ao ultimo, usar a funcao de inserir no final
        if ref_aluno == self.fim:
            self.insere_fim(aluno)
            
        # inserindo na posicao desejada
        novo_aluno = No(aluno)
        ref_prox = ref_aluno.prox
        ref_aluno.prox = novo_aluno
        novo_aluno.prox = ref_prox
        
    def deleta_inicio(self):
        '''Deleta o Aluno ao inicio da Fila'''
        # se tiver algo na lista 
        if self.inicio != None:
            # Pegar o prox elemento 
            temp = self.inicio.prox
            
            self.fim.prox = temp
            
            # setar o inicio
            self.inicio = temp

        else:
            raise EmptyLinkedList
      
    def deleta_fim(self):
        '''Deleta o aluno ao fim da Fila'''
        # se tiver algo na lista 
        if self.inicio != None:
            atual = self.inicio
            
           #percorre até o nó, verifica se os proximos nós são diferentes do inicial
            while atual.prox.prox != self.inicio:
                atual = atual.prox
                
            # pegando o final
            self.fim = atual
            
            # recupera o ultimo nó
            atual.prox = self.inicio
            
        else:
            raise EmptyLinkedList
    
    def deleta_mei(self, posi):
        '''Deleta o aluno no meio da lista a partir de uma posicao estipulada'''
        # if position is 0 e vamos deletar o primeo
        print(f"Posicao escolhida: {posi}")
        if posi == 0:
            print("entrei aq")
            self.deleta_inicio()
            return
        
        if posi == self.len_fila() - 1:
            
            self.deleta_fim()
            return 
        
        if posi >= self.len_fila() -1 :
            print(f"Tamanho da fila: {self.len_fila()}")  
            posi = posi % (self.len_fila() -1)
            
        # pegando o novo primeiro nó
        atual = self.inicio.prox
        
        # percorrendo até aposicao
        cont = 0
        
        while cont <= posi:
            cont = cont + 1
            atual = atual.prox

        atual.prox = atual.prox.prox
        
    def len_fila(self):
        '''Pega o tamanho da fila'''
        # pega o primeiro nó
        atual = self.inicio
        cont =0
        
        while atual.prox:
            cont += 1
            #percorre até o nó novamente
            atual = atual.prox

            #encerra o loop pois chegamos ao primeiro nó
            if atual == self.inicio:
                break
        return cont
    
    def __str__(self):
        return "Lista circular referenciada com sucesso"

lista_circular = Circular()
print(lista_circular)

print("Inserindo alunos")
lista_circular.insere_fim(Aluno('Sara', 9.8))
lista_circular.insere_fim(Aluno('Lucas', 7.8))
lista_circular.insere_inicio(Aluno('Sabrina', 8.8))

lista_circular.show_fila()

print("Inserindo aluno no meio")
first_node = lista_circular.inicio
lista_circular.insere_mei(first_node, Aluno('Olaf', 2.0))

lista_circular.show_fila()

print("Deletando no inicio")
lista_circular.deleta_inicio()

lista_circular.show_fila()

print("Deletando no final")
lista_circular.deleta_fim()

lista_circular.show_fila()

print("Deletando no meio a partir de uma posicao")
lista_circular.deleta_mei(7)

lista_circular.show_fila()

