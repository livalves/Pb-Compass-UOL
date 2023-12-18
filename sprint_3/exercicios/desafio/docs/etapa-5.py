with open('actors.csv') as arquivo:
    dict_ac_total = {}
    
    for i, valor in enumerate(arquivo):
        colunas = valor.replace(', ', ' ').split(',')
        
        if i:
            dict_ac_total.update({colunas[0]: float(colunas[1])})

    with open("etapa-5.txt", "w", encoding='utf-8') as etapa:
        for i in sorted(dict_ac_total, key = dict_ac_total.get, reverse=True):
            print(f"{i} - {dict_ac_total[i]}", file=etapa)