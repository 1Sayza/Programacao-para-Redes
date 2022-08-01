# importa a biblioteca socket é a blioteca responsável pelas conexões.
import socket

HOST = '127.0.0.1'
PORT = 2222

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
cliente.connect((HOST, PORT))

#Criei uma função para escrever os dados recebidos pelo servidor. 
def arquivo(namefile):
    with open(namefile, 'wb') as file:
        while True:
            data = cliente.recv(1024)
            if not data:
                break
            file.write(data)
            
#Criei uma função de menu para ajudar o usuário as opções que ele deseja. 
def pergunta():
    print('Escolha uma opção: ')
    print('1 - Listar os arquivos')
    print('2 - Baixar arquivo')
    print('0 - Sair')
    return (input('R: '))
    
#Criei um laço usando o while e puxando a funçao pergunta para a interação com o usurário nas opções. 
msg = pergunta()
while msg != '0':
     #Esse primeiro if que o cliente seleciona na opção. O cliente irá enviar dados para comunicação com o servidor. 
    if msg == '1':
        msgB = msg.encode('utf-8')
        cliente.send (msgB)
        #A variável msg está recebendo dados de um json com as informações da listagem dos arquivos do servidor e a quantidade de bytes.
        data = cliente.recv(4096)
        msg = data.decode('utf-8')
        print(f'Lista recebida: {msg}')
        #Esse segundo if que o cliente seleciona na opção. O cliente irá enviar dados para comunicação com o servidor. Nesse caso o nome do arquivo. E o cliente.send(msgC) estará recebendo os dados do arquivo. E jogando em seguida na função para escrever o arquivo no diretório atual desse arquivo py.
    if msg == '2':
        a = input('Digite o nome do arquivo: ')
        msgC = a.encode('utf-8')
        cliente.send('2'.encode())
        cliente.send(msgC)
        arquivo(msgC)
        print('recebido!')
    msg = pergunta() 
cliente.close()

        
  
        