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
    fibonacci_sequence = [0, 1]

    for number in range(quantity - 2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    return fibonacci_sequence


@func_time_decorator
def calculate_prime_numbers(quantity):
    prime_numbers_sequence = []

    for number in range(1000000):
        if _is_prime_number(number):
            prime_numbers_sequence.append(number)
        if len(prime_numbers_sequence) == quantity:
            break

    return prime_numbers_sequence


def _is_prime_number(number):
    counter = number
    is_prime = False

    while counter > 1:
        counter = counter - 1
        if number % counter == 0:
            break
        if counter == 2:
            is_prime = True

    return is_prime


@func_time_decorator
def raise_exception():
    raise NameError('Error')


# calculate_fibonacci(100)
# calculate_prime_numbers(1000)
