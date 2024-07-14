import struct

# converte de float para binario e representa em formato ieee754 


def float_to_ieee754(num):
    pacote = struct.pack(">f", num)

    variavel = struct.unpack(">I", pacote)[0]

    binario = format(variavel, "032b")

    sinal = binario[0]
    expoente = binario[1:9]
    mantissa = binario[9:]

    return f"sinal : {sinal}\expoente: {expoente}\mantissa: {mantissa}"


entrada = input()
print(float_to_ieee754(float(entrada)))
