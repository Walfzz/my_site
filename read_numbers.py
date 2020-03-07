def read_nums():
  a = int(input())
  b = int(input())
  c = int(input())
  #print(a, b, c)
  sa, sb, sc = a**2, b**2, c**2
  print('input:', a, 'square:', sa)
  print('input:', b, 'square:', sb)
  print('input:', c, 'square:', sc)
  print('sum:', a + b + c)
  print('product:', a * b * c)
  print('square sum:', sa + sb + sc)
  
read_nums()