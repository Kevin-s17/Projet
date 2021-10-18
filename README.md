# Projet 6

Voulant connaitre les hotes et leur addresses ip sur mon réseau, je n'avais pas vraiment de commandes qui me listaient rapidement tout cela.

J'ai donc créé un script en python afin de reproduire ceci.

J'ai donc mis au point un SCANNEUR D'IP.

Processus du scipt:

Le processus du script va se faire en deux partie:

1ere partie il va scanner le reseau grace à la classe Scan qui contient la commande socket.gethostbyaddr, qui va donc répertorier tout les ips et hostnames du réseau en memoire sur la machine locale puis les afficher.

2ieme partie la classe Ping va s'éxécuter et pinguer tout les ip de ce même reseau afin de répertorier les ips dont le hostname n'est pas reconnu par la machine locale puis les afficher.

1 - Pour faire fonctionner le script, veuillez récupérer le fichier scan_ip.py (script) 

2.a - Si vous voulez l'executer depuis l'invite de commande, mettez le dans un repertoire facilement accessible (sur le bureau par exemple)
    
   Lancez l'invite de commande, puis entrez:  cd chemindufichier
    
   Puis entrez le nom du script afin de l'exécuter.
    
2.b - Si vous avez un interpréteur python(ex IDLE), exécutez simplement le script avec celui-ci.
    
   clic droit sur  le script - Edit with(nom de l'interpréteur) puis f5 ou run pour éxécuter le script
    
3 - Entrez une (ou plusieurs) adresse(s) reseau(x) Format(EX: 192.168.1.)
    
   Exemple:
            
   Reseau: 192.168.1.
    
   Pour stopper le processus entrez Stop
            
   Reseau: Stop
    
   Resultat (capture éxécution du scipt)
    
            Entrez une (ou plusieurs) adresse(s) reseau(x) Format(EX: 192.168.1. ) Entrez 'Stop' pour arreter la saisie.

            Reseau: 192.168.1.
            Reseau: Stop
    
            ---------- Réseau  192.168.1.0 ----------

            IP			            Hostname
            ------------------------------------------
            192.168.1.1             PC1
            192.168.1.2             PC2
            192.168.1.254           Routeur
            192.168.1.25            Not Found
            
            -------------- Fin du Scan ---------------
            
   Fin de l'exemple.


Compatibilité: Windows 10 (non testé avec les versions précedentes), Linux(non testé), IOS(non testé), Python 3.9.1(versions antérieur non testé)

Développé avec: Windows 10/Python 3.9.1 avec l'interpréteur IDLE

Versions: 1.0

Auteur: Kevin Sousa alias Kevin-s17

License: GNU General Public License v3.0

https://github.com/Kevin-s17/Projet.git



