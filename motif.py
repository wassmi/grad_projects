import datetime
role = "Ce programme permet d'indiquer le nombre de fois qu'un motif saisie \napparait dans les séquences lus dans le fichier sequences.txt"
date_today = datetime.date.today()
print("="*len(role))
print("Motifs2.py v1.0")
print("Auteur: Wasmi Algasim")
print("Date:  ", date_today)
print(role)
print("="*len(role))

#les paramètres initiaux
liste_de_seq = []
cmd = ""
dict_seq = {}
sequence_valide = False

#import ou creatiion du fichier sequences.txt
fichier_seq_input = open("sequences.txt", "a")
fichier_seq_input.close()

"""
Fonction debut permet de copier les séquences du fichier principale 
dans un fichier de travail afin de consérver le fichier principale intacte. 
"""
def debut():
	fichier_seq_input = open("sequences.txt", "r")
	fichier_seq_output = open("sequences_actuel.txt", "w")
	for ligne in fichier_seq_input:
		print(ligne, end="", file = fichier_seq_output)
	fichier_seq_input.close()
	fichier_seq_output.close()

"""
Fonction sauvgarder permet de copier les séquences du fichier de travail dans le fichier 
principale
"""
def sauvegarder():
	fichier_seq_input = open("sequences_actuel.txt", "r")
	fichier_seq_output = open("sequences.txt", "a")
	for ligne in fichier_seq_input:
		fichier_seq_output.write(ligne)
	fichier_seq_input.close()
	fichier_seq_output.close()

# ajouter les séquences entrée dans le fichier de travail sous forme d'un dictionnaire
def ajouter_dans_fichier():
	fichier_seq = open("sequences_actuel.txt", "w")
	for seq in dict_seq:
		print(seq, ' : ', dict_seq[seq], "\n", file = fichier_seq)
	fichier_seq.close()

#validation de l'entrée de la séquence saisie
def sequence_valide(sequences):
	if len(sequences) > 0 and (sequences.count("A") + sequences.count("T") + sequences.count("G") + sequences.count("C")) == len(sequences):
		return True
	else:
		print("sequence non valide")
		return False


# la fonction principale d'ajout de séquence saisie dans le fichier avec numérotage unique
def ajouter(compte):
	tentative = 0
	sequences = str(input("Veuillez entrer une séquence ADN valide: ")).upper()
	while not sequence_valide(sequences) and tentative !=2:
		if not sequence_valide(sequences):
			tentative +=1
			sequences = str(input("Veuillez entrer une séquence ADN valide: ")).upper()
	if sequence_valide(sequences) :
		for clef in dict_seq.keys():
			compte += 1 # permet de numéroter chaque entrée dans le dictionnaire (keys)
		dict_seq[compte] = sequences
		ajouter_dans_fichier()

#fonction optionnel pour visualiser quelles sont les séquences existantes actuellement
def afficher ():
	for seq in dict_seq:
		if seq == "":
			print("Aucune séquence à afficher.")
		print(seq, ' : ', dict_seq[seq])


def valider_supprimer(choix_del):
		if choix_del >0:
			return True
		else:
			return False


def supprimer():
	afficher()
	fichier_seq = open("sequences_actuel.txt", "a")
	choix_del = int(input("Veuiller indiquer le numéro de la séquence à supprimer \n(voir la liste ci-dessus): "))
	valider_supprimer(choix_del)
	while not valider_supprimer(choix_del):
		print("Entrée invalide. Veuillez choisir une position de la liste ci-dessus.")
		choix_del = int(input("Veuiller indiquer le numéro de la séquence à supprimer \n(voir la liste ci-dessus): "))
	while not False:
		try:
			if valider_supprimer(choix_del):
				del dict_seq[choix_del]
				ajouter_dans_fichier()
				fichier_seq.close()
				break
		except KeyError:
			print("Aucune séquence avec numéro n'existe.")
			break

# verifier si le motif rechercher est valide
def valider_motif(motif):
	if len(motif) > 0 and (motif.count("A") + motif.count("T") + motif.count("G") + motif.count("C")) == len(motif):
		return True
	else:
		print("motif non valide")
		return False

# fonction principal de recherche de motif dans les séquences une par une
#permet aussi d'afficher le résultat du nombre d'apparation, si applicable
def rechercher():
	tentative = 0
	entree_motif = str(input("Veuillez indiquer le motif rechercher: ")).upper()
	motif = entree_motif
	valider_motif(motif)
	while not valider_motif(motif) and tentative != 2 :
		if not valider_motif(motif):
			tentative += 1
			#rechercher()
			entree_motif = str(input("Veuillez indiquer le motif rechercher: ")).upper()
			motif = entree_motif
	if valider_motif(motif):
		liste_seq = list(dict_seq.values())
		for seq in liste_seq:
			chaque_seq = seq
			if motif in chaque_seq:
				compteur_motif = chaque_seq.count(str(motif))
				print("La séquence", chaque_seq, "contient le motif", motif, compteur_motif,"fois.", sep=" ")
			else:
				print("La séquence", chaque_seq, "ne contient pas le motif", motif, sep=" ")

# fonciton des options de commande
def action_par_commande(cmd):
	if cmd == "ajouter":
		ajouter(compte = 1)
	elif cmd == "supprimer":
		supprimer()
	elif cmd == "rechercher":
		rechercher()
	elif cmd == "quitter":
		sauvegarder()
	elif not cmd == ("ajouter" or "supprimer" or "rechercher" or "quitter" or "afficher"):
		print("Votre saisie est innexistante. Veuillez choisir l'une des options mentionnées. ")


# fonction principal, englobe tout les autres fonctions ci-dessus.

def main(cmd):
	while cmd != "quitter":
		cmd = input("Veuillez écrire une des commandes suivantes (ajouter/supprimer/rechercher/afficher/quitter): ")
		action_par_commande(cmd)
		if cmd == "afficher":
			afficher()

### partie principal du code ###
debut()
main(cmd)
print("fin normal du script")
