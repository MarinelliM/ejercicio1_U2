class Email:
    __idcuenta = ""
    __dominio = ""
    __tipo = ""
    __con = ""

    def __init__(self, idcuenta, dominio, tipo, con=None):
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipo = tipo
        self.__con = con

    def retornaEmail(self):
        return self.__idcuenta + '@' + self.__dominio + '.' + self.__tipo

    def getIDCuenta(self):
        return self.__idcuenta

    def getDominio(self):
        return self.__dominio

    def getContra(self):
        return self.__con

    def comprobar(self, con):
        if con == self.__con:
            condicion = True
            return condicion
        else:
            print('Las contraseñas no son iguales')

    def modificar(self, nueva):
        self.__con = nueva
        print('Se modifico con exito'.center(30, '-'))

    def crearCuenta(direc):
        c = direc.split("@")
        c1 = c[1].split(".")
        return Email(c[0], c1[0], c1[1])
