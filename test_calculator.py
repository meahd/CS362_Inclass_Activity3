import unittest
import calculator


class TestCase(unittest.TestCase):
#Addition
    def test1(self):
        self.assertEqual(calculator.add(2, 1),3)
    def test2(self):
        self.assertEqual(calculator.add(-1, 0),-1)
    def test3(self):
        self.assertEqual(calculator.add(30.5, 0.5),31)

#subtraction
    def test4(self):
        self.assertEqual(calculator.subtract(2, 1),1)
    def test5(self):
        self.assertEqual(calculator.subtract(5, -7),12)
    def test6(self):
        self.assertEqual(calculator.subtract(0.5, 1),-0.5)

#multiplication
    def test7(self):
        self.assertEqual(calculator.multiply(2, 1),2)
    def test8(self):
        self.assertEqual(calculator.multiply(-1, 0),0)
    def test9(self):
        self.assertEqual(calculator.multiply(9.5, 2.5),23.75)

#division
    def test10(self):
        self.assertEqual(calculator.divide(2, 1),2)
    def test11(self):
        self.assertEqual(calculator.divide(-1, 0),None)
    def test12(self):
        self.assertEqual(calculator.divide(0.5, 2),0.25)


    if __name__ == '__main__':
        unittest.main()
