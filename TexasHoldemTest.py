import unittest
from TexasHoldem import TexasHoldem


class TestTexasHoldem(unittest.TestCase):
    def test_input(self):
        texasholdem = TexasHoldem("1S,5D,AH,3D,1C", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem
        texasholdem = TexasHoldem("1S 5D AH 3D 1C", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), True)
        del texasholdem
        texasholdem = TexasHoldem("1S 5D AH 3D", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem
        texasholdem = TexasHoldem("1TTT 5D AH 3D 1C", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem


if __name__ == '__main__':
    unittest.main()
