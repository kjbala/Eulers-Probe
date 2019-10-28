
try:
    start=int(input('Enter the range within: '))
    
except:
    print('Please enter the numeric value: ')
    quit()

primenum=list()
for val in range(start+1): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           #print(val)
           primenum.append(val)

print('Prime list within range: ',primenum)
print('sum of the prime foundL ',sum(primenum))
