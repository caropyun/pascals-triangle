###
# CS 3C Advanced Data Structures and Algorithms in Python
# Description:  This program is the test driver for pascal triangle recursive function.
#               User input: Int of which row of the triangle, -1 to escape
#               Prints the user-inputted row of pascal's triangle
# Time and Space Complexity: O(n!)
# Solution File: demo4_carolynPyun.py
# Date:  2/1/22
###

import time
from carolynPyunLab4 import pascals_triangle


def main():
    print("Enter -1 to exit.")
    n = 0

    while n >= 0:
        n = int(input("Pascal triangle row: "))
        start = time.time()   # Start timing
        triangle = pascals_triangle(n + 1)
        total_time = (time.time() - start)   # Stop timing
        if triangle:   # If no return empty list aka n >= 0
            print(f"row {n} {triangle[-1]}")
            print(f"Time: {total_time} secs")
        print()


if __name__ == '__main__':
    main()


'''
Enter -1 to exit.
Pascal triangle row: 0
row 0 [1]
Time: 9.298324584960938e-06 secs

Pascal triangle row: 1
row 1 [1, 1]
Time: 1.6927719116210938e-05 secs

Pascal triangle row: 2
row 2 [1, 2, 1]
Time: 1.9073486328125e-05 secs

Pascal triangle row: 3
row 3 [1, 3, 3, 1]
Time: 2.0265579223632812e-05 secs

Pascal triangle row: 4
row 4 [1, 4, 6, 4, 1]
Time: 2.3126602172851562e-05 secs

Pascal triangle row: 5
row 5 [1, 5, 10, 10, 5, 1]
Time: 3.314018249511719e-05 secs

Pascal triangle row: 6
row 6 [1, 6, 15, 20, 15, 6, 1]
Time: 3.314018249511719e-05 secs

Pascal triangle row: 11
row 11 [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
Time: 4.410743713378906e-05 secs

Pascal triangle row: -1
'''