#Factorial digit sum

def factdigi(number):
    #faclis.append(number)
    while number>=1:  
        faclis.append(number)
        number=number-1
    tot=1
    for i in faclis:
        tot=tot*i
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
