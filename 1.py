try:
    number = int(input("Please Enter any Number: "))
except:
    print('Please Enter the valid integer!')
    quit()


print("The List of Natural Numbers from 1 to %d are" % number) 
#print("The List of Natural Numbers from 1 to {0} are" .format(number))
mult=list()
for i in range(1, number): # Below 1000, if equal to 1000 means number+1
    print (i, end=' ')
    if i%3==0 or i%5==0:
        mult.append(i)
print(mult)
print('Total digits that are multiples of 3 or 5: ',len(mult))
print('Sum of the digits that are multiples of 3 or 5: ',sum(mult))
print('Max is : ', max(mult))
print('Min is : ', min(mult))


def find_sum_of_multiples(n):
    multiples = [num for num in range(n) if num % 3 == 0 or num % 5 == 0]
    return sum(multiples)

print(find_sum_of_multiples(1000))

# Faster version with generators
def find_sum_of_multiples(n):
    sum_of_multiples = sum( num for num in range(n) if num % 3 == 0 or num % 5 == 0 )
    return sum_of_multiples

print(find_sum_of_multiples(1000))