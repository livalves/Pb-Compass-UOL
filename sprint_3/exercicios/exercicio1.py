"""
1. Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, 
imprima o ano em que a pessoa completará 100 anos de idade.
"""

from datetime import datetime 

nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))

ano_atual = datetime.now().year 
ano_nasc = ano_atual - idade
ano_futuro = ano_nasc + 100

print(ano_futuro)


""""
2. Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou 
ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para
cada número lido). Importante: Aplique a função range() em seu código.

Exemplos de saída:
Par: 2
Ímpar: 3
"""

numeros =  []

def verificacao(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

for i in range(3): 
    numeros.append(int(input(f"Informe o {i + 1}° número: ")))
      
for lista in numeros: 
    verificado = verificacao(lista)
    print(f"{verificado}: {lista}")


"""
3. Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).
Importante: Aplique a função range() em seu código.
"""

for i in range(21): 
    if i % 2 == 0:
        print(f"{i}")
   
        
"""
4. Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().
"""

for i in range(1, 101): 
    divisao = 0
    for count in range(1, i+1):
        if i % count == 0:
            divisao += 1
    if divisao == 2:
        print(f"{i}")
  
        
"""
5. Escreva um código Python que declara 3 variáveis:
dia, inicializada com valor 22
mes, inicializada com valor 10 e
ano, inicializada com valor 2022
Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.
"""

dia = 22
mes = 10
ano = 2022

print(f"{dia}/{mes}/{ano}")
