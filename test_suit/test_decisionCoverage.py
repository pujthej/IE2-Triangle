import unittest
from isTriangle import Triangle

class DecisionCoverageTests(unittest.TestCase):
    def test_invalid_side(self):
        self.assertEqual(Triangle.classify(-1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, -2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, -3), Triangle.Type.INVALID)
    
    def test_scalene(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
    
    def test_equilateral(self):
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)
    
    def test_isosceles(self):
        self.assertEqual(Triangle.classify(3, 3, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 3, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 3), Triangle.Type.ISOSCELES)

    def test_invalid_triangle_inequality(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

if __name__ == '__main__':
    unittest.main()