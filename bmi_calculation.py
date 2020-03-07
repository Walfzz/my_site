def get_memo(BMI):
    if BMI < 18.5:
        return 'too light'
    elif BMI < 22.9:
        return 'normal'
    elif BMI < 27:
        return 'too heavy'
    elif BMI < 30:
        return 'slightly fat'
    elif BMI < 35:
        return 'fat'
    elif BMI >= 35:
        return 'too fat'

def table():
    with open('bmi_info.txt') as f:
        first = f.readline()
        tokens = first.split()
        fmt = '{:10}{:10}{:<10}{:<10}{:<10}{:10}'
        print(fmt.format(*tokens, 'BMI', 'Memo'))
        print('-' * 60)
        for line in f:
            line = line.strip()
            tokens = line.split()
            name, gender = tokens[0], tokens[1]
            h, w = float(tokens[2]), float(tokens[3])
            bmi = round(w/((h/100)**2), 2)
            print(fmt.format(name, gender, h, w, bmi, get_memo(bmi)))

table()