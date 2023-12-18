with open('actors.csv') as arquivo:
    dict_ac_num = {}
    
    for i, valor in enumerate(arquivo):
        colunas = valor.replace(', ', ' ').split(',')
        
        if i:
            dict_ac_num.update({colunas[0]: int(colunas[2])})

    with open("etapa-1.txt", "w", encoding='utf-8') as etapa:   
        for chave, valor in dict_ac_num.items():
            if valor == max(dict_ac_num.values()):
                print(f"O ator/atriz com maior número de filmes é {chave} com {valor} filmes.", file=etapa)