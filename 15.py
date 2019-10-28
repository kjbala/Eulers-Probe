#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
import math
try:
    gridimen=int(input('Enter the Grid dimension: '))
except:
    print('Kindly enter the numeric integer,Exiting program!')
n = gridimen
result = math.factorial(2*n)//(math.factorial(n)**2)
print(result)
