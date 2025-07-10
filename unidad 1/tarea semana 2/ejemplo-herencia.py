class peraonaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre,":", sep="")
        print("fuerza: ", self.fuerza)
        print("inteligencia: ", self.inteligencia)
        print("defensa: ", self.defensa)
        print("vida: ", self.vida)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza+fuerza
        self.inteligencia = self.inteligencia+inteligencia
        self.defensa = self.defensa+defensa

    def esta_vivo(self):
        return self.vida>0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizdo", daño, "puntos de daños a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class  Guerrero(peraonaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre,fuerza,inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("eligue un arma: (1) Colmillo de Acero, daño 10. (2) colmillo sagrado, daño 12"))
        if opcion == 1:
            self.espada = 6
        elif opcion == 2:
            self.espada = 8
        else:
            print("numero de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("espada:", self.espada)

    def daño (self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(peraonaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre,fuerza,inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("libro:", self.libro)

    def daño (self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

ibeth = peraonaje("ibeth", 15, 20, 18, 100)
maly = Guerrero("Maly", 15, 20, 18, 100, 4)
pianda = Mago("Pianda", 15, 20, 18, 100, 8)
ibeth.atacar(pianda)
maly.atacar(ibeth)
pianda.atacar(maly)
ibeth.atributos()
maly.atributos()
pianda.atributos()
