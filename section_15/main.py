from random import randint
import sys


def run_guess(guess, answer):
    if guess < answer:
        print('too low!')
        return False
    elif guess > answer:
        print('too high!')
        return False
    else:
        print('you got it!')
        return True


def measure_guess(low, high, guess):
    # generate a random number
    answer = randint(low, high)
    if low <= guess <= high:
        if run_guess(guess, answer):
            return True
        else:
            return False
    else:
        print(f'must be between {low}~{high}')
        return False


def validate_int(guess):
    return int(guess)


def run(low=1, high=10):
    # check that input is a number 1~10
    while True:
        # input from user
        try:
            guess = validate_int(
                input(f'Guess a number between {low}~{high}: '))
        except ValueError:
            print(f'please enter a number between {low}~{high}')
            continue

        # check if number is the right guess. Otherwise ask again
        if measure_guess(low, high, guess):
            break
        else:
            continue


if __name__ == "__main__":
    # default guessing range
    low = 1
    high = 10

    if len(sys.argv) > 1:
        low = int(sys.argv[1])
        high = int(sys.argv[2])

    run(low, high)
