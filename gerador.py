import mod.source as source #importa as funções que estão na pasta mod

source.tamanhoSenha("Tamanho da senha: ") #chama a função que cria o input para ler o tamanho da senha

while True: #while de verificação de dados 
    escolha_caracter = input("Caracteres especiais? ").lower().strip()[0] #deixa minusculo e pega apenas a primeira letra
    if escolha_caracter in "sn": #verifica se a escolha está correta
        break #se sim para o loop
    
    else: #senao printa um erro
        print("INVÁLIDO. Responda apenas SIM ou NÃO (S,N).")

while True: #while de verificação de dados
    escolha_numeros = input("Numeros? ").lower().strip()[0] #deixa em minusculo e pega apenas a primeira letra
    if escolha_numeros in "sn": #verifica se a escolha está correta
        break #se sim para o loop
    else: #senao printa um erro
        print("INVÁLIDO. Responda apenas SIM ou NÃO (S,N).")

source.linha() #chama função de linha
print(f"Sua senha foi criada: ") 
print(" ----->")
senha = source.escolhaEspecial(escolha_caracter, escolha_numeros) #cria uma variavel que recebe o retorno da função escolhaEspecial ou seja a senha.
print(f"    {senha}") #printa a variavel com resultado da senha
source.linha()









