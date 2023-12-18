with open('actors.csv') as arquivo:
    movies = []
    for i, valor in enumerate(arquivo):
        colunas = valor.replace(', ', ' ').split(',') 
        if i:
            movies.append(colunas[4])
     
    movies_qtde = {}
    for i in movies: 
        count = 0 
        for m in movies:
            if i == m:
                count += 1
        movies_qtde.update({i:count})
        
    movies_ord = sorted(movies_qtde.items(), key=lambda item: (-item[1], item[0]))
    
    with open("etapa-4.txt", "w", encoding='utf-8') as etapa: 
        for i, (movie, count) in enumerate(movies_ord):   
            print(f"{i+1} - O filme {movie} aparece {count} vez(es) no dataset", file=etapa)
