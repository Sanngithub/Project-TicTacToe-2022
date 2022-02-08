def test_entier(saisie):
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
            print("1er cas")
            return False

        elif sign and not space and (saisie[i] in signes):
            print("1er cas bis")
            return False

        elif not space and not sign and not number and (saisie[i] not in nombres and saisie[i] not in signes and saisie[i] != " "):
            print("2eme cas : chaine de caractère")
            return False
  
        elif space and saisie[i] in allLetters:
            print("3eme cas ")
            return False

        elif number and space and sign and (saisie[len(saisie) - 1] in signes):
            print("4eme cas")
            return False

        elif number and saisie[i] in signes:
            print("5eme cas")
            return False 

        elif spaceAfterNumber and saisie[i] in nombres:
            return False 


        # initilisation des drapeaux
        elif saisie[i] == "+" or saisie[i] == "-":
            print(" sign ")
            sign = True 
        elif saisie[i] in nombres:
            print(" number ")
            number = True 
        elif saisie[i] == " ":
            print(" space ")
            space = True 
            if number: # number true avant que space soit true, alors spaceAfterNumber true 
                spaceAfterNumber = True
    
    if not number:
        return False
             
    return True 

def bonne_coordonnée(indice, taille):
    if indice < 0:
        print("Vous avez entré un nombre négatif !")
        return False
    elif indice > taille - 1:
        print("Vous avez entré un nombre supérieur à la taille de la grille !")
        return False
    else:
        return True


def numéro_ligne_saisi(taille):

    numéro_ligne = input("Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) :")
    while numéro_ligne != "" and (not test_entier(numéro_ligne) or not bonne_coordonnée(int(numéro_ligne), taille)):
        numéro_ligne = input("Erreur ! Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) :")
    return numéro_ligne


def Taille():
    saisie = input("Entrez la taille de la grille : ")
    while saisie == "" or not test_entier(saisie) or int(saisie) < 3:  
        if saisie == "":
            saisie = input("Il faut saisir un entier : ")
        elif not test_entier(saisie):
            saisie = input("Erreur: FALSE A à la fonction test_entier :  Il faut saisir un entier : ")          
        else:
            if int(saisie) < 3:
                saisie = input("Erreur, nombre entrez un nombre supérieur ou égale à 3 :")       
    return int(saisie)


gameSize = Taille()
lignNumber = numéro_ligne_saisi(gameSize)
print(lignNumber)







# def Taille():
#     saisie = input("Entrez la taille de la grille : ")
#     while saisie == "" or saisie=="+" or saisie=="-" or not test_entier(saisie) or int(saisie) < 3:  
#         if saisie == "" or saisie=="+" or saisie=="-":
#             saisie = input("Il faut saisir un entier : ")
#         elif not test_entier(saisie):
#             saisie = input("Erreur, Il faut saisir un entier : ")          
#         else:
#             if int(saisie) < 3:
#                 saisie = input("Erreur, entrez un nombre supérieur ou égale à 3 :")       
#     return int(saisie)



# x = Taille()

# print("mon entier = ", int(x))



    




# sign = ["+", "-", " "]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# count = 0

# if saisie == "+1" or saisie == "+2" or saisie == "+3" or saisie == "+4" or saisie == "+5" or saisie == "+6" or saisie == "+7" or saisie == "+8" or saisie == "+9" :
#     print(saisie[1])
#     print("cas signe + ok")
# elif saisie == "-1" or saisie == "2" or saisie == "-3" or saisie == "-4" or saisie == "-5" or saisie == "-6" or saisie == "-7" or saisie == "-8" or saisie == "-9":
#     print(saisie[1])
#     print("cas signe - ok")
# else:
#     print("deux cas marche pas")



        

