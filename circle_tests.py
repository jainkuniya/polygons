import unittest
from circle import find_area, find_circumference

class CircleTestCase(unittest.TestCase):
    
    def test_find_area(self):
       area = find_area(5)
       self.assertEqual(area, 78.53750000000001)
    
    def test_find_circumference(self):
        circumference = find_circumference(5)
        self.assertEqual(circumference, 31.415000000000003)

if __name__ == '__main__':
    unittest.main()