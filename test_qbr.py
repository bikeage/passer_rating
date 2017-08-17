import unittest
from qbr import QB

class FooTestCase(unittest.TestCase):

    def test_sanity(self):
        assert 1+1==2

    def test_passer_rating(self):
        qb = QB()
        self.assertEqual(qb.passer_rating(432, 3554, 291, 28, 2), 112.2)
        self.assertEqual(qb.passer_rating(48, 192, 19, 2, 3), 39.6)
        self.assertEqual(qb.passer_rating(1, 2, 1, 1, 0), 118.8)

        self.assertEqual(qb.passer_rating(34, 172, 20, 1, 1), 69.7)
        self.assertEqual(qb.passer_rating(5, 76, 4, 1, 0), 158.3)
        self.assertEqual(qb.passer_rating(10, 17, 2, 0, 1), 0.0)
