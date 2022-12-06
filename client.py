import socket

HOST = 'localhost'
PORT = 5500

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
print("Bem vindo ao jogo de dados! Voce tentara adivinhar o valor do dado jogado pelo servidor.\n")
print("Se voce acertar pelo menos 2 de tres tentativas, voce ganha. Caso contrario, o servidor ganha :(\nBoa sorte!\n")
acertos = 0
erros = 0

for i in range(1,4):
    chute = str(input("Rodada " + str(i) + ":\nDigite seu palpite: "))
    mensagemenviocliente = chute
    sock.sendall(str.encode(mensagemenviocliente))
    
    data = sock.recv(1024)
    resultadodado = data.decode()
    print("Resultado do dado: " + resultadodado + "\n")
    if resultadodado == chute:
        print("Parabens, voce acertou\n")
        acertos = acertos+1
    else:
        print("Infelizmente voce errou\n")
        erros = erros + 1
    print("Placar atual:\n")
    print("Cliente ", acertos, " x Servidor ", erros)    
if acertos>erros:
    print("Parabens, voce ganhou o jogo!\n" )
else:
    print("Que pena, o servidor ganhou o jogo :(\n")
print("Placar final: \n")
print("Cliente ", acertos, " x Servidor ", erros, "\n")    