import string


class CaesarCipher:
    __alphabet = list(string.ascii_lowercase)

    def encode(self, input: str):
        output = ''
        for value in input:
            if not value.isalpha():
                output += value
                continue
            output += self.__encode_letter(value)
        return output

    def decode(self, input: str):
        output = ''
        for value in input:
            if not value.isalpha():
                output += value
                continue
            output += self.__decode_letter(value)
        return output

    def __encode_letter(self, letter: str):
        is_upper = letter.isupper()
        letter = letter.lower()
        letter_index = self.__alphabet.index(letter)
        index = (letter_index + 7) % len(self.__alphabet)
        output = self.__alphabet[index]
        return output.upper() if is_upper else output

    def __decode_letter(self, letter: str):
        is_upper = letter.isupper()
        letter = letter.lower()
        letter_index = self.__alphabet.index(letter)
        index = (letter_index - 7) % len(self.__alphabet)
        output = self.__alphabet[index]
        return output.upper() if is_upper else output
