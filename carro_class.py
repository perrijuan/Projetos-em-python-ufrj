carro_class
class carro(object):
    
    #construtor 
    def __init__(self, velociadade, kilometragem, cor="branco"
                 ): 
        self.velocidade = velociadade
        self.kilometragem = kilometragem
        #gera o padrao de cor 
        self.cor= cor  

    def capaciade_pessoas(self, numero_pessoas):
        self.numeropessoas = numero_pessoas 

    #saida do codigo 
    def output(self):
        print("informacoes do carro")
        print(f"Cor: {self.cor}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Quilometragem: {self.quilometragem} km")


carro1 = carro(200, 20)
carro1.capaciade_pessoas(4)
carro1.output()

carro2 = carro(180, 25)
carro2.capaciade_pessoas(7)
carro2.output()