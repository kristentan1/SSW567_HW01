'''
Created on Aug 29, 2018

@author: Kristen Tan
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment/examination.
I further pledge that I have not copied any material from a book, article, the Internet or any other source except
where I have expressly cited the source. ktan1
'''

def classify_triangle(a,b,c):
    """
    This function returns a string with the type of triangle from three values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If the sum of the squares of any two sides equals the square of the third side, then return 'Right'
    """
    result_list = []
    if a == b and b == c:
        result_list.append('Equilateral')
    if (a == b or a == c or b == c) and not(a == b and b==c):
        result_list.append('Isosceles')
    if a != b and b != c and a != c:
        result_list.append('Scalene')
    orig_a = a
    orig_b = b
    orig_c = c
    sides_list = [orig_a, orig_b, orig_c]
    c = max(orig_a, orig_b, orig_c)
    sides_list.remove(c)
    a = sides_list[0]
    b = sides_list[1]
    if round((a**2) + (b**2), 2) == round (c**2, 2): # Round to two decimal places to allow for some error in rounding during comparison
        result_list.append('Right')
    result_string = ''
    for i in range(0, len(result_list)):
        if i != len(result_list) - 1:
            result_string += result_list[i] + ' '
        else:
            result_string += result_list[i]
    return result_string
    
    
def classify_triangle_with_bugs(a, b, c):
    """
    This is a buggy version of the classify_triangle() function written above.
    Used in testing to show functionality of unit test tool.
    """
    result_list = []
    if a == b and b == c:
        result_list.append('Equilateral')
    if (a == b or a == c or b == c) and not(a == b and b==c):
        result_list.append('Isosceles')
    if a != b and b != c and a != c:
        result_list.append('Scalene')
    if round((a**2) + (b**2), 2) == round (c**2, 2): # Intentionally skip rounding
        result_list.append('Right')
    result_string = ''
    for i in range(0, len(result_list)):
        if i != len(result_list) - 1:
            result_string += result_list[i] + ' '
        else:
            result_string += result_list[i]
    return result_string