# fully PEP8-compliant collection of tests for 2014/02-five_functions

import unittest

import solution


class TestFiveFunctions(unittest.TestCase):
    # sample tests

    def test_is_pangram(self):
        # fmi/sample_test.py
        self.assertFalse(
            solution.is_pangram('Малката пухкава панда яде бамбук.'))

        self.assertTrue(
            solution.is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'))

        # stoyaneft/tests.py - uppercase letters
        self.assertTrue(
            solution.is_pangram('АБВ ГДЕЖЗ ЯЮъьЩшчц ийКлМН опрстуфьдх'))

        self.assertTrue(
            solution.is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'.upper()))

        # stoyaneft/tests.py - latin letters
        self.assertFalse(
            solution.is_pangram(
                'Ах, чудна българска зеmьо, полюшвай цъфтящи жита!'))

        self.assertTrue(
            solution.is_pangram(
                'Ах, чудна българска земmьо, полюшвай цъфтящи жита!'))

        # antonionikolov/is_pangram.py
        self.assertTrue(
            solution.is_pangram('За миг бях в чужд, скърцащ плюшен фотьойл.'))

        self.assertTrue(
            solution.is_pangram(
                'Хълцащ змей плюе шофьор стигнал чуждия бивак.'))

        self.assertTrue(
            solution.is_pangram(
                'Шугав льохман, държащ птицечовка без сейф и ютия.'))

        self.assertTrue(
            solution.is_pangram(
                'Шейхът-глупак ще изяжда дървена сьомга без юфчица.'))

        self.assertTrue(
            solution.is_pangram(
                'Щурчо Цоньо хапваше ловджийско кюфте с бяла гъмза.'))

        self.assertFalse(
            solution.is_pangram(
                'Отидох у леля ми, която беше направила сладки.'))

        self.assertFalse(
            solution.is_pangram(
                'Човекът влезе в апарата, закрепи се здраво на подпорите, '
                + 'завърза въже около тялото си.'))

    def test_char_histogram(self):
        # fmi/sample_test.py
        self.assertEqual(
            {' ': 3, 'i': 2, 'a': 2, 'e': 2, 's': 2, 'h': 1, 'l': 1, 'm': 1,
             'n': 1, 'x': 1, '!': 1, 'p': 1, 'T': 1},
            solution.char_histogram('This is an example!'))

        # stoyaneft/tests.py
        self.assertEqual(
            solution.char_histogram(
                'Ах, чудна българска зеmьо, полюшвай цъфтящи жита!'),
            {'m': 1, ',': 2, '!': 1, ' ': 6, 'л': 2, 'к': 1, 'й': 1, 'и': 2,
             'п': 1, 'о': 2, 'н': 1, 'г': 1, 'в': 1, 'б': 1, 'а': 5, 'з': 1,
             'ж': 1, 'е': 1, 'д': 1, 'ъ': 2, 'щ': 1, 'ш': 1, 'я': 1, 'ю': 1,
             'ь': 1, 'у': 1, 'т': 2, 'с': 1, 'р': 1, 'ч': 1, 'ц': 1, 'х': 1,
             'ф': 1, 'А': 1})

        self.assertEqual(
            solution.char_histogram('aaaabbaaaabaa'), {'a': 10, 'b': 3})

    def test_sort_by(self):
        # fmi/sample_test.py
        self.assertEqual(
            ['a', 'ab', 'abc'],
            solution.sort_by(lambda x, y: len(x) - len(y), ['abc', 'a', 'ab']))

        # stoyaneft/tests.py
        self.assertEqual(
            solution.sort_by(lambda x, y: len(y) - len(x),
                             ['abc', 'a', 'ab', 'Pesho', [1, 2, 3, 4]]),
            ['Pesho', [1, 2, 3, 4], 'abc', 'ab', 'a'])

        # Ralitsa-Ts/tests.py
        words = ['hey', 'hi', 'hello', 'buy', 'io', 'a']
        self.assertEqual(
            ['a', 'hi', 'io', 'hey', 'buy', 'hello'],
            solution.sort_by(lambda x, y: len(x) - len(y), words))

        self.assertEqual(
            [3, 3, 5, 10, 15, 30, 100],
            solution.sort_by(lambda x, y: x - y, [15, 3, 10, 100, 5, 3, 30]))

        self.assertEqual(
            [1, 2, 7, 9, 15, 32, 33],
            solution.sort_by(lambda x, y: x - y, [7, 2, 9, 1, 15, 33, 32]))

        self.assertEqual(
            [0, 4, 4, 5, 11, 12, 16],
            solution.sort_by(lambda x, y: x - y, [12, 5, 4, 16, 0, 4, 11]))

    def test_group_by_type(self):
        # fmi/sample_test.py
        self.assertEqual(
            {str: {'b': 1, 'a': 12}, int: {1: 'foo'}},
            solution.group_by_type({'a': 12, 'b': 1, 1: 'foo'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b'}, tuple: {(1, 2): 12, ('a', 1): 1}},
            solution.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b', 'c': 15}))

        # stoyaneft/tests.py
        self.assertEqual(
            solution.group_by_type(
                {int: 2, str: 'a', (1,): [1, 2], 'a': (1, 'v')}),
            {type: {str: 'a', int: 2}, tuple: {(1,): [1, 2]},
                str: {'a': (1, 'v')}})

        # Ralitsa-Ts/tests.py
        self.assertEqual(
            {str: {'val': 5, 'var': 7}, int: {1: 2}, tuple: {(3, 4): 'c'}},
            solution.group_by_type({'val': 5, 'var': 7, 1: 2, (3, 4): 'c'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b', 12: 202},
             tuple: {(1, 2): 12, ('a', 1): 1, (3, 4, 5, 6): 7}},
            solution.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b',
                                    (3, 4, 5, 6): 7, 'c': 15, 12: 202}))

    def test_anagrams(self):
        # fmi/sample_test.py
        words = ['army', 'mary', 'ramy', 'astronomer', 'moonstarer',
                 'debit card', 'bad credit', 'bau']
        anagrams = [['army', 'mary', 'ramy'], ['bad credit', 'debit card'],
                    ['astronomer', 'moonstarer'], ['bau']]

        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))

        # stoyaneft/tests.py
        words = ['listen', 'are', 'pets', 'inlets', 'ear', 'enlist', 'step',
                 'pest', 'silent', 'tinsel', 'ERA']
        anagrams = [['listen', 'inlets', 'enlist', 'silent', 'tinsel'],
                    ['are', 'ear', 'ERA'], ['pets', 'step', 'pest']]

        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))

        # Ralitsa-Ts/tests.py
        words = ['woman Hitler', 'the eyes', 'dormitory', 'mother-in-law',
                 'dirty room', 'they see']
        anagrams = [['woman Hitler', 'mother-in-law'],
                    ['the eyes', 'they see'], ['dormitory', 'dirty room']]

        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))

if __name__ == '__main__':
    unittest.main()
