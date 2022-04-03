 1#coding:utf-8
 2 import json
 3 import socket
 4 import mysql.connector as MC
 5
 6 def TesterInfo():
 7     #connexion a la bd
 8     try:
 9         connexion = MC.connect(host='localhost', database='users', user='root', password='root')
10         curseur = connexion.cursor()
11         req = "select * from user"
12         curseur.execute(req)
13         resultat = curseur.fetchall()
14         return resultat
15     except MC.Error as err:
16         print(err)
17     finally:
18         connexion.close()
19
20
21 host= ''
22 port = 5566
23 # Creation de socket
24 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
25  # Demarrage du server
26 server.bind((host, port))
27 print(" Server start....")
28 while True:
29   #server ecoute sur le port '5566'
30     server.listen(5) 
31     conn, addr = server.accept()
32
33     #Demande d'info aux client
34     messagesend = f"Veuillez saisir vos identifiants"
35     messagesend = messagesend.encode("utf8")
36     conn.sendall(messagesend)
37     print("Info du client en cours")
38
39     #communication entre Server/Client
40     messagerecv = conn.recv(1024)  
41     messagerecv = messagerecv.decode("utf8")
42     data = json.loads(messagerecv)
43
44     #Tester les infos de la bd
45
46     info = TesterInfo()
47     for element in info:
48         if element[2] == data[1] and element[3]== data[2]:
49             #accuser de reception
50             messagesend_2 = f"Connexion etablie avec succes"
51             messagesend_2 = messagesend_2.encode("utf8")
52             conn.sendall(messagesend_2)
53         else:
54             # message d'erreur en cas d'echec
55             messagesend_2 = f"Erreur: veuillez verifier vos identifiants svp!"
56             messagesend_2 = messagesend_2.encode("utf8")
57             conn.sendall(messagesend_2)
58
59 conn.close()
60 server.close()
