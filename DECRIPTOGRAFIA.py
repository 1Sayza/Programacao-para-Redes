import os
import sys

# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

arquivo = input('Digite o nome do arquivo: ')
arquivoNome = arquivo + ".enc"

chave = input('Digite a chave decodificadora:  ').encode()

try:
    with open(arquivoNome, "rb") as arquivoLoad:
        linha = arquivoLoad.readlines()
            
except:
    print("Arquivo não encontrado")

print(linha)

#Utilizei o primeiro for para ler o contéudo em bytes do arquivo linha por linha. Depois utilizei outro for para fazer a interação da chave a cada byte com cada byte da lista linha. Usando o formato de interação cifra XOR para descriptografar. E cada interação é armazenada separadamente na lista. E no final utilizo o conversor chr para retornar de acordo com a tabela ASCII a leitura visível para nós humanos. Um exemplo seria ord('B') que retorna no print 66 e o chr(66) retorna no print B. Tudo relacionado a tabela ASCII.
contador = 0 
lista = []
for j in (linha):
    for i in j:
        texto = i ^ chave[contador % len(chave)]
        contador +=1
        if contador == len(chave):
            contador == 0
        lista.append(chr(texto))

#Utilizei o método join para retornar uma string, já que os elementos estavam separados por causa da interação. 
lista1 = ''.join(lista)

nome_arquivo_output = diretorio + '\\descriptografado.txt'

arquivo_output = open(nome_arquivo_output, "w" , encoding = "utf-8")
for valor in lista1:
    arquivo_output.write(str(valor))
arquivo_output.close()