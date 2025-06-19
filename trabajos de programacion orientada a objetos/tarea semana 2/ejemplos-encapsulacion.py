class peraonaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(self.__nombre,":", sep="")
        print("fuerza: ", self.__fuerza)
        print("inteligencia: ", self.__inteligencia)
        print("defensa: ", self.__defensa)
        print("vida: ", self.__vida)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.__fuerza = self.__fuerza+fuerza
        self.__inteligencia = self.__inteligencia+inteligencia
        self.__defensa = self.__defensa+defensa

    def esta_vivo(self):
        return self.__vida>0

    def morir(self):
        self.vida = 0
        print(self.__nombre, "ha muerto")

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizdo", daño, "puntos de daños a ", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.morir()

    def gef_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            preint("error, has introducido un valor negativo")
        else:
            self.__fuerza = fuerza



mi_personaje = peraonaje("maly", 8, 4, 10,100)
mi_enemigo = peraonaje("ibeth", 7, 5, 2,100)
mi_personaje.atacar(mi_enemigo)
mi_personaje.atributos()