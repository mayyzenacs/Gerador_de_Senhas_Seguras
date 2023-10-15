
import string #importa o modulo que pega o alfabeto, os numeros e os simbolos
from random import choice #importa o modulo que vai randomizar a senha


def linha(comp=60): #função que cria uma linha para organização 
    print("-"*comp) #cria uma linha do tamanho do parâmetro

def tamanhoSenha(enter): #função que vai ler o tamanho da senha
    while True: #while para verificação de dados
        entrada = input(enter)  #cria-se a entrada do dado
        if entrada.isnumeric(): #verifica se a entrada é numerica
            global tam #globaliza o escopo de tam para poder ser usado em outras funções
            tam = int(entrada) #converte tam em numero inteiro
            if tam <= 100 and tam >= 6: #verifica se o tamanho da senha está dentro das regras
                break #se estiver o loop para
            else:
                print("Sua senha deve ser menor que 100 caracteres e por questões de segurança ter entre 6 e 8 caracteres.") 
        else:
            print("Digite um número INTEIRO válido.") 


def geradorAleatorio(rando=string.ascii_letters + string.digits + string.punctuation): #função que cria uma senha de letras aleatorias com numeros e simbolos
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)

def geradorSoLetras(rando=string.ascii_letters): #função que cria uma senha apenas com letras
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)

def geradorNumLetra(rando=string.digits + string.ascii_letters): #função que cria uma senha apenas com numeros e letras
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)

def geradorLetraSimbol(rando=string.ascii_letters + string.punctuation): #função que cria uma senha apeans letras e simbolos
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)


def escolhaEspecial(escolhaChar, escolhaNum): #função que recebe as escolhas sobre numero e simbolos
    #as condições vão verificar as escolhas e retornar a função especifica que retorna a senha para o programa principal.
    if escolhaChar == "s" and escolhaNum == "s": 
        return geradorAleatorio()
    elif escolhaChar == "n" and escolhaNum == "n":
        return geradorSoLetras()
    elif escolhaChar == "s" and escolhaNum == "n":
        return geradorLetraSimbol()
    elif escolhaChar == "n" and escolhaNum == "s":
        return geradorNumLetra()

