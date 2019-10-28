import numpy as np

# Brute force: start computing triplets until the correct one has been found
def find_triplet():
    for a in range(1, 500):
        for b in range(1, 500):

            c = np.sqrt(a**2 + b**2)

            if a + b + c == 1000:
                print(f"Triplet found!")
                print(f"a: {a}, b: {b}, c: {c}")
                print(f"a + b + c = {a + b + c}")
                print(f"Product abc = {a*b*c}")
                return


find_triplet()