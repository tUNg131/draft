def main():
    number = int(input("The interger: "))
    while number != 1:
        number = collatz(number)
        print(int(number))

def collatz(number):
    if (number % 2) == 0:
        return number/2
    else: return 3*number + 1

main()
