import random

Randomint = random.randint(1, 10)  # Random number between 1 and 10
guess = 0
attempts = 5

print("Devinez un nombre de 1 à 10 ! Vous n'avez que 5 chances !")

for i in range(attempts):
    guess = int(input("Entrez votre devinette : "))
    
    if guess < 1 or guess > 10:
        print("Mauvais numéro ! Veuillez choisir un nombre entre 1 et 10.")
        continue  
    
    if guess == Randomint:
        print("Correct ! Vous avez deviné le bon nombre !")
        break  
    elif guess < Randomint:
        print("Trop bas, essayez encore.")
    else:
        print("Trop haut, essayez encore.")
    
    # Provide feedback on remaining attempts
    remaining_attempts = attempts - i - 1
    if remaining_attempts > 0:
        print(f"Il vous reste {remaining_attempts} essais.")

if guess != Randomint:
    print(f"Désolé, le nombre correct était {Randomint}.")
