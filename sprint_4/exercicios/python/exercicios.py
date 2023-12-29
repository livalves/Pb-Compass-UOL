"""
1- Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício: map, filter, sorted e sum.
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
- a lista dos 5 maiores números pares em ordem decrescente;
- a soma destes valores.
"""

with open('number.txt') as arquivo:
    numeros = list(map(int, arquivo.readlines()))
    
    numeros_pares = list(filter(lambda n: n % 2 == 0, numeros))
    cinco_maiores = list(reversed(sorted(numeros_pares)[-5:]))
    
    print(cinco_maiores)
    print(sum(cinco_maiores))
  
    
"""
2- Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada 
será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções: len, filter e lambda.
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
"""
def conta_vogais(texto:str)-> int:  
    selec_vogais = lambda t: t.lower() in 'aeiou'
    qtde_vogais = list(filter(selec_vogais, texto))

    return len(qtde_vogais)


"""
3- A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools) e map.
"""

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    creditos = reduce(lambda x, y: x+y, map(lambda l: l[0] if l[1] == 'C' else 0, lancamentos))
    debitos = reduce(lambda x, y: x+y, map(lambda l: l[0] if l[1] == 'D' else 0, lancamentos))
    
    return float(creditos-debitos)


"""
4- A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. 
Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas 
(+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar 
cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
Na resolução da atividade você deverá aplicar as seguintes funções: max, zip e map.
"""

def calcular_valor_maximo(operadores,operandos) -> float:
    lista = list(zip(operadores, operandos))
    
    def calculo(op, num):
        dict_operadores = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '%': lambda x, y: x%y
        }
        calculando = dict_operadores.get(op, lambda x, y: 0)
        return calculando(*num)

    calculos_totais = list(map(lambda l: calculo(l[0], l[1]), lista)) 

    return max(calculos_totais)


"""
5- Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo 
corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
É o arquivo estudantes.csv do exercício.
Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo 
as seguintes informações: Nome do estudante, três maiores notas, em ordem decrescente e média das três maiores notas, 
com duas casas decimais de precisão. O resultado do processamento deve ser escrito na saída padrão 
(print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções: round, map e sorted.
"""

with open('estudantes.csv', encoding='utf8') as arquivo:
    in_dados = {
        colunas[0]: list(map(int, colunas[1:]))
        for valor in arquivo
            if (colunas := valor.replace('"', '').split(','))
    }
    
    estudantes = dict(sorted(in_dados.items()))
    
    def calculos(notas):
        maiores_notas = sorted(notas, reverse=True)[:3]
        media_notas = round(sum(maiores_notas)/3, 2)
        return maiores_notas, media_notas

    for aluno, notas in estudantes.items(): 
        maiores_notas, media_notas = calculos(notas)
        print(f"Nome: {aluno} Notas: {maiores_notas} Média: {media_notas}")
        
