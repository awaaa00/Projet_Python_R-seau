 1#!/bin/bash
 2 LIST_OF_IREDMAIL_DEPENDENCIES= "nginx mariadb-server dovecot postfix mlmmj amavisd
 iredapd sogo clamav spamassassin roundcube fail2ban "

 3apt-get install -y $LIST_OF_IREDMAIL_DEPENDENCIES
  #Cette commande installera toutes les dépendances
 4 wget https://github.com/iredmail/iRedMail/releases/download/1.3.1/iRedMail-1.3.1.tar.gz
 5 #Cette commamde sert à  télécharger la dernière version du programme d'installation de script iRedMail à partir de son référentiel Github.
 6
 7 tar xvf iRedMail-1.3.1.tar.gz
 8 #pour extraire le fichier archivé.
 9
 10 cd iRedMail-1.3.1/
 11 #pour déplacer dans le répertoire nouvellement créé.
 12
 13 chmod + x iRedMail.sh
 14 #pou rendre  exécutable le fichier.
 15
 16 bash iRedMail.sh
 17#pour exécuter le script Bash.

