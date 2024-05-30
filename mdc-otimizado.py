def mdc(a, b):
    contador = 0
    while b != 0:
        contador += 1
        #usando o algoritimo extendido de euclides.....
        #utilizamos o resto e vamos dividindo
        r = a % b
        a = b
        b = r
    return a, contador

num = 11
num2 = 9
resultado, contador_mdc = mdc(num, num2)
#melhor metodo e otimizado...
print("mdc:", resultado)
print("número de interações:", contador_mdc)

