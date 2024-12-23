import random

latter = "AZERTYUIOPQSDFGHJKLMWXCVBN"
nomber = "123456789"
symbol = "%ùµ*;!§#[]'():"
caractere = latter + latter.lower() + nomber + symbol
caractere_no_symbol = latter + latter.lower() + nomber

while True:
    longueur_mdp = int(input("Entrez la longueur du mot de passe : "))
    nombre_mdp = int(input("Entrez le nombre de mots de passe à afficher : "))
    caractere_speciaux_ask = input("Dois-je mettre des caractères spéciaux dans le mot de passe ? (oui/non) : ").strip().lower()

    if caractere_speciaux_ask == 'oui':
        for _ in range(nombre_mdp):
            mdp = "".join(random.choice(caractere) for _ in range(longueur_mdp))
            print("Votre mot de passe est :", mdp)
    elif caractere_speciaux_ask == 'non':
        for _ in range(nombre_mdp):
            mdp = "".join(random.choice(caractere_no_symbol) for _ in range(longueur_mdp))
            print("Votre mot de passe est :", mdp)
    else:
        print("ERREUR : Veuillez répondre par 'oui' ou 'non'.")
