from unittest import TestCase, main
from mains.Calc import calc


class CalcTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calc('10-20'), -10)

    def test_multi(self):
        self.assertEqual(calc('5*20'), 100)

    def test_divide(self):
        self.assertEqual(calc('25/5'), 5)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('fqrw2')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2-3-5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2-3*5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calc('2.3-3*5.0')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calc('b+c')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
