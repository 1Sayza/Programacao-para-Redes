import os
import sys

# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

arquivo = input('Digite o nome do arquivo: ')
arquivoNome = arquivo + ".txt"

#Utilizei o encode() logo na entrada(input) da chave para retornar a versão codificada da string.

chave = input('Qual será a chave:  ').encode()
#Ler em formato de bytes "rb". 
try:
    with open(arquivoNome, "rb") as arquivoLoad:
        linha = arquivoLoad.readline()
            
except:
    print("Arquivo não encontrado")

#Utilizei o bytearray, por que as strings a nível de bytes são read-only. Não da para fazer atribuições. Então nesse caso a alternativa é a bytearray. Em que é possível criar um conjunto de bytes e permite a escrita nos elementos.  Ou seja, uma array de bytes, que é mutável, sequência de inteiros no intervalo. 

byteschave = bytearray(linha)

#Utilizei o for para a lógica da aplicação da cifra XOR de cada byte da chave a cada byte do conjunto de bytes do arquivo txt. E assim que a sequênci de bytes da chave termina, se começa novamente a leitura dos bytes inicialmente até o final do byte, até o processo da aplicação do for terminar de ler toda sequência de bytearray do arquivo. E a cada processo de interação também da cifra xor ta sendo adicionado na variável byteschave. 

for i in range(len(byteschave)):
    byteschave[i] = byteschave[i] ^ chave[i % len(chave)]

print(byteschave)

# Montando o nome do arquivo
nome_arquivo_output = diretorio + '\\criptografado.enc'

#Com a sequência do contéudo do arquivo cifrada armazenada na variável byteschave, reescrevo em um novo arquivo no formato de enc. 

with open(nome_arquivo_output, 'wb') as valor:
    valor = valor.write((byteschave))

#Depois de reescrever o arquivo. Uso da função os.remove que deleta o arquivo armazenado na pasta.   
os.remove(arquivoNome)


        
