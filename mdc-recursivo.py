def mdc_subtracao(a, b, contador=0):
    if a == b:
        return a, contador +1
    elif a > b:
        return mdc_subtracao(a - b, b, contador +1)
    else:
        return mdc_subtracao(a, b - a, contador +1)

num1 = 7979
num2 = 13
resultado, contador_mdc = mdc_subtracao(num1, num2)
#meotodo de pior caso, ou seja é exponencial
#não otimizado
print("MDC:", resultado)
print("Número de interações:", contador_mdc)
