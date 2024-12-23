import random
print("********hangman game*********")
def hangman():
    # List of words to choose from
    words = ['canada', 'italy', 'brazil', 'Algeria', 'iran', 'spain', 'maroco', 'Egypt','tunisia','irak','libya']
    # Randomly select a word
    word = random.choice(words).lower()
    guessed_word = ['_'] * len(word) # len : returnue la langeur de mots choise
    attempts = 6  # Nombre de tentatives incorrectes autorisées
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word:", ' '.join(guessed_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha(): #isalpha vérifie si tous les caractères de la chaîne d'entrée sont des caractères alphabétiques.
            print("Please enter a single valid letter.")
            continue

        # Vérifiez si la lettre a déjà été devinée
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess) #append : Il s'agit d'une méthode de l'objet liste qui ajoute l'élément spécifié (dans ce cas, la variable de supposition) à la fin de la liste.

        if guess in word:
           # Révélez la lettre devinée dans le mot
            for i, letter in enumerate(word):
                #enumerate():fonction génératrice intégrée qui vous permet de parcourir une séquence (comme une liste, un tuple ou une chaîne) tout en gardant une trace de l'index de chaque élément. +
                if letter == guess:
                    guessed_word[i] = guess
            print("Good job! The word now looks like this:", ' '.join(guessed_word))
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")

       # Vérifiez si le joueur a deviné le mot
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word:", word)
            break

    if attempts == 0:
        print("Game over! You've run out of attempts.")
        print("The word was:", word)

# Start the game
hangman()