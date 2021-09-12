import time

def func_time_decorator(func):
    def wrapper(*args, **kwargs):
        with open('test.txt', 'w') as log_file:
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time() - start_time
            log_file.write(f'{func.__name__}  {args[0]} {end_time:.9f}')

    return wrapper

@func_time_decorator
def calculate_fibonacci(quantity):
    fibonacciSequence = [0, 1]

    for number in range(quantity - 2):
        fibonacciSequence.append(fibonacciSequence[-1] + fibonacciSequence[-2])

    return fibonacciSequence

@func_time_decorator
def calculate_prime_numbers(quantity):
    primeNumbersSequence = []

    for number in range(1000000):
       if _is_prime_number(number):
           primeNumbersSequence.append(number)
       if len(primeNumbersSequence) == quantity:
           break

    return primeNumbersSequence

def _is_prime_number(number):
    counter = number
    isPrime = False

    while counter > 1:
        counter = counter - 1
        if number % counter == 0:
            break
        if counter == 2:
            isPrime = True

    return isPrime

@func_time_decorator
def raise_exception():
    raise NameError('Error')

#calculate_fibonacci(100)
#calculate_prime_numbers(1000)
