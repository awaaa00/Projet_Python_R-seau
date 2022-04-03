 1#!/bin/bash
 2 LIST_OF_IREDMAIL_DEPENDENCIES= "nginx mariadb-server dovecot postfix mlmmj amavisd
 iredapd sogo clamav spamassassin roundcube fail2ban "

 3apt-get install -y $LIST_OF_IREDMAIL_DEPENDENCIES
  #Cette commande installera toutes les d�pendances
 4 wget https://github.com/iredmail/iRedMail/releases/download/1.3.1/iRedMail-1.3.1.tar.gz
 5 #Cette commamde sert �  t�l�charger la derni�re version du programme d'installation de script iRedMail � partir de son r�f�rentiel Github.
 6
 7 tar xvf iRedMail-1.3.1.tar.gz
 8 #pour extraire le fichier archiv�.
 9
 10 cd iRedMail-1.3.1/
 11 #pour d�placer dans le r�pertoire nouvellement cr��.
 12
 13 chmod + x iRedMail.sh
 14 #pou rendre  ex�cutable le fichier.
 15
 16 bash iRedMail.sh
 17#pour ex�cuter le script Bash.

