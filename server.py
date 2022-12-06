import socket
import random

HOST = 'localhost' # Identifica o nome do servidor
PORT = 5500 # Identifica a porta do servidor
addr = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)

sock.listen(5)

print("Aguardando conexão de um cliente:")

conn, ender = sock.accept() # Conexão e endereço

print('Connectado com', ender) # Apresentação do endereço do cliente, composto de nome do host e a porta que foram conectados.

valordado = ['1','2','3','4','5','6']
acertos = 0
erros = 0
rodada = 1

while True:
    data = conn.recv(1024)
    if not data:
        print("\nconexao encerrada!\n")
        conn.close()
        break
    
    palpitecliente = data.decode()
    palpiteservidor = random.choice(valordado)
    print("Rodada ", rodada, ":\n")
    print("O palpite do cliente foi: " + palpitecliente + "\n")
    print("O resultado do dado pelo servidor foi: " + palpiteservidor + "\n")
    
    if(palpiteservidor == palpitecliente):
        acertos = acertos + 1
        print("O cliente acertou!\n")
    else:
        print("O cliente errou!\n")
        erros = erros + 1
        
    print("Placar atual:\n")
    print("Cliente ", acertos, " x Servidor ", erros)    
    conn.sendall(bytes(str(palpiteservidor), 'utf8'))
    rodada = rodada + 1

if acertos>erros:
    print("O cliente venceu o jogo\n" )
else:
    print("O servidor venceu o jogo\n")
    
print("Placar final: \n")
print("Cliente ", acertos, " x Servidor ", erros, "\n")