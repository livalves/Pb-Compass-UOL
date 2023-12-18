with open('actors.csv') as arquivo:
    dict_ac_avg = {}
    
    for i, valor in enumerate(arquivo):
        colunas = valor.replace(', ', ' ').split(',')
        
        if i:
            dict_ac_avg.update({colunas[0]: float(colunas[3])})
 
    with open("etapa-3.txt", "w", encoding='utf-8') as etapa: 
        for chave, valor in dict_ac_avg.items():
            if valor == max(dict_ac_avg.values()):
                print(f"O ator/atriz com maior média de receita por filme é {chave}.", file=etapa)