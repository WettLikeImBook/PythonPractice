import sys , time

def collatz(number):
    if number == 1:
        return number
    if (number % 2) == 0:
        return number // 2
    elif (number % 2) == 1:
        return number * 3 + 1

while True:
    print('Enter a number (Or [x] to quit):')
    number = input()
    if number == 'x':
        sys.exit()
    else:
        number = int(number)
        print('Collatz Sequence:')
        while (number != 1):
            number = collatz(number)
            print(number)
            time.sleep(.1)