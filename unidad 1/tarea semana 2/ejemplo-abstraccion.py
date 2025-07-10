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


mi_personaje = peraonaje("maly", 8, 4, 10,100)
mi_enemigo = peraonaje("ibeth", 7, 5, 2,100)
mi_personaje.atacar(mi_enemigo)
mi_personaje.atributos()