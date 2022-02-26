###
# CS 3C Advanced Data Structures and Algorithms in Python
# Application: Pascal Triangle Recursive Solution
# Solution File: carolynPyunLab4.py
# Date:  2/1/22
###

def pascals_triangle(n): # Build the triangle as list of lists
    if n <= 0:   # Base case: for neg input
        return []
    if n <= 1:   # Base case: first/top row
        return [[1]]
    triangle = pascals_triangle(n-1)   # Recurse to get triangle of row b4
    new_row = [1]   # Leftmost 1 of new row
    prev_row = triangle[-1]   # From triangle, last row is last []
    for i in range(len(prev_row) -1):   # Loop thru the last row
        new_row.append(prev_row[i] + prev_row[i+1])   # Calculate sum and add
    new_row += [1]   # Rightmost 1 of new row
    triangle.append(new_row)   # Add the last row to triangle
    return triangle




