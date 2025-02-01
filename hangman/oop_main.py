import os

DRAW = [
    "\t   ************\n\t   |          *\n\t              *\n\t              *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t              *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t   |          *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|          *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t              *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t  /           *\n\t            *****\n\t          *********\n",
    "\t   ************\n\t   |          *\n\t  ( )         *\n\t  /|\\         *\n\t  / \\         *\n\t            *****\n\t          *********\n",
]


class Hangman:
    def __init__(self, word: str):
        self.__total_lives = 6
        self.__remaining_lives = self.__total_lives
        self.__user_won = False
        self.__user_inputs = []
        self.__current_letter = ""
        self.__word = list(word.upper())
        self.__progression = ["_" for _ in self.__word]

    def draw(self):
        print("Palabra válida. EL JUEGO YA COMENZÓ!\n")

        while self.__remaining_lives > 0 and not self.__user_won:
            self.__current_letter = input("Ingrese una letra: ").upper()
            print(f"letter: {self.__current_letter}")

            if not self.valid_letter():
                continue
            else:
                self.__user_inputs.append(self.__current_letter)
            if self.__word.__contains__(self.__current_letter):
                self.append_letters()
            else:
                self.__remaining_lives -= 1

            self.print_stats()
            if self.__progression.count("_") == 0:
                self.__user_won = True
        if self.__user_won:
            print("Felicitaciones por la victoria!!!.")
        else:
            print("Te quedaste sin vidas. Perdiste la partida :/")

    def print_stats(self):
        print("hoi")
        print(end="\n")
        print(f"Vidas restantes: {self.__remaining_lives}")
        print(end="\n")
        print(DRAW[self.__total_lives - self.__remaining_lives])
        print(self.__progression)
        print(end="\n")

    def append_letters(self):
        for i, l in enumerate(self.__word):
            if l == self.__current_letter:
                self.__progression[i] = self.__word[i]

    def valid_letter(self):
        if not self.__current_letter.isalpha():
            print("\nNo se aceptan números, ni caracteres especiales.\n")
            return False
        if self.__user_inputs.__contains__(self.__current_letter):
            print(f"\nLa letra {self.__current_letter!r} ya fué ingresada\n")
            return False
        return True


if __name__ == "__main__":
    word = input("Ingrese la palabra para la partida: ")
    while not word.isalpha():
        print("\nPalabra no válida.")
        print("No se aceptan números, ni caracteres especiales.\n")
        word = input("Ingrese la palabra para la partida: ")

    hangman = Hangman(word)
    os.system("clear")
    hangman.draw()
