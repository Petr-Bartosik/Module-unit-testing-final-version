import unittest
from task_1 import SadaCisel


class TestSadaCisel(unittest.TestCase):

    def test_soucet(self):
        sada = SadaCisel([1, 2, 3, 4, 5])
        self.assertEqual(sada.soucet, 15)

    def test_prumer(self):
        sada = SadaCisel([1, 2, 3, 4, 5])
        self.assertEqual(sada.prumer, 3.0)

    def test_maximum(self):
        sada = SadaCisel([1, 2, 3, 4, 5])
        self.assertEqual(sada.maximum, 5)

    def test_minimum(self):
        sada = SadaCisel([1, 2, 3, 4, 5])
        self.assertEqual(sada.minimum, 1)

    def test_empty_soucet(self):
        sada = SadaCisel()
        self.assertEqual(sada.soucet, 0)

    def test_empty_prumer(self):
        sada = SadaCisel()
        self.assertEqual(sada.prumer, 0)

    def test_empty_maximum(self):
        sada = SadaCisel()
        self.assertIsNone(sada.maximum)

    def test_empty_minimum(self):
        sada = SadaCisel()
        self.assertIsNone(sada.minimum)

if __name__ == "__main__":
    unittest.main()
