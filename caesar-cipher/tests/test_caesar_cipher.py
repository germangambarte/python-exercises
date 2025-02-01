import unittest
from main import CaesarCipher


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cipher = CaesarCipher()
        cls.decoded_text = "Happy hacking!"
        cls.encoded_text = "Ohwwf ohjrpun!"
        cls.special_characters = "12345 ! @ #"

    def test_encoding(self):
        output = self.cipher.encode(self.decoded_text)
        self.assertEqual(self.encoded_text, output)

    def test_decoding(self):
        output = self.cipher.decode(self.encoded_text)
        self.assertEqual(self.decoded_text, output)

    def test_special_chars_encode(self):
        output = self.cipher.encode(self.special_characters)
        self.assertEqual(self.special_characters, output)

    def test_special_chars_decode(self):
        output = self.cipher.decode(self.special_characters)
        self.assertEqual(self.special_characters, output)


if __name__ == '__main__':
    unittest.main()
