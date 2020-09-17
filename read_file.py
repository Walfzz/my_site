def read():
    with open('input.txt') as f:
        total = 0
        for line in f:
            line = line.strip()
            tokens = line.split()
            name = tokens[0]
            n = int(tokens[1])
            cost = int(tokens[2])
            print(name, n*cost)
            total += n*cost
        print('total:', total)
read()