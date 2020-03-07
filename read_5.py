def read():
    #cnt = int(input())
    print(cnt)
    for i in range(cnt):
        x = int(input())
        str1 = 'input{}' . format(i + 1) + ':'
        str2 = 'sqrt{}:'. format(i+1)
        print(str1, x, str2, round(x**0.5, 2))


read()