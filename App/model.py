"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as she
assert cf
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    catalog = {'videos': None,
               'country': None,
               'category': None}

    catalog['videos'] = lt.newList(datastructure="ARRAY_LIST",
                                   cmpfunction=compVideosByLikes)
    catalog['country'] = mp.newMap(numelements=17,
                                prime=109345121,
                                maptype='CHAINING',
                                loadfactor=6.00,
                                comparefunction=None)
    catalog['category'] = mp.newMap(numelements=17,
                                prime=109345121,
                                maptype='CHAINING',
                                loadfactor=6.00,
                                comparefunction=None)
    return catalog
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addVideoCountry(catalog, video,contador):
    countryname = video["country"]
    countries = catalog['country']
    if mp.contains(countries,countryname):
        l = mp.get(countries,countryname)["value"]
        l.append(contador)
        mp.put(countries,countryname,l)
    else:
        l=[contador]
        mp.put(countries,countryname,l)


def addVideoCategory(catalog, video,contador):
    categoryidnu = video["category_id"]
    categories = catalog['category']
    name = None
    categoryfile = cf.data_dir + 'Videos/category-id.csv'
    with open(categoryfile, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,delimiter="\t")
        for row in reader:
            if row['id'] ==categoryidnu :
                name = row['name']
                break

    if mp.contains(categories,name):
        l = mp.get(categories,name)["value"]
        l.append(contador)
        mp.put(categories,name,l)
    else:
        l=[contador]
        mp.put(categories,name,l)
# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def newSList(lst, pos, numelem):
    return lt.subList(lst, pos, numelem)

def findVideos(category,catalog):
    categories = catalog['category']
    c = mp.get(categories,category)['value']
    v=idTranslate(c,catalog['videos'])
    return v

def idTranslate(ids,videos):
    v=lt.newList(datastructure='ARRAY_LIST',cmpfunction=compVideosByLikes)
    for i in ids:
        lt.addLast(v,lt.getElement(videos,i))
    return v

def sortLikes(lst, fun):
    if fun == "shellsort":
        return shesort(lst,compVideosByLikes)

    else:
        print("Funcion de ordenamiento no existe.")

def shesort(lst,cmpfunction):
    return she.sort(lst, cmpfunction)

def compVideosByLikes(video1,video2):
    if int(video1["likes"]) > int(video2["likes"]):
        return True
    else:
        return False

def presentacion(l):
    newIterator=lt.iterator(l)
    for i in newIterator:
        print('Title: '+i['title']+'\t'+'Channel Title: '+i['channel_title']+'\t'+'Publish Time: '+str(i['publish_time'])+'\t'+'Views: '+i['views']+'\t'+'Likes: '+i['likes']+'\t'+'Category: '+i['category_id']+'\n'+'\n')