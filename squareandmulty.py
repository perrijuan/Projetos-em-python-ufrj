def squareormulti(a,b,n):
  c=1
  d=a
  binario_b= bin(b)[2:]

  for bit in binario_b:
    if bit =='1':
      c=(c*d)%n
      d= (d*d)%n

  return c
#base a, expoente b, modulo(n) c
a=2
b=12
c=17
print(squareormulti(a,b,c))
