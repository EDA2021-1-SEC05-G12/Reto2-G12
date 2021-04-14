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
    catalog['country'] = mp.newMap(numelements=19,
                                maptype='CHAINING',
                                loadfactor=0.5
                                )
    catalog['category'] = mp.newMap(numelements=19,
                                maptype='CHAINING',
                                loadfactor=0.5
                                )
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

def sortViews(lst, fun):
    if fun == "shellsort":
        return shesort(lst,compVideosByViews)

    else:
        print("Funcion de ordenamiento no existe.")
        

def shesort(lst,cmpfunction):
    return she.sort(lst, cmpfunction)

def compVideosByLikes(video1,video2):
    if int(video1["likes"]) > int(video2["likes"]):
        return True
    else:
        return False
def compVideosByViews(video1,video2):
    if int(video1["views"]) > int(video2["views"]):
        return True
    else:
        return False 

def presentacion(l):
    newIterator=lt.iterator(l)
    for i in newIterator:
        print('Title: '+i['title']+'\t'+'Channel Title: '+i['channel_title']+'\t'+'Publish Time: '+str(i['publish_time'])+'\t'+'Views: '+i['views']+'\t'+'Likes: '+i['likes']+'\t'+'Category: '+i['category_id']+'\n'+'\n')


def verP(catalog):
    print(mp.size(catalog['country']))
    print(mp.size(catalog['category']))

def videosTrending(country,category,catalog):
    videos= findVideos(country,category,catalog)
    return videos

def findVideos(country,category,catalog):
    countries= catalog['country']
    categories = catalog['category']
    l = mp.get(countries,country)['value']
    c = mp.get(categories,category)['value']
    lf=[]
    for u in l:
        if u in c:
            lf.append(u)
    v=idTranslate(lf,catalog['videos'])
    return v

def tagsEsp(country,tag,catalog):
    video=catalog['videos']
    countries=catalog['country']
    l = mp.get(countries,country)['value']
    r=[]
    for u in l:
        v=lt.getElement(video,u)
        y=v['tags']
        if tag in y:
            r.append(u)
    ra=idTranslate(r,video)
    return ra
def presantacionTag(l):
    newIterator=lt.iterator(l)
    for i in newIterator:
        print('Title: '+i['title']+'\t'+'Channel Title: '+i['channel_title']+'\t'+'Publish Time: '+str(i['publish_time'])+'\t'+'Views: '+i['views']+'\t'+'Likes: '+i['likes']+'\t'+'Dislikes: '+i['dislikes']+'\t'+'Tags: '+i['tags']+'\n'+'\n')

def duracionTen(country,catalog):
    videos=catalog['videos']
    c= catalog['country']
    z = mp.get(c,country)['value']
    d=mp.newMap(numelements=1)
    for x in z:
        t=lt.getElement(videos,x)
        if mp.contains(d,t['video_id']):
            v=mp.get(d,t['video_id'])['value']
            v+=1
            mp.put(d,t['video_id'],v)
        else:
            mp.put(d,t['video_id'],1)
    temp= None
    mayor = 0
    keySet= mp.keySet(d)
    iterator=lt.iterator(keySet)
    for k in iterator:
        tv=mp.get(d,k)['value']
        if tv > mayor:
            mayor= tv
            temp =k
    for y in z:
        t=lt.getElement(videos,y)
        if t['video_id']==temp:
            lr=[t['title'],t['channel_title'],t['country'],mayor]
            return lr

def presentacionReq2(lr):
    print('Titulo: '+lr[0]+'\n'+'Nombre del canal: '+lr[1]+'\n'+'Pais: '+lr[2]+'\n'+'Dias: '+str(lr[3]))

def contVidsCat(category,catalog):
    videos=catalog['videos']
    c= catalog['category']
    l = mp.get(c,category)['value']
    d=mp.newMap(numelements=1)
    for i in l:
        t=lt.getElement(videos,i)
        if mp.contains(d,t['video_id']):
            v=mp.get(d,t['video_id'])['value']
            v+=1
            mp.put(d,t['video_id'],v)
        else:
            mp.put(d,t['video_id'],1)
    temp= None
    mayor = 0
    keySet= mp.keySet(d)
    iterator=lt.iterator(keySet)
    for k in iterator:
        tv=mp.get(d,k)['value']
        if tv > mayor:
            mayor= tv
            temp =k
    for u in l:
        t=lt.getElement(videos,u)
        if t['video_id']==temp:
            lr=[t['title'],t['channel_title'],t['category_id'],mayor]
            return lr

def presentacionReq3(lr):
    print('Title: '+lr[0]+'\n'+'Channel Title: '+lr[1]+'\n'+'Category ID: '+lr[2]+'\n'+'Dias: '+str(lr[3]))
