#Factorial digit sum
import numpy
def factdigi(number):
    #faclis.append(number)
    while True:
        if number>=1:
            
            faclis.append(number)
            number=number-1
        else:
            break
    #return faclis
    tot=numpy.prod(faclis) 
    
    print(tot)
    sumlis=[int(i) for i in str(tot)]
    return sum(sumlis)

while True:
    try:
        innum=int(input('Enter the number to be factored:'))
        break
    except:
        print('invalid entry',innum,'Please enter the numeric values!')
        continue

faclis=list()
facout=factdigi(innum)
print('Digits : ',faclis)
print('Sum : ',facout)
