'''
Created on Aug 30, 2018

@author: Kristen Tan
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment/examination.
I further pledge that I have not copied any material from a book, article, the Internet or any other source except
where I have expressly cited the source. ktan1
'''

import unittest
import TriangleClassifier

class Test(unittest.TestCase):
    
    def test01(self):
        '''Test values that represent an equilateral triangle.'''
        self.assertEqual(TriangleClassifier.classify_triangle(1,1,1), 'Equilateral')
        self.assertEqual(TriangleClassifier.classify_triangle(100.55, 100.55, 100.55), 'Equilateral')
        self.assertNotEqual(TriangleClassifier.classify_triangle(100.55, 100.55, 100.55), 'Scalene')
        
    def test02(self):
        '''Test values that represent an isosceles triangle.'''
        self.assertEqual(TriangleClassifier.classify_triangle(10, 10, 15), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(700, 1200, 700), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(1000, 12345, 12345), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(45.9, 45.9, 99.72), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(3.02, 2.459, 3.02), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(34.87, 60.77, 60.77), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(100.2, 100.2, 70), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(40, 85.892, 40), 'Isosceles')
        self.assertEqual(TriangleClassifier.classify_triangle(900, 1000.75, 1000.75), 'Isosceles')
        self.assertNotEqual(TriangleClassifier.classify_triangle(900, 1000.75, 1000.75), 'Isosceles Right')
    
    def test03(self):
        '''Test values that represent a scalene triangle.'''
        self.assertEqual(TriangleClassifier.classify_triangle(14, 100, 88), 'Scalene')
        self.assertEqual(TriangleClassifier.classify_triangle(900.7, 100, 88), 'Scalene')
        self.assertEqual(TriangleClassifier.classify_triangle(100.58, 72.3, 35), 'Scalene')
        self.assertEqual(TriangleClassifier.classify_triangle(17.5, 67.88, 90.45), 'Scalene')
        self.assertNotEqual(TriangleClassifier.classify_triangle(17.5, 67.88, 90.45), 'Equilateral')
    
    def test04(self):
        '''Test values that represent a right isosceles triangle.'''
        self.assertEqual(TriangleClassifier.classify_triangle(1, 1, 2**0.5), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(1, 2**0.5, 1), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(2**0.5, 1, 1), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(12.5, 12.5, 12.5 * (2**0.5)), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(12.5, 12.5 * (2**0.5), 12.5), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(12.5 * (2**0.5), 12.5, 12.5), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(7.5, 7.5, 10.6066), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(7.5, 10.6066, 7.5), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(10.6066, 7.5, 7.5), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.12, 4.12, 5.8266), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.12, 5.8266, 4.12), 'Isosceles Right')
        self.assertEqual(TriangleClassifier.classify_triangle(5.8266, 4.12, 4.12), 'Isosceles Right')
        self.assertNotEqual(TriangleClassifier.classify_triangle(5.8266, 4.12, 4.12), 'Scalene Right')
    
    def test05(self):
        '''Test values that represent a right scalene triangle.'''
        self.assertEqual(TriangleClassifier.classify_triangle(3, 4, 5), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(3, 5, 4), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4, 3, 5), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4, 5, 3), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(5, 3, 4), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(5, 4, 3), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(2.25, 3.75, 4.3732), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(2.25, 4.3732, 3.75), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(3.75, 2.25, 4.3732), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(3.75, 4.3732, 2.25), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.3732, 2.25, 3.75, ), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.3732, 3.75, 2.25), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(2, 4.5, 4.9244), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(2, 4.9244, 4.5), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.5, 2, 4.9244), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.5, 4.9244, 2), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.9244, 2, 4.5), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(4.9244, 4.5, 2), 'Scalene Right')
        self.assertEqual(TriangleClassifier.classify_triangle(75.22, 34.89, 82.9178), 'Scalene Right')
        self.assertNotEqual(TriangleClassifier.classify_triangle(75.22, 34.89, 82.9178), 'Scalene')
         
    def test06(self):
        '''Invalid input (not a triangle due to triangle Inequality Rule) given in order to display requirements shortcomings
        The following test displays that the method simply assumes the sides form an isosceles triangle
        In reality, sides of these lengths cannot form a triangle
        An error should occur, but none does, illustrating the effect of a missing requirement'''
        self.assertEqual(TriangleClassifier.classify_triangle_with_bugs(1, 1, 2), 'Isosceles')
    
    def test07(self):
        '''Buggy method called to display functionality of testing tool.'''
        self.assertEqual(TriangleClassifier.classify_triangle_with_bugs(4, 5, 3), 'Scalene Right')   
        
if __name__ == "__main__":
    unittest.main()