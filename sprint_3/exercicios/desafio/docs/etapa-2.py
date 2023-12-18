with open('actors.csv') as arquivo:
    gloss = []
    
    for i, valor in enumerate(arquivo):
        colunas = valor.replace(', ', ' ').split(',')
        
        if i:
            gloss.append(float(colunas[5]))
            
    with open("etapa-2.txt", "w", encoding='utf-8') as etapa:   
        media = sum(gloss)/len(gloss)
        print(f"A média de receita de bilheteria bruta dos principais filmes é {media}.", file=etapa)