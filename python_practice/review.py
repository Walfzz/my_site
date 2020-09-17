import math
def weight():
    x = input('Weight: ')
    unit = (input('(l)bs or (k)g: '))
    if unit == 'l':
        kg = float(x) // 0.45
        print(math.floor(kg))
    elif unit == 'k':
        lbs = float(x) * 0.45
        print(math.floor(lbs))

weight()  