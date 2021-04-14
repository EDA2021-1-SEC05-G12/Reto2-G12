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
from DISClib.ADT import map as mp
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
    print("2- Cargar Videos con trending en un pais y categoria")    
    print("3- Cargar Video con mas trading segun su país")
    print("4- Cargar Video con mas trading segun su categoría")
    print("5- Cargar Video con mas likes segun Tags")
    print("0- Salir")
    

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.initCatalog()
        answer = controller.loadData(cont)
        print('Videos cargados: ' + str(lt.size(cont['videos'])))
        print('Paises cargados: ' + str(mp.size(cont['country'])))
        print('Categorias cargadas: ' + str(mp.size(cont['category'])))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")


    elif int(inputs[0]) == 2:
        t1=time.process_time()
        pais = input("Ingrese el pais que desea ver:\n")
        categ = ' '+input("Ingrese la categoria que desea ver:\n")
        num = int(input("Ingrese la cantidad de datos que desa ver:\n"))
        print("Cargando Videos trending....")
        controller.req1(pais,categ,num,cont)
        t2=time.process_time()
        tft=round(((t2-t1)*1000),2)
        print('El tiempo de procesamiento es: {}.'.format(tft))

    elif int(inputs[0]) == 3:
        t1=time.process_time()
        print("Cargando Video con mas trading segun su país ....")
        country=input('Ingrese el pais que desea ver: ')
        controller.req2(country,cont)
        t2=time.process_time()
        print('El tiempo de procesamiento es: {}.'.format(t2-t1))

    elif int(inputs[0]) == 4:
        t1=time.process_time()
        categ = ' '+input("Ingrese la categoria que desea ver:\n")
        print("Cargando Video con mas trading segun su categoria ....")
        controller.req3(categ,cont)
        t2=time.process_time()
        print('El tiempo de procesamiento es: {}.'.format(t2-t1))

    elif int(inputs[0]) == 5:
        t1=time.process_time()
        print("Cargando Video con mas likes segun Tags ....")
        country= input("Ingrese el pais del video que desea ver:\n")
        tag=input("Ingrese el tag del video que desea ver:\n")
        num=input("Ingrese el numero de videos que desea ver:\n")
        controller.req4(country,tag,num,cont)
        t2=time.process_time()
        print('El tiempo de procesamiento es: {}.'.format(t2-t1))
    

    else:
        sys.exit(0)
sys.exit(0)
