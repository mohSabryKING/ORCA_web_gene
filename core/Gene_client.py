
import socket as s

'''
serv will add his mesage from a view function ,and it will be pased to gene function


'''
def gene(self,call):
    print("Client msg:",call)
    return call


Client=s.socket(s.AF_INET,s.SOCK_STREAM)

#Client.connect(("localhost",9999))


end=False

while not end:
      Client.send(gene("").encode('utf-8'))
      msg=Client.recv(1024).decode('utf-8')
      if end=="شكرا":
            end=True
      else:
            print(gene(""))
            gene("")




Client.close()

