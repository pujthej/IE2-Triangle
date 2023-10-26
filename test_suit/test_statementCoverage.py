import unittest
from isTriangle import Triangle

class TestTriangleClassification(unittest.TestCase):

    def test_invalid_sides(self):
        # Test negative sides
        self.assertEqual(Triangle.classify(-1, 2, 2), Triangle.Type.INVALID)
        # Test one side being 0
        self.assertEqual(Triangle.classify(0, 2, 2), Triangle.Type.INVALID)
        # Test sides that don't form a triangle
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def test_equilateral(self):
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        # Test different combinations for isosceles triangles
        self.assertEqual(Triangle.classify(3, 3, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 3, 3), Triangle.Type.ISOSCELES)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)

if __name__ == '__main__':
    unittest.main()

