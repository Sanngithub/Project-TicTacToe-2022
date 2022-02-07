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


# ------ Contrôle de saisie d'un entier pour chaque entrées dans le jeu, je vérifie mes cas dans des if ------
def is_goodInt(saisie):
    # Veuillez m'excuser en avance si cette fonction vous semble longue. 
    sign = False 
    number = False 
    space = False  
    spaceAfterNumber = False

    nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    signes = ["+", "-"]
    lower = "azertyuiopqsdfghjklmwxcvbn"
    upper = "AZERTYUIOPQSDFGHJKLMWXCVBN"
    allLetters = lower + upper 

    for i in range(len(saisie)):

        if sign and not number and (saisie[i] == " " or saisie[i] in signes):
            return False

        elif sign and not space and (saisie[i] in signes):
            return False

        elif not space and not sign and not number and (saisie[i] not in nombres and saisie[i] not in signes and saisie[i] != " "):
            return False
  
        elif space and saisie[i] in allLetters:
            return False

        elif number and space and sign and (saisie[len(saisie) - 1] in signes):
            return False

        elif number and saisie[i] in signes:
            return False 

        elif spaceAfterNumber and saisie[i] in nombres:
            return False 

        # initilisation des drapeaux pour les vérifications
        elif saisie[i] == "+" or saisie[i] == "-":
            sign = True 
        elif saisie[i] in nombres:
            number = True 
        elif saisie[i] == " ":
            space = True 
            if number: # si number est true avant que space soit true, alors spaceAfterNumber true 
                spaceAfterNumber = True
    
    if not number:
        return False
             
    return True


# ------- Fonction pour saisir la taille du jeu -------- 
def Taille():
    saisie = input("Entrez la taille de la grille : ")
    while saisie == "" or not is_goodInt(saisie) or int(saisie) < 3:  
        if saisie == "":
            saisie = input("Il faut saisir un entier : ")
        elif not is_goodInt(saisie):
            saisie = input("Erreur, Il faut saisir un entier : ")          
        else:
            if int(saisie) < 3:
                saisie = input("Erreur, entrez un nombre supérieur ou égale à 3 :")       
    return saisie


# ------- Fonction pour définir une grille pleine en retournant un compteur -------- 
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
    elif saisie == 'N':   # ----------------> Partie interrompue
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
    while numéro_ligne != "" and (not is_goodInt(numéro_ligne) or not bonne_coordonnée(int(numéro_ligne), taille)):
        numéro_ligne = input("Veuillez saisir un entier ; Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) :")
    return numéro_ligne


# ------- Fonction pour saisir le numéro de la colonne -------- 
def numéro_colonne_saisi(taille):

    numéro_colonne = input("Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie) :")
    while numéro_colonne != "" and (not is_goodInt(numéro_colonne) or not bonne_coordonnée(int(numéro_colonne), taille)):
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
                compteur_o += 1         
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
def partie_gagnée(grille, taille):
    return ligne_gagnante(grille, taille) or colonne_gagnante(grille, taille) or diagonale_1_gagnante(grille, taille) or diagonale_2_gagnante(grille, taille)


# ------- Fonction qui écrit un coup joué dans l'historique et dans la grille -------
def ajouter_coup(grille_matrix, ligne, colonne, symbole, grille, mon_historique):
    mon_historique.append((int(ligne), int(colonne), symbole))
    écrire(grille, int(ligne), int(colonne), symbole)
    grille_matrix.write(ligne, colonne, symbole)


# ------- Fonction qui supprime le coup joué dans l'historique et dans la grille -------
def supprimer_coup(grille_matrix, grille, mon_historique):
    dernier_coup_joué = mon_historique.pop()
    effacer(grille, dernier_coup_joué[0], dernier_coup_joué[1])
    grille_matrix.erase(dernier_coup_joué[0], dernier_coup_joué[1])



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

    
# ------ Fonction fin de jeu ------
def end_game(compteur, taille, grille, joueur_symbole):
    if partie_gagnée(grille, int(taille)):
        print("le joueur", joueur_symbole, "a gagné")
        return True
    elif compteur == int(taille)**2 and not partie_gagnée(grille, int(taille)):
        print("Égalité !")
        return True
    else:
        return False


# ------------------ DÉROULEMENT DU JEU ------------------
def jeu():
    
    gameSize = Taille()
    matrix = GraphicalGrid(int(gameSize))
    newMatrix = crée_grille(int(gameSize))
    tourCounter = 0
    historique = []
    game = False
    case_invalide = False
    playAgain = continuer_partie()
    
    while playAgain:   

        if len(historique) > 0 and not case_invalide:

            dernier_coup_joué = historique[len(historique)-1]
            print("dernier coup joué :", dernier_coup_joué)
            cancel_hit = annuler_coup()
            if cancel_hit:
                supprimer_coup(matrix, newMatrix, historique)
                tourCounter -= 1  

        if len(historique) == 0 or not cancel_hit or case_invalide:  

            case_invalide = False
            joueur_qui_joue = player(tourCounter)
            print("C'est au tour du joueur ", joueur_qui_joue)

            numéro_ligne_joueur = numéro_ligne_saisi(int(gameSize))

            if numéro_ligne_joueur != "":                                    
                numéro_colonne_joueur = numéro_colonne_saisi(int(gameSize))

                if numéro_colonne_joueur != "":
                    if not est_vide(newMatrix, int(numéro_ligne_joueur), int(numéro_colonne_joueur)):
                        print()
                        print("Cette case n'est pas vide ! ")     
                        case_invalide = True 
                    else:
                        ajouter_coup(matrix, int(numéro_ligne_joueur), int(numéro_colonne_joueur), joueur_qui_joue, newMatrix, historique)                       
                        tourCounter += 1
                        compteur_cases = grille_pleine(newMatrix)
                        game = end_game(compteur_cases, int(gameSize), newMatrix, joueur_qui_joue)

                        if game:
                            playAgain = False

        if not game and not case_invalide:
            playAgain = continuer_partie()
         
    matrix.wait_quit()
                    
jeu()



