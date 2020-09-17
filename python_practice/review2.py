import random
def guess():
    secret = random.randint(0, 9)
    chances = 5
    while chances > 0:
        x = int(input('Guess: '))
        chances -= 1
        if x == secret:
            print('you are correct!')
            break
        elif chances < 0:
            print("no more chances")

guess()
