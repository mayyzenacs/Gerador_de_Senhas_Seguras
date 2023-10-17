#importa o modulo que pega o alfabeto, os numeros e os simbolos
import string 
#importa o modulo que vai randomizar a senha
from random import choice 
#modulo que contém timer
from time import sleep


def linha(comp=70): #função que cria uma linha para organização 
    print("-"*comp) #cria uma linha do tamanho do parâmetro


def tamanhoSenha(enter): #função que vai ler o tamanho da senha
    while True: #while para verificação de dados
        entrada = input(enter)  #cria-se a entrada do dado
        if entrada.isnumeric() and len(entrada) > 0: #verifica se a entrada é numerica e não está vazia
            global tam #globaliza o escopo de tam para poder ser usado em outras funções
            tam = int(entrada) #converte tam em numero inteiro
            if tam <= 100 and tam >= 6: #verifica se o tamanho da senha está dentro das regras
                break #se estiver o loop para
            else:
                print("Sua senha deve ser menor que 100 caracteres e por questões de segurança ter entre 6 e 8 caracteres.") 
        else:
            print("Digite um número INTEIRO válido.") 


def checkCaracters(enter):
    while True: #while de verificação de dados 
        while True: 
            try: #verifica se não há espaços em branco
                #global escolha_caracter
                escolha_caracter = input(enter).strip().lower()[0]
                break #deixa minusculo e pega apenas a primeira letra
            except IndexError:
                print("INVÁLIDO. Responda apenas SIM ou NÃO! (S,N)")
        if escolha_caracter in "sn" and len(escolha_caracter) > 0: #verifica se a escolha está correta
            break #se sim para o loop
        
        else: #senao printa um erro
            print("INVÁLIDO. Responda apenas SIM ou NÃO! (S,N)")
    return escolha_caracter    

def checkNumeros(enter):
    while True:  
        while True: 
            try:
                #global escolha_numeros
                escolha_numeros = input(enter).strip().lower()[0] #deixa em minusculo e pega apenas a primeira letra
                break
            except IndexError:
                print("INVÁLIDO. Responda apenas SIM ou NÃO! (S,N)")
        if escolha_numeros in "sn" and len(escolha_numeros) > 0: #verifica se a escolha está correta
            break #se sim para o loop
        else: #senão printa um erro
            print("INVÁLIDO. Responda apenas SIM ou NÃO! (S,N)")
    return escolha_numeros

def geradorAleatorio(rando=string.ascii_letters + string.digits + string.punctuation): #função que cria uma senha de letras aleatorias com numeros e símbolos
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido


def geradorSoLetras(rando=string.ascii_letters): #função que cria uma senha apenas com letras
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)


def geradorNumLetra(rando=string.digits + string.ascii_letters): #função que cria uma senha apenas com numeros e letras
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)


def geradorLetraSimbol(rando=string.ascii_letters + string.punctuation): #função que cria uma senha apeans letras e símbolos
    return "".join(choice(rando) for tamanho in range(tam)) #retorna a junção dos dados acima num tamanho de tam(tamanho da senha escolhido)


def escolhaEspecial(escolhaChar, escolhaNum): #função que recebe as escolhas sobre numero e simbolos
    #as condições vão verificar as escolhas e retornar a função especifica que retorna a senha para o programa principal.
    if escolhaChar == "s" and escolhaNum == "s": 
        sleep(0.5)
        return geradorAleatorio()
    elif escolhaChar == "n" and escolhaNum == "n":
        sleep(0.5)
        return geradorSoLetras()
    elif escolhaChar == "s" and escolhaNum == "n":
        sleep(0.5)
        return geradorLetraSimbol()
    elif escolhaChar == "n" and escolhaNum == "s":
        sleep(0.5)
        return geradorNumLetra()

