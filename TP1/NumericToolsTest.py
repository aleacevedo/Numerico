import unittest
import NumericTools as nt


def f1(x):
    return 2 + x

def f2(x):
    return pow(x, 2) - 25


class NumericToolsTest(unittest.TestCase):

    def test_Biseccion(self):
        delta = 1.0e-3
        rz = nt.biseccion(f1, -4, 4, delta)
        self.assertAlmostEqual(rz, -2, msg="Bissecion funciona mal", delta=delta)
        rz = nt.biseccion(f2, -15, 0, delta)
        self.assertAlmostEqual(rz, -5, msg="Bissecion funciona mal", delta=delta)