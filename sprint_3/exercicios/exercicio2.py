"""
6. Considere as duas listas abaixo:
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), 
imprimindo a lista de valores da interseção na saída padrão.
Importante:  Esperamos que você utilize o construtor set() em seu código.
"""

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

a_set = set(a)
b_set = set(b)

intersec = a_set.intersection(b_set)

print(list(intersec))


"""
7. Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista = []

for i in a: 
    if i % 2 != 0:
        lista.append(i)

print(lista)


"""
8. Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou 
não um palíndromo.
Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
É necessário que você imprima no console exatamente assim:
A palavra: maça não é um palíndromo
A palavra: arara é um palíndromo
A palavra: audio não é um palíndromo
A palavra: radio não é um palíndromo
A palavra: radar é um palíndromo
A palavra: moto não é um palíndromo
"""

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

def inverter(palavra):
    return palavra[::-1]

def verificacao(palavra):
    invertido = inverter(palavra)

    if palavra == invertido:
        return "é um palíndromo"
    else:
        return "não é um palíndromo"

for palavras in lista: 
    verificado = verificacao(palavras)
    print(f"A palavra: {palavras} {verificado}")


"""
9. Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
Exemplo:
0 - João Soares está com 19 anos
"""

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(primeirosNomes):
    print(f"{i} - {nome} {sobreNomes[i]} está com {int(idades[i])} anos")


"""
10. Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
Utilize a lista a seguir para testar sua função. ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
"""

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

nova_lista = set(lista)

print(list(nova_lista))


"""
11. Escreva um programa para ler o conteúdo do arquivo texto arquivo_texto.txt e imprimir o seu conteúdo.
Dica: leia a documentação da função open(...) 
"""

with open('arquivo_texto.txt') as arquivo:
    print(arquivo.read())


"""
12. Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json.
"""

import json

with open('person.json') as arquivo:
    print(json.loads(arquivo.read()))


"""
13. Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo 
argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma 
nova lista.
Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 
para cada elemento.
"""

def my_map(list, f):
    return [f(i) for i in list]
    
def f(i):
    return i ** 2
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, f))


"""
14. Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de 
parâmetros nomeados e imprime o valor de cada parâmetro recebido.
Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
"""

def my_func(*args, **kwargs):
    for i in args:
        print(i)
    
    for k in kwargs:
        print(kwargs[k])

my_func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


"""
15. Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver
ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
liga(): muda o estado da lâmpada para ligada
desliga(): muda o estado da lâmpada para desligada
esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
Para testar sua classe:
Ligue a Lampada
Imprima: A lâmpada está ligada? True
Desligue a Lampada
Imprima: A lâmpada ainda está ligada? False
"""

class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada
    
    def esta_ligada(self):
        return self.ligada
        
    def liga(self):
        self.ligada = True
        print("A lâmpada está ligada? True")
        
    def desliga(self):
        self.ligada = False
        print("A lâmpada ainda está ligada? False")
            
lamp = Lampada()
lamp.liga()
lamp.desliga()


"""
16. Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
"""

def soma(string):
    numeros =  string.split(',')
    soma = 0
    for i in numeros:
        soma += int(i)
    print(soma)

string = "1,3,4,6,10,76"

soma(string)


"""
17. Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 
partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

def divisao(lista):
    tamanho = len(lista)//3

    lista1 = lista[:tamanho]
    lista2 = lista[tamanho:2*tamanho]
    lista3 = lista[2*tamanho:]
    
    print(lista1, lista2, lista3)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

divisao(lista)


"""
18. Dado o dicionário a seguir:
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
"""

def valores(speed):
    lista = []
    for i in speed.values(): 
        lista.append(i)
    print(list(set(lista)))


speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

valores(speed)


"""
19. Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
import random #amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)
Use as variáveis abaixo para representar cada operação matemática:
mediana
media
valor_minimo 
valor_maximo 
Importante: Esperamos que você utilize as funções abaixo em seu código:
random
max
min
sum
"""
import random

random_list = random.sample(range(500), 50)

def func_mediana(lista):
   ordenada = sorted(lista)
   tam_lista = len(ordenada)
   
   if tam_lista % 2 != 0:
       indice = (tam_lista//2)
       return ordenada[indice]
   else:
        indice = (tam_lista//2)
        soma = ordenada[indice] + ordenada[indice-1]
        return soma/2
    
mediana = func_mediana(random_list)
media = sum(random_list)/len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")


"""
20. Imprima a lista abaixo de trás para frente.
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a[::-1])
