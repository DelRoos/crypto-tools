from controllers.classic.substitution.vigenere import controller as vigenere
from controllers.classic.cesar import test as test_cesar
from controllers.classic.substitution.vigenere import test as test_vigenere
import unittest

if __name__ == '__main__':

    print("==== Vigenere crypthographie method test ========\n\n")
    vigenere_t = unittest.TestLoader().loadTestsFromModule(test_vigenere)
    unittest.TextTestRunner(verbosity=2).run(vigenere_t)
    print("\n\n==== --------------------------------- ========")

    print("==== Cesar crypthographie method test ========\n\n")
    cesar_t = unittest.TestLoader().loadTestsFromModule(test_cesar)
    unittest.TextTestRunner(verbosity=2).run(cesar_t)
    print("\n\n==== --------------------------------- ========")
