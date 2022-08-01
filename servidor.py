# importa a biblioteca socket é a blioteca responsável pelas conexões.
import socket 

from os import listdir, stat
from os.path import isfile, join, dirname, abspath, sep
import json

#Verifica no diretório arquivos dentro do contexto do arquivo python em execução quais são os arquivos válidos. Forma um dicionário {<nome_arquivo>:<tamanho_arquivo(bytes)>}, retorna o JSON gerado a partir do dicionário.
def files2json():
	files_length = {}
	base_dir = f"{dirname(abspath(__file__))}{sep}arquivos"
	print(base_dir)
	for file in listdir(base_dir):
		if(isfile(join(base_dir,file))):
			files_length[file] = stat(join(base_dir, file)).st_size
	return json.dumps(files_length, indent=4)

HOST = '0.0.0.0'
PORT = 2222

#Cria um objeto socket passando que a conexõa serão aceita via IPv4 ou um domínio. E o segundo parâmetro vai ser via protocolo TCP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#Ligou o socket ao endereço do servidor.
sock.bind((HOST, PORT))
sock.listen(1) #No modo de escuta o endereço ligado ao servidor. Ou seja, aceitando conexões. 
print('Ouvindo a conexão!')

# Aceitar uma conexão de cliente.
con, client = sock.accept()
print ("conexão estabelecida ...")

#Uma função para abrir o arquivo do diretório que o cliente solicitou, irá fazer a leitura desse arquivo e irá ler o contéudo. 
def arquivo(namefile):
    try:
        with open(namefile, 'rb') as file:
            for data in file.readlines():
                con.send(data)
                print('Arquivo enviado!')
    except:
        print('Arquivo não encontrado!')

#Nesse while é um laço com a interação do cliente. Se o cliente digitar a opção 1 será enviado um json com as informações listadas. O con.send envia uma conexão uma mensagem um pacote. Já a função recv recebe dados.
while True:
    data = con.recv(4096).decode()
    if data == '1':
        msg = f"received {data} from {client} ..."
        print(msg, 'devolvendo...')
        con.send(files2json().encode('utf-8'))
        
    if data == '2':
        arquivo1 = con.recv(4096).decode()
        arquivo(arquivo1)

con.close()
sock.close()
    


