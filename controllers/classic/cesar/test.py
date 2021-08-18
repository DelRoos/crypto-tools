# from controllers.classic.cesar import controller as cesar
import  unittest
import controllers.classic.cesar.controller as cesar

class CesarTest(unittest.TestCase):
    def test_cesar_crypt(self):
        self.assertEqual(
            cesar.encode_decode(text="delano.", keys=[3,2]),
            {
                'method': 'Cesar', 
                'text': 'delano', 
                'result': [
                    {
                        'key': 3, 
                        'text': 'ghodqr'
                    }, 
                    {
                        'key': 2, 
                        'text': 'fgncpq'
                    }
                ]
            }
        )

    def test_cesar_decrypt(self):
        self.assertEqual(
            cesar.encode_decode(text="ghodqr", keys=[3, 2], crypt=False),
            {
                'method': 'Cesar', 
                'text': 'ghodqr', 
                'result': [
                    {
                        'key': 3, 
                        'text': 'delano'
                    }, 
                    {
                        'key': 2, 
                        'text': 'efmbop'
                    }
                ]
            }
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
