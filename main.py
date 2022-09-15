import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls')


def main():
    number = 1
    while True:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            number += 1
        elif (number % 3) == 0:
            print("Fizz")
            number += 1
        elif (number % 5) == 0:
            print("Buzz")
            number += 1
        else:
            print(number)
            number += 1


if __name__ == "__main__":
    main()
