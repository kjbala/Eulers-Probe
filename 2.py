while True:
    try:
        number1=int(input('Enter the first number : '))
        number2=int(input('Enter the second number : '))
        break
    except:
        print('Please Enter the numeric int values! ')
        continue

def fib(limit):
    a, b = number1, number2
    fib_sequence = []
    while b < limit:
        a, b = b, a + b
        fib_sequence.append(a)

    return fib_sequence

#Using generators
#def sum_even_numbers(sequence):
#    return sum(num for num in sequence if num % 2 == 0 )

fib_sequence = fib(4000000)
#result = sum_even_numbers(fib_sequence)
result = sum(num for num in fib_sequence if num % 2 == 0 )
print(fib_sequence)
print('result: ', result)


