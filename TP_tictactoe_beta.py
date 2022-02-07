# PROJET : TICTACTOE 
# NGUYEN BERNARD AS 2021
from tkinter.constants import TRUE, X
from graphicalgrid import GraphicalGrid

# --- Question 1 ---
def crée_grille(n):  

    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
                ligne.append("")  
        grille.append(ligne)
    return grille


# --- Question 2 ---
def taille_coté(grille):

    taille_coté = 0
    for i in range(len(grille)):
        taille_coté += 1
    return taille_coté


# --- Question 3 ---
def est_vide(grille, i, j):

    longueur_grille = taille_coté(grille)
    if i < 0 or i > longueur_grille -1 or j < 0 or j > longueur_grille -1:
        return False
    elif grille[i][j] ==  "":
        return True
        

# --- fonction pour savoir si la case est bien une bonne coordonnée du jeu ---
def est_une_bonne_coord(grille,i,j): 
    if (0 <= i < taille_coté(grille) and 0 <= j < taille_coté(grille)):
        return True
    return False

 # --- fonction pour savoir si le symbole de la case est correct ---
def est_un_bon_symbole(symbole): 

    if symbole == "X" or symbole == "O":
        return True
    return False


# --- Question 4 ---
def écrire(grille, i, j, symbole):

    if (0 <= i < taille_coté(grille) and 0 <= j < taille_coté(grille)) or est_vide(grille, i,j) or (symbole == "X" and symbole == "O"):

        grille[i][j] = symbole


# --- Question 5 ---
def effacer(grille, i, j):

    if grille[i][j] == "X" or grille[i][j] == "O":
        grille[i][j] = ""


# --- Question 6 ---
def est(grille, i, j, symbole):

    if est_un_bon_symbole(symbole) and est_une_bonne_coord(grille, i, j) and grille[i][j] == symbole:
        return True
    return False


# --- Question 7 ---
def affichage_grille(grille):

    for i in range(len(grille)):
        for j in range(len(grille[i])):

            # partie pour traiter si la case est vide jusqu'à l'avant dernière case
            if est_vide(grille, i, j) and j < taille_coté(grille)-1: 
                print(" ", grille[i][j], "|", end="")

            # partie pour traiter si la case n'est pas vide
            elif j < taille_coté(grille)-1:
                print("", grille[i][j], "|", end="")
            elif j == taille_coté(grille)-1:
                print("", grille[i][j], end="")        
        print("")
        
        # variable qui stock les paramètres pour afficher la ligne en pointillets 
        une_ligne_entre = "---"*(taille_coté(grille)) + "-"*(taille_coté(grille)-1)

        if i < (taille_coté(grille)-1):
            print(une_ligne_entre)


# ------- Fonction pour définir le joueur qui joue ------- 
def player(tour):
    if tour % 2 != 0:
        return "O"
    else:
        return "X"


# ------- Fonction pour définir la taille du jeu -------- 
def Taille():
    saisie = input("Entrez la taille de la grille : ")
    while saisie == "" or not saisie_entier(saisie) or int(saisie) < 3:  
        if saisie == "":
            saisie = input("Il faut saisir un entier : ")
        elif not saisie_entier(saisie):
            saisie = input("Il faut saisir un entier : ")          
        else:
            if int(saisie) < 3:
                saisie = input("Erreur, entrez un nombre supérieur ou égale à 3 :")
            
    return saisie


# ------- Fonction pour définir une grille pleine avec un compteur -------- 
def grille_pleine(grille):
    compteur = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if not est_vide(grille, i, j):
                compteur += 1
    return compteur


# ------- Fonction pour définir si on continue la partie -------- 
def continuer_partie(): 
    saisie = input("On continue ? [O]ui ou [N]on :")
    while saisie != "O" and saisie != "N":
        print("Entrez 'O' pour Oui ou 'N' pour Non")
        saisie = input("On continue ? [O]ui ou [N]on :")
    if saisie == 'O':
        return True
    elif saisie == 'N':       # ----> partie interrompue
        print("Partie interrompue !")
        return False


# ------- Fonction pour vérifier si la coordonnée rentre bien dans la grille -------- 
def bonne_coordonnée(indice, taille):
    if indice < 0:
        print("Vous avez entré un nombre négatif !")
        return False
    elif indice > taille - 1:
        print("Vous avez entré un nombre supérieur à la taille de la grille !")
        return False
    else:
        return True


# ------- Fonction pour saisir le numéro de la ligne -------- 
def numéro_ligne_saisi(taille):

    numéro_ligne = input("Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) :")
    while numéro_ligne == "" or not saisie_entier(numéro_ligne) or not bonne_coordonnée(int(numéro_ligne), taille):
        if numéro_ligne == "":
            return False      
        else:
            numéro_ligne = input("Veuillez saisir un entier ; Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) :")
    return numéro_ligne


# ------- Fonction pour saisir le numéro de la colonne -------- 
def numéro_colonne_saisi(taille):

    numéro_colonne = input("Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie) :")
    while numéro_colonne == "" or not saisie_entier(numéro_colonne) or not bonne_coordonnée(int(numéro_colonne), taille):
        if numéro_colonne == "":
            return False
        numéro_colonne = input("Veuillez saisir un entier ; Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie) :")
    return numéro_colonne
    

# ------- Vérification pour une ligne gagnante -------- 
def ligne_gagnante(grille,taille):
    res = False
    for i in range(len(grille)):
        compteur_x = 0
        compteur_o = 0
        for j in range(len(grille[i])):
            if est(grille, i, j, "X"):
                compteur_x += 1
            elif est(grille,i, j,"O"):
                compteur_o +=1         
        if (compteur_x == taille) or (compteur_o == taille): 
            res = True
    return res
    
# ------- Vérification pour une colonne gagnante -------- 
def colonne_gagnante(grille, taille):
    res = False
    for i in range(len(grille[0])):
        compteur_o = 0
        compteur_x = 0
        for j in range(len(grille)):
            if est(grille, j, i, "O"):
                compteur_o += 1
            elif est(grille, j, i, "X"):
                compteur_x += 1
        if (compteur_x == taille) or (compteur_o == taille):
            res = True
    return res

# ------- Vérification pour la première diagonale gagnante -------- 
def diagonale_1_gagnante(grille, taille):
    compteur_o = 0
    compteur_x = 0
    res = False
    for i in range(len(grille)):
        for j in range(i,i+1):
            if est(grille, i, j, "X"):
                compteur_x += 1
            elif est(grille,i, j,"O"):
                compteur_o +=1    
        if (compteur_x == taille) or (compteur_o == taille):
            res = True
    return res

# ------- Vérification pour la seconde diagonale gagnante -------- 
def diagonale_2_gagnante(grille, taille):
    compteur_o = 0
    compteur_x = 0
    res = False
    for i in range(len(grille)):
        for j in range(len(grille[i])-1-i, len(grille)-i):
            if est(grille, i, j, "X"):
                compteur_x += 1
            elif est(grille,i, j,"O"):
                compteur_o +=1    
        if (compteur_x == taille) or (compteur_o == taille):
            res = True
    return res

    
# ------- Fonction qui retourne les vérifications d'une partie gagnée -------
def partie_gagné(grille, taille):
    return ligne_gagnante(grille, taille) or colonne_gagnante(grille, taille) or diagonale_1_gagnante(grille, taille) or diagonale_2_gagnante(grille, taille)


# ------- Fonction qui enregistre le coup joué -------
def ajouter_coup(grille_graphique, ligne, colonne, symbole, grille):
    écrire(grille, int(ligne), int(colonne), symbole)
    grille_graphique.write(ligne, colonne, symbole)


# ------- Fonction qui supprime le coup joué -------
def supprimer_coup(grille_graphique, grille, dernier_coup_joué):
    effacer(grille, dernier_coup_joué[0], dernier_coup_joué[1])
    grille_graphique.erase(dernier_coup_joué[0], dernier_coup_joué[1])



# ------- Fonction pour définir si on annule le coup joué -------
def annuler_coup():
    saisie = input("Voulez-vous annuler le coup ? [O]ui ou [N]on :")
    while saisie != "O" and saisie != "N":
        print("Entrez 'O' pour Oui ou 'N' pour Non")
        saisie = input("Voulez-vous annuler le coup ? [O]ui ou [N]on :")
    if saisie == 'O':
        return True
    elif saisie == 'N': 
        return False


# ------ Fonction pour annuler un coup joué ------
def last_hit(liste, grille, grille_graphique, compteur):

    res = False 
    while not res:
        if len(liste) > 0:
            dernier_coup_joué = liste[-1]
            print("dernier coup joué :", dernier_coup_joué)
            saisie = annuler_coup()  

            if saisie == True:
                liste.pop() 
                supprimer_coup(grille_graphique,grille,dernier_coup_joué)
                compteur -= 1 
                jouer_encore = continuer_partie()
                if jouer_encore == True:
                    pass
                else:
                    res = True
                    jouer_encore = False  
                    return False                        
            else:
                res = True               
        else:     
            res = True
            
    return compteur

    

# ------ Contrôle de saisie d'un entier ------
def saisie_entier(mot):
    carac = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in str(mot):
        drapeau = False
        for j in carac:
            if i == j:
                drapeau = True
        if drapeau == False:
            return False
    return True
    
# ------ Fonction fin de jeu ------
def end_game(compteur, taille, grille, joueur):
    if partie_gagné(grille, int(taille)):
        print("le joueur", joueur, "a gagné")
        return True
    elif compteur == int(taille)**2 and not partie_gagné(grille, int(taille)):
        print("Égalité !")
        return True
    # elif not continuer_partie():
    #     return True
    else:
        return False

    

# ------------------ DÉROULEMENT DU JEU ------------------
def jeu():

    taille_saisi_pour_jouer = Taille()
    graphique = GraphicalGrid(int(taille_saisi_pour_jouer))
    nouvelle_grille = crée_grille(int(taille_saisi_pour_jouer))
    compteur_tour = 0
    historique = []

    jouer_encore = continuer_partie()

    while jouer_encore:
   
            joueur_qui_joue = player(compteur_tour)
            print("C'est au tour du joueur ", joueur_qui_joue)
        
            numéro_ligne_joueur = numéro_ligne_saisi(int(taille_saisi_pour_jouer))
            while not numéro_ligne_joueur:
                print("C'est au tour du joueur ", joueur_qui_joue)
                numéro_ligne_joueur = numéro_ligne_saisi(int(taille_saisi_pour_jouer))  
                            
            numéro_colonne_joueur = numéro_colonne_saisi(int(taille_saisi_pour_jouer))
            if numéro_colonne_joueur:
                while not est_vide(nouvelle_grille, int(numéro_ligne_joueur), int(numéro_colonne_joueur)):
                    print("Cette case n'est pas vide ! ")
                    numéro_ligne_joueur = numéro_ligne_saisi(int(taille_saisi_pour_jouer))
                    numéro_colonne_joueur = numéro_colonne_saisi(int(taille_saisi_pour_jouer))

                ajouter_coup(graphique, int(numéro_ligne_joueur), int(numéro_colonne_joueur),joueur_qui_joue, nouvelle_grille)
                compteur_tour += 1
                compteur_cases = grille_pleine(nouvelle_grille)
                game = end_game(compteur_cases, taille_saisi_pour_jouer, nouvelle_grille, joueur_qui_joue)

                if game == True:
                    jouer_encore = False
                else:
                    jouer_encore = continuer_partie()                               
                    if not jouer_encore:
                        jouer_encore = False           
                    else:
                        historique.append((int(numéro_ligne_joueur), int(numéro_colonne_joueur), joueur_qui_joue))
                        compteur_tour_diff = last_hit(historique, nouvelle_grille, graphique, compteur_tour)         
                        compteur_tour = compteur_tour_diff
            print()
        
    graphique.wait_quit()
                    
jeu()



