import unittest
import rev_binary

class TestSpotify(unittest.TestCase):

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def test_reverse(self):
        test = rev_binary.reverse('10')
        self.assertEqual(test, '01')
        test = rev_binary.reverse('1011011')
        self.assertEqual(test, '1101101')

    def test_to_binary(self):
        test = rev_binary.to_binary(13)
        self.assertEqual(test, '1101')

    def test_to_integer(self):
        test = rev_binary.to_integer('1011')
        self.assertEqual(test, 11)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
