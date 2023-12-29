from hashlib import sha1

texto = input("Informe o texto ou 'S' para sair: ").encode("utf-8")
while texto != ("S").encode("utf-8"):
    print("Hash: " + sha1(texto).hexdigest())
    texto = input("Informe o texto ou 'S' para sair: ").encode("utf-8")
