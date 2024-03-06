
import socket as s

'''
serv will add his mesage from a view function ,and it will be pased to gene function


'''
def gene(self,call):
    print("Server msg:",call)
    return call


SERVER=s.socket(s.AF_INET,s.SOCK_STREAM)
#SERVER.bind(("localhost",9999))

SERVER.listen()
gene_client,addr=SERVER.accept()


end=False

while not end:
    msg=gene_client.recv(1024).decode('utf-8')
    print(msg)
    if msg=='شكرا':
        end=True
    else:
        print(msg)
    gene_client.send(gene().decode('utf-8'))




SERVER.close()
gene_client.close()