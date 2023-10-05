import string
from random import choice

def leiaInt(enter):
    global entrada
    entrada = int(input(enter))
    return entrada

def geradorAleatorio(rando=string.ascii_letters + string.digits + string.punctuation):
    tam = entrada
    return "".join(choice(rando) for tamanho in range(tam))


leiaInt("Tamanho da senha: ")
print(f"Sua senha foi criada: ")
print(geradorAleatorio())






