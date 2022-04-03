 1#!/bin/bash
 2 LIST_OF_MYSQL_DEPENDENCIES= "libaio1 libcgi-fast-perl libcgi-pm-perl libevent-core-2.1-7
  libevent-pthreads-2.1-7 libfcgi-perl libhtml-template-perl libmecab2
  mecab-ipadic mecab-ipadic-utf8 mecab-utils mysql-client-8.0
  mysql-client-core-8.0 mysql-server-8.0 mysql-server-core-8.0 "

 3 sudo apt update
 4 #Cette commande sert à  mettre à jour l’index des paquets sur votre serveur 
 5
 6 apt-get install -y $LIST_OF_MYSQL_DEPENDENCIES
 7 #Cette commande installera toutes les dependances de MYSQL.

