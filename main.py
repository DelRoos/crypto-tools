from controllers.classic.cesar import controller as cesar
from controllers.classic.cesar import test as test_cesar
import unittest

if __name__ == '__main__':
    print("==== Cesar crypthographie method test ========\n\n")
    suite = unittest.TestLoader().loadTestsFromModule(test_cesar)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print("\n\n==== --------------------------------- ========")
