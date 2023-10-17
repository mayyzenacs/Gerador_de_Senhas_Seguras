#importa as funções que estão na pasta mod
import mod.source as source 
#modulo que contém timer
from time import sleep 

source.tamanhoSenha("Tamanho da senha: ") #chama a função que cria o input para ler o tamanho da senha

caracter = source.checkCaracters("Caracteres especiais? ")
numeros = source.checkCaracters("Números? ") 

source.linha() #chama função de linha
print(f"Sua senha foi criada: ") 
#sleep(0.5)
print(" ----->")
senha = source.escolhaEspecial(caracter, numeros) #cria uma variavel que recebe o retorno da função escolhaEspecial ou seja a senha.
print(f"    {senha}") #printa a variavel com resultado da senha
source.linha()









