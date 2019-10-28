import math

def powdigisum(num,pw):
    result=str(int(math.pow(num,pw)))
    return result
try:
    digi=int(input('Enter the digit: '))
    power=int(input('Enter the Power: '))
except:
    print('Please Enter the valid integer values!')
    quit()

fnout=powdigisum(digi,power)
print(type(fnout))
print(fnout)
rslist=[int(i) for i in fnout]
print(rslist)
print('Sum of the total: ',sum(rslist))