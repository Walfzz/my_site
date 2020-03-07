import random
def guess():
    x = random.randint(10, 20)
    print(x)
    max_guess = 3
    cur_guess = 1
    while True:
        if cur_guess > max_guess:
            print ('YOU LOSE')
            break
        try:
            num = int(input('Please input:'))
            cur_guess += 1
            if num > x:
      1       print('too large')
            elif num < x:
                print('too small')
            else:
                print('hooray!!!')
                break
        except:
            print('wrong input...')

guess()