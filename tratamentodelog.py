import statistics
import os
from operator import itemgetter

# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

arquivo = input('Digite o nome do arquivo: ')
arquivoNome = arquivo + ".txt"

# Criei várias listas para armazenar campos do arquivo apache que precisaria para responder a questão ou armazenar mais uns dados, caso esse código fosse necessário para outro análise de critério de log.

data, hora, ip, navegador, codigo, metodo, sistema, dataehora, horaeip, pagina= [], [], [], [], [], [], [], [], [], []

# Utilizei a função do split para quebrar a string e armazenar cada dado em uma lista. 
try:
    with open(arquivoNome, "r") as arquivoLoad:
        arquivo1 = arquivoLoad.readlines()
        
        for linha in arquivo1[1:]:
            data.append(((linha.split(' ')[0]).split('[')[1]).split(':',1)[0])
            hora.append(linha.split(' ')[0].split('[')[1].split(':',1)[1])
            ip.append(linha.split(' ')[2])
            if (linha.split(' ')[5]) != '-':
                navegador.append(linha.split(' ')[5])
            codigo.append(linha.split(' ')[7])
            metodo.append(linha.split(' ')[8])
            dataehora.append(linha.split(' ')[0].split('[')[1])
            horaeip.append(linha.split(' ')[0:3])
            if (linha.split(' ')[6].split('/')[1]) != '':
                pagina.append(linha.split(' ')[6].split('/')[1])
                           
except:
    print("Arquivo não encontrado")


# Utilizei a biblioteca statistics para responder várias questões por que é uma biblioteca do python que trabalha pegando a medida da localização central dos dados. Ou seja, o dado que mais se repete dentro da lista.

tentativas = statistics.mode(dataehora)
qtip = statistics.mode(ip)
navegadorr = statistics.mode(navegador)

dic = dict()
lista = list ()

#Utilizei o parâmetro do for para criar um dicionário, em que a chave será a página e o contéudo da chave será o contador, aparecendo a quantidade de vezes que o caracter específico aparece dentro da lista.

for string in pagina:
    dic[string] = pagina.count(string)

#Utilizei o parâmetro do for para ordenar meu dicionário de forma decrescente a partir do contéudo da chave que estava armazenado em numeral. Só uma observação que utilizei o método sorted mas no final tem um parâmetro de reverse = True, que faz ao contrário, ou seja, decresce. E como informei que a organização da lista foi pelo numeral utilizei a biblioteca from operator import itemgetter para específicar. E adicionei só na lista os nomes das páginas que eram as chaves, por que a questão só podia as 5 primeiras mais requisitadas aonde tinha mais contador somado. Então no print especifiquei o print na lista[0:5], imprima só as 5 primeiras da lista. 

for nome,contador in sorted(dic.items(), key=itemgetter(1), reverse = True):
    lista.append(nome) 

print('O momento (data/hora/minuto/segundo) que obteve mais tentativas de ataques é {}'.format(tentativas))
print(f'O IP que teve o maior número de tentativas de ataque {qtip}.')
print('A lista em ordem decrescente das cinco páginas mais requisitas ao servidor {}.'.format(lista[0:5]))
print(f'O navegador mais usado foi {navegadorr}. ')
print('O número de páginas que não foram atendidas pelo servidor é {}.' .format(len(codigo) - codigo.count('200')))

        