# from controllers.classic.cesar import controller as cesar
import  unittest
import controllers.classic.substitution.vigenere.controller as vigenere

class VigenereTest(unittest.TestCase):
    def test_cesar_crypt(self):
        self.assertEqual(
            vigenere.encode_decode(text="delanoroosvelttoungsiyoumbissi", keys=["cyndi", "loic"]),
            {
                'action': 'Crypt',
                'method': 'Vigenere', 
                'text': 'delanoroosvelttoungsiyoumbissi', 
                'result': [
                    {
                        'key': 'cyndi', 
                        'text': 'fcydvqpbraxcywbqsajakwbxudgfvq'
                    }, 
                    {
                        'key': 'loic', 
                        'text': 'ostcyczqzgdgwhbqfboutmwwxpqudw'
                    }
                ]
            }
        )

    def test_cesar_decrypt(self):
        self.assertEqual(
            vigenere.encode_decode(text="fcydvqpbraxcywbqsajakwbxudgfvq", keys=["cyndi", "loic"], crypt=False),
            {
                'action': 'Decrypt',
                'method': 'Vigenere', 
                'text': 'fcydvqpbraxcywbqsajakwbxudgfvq', 
                'result': [
                    {
                        'key': 'cyndi', 
                        'text': 'delanoroosvelttoungsiyoumbissi'
                    }, 
                    {
                        'key': 'loic', 
                        'text': 'uoqbkchzgmpanitohmbyzitvjpydkc'
                    }
                ]
            }
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
