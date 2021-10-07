#A comunicação funciona de maneira parecida a um walkie talkie,
#Só se pode responder um de cada vez
import socket
def Servidor():
    name2 = ("Cliente: ")
    host = "192.168.0.104"
    #O host precisa ser o endereço ip do que será o servidor
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Conexão de: " + str(addr))
    msg = ''
    while msg !='q':
            data = conn.recv(1024).decode()
            print (name2 + str(data))
            msg = input("Mensagem: ")
            msg = str(msg)
            conn.send(msg.encode())
             
    conn.close()
import socket
 
def Cliente():
        name = ("Servidor: ")
        host = '192.168.0.100'
        #precisa ser o endereco do ip do host
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = ''
         
        while message != 'q':
                
                message = input("Digite a msg: ")
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                print (name + str(data))
   
                    
        mySocket.close()
        
 



while True:
    print("[1] cliente")
    print("[2] servidor")
    op = input("opção: ")
    if op == '1':
        Cliente()
    if op == '2':
        Servidor()
    else:
        break
        