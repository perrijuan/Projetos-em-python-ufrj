import math

a=int(input("digite a\n"))
b=int(input("digite b\n"))
c=int(input("digite c\n"))

delta=(pow(b,2))-(4*a*c)

if delta<0:
    print("a equaçaõ nao tem raiz")
elif delta>0 or delta !=0:
    raiz1=-b+math.sqrt(delta)/(2*a)
    raiz2=-b-math.sqrt(delta)/(2*a)
    print("valor de raiz 1 é", raiz1, "de raiz 2", raiz2)
else:
    raiz=-b/(2*a)
    print("a raiz é", raiz)