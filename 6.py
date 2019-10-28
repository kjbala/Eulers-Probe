import math

def sumsqrsum(num):
    for i in range(1,num+1):
        sumsqr.append(int(math.pow(i,2)))
        sqrsum.append(i)

try:
    numrng=int(input('Enter the Range uptill: '))
except:
    print('Please enter the numeric key values!')
    quit()
sumsqr=list()
sqrsum=list()
sumsqrsum(numrng)
print('sumsqr list: ', sumsqr)
print('sqsum list: ', sqrsum)
result=int(math.pow(sum(sqrsum),2)-sum(sumsqr))
print('Result: ', result)