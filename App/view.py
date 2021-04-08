"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar videos por categoria con mas likes")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.initCatalog()
        catalog = initCatalog()
        answer = controller.loadData(cont)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Paises cargados: ' + str(lt.size(catalog['country'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['category'])))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")


    elif int(inputs[0]) == 2:
        t1=time.process_time()
        categ = ' '+input("Ingrese la categoria que desea ver:\n")
        num = int(input("Ingrese la cantidad de datos que desa ver:\n"))
        print("Cargando Videos trending....")
        controller.req1(categ,num,catalog)
        t2=time.process_time()
        tft=round(((t2-t1)*1000),2)
        print('El tiempo de procesamiento es: {}.'.format(tft))
        pass

    else:
        sys.exit(0)
sys.exit(0)
