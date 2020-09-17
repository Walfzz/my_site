def car():
    command = ''
    start = 0
    stop = 0
    while True:
        command = input('> ')
        if command.lower() == 'start':
            if start > 0:
                print('Already started')
            else: 
                print('Car Started')
                start += 1
        elif command.lower() == 'stop':
            if stop > 0:
                print('Already stopped')
            else:
                print('Car stopped')
                stop += 1
        elif command.lower() == 'help':
            print('start - start the car\nstop - stop the car\nnone - quit')
        elif command.lower() == 'quit':
            break
        else:
            print("i dont undastand...")

car()