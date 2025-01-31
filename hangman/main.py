import os

total_lifes = 6
lifes_consumed = 0
wins = False
draw = [
    "\t   ************\n\t   |          *\n\t              *\n\t              *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t              *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t   |          *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|          *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t  /           *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t  / \\         *\n\t            *****\n\t          *********\n",
]

word = input("Ingrese la palabra para la partida: ")
while not word.isalpha():
    print("\nPalabra no válida.")
    print("No se aceptan números, ni caracteres especiales.\n")
    word = input("Ingrese la palabra para la partida: ")

os.system("clear")
print("Palabra válida. EL JUEGO YA COMENZÓ!\n")

word = list(word.upper())
progression = ["_" for _ in word]
inputs = []


def print_stats():
    print("hoi")
    print(end="\n")
    print(f"Vidas restantes: {total_lifes - lifes_consumed}")
    print(end="\n")
    print(draw[lifes_consumed])
    print(progression)
    print(end="\n")


def append_letters(letter):
    for i, l in enumerate(word):
        if l == letter:
            progression[i] = word[i]


def valid(letter):
    if not letter.isalpha():
        print("\nNo se aceptan números, ni caracteres especiales.\n")
        return False
    if inputs.__contains__(letter):
        print(f"\nLa letra {letter!r} ya fué ingresada\n")
        return False
    return True


while lifes_consumed < total_lifes and not wins:
    letter = input("Ingrese una letra: ").upper()

    if not valid(letter):
        continue
    else:
        inputs.append(letter)

    if word.__contains__(letter):
        append_letters(letter)
    else:
        lifes_consumed += 1
    
    print_stats()
    if progression.count("_") == 0:
        wins = True
if wins:
    print("Felicitaciones por la victoria!!!.")
else:
    print("Te quedaste sin vidas. Perdiste la partida :/")
