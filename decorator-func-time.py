def calculateFibonacci(quantity):
    fibonacciSequence = [0, 1]

    for number in range(quantity - 2):
        fibonacciSequence.append(fibonacciSequence[-1] + fibonacciSequence[-2])

    return fibonacciSequence

def calculatePrimeNumbers(quantity):
    primeNumbersSequence = []

    while len(primeNumbersSequence) < quantity:
        for number in range(1000000):
            if number

    return quantity

def raiseExceptionFunction():
    raise NameError('Error')

'''class FuncTimeDecorator:
    def __init__(self):
        self.file_name = file_name

    def log_time(self):
        with open('func_time.txt', 'w') as log_file:'''

print(calculateFibonacci(100))