animais = ["Cachorro", "Gato", "Tartaruga", "Leão", "Rato", "Elefante", 
           "Peixe", "Golfinho", "Girafa", "Urso", "Baleia", "Papagaio",
           "Tubarão", "Girafa", "Canguru", "Coala", "Coruja",  "Galinha",
           "Morcego", "Panda"]

[print(animal) for animal in sorted(animais)]

with open("animais.csv", "w", encoding='utf-8') as arquivo: 
    for animal in sorted(animais):
        print(animal, file=arquivo) 
    print(" -- Salvo! Acesse o arquivo animais.csv") 