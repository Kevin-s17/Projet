# Projet

Voulant connaitre les hotes et leur addresses ip sur mon réseau, je n'avais pas vraiment de commandes qui me listaient rapidement tout cela.

J'ai donc créé un script en python afin de reproduire ceci.

J'ai donc mis au point un SCANNEUR D'IP.

1 - Pour le faire fonctionner, veuillez récupérer le fichier scan_ip.py (script) 

2.a - Si vous voulez l'executer depuis l'invite de commande, mettez le dans un repertoire facilement accessible (sur le bureau par exemple)
    
   Lancez l'invite de commande, puis entrez:  cd chemindufichier
    
   Puis entrez le nom du script afin de l'exécuter.
    
2.b - Si vous avez un interpréteur python, exécutez simplement le script avec celui-ci.
    
   Edit with.. puis f5 pour éxécuter le script
    
3 - Entrez une (ou plusieurs) adresse(s) reseau(x) Format(EX: 192.168.1.)
    
   Exemple:
            
   Reseau: 192.168.1.
    
   Pour stopper le processus entrez Stop
            
   Reseau: Stop
    
   Resultat:
    
            Entrez une (ou plusieurs) adresse(s) reseau(x) Format(EX: 192.168.1. ) Entrez 'Stop' pour arreter la saisie.

            Reseau: 192.168.1.
            Reseau: Stop
    
            ---------- Réseau  192.168.1.0 ----------

            IP			            Hostname
            ------------------------------------------
            192.168.1.1             PC1
            192.168.1.2             PC2
            192.168.1.254           Routeur
            
            -------------- Fin du Scan ---------------
            
   Fin de l'exemple.



Développé avec: Windows 10/Python 3.9.1 avec l'interpréteur IDLE

Versions: 1.0

Auteur: Kevin Sousa alias Kevin-s17

License:





