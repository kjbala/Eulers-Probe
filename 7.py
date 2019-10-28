#10001th Prime number
# 
try:
    start=int(input('Enter the range within: '))
    pos=int(input('Enter the position num: '))
    if start>1 and pos>1:
        pass
except:
    print('Please enter the numeric value: ')

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
print('Prime Num at your position: ',primenum[pos-1])
