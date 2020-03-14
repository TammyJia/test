import unittest
from TexasHoldem import TexasHoldem


class TestTexasHoldem(unittest.TestCase):
    def test_input(self):
        texasholdem = TexasHoldem("1S,5D,AH,3D,1C", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem
        texasholdem = TexasHoldem("2H 3D 5S 9C KD", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), True)
        del texasholdem
        texasholdem = TexasHoldem("1S 5D AH 3D", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem
        texasholdem = TexasHoldem("1TTT 5D AH 3D 1C", "2C 3H 4S 8C AH")
        self.assertEqual(texasholdem.check_input(), False)
        del texasholdem

    def test_sortcards(self):
        texasholdem = TexasHoldem("2H 3D 5S 9C KD", "2C 3H 4S 8C AH")
        texasholdem.card_sort()
        self.assertEqual(texasholdem.newblack, ['KD', '9C', '5S', '3D', '2H'])
        self.assertEqual(texasholdem.newwhite, ['AH', '8C', '4S', '3H', '2C'])

        texasholdem.newblack = ['7D', '9C', '7S', '3D', '8H']
        texasholdem.newwhite = ['3H', '5D', '3S', '5C', '3D']
        texasholdem.card_sort()
        print(texasholdem.newblack)
        print(texasholdem.newwhite)
        self.assertEqual(texasholdem.newblack, ['7D', '7S', '9C', '8H', '3D'])
        self.assertEqual(texasholdem.newwhite, ['3S', '3D', '3H', '5D', '5D'])

        del texasholdem


if __name__ == '__main__':
    unittest.main()
