from random import randint
import sys


def run(low=1, high=10):
    # generate a random number
    answer = randint(low, high)
    # check that input is a number 1~10
    while True:
        try:
            # input from user
            guess = int(input(f'Guess a number between {low}~{high}: '))

            # check if number is the right guess. Otherwise ask again
            if low <= guess <= high:
                if guess < answer:
                    print('too low!')
                    continue
                elif guess > answer:
                    print('too high!')
                    continue
                else:
                    print('you got it!')
                    break
            else:
                print(f'must be between {low}~{high}')
                continue
        except ValueError:
            print(f'please enter a number between {low}~{high}')
            continue


if __name__ == "__main__":
    # default guessing range
    low = 1
    high = 10

    if len(sys.argv) > 1:
        low = int(sys.argv[1])
        high = int(sys.argv[2])

    run(low, high)
