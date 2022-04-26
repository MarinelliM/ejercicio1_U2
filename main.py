from Cemail import Email

def prueba():
    objetoP = Email('xxx','gmail','com','yyyy')
    print('Prueba: {}'.format(objetoP.retornaEmail()))

if __name__ == "__main__":
    prueba()
    nombre = input("Ingrese su Nombre: ")
    cuenta = input("Ingrese el nombre de la cuenta: ")
    ID = input('Ingrese ID de la cuenta: ')
    dom = input('Ingrese Dominio: ')
    tipo = input('Ingrese tipo de dominio: ')
    con = input('Ingrese la contraseña: ')
    objeto = Email(ID, dom, tipo, con)

    print('Estimado {}'.format(nombre))
    print('Te enviaremos tus mensajes a la direccion {}'.format(objeto.retornaEmail()))
    print("Modificar contraseña".center(30, '-'))
    contra = input("Ingrese la contraseña actual: ")
    con = objeto.comprobar(contra)

    if con is True:
        nueva = input('Ingrese contraseña nueva: ')
        objeto.modificar(nueva)

    direccion = input('Ingrese direccion de correo: ')
    Obj1 = Email.crearCuenta(direccion)
    print(Obj1.retornaEmail())

    with open('Cuentas.txt', 'r', encoding='utf8') as archivo:
        lista = archivo.readline()
        l = lista.split(',')
        listaO = list(map(lambda x: Email.crearCuenta(x), l))
        cont = 0
        idc = input("Ingrese un identificador de Cuenta: ")
        for cuenta in listaO:
            if idc == cuenta.getIDCuenta():
                cont = cont + 1
        if cont >= 1:
            print("Esta repetido")
