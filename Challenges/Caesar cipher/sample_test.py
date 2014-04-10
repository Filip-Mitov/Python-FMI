import unittest
import io
import sys

from solution import ceaser_output, ceaser_input


class Tests():

    @ceaser_output(13)
    def cross_the_river():
        return "ALEA IACTA EST"

    @ceaser_output(-2)
    def actual_test():
        return "ku vjku CP CeVWcn WPKVVGUV?"

    @ceaser_output(26)
    def same_test():
        return "only upper case, same text"

    @ceaser_output(-17)
    def no_letters():
        return "1 2 3 4 127 0 [ ] ) :"

    @ceaser_input(-13, lambda key: key > 0)
    def make_a_speech(name, *args):
        print('{} says:\n{}'.format(name, ' '.join(args)))

    @ceaser_input(3, lambda key: key % 2 == 0)
    def odd_positions(*args):
        print('{}'.format(' '.join(args)))

    @ceaser_input(-7, lambda key: key >= 0)
    def shift_alphabet(*args):
        print('{}'.format(''.join(args)))


class CeaserOutputTest(unittest.TestCase):

    def test_ceaser_output(self):
        self.assertEqual(Tests.cross_the_river(), "NYRN VNPGN RFG")
        self.assertEqual(Tests.actual_test(), "IS THIS AN ACTUAL UNITTEST?")
        self.assertEqual(Tests.same_test(), "ONLY UPPER CASE, SAME TEXT")
        self.assertEqual(Tests.no_letters(), "1 2 3 4 127 0 [ ] ) :")


class CeaserInputTest(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_ceaser_input1(self):
        Tests.make_a_speech('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                            'RIRE', 'QBAR', 'SBE', 'HF?', '...')
        self.assertEqual(
            sys.stdout.getvalue(),
            "Reg says:\nWHAT HAVE THE ROMANS EVER DONE FOR US? ...\n")

    def test_ceaser_input2(self):
        Tests.odd_positions('a', 'b', 'cdefg', 'hi', 'JKL',
                            'm', 'n', 'OPQRSTU', 'V', 'WXYZ')
        self.assertEqual(
            sys.stdout.getvalue(),
            "D b FGHIJ hi MNO m Q OPQRSTU Y WXYZ\n")

    def test_ceaser_input3(self):
        Tests.shift_alphabet('a', 'b', 'c', 'd', 'e', 'f', 'G', 'H', 'I', 'J',
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'T',
                             'U', 'v', 'w', 'x', 'y', 'z')
        self.assertEqual(sys.stdout.getvalue(), "TUVWXYZABCDEFGHIJKLMNOPQRS\n")

    def tearDown(self):
        sys.stdout = self.held


# Tests from George Staikov
class TestCesar(unittest.TestCase):

    def test_ceaser_output1(self):
        @ceaser_output(13)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "NYRN VNPGN RFG")

    def test_ceaser_output2(self):
        @ceaser_output(-13)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "NYRN VNPGN RFG")

    def test_ceaser_output3(self):
        @ceaser_output(52)
        def test_function():
            return "ALEA IACTA EST"
        self.assertEqual(test_function(), "ALEA IACTA EST")

    def test_ceaser_output4(self):
        @ceaser_output(23)
        def test_function():
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(test_function(), "XYZABCDEFGHIJKLMNOPQRSTUVW")

    def test_ceaser_output5(self):
        @ceaser_output(872136871623)
        def test_function():
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(test_function(), "RSTUVWXYZABCDEFGHIJKLMNOPQ")

    def test_ceaser_input1(self):
        @ceaser_input(-13, lambda key: key > 0)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                          'RIRE', 'QBAR', 'SBE', 'HF?', '...'),
            "Reg says: WHAT HAVE THE ROMANS EVER DONE FOR US? ...")

    def test_ceaser_input2(self):
        @ceaser_input(3, lambda key: key > 0)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('George', "QEB NRFZH YOLTK", "CLU GRJMP LSBO",
                          "QEB IXWV ALD"),
            "George says: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

    def test_ceaser_input3(self):
        @ceaser_input(-13, lambda key: key > 2)
        def test_function(name, *args):
            return '{} says: {}'.format(name, ' '.join(args))
        self.assertEqual(
            test_function('Reg', 'JUNG', 'UNIR', 'GUR', 'EBZNAF',
                          'RIRE', 'QBAR', 'SBE', 'HF?', '...'),
            "Reg says: JUNG UNIR THE ROMANS EVER DONE FOR US? ...")

if __name__ == '__main__':
    unittest.main()