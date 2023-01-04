# Desafio de bicicletaria, python orientado a objetos.
# self representa a instancia do objeto.
#començo nomeando a classe
class Bicicleta:
    #metodo constructor para iniciar as caracteristicas ou atributos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor=cor 
        self.modelo=modelo
        self.ano=ano 
        self.valor=valor
        #vamos a definir comportamentos com métodos
    def buzinar(self):
        print("piiiiii")
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")
    def correr(self):
        print("vrum")
  # Para deixar mais legivel para o usuario se pode chamar os valores assim, mas se deve colocar print(b2) la embaixo:      
    def __str__(self):
        return f"Bicicleta: cor={self.cor}, ano={self.ano}, modelo={self.modelo}, valor= {self.valor}"   
    #def __str__(self):
     #   return f"{self.__class__.__name__}: {",".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
            
#vamos crear uma instancia
b1 = Bicicleta("vermelha", "caloi",2022 ,600)
b1.buzinar()
b1.correr()
b1.parar()
#para pedir os atributos da classe:
print(b1.cor ,b1.modelo ,b1.ano ,b1.valor)
b2=Bicicleta("verde","bmx",2020,400)
print(b2)

 #chamando por chave:valor   
    