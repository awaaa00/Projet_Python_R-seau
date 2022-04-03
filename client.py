 1 #coding:utf-8
 2 import socket
 3 import json
 4
 5 class Objetmail:
 6     def __init__(self,add_src,add_dest,obj_mail,corp_message):
 7         self.add_src= add_src
 8         self.add_dest = add_dest
 9         self.obj_mail = obj_mail
10         self.corp_message = corp_message
11
12 host= '192.168.10.1'
13 port = 5566
14
15 # Creation de socket
16
17 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
18 try:
19 # Connexion au server
20     client.connect((host, port))  
21
22 # Echange d'info avec le server cote client
23     data = client.recv(1024)
24     data = data.decode("utf8")
25     print(data)
26
27  # variable dinfo client
28     Info = [] 
29     nom = input("Veuillez saisir votre nom svp :")
30     mail = input("Veuillez saisir votre addresse mail svp:")
31     pwd = input("Veuillez entrer votre mot de passe svp:")
32     Info.append(nom)
33     Info.append(mail)
34     Info.append(pwd)
35     messagesend = json.dumps(Info)
36     messagesend = messagesend.encode("utf8")
37     client.sendall(messagesend)
38
39     data = client.recv(1024)
40     data = data.decode("utf8")
41     print(data)
42
43 except Exception as e:
44     print(e)
45 finally:
46     client.close()
