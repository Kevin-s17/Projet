import socket
from threading import Thread

host = {} #dictionnaire stockant les noms d'hôte récupérés
ip_list = [] #Tableau qui stockera les IP
nb_sr = [] #Tableau qui stockera les sous_reseaux entrés par l'utilisateur


#classe définissant le thread de scan d'adresse Ip servant à récupérer le hostname du périphérique réseau
class Scan(Thread):

#Constructeur de la classe prend en argument les paramètres suivants: address : adresse IP à scanner 
    def __init__(self, ip):
        Thread.__init__(self)
        self.address = ip
#Définition de la méthode Run de notre classe de scan
    def run(self):
        self.lookup(self.address)

#Méthode de classe permettant de récupérer le hostname du périphérique connecté au réseau. Elle prend en paramètrre la variable de classe représentant l'adresse IP à recherchée
    def lookup(self, ip):
        try:
            hostname, alias, addressip = socket.gethostbyaddr(ip)
            host[ip] = hostname #On associe le hostname à l'adresse IP et on les sauve dans le dictionnaire
        except:
            hostname = "Not found"

        
#programme principal    
if __name__ == '__main__':
    sous_reseau = input("Entrez une (ou plusieurs) adresse(s) reseau(x) Format(EX: 192.168.1. ) Entrez 'Stop' pour arreter la saisie.\n\nReseau: ")
    while sous_reseau != "Stop":
        nb_sr.append(sous_reseau)
        sous_reseau = input("Reseau: ")
    
    for sr in nb_sr:
        print("\n\n---------- Réseau ",sr + "0","----------")
        print("\nIP\t\t\t Hostname\n------------------------------------------")

#On définit une plage d'adresses IP à scanner
        for i in range(1, 256):
            ip_list.append(sr + str(i)) #On stock chaques IP dans ip_list

        thread_list = [] #Tableau qui stockera les threads créés

#On créée autant de threads qu'il y à d'adresses IP à scanner
        for thread in (Scan(ip) for ip in ip_list) :
            thread.start() #Chaque thread est démarré en même temps
            thread_list.append(thread) #On ajoute chaque thread dans le tableau
            
#On unit tous les threads pour être sûr que tous ceux-ci renvoient leur valeur
        for t in thread_list:
            t.join()

#On affiche le résultat qui affiche pour chaque machine connectée son nom d'hôte
        for ip, hostname in host.items():
            if (hostname != "Not Found"):
                print(ip, "\t\t" , hostname)
        
#On vide le dictionnaire et les listes afin de les remplir avec un nouveau sous-reséau
        host = {}
        ip_list = []
        thread_list = []
        
    print("-------------- Fin du Scan ---------------")  
