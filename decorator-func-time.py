def calculateFibonacci(quantity):
    fibonacciSequence = [0, 1]

    for number in range(quantity - 2):
        fibonacciSequence.append(fibonacciSequence[-1] + fibonacciSequence[-2])

    return fibonacciSequence

def calculatePrimeNumbers(quantity):
    primeNumbersSequence = []

    for number in range(1000000):
       if _isPrimeNumber(number):
           primeNumbersSequence.append(number)
       if len(primeNumbersSequence) == quantity:
           break

    return primeNumbersSequence

def _isPrimeNumber(number):
    counter = number
    isPrime = False

    while counter > 1:
        counter = counter - 1
        if number % counter == 0:
            break
        if counter == 2:
            isPrime = True

    return isPrime

def raiseExceptionFunction():
    raise NameError('Error')

class FuncTimeDecorator:
    def __init__(self):
        self.file_name = file_name

    def log_time(self):
        #with open('func_time.txt', 'w') as log_file:
        pass
#print(calculateFibonacci(10))
#print(_isPrimeNumber(1))
print(calculatePrimeNumbers(100))
