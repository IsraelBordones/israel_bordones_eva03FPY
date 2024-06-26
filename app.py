from pathlib import Path
import os
import csv
import json

#¿se sabe el chiste del bus?
#suele pasar...
#piedad :(

home = Path(__file__).parent
rutaj = Path(home/"bases.json")
rutac = Path(home/"pinturas.csv")

menup = ['Ver Listado de Pinturas', 'Buscar Pintura',
         'Agregar Pintura', 'Eliminar Pintura',
         'Exportar Pinturas',"Salir"]

def verificar_existenciaj():
    '''
    verifica la existencia de un archivo .json. si no existe, lo crea
    ---NO PARAMS---
    '''
    if not rutaj.exists():
        rutaj.touch()
    else:
        pass


def verificar_existenciac():
    '''
    verifica la existencia de un archivo .csv. si no existe, lo crea
    ---NO PARAMS---
    '''
    if not rutac.exists():
        rutac.touch()
    else:
        pass


def limpiar():
    '''
    esta función limpia la pantalla automaticamente
    ----PARAMS---
    '''
    os.system("cls")


def listar(iter):
    '''
    está función toma un iterable(preferencia lista) y la
    devuelve con indice y con números
    ---PARAMS---
    poner iterable lista
    '''
    for ind in range(len(iter)):
        print(f"{ind+1}. {iter[ind]}")


def pedir_resp():
    '''
    Está función pide respuesta y la devuelve
    '''
    resp = input("¿Que opción escoges?\n")
    return resp


def errorp():
    '''
    Muestra en pantalla que escogiste una opción no valida
    ---NO PARAMS---
    '''
    print("ERROR: ESCOGISTE UNA OPCIÓN NO VALIDA")


def agregar_texto(contenido):
    '''
    Esto se suponer que debería añadir texto 
    al coso ese del json pero no se como hacer lo funcionar así que ya coperé
    '''
    try:
        with open(rutaj,"r") as stream:
            datos = json.load(stream)
    except FileNotFoundError:
        datos = {}

    datos = contenido

    with open(rutaj,"w") as stream:
        json.dump(datos,stream)


def lectura(ruta,ruta2):
    '''
    esto deberia hacer leer el archivo json (miami me lo confirmo)
    '''
    with open(rutaj, mode='r') as stream:
            txt = stream.read()
            json = json.load(stream)
            print (txt)
    

def escritura(contenido):
    '''
    Esto deberia escribir en el json pero no supe como hacerlo funcionar
    '''
    with open(rutaj, mode='w') as stream:
        stream.write(contenido)
        json.dump(contenido, stream)

def agregar_pintura():
        '''
        pide un codigo, un nombre, un tipo, un valor y un stock sobre la pintura
        si cuando pide un valor númerico, das un str te marca error y aborta la función
        '''
        while True:
            try:
                cod = int(input("Ingresa el codigo de la nueva pintura\n"))
            except:
                errorp()
                break

            nom = input("nombre del color\n")
            tipo = input("Acrílico o Látex\n")

            try:
                valor = int(input("Ingresa el Valor de la nueva pintura\n"))
            except:
                errorp()
                break
            try:
                stock = int(input("Ingresa el Stock de la nueva pintura\n"))
            except:
                errorp()
                break
            contenido[cod] = [nom,tipo,valor,stock]
            agregar_texto(contenido)
            break


limpiar()
verificar_existenciaj()
verificar_existenciac()
print("="* 50)
print(" PINTURAS ACRILICAS MANDARINA ".center(50,"="))
print("="*50)
#no funciona nada pero al menos hice la estructura pipipi
contenido = {}
while True:
    listar(menup)
    ans = pedir_resp()
    limpiar()

    if ans == "1":
        lectura(rutaj,rutac)
    elif ans == "2":
        pass
    elif ans == "3":
        agregar_pintura()
    elif ans == "4":
        pass
    elif ans == "5":
        pass
    elif ans == "6":
        exit("Adios")
    else:
        errorp()
 