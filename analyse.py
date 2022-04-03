#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import csv

fichierdict= []
with open("analyse.csv") as fichier:
    reader= csv.DictReader(fichier, delimiter=' ')
    for line in reader:  
        fichierdict.append(line)
    print(fichierdict)

msg = MIMEMultipart()    
msg['FROM']= "diayla@redmail.com"
msg['password']= "passer"
msg['TO'] = "awa@redmail.com"
msg['Subject']= "Analyse"
corp_message= f"{fichierdict[0]}"
msg.attach(MIMEText(corp_message,'html'))
echange = smtplib.SMTP('mail.redmail.com',587)
echange.starttls()
try:
    echange.login(msg['FROM'], msg['password'])
    echange.sendmail(msg['FROM'], msg['TO'], msg.as_string())
    print("Message envoy�")
except:
    print("Mauvais compte")
finally:
    echange.quit()
