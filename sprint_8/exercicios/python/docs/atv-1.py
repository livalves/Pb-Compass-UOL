import random

lista = [random.randrange(1000) for _ in range(250)]
    
print(f"Lista original: {lista} \n")

lista.reverse()
print(f"Lista invertida: {lista}")