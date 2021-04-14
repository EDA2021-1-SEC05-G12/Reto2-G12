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
 """

import config as cf
import model
import csv
import time
import tracemalloc
from datetime import datetime
from datetime import date
import iso8601 as iso

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def initCatalog():
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # TODO: modificaciones para medir el tiempo y memoria
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory



def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    contador = 1
    for e in input_file:
        ee={
                'video_id':e['video_id'],
                'trending_date': datetime.strptime(e['trending_date'],'%y.%d.%m').date(),
                'title':e['title'],
                'channel_title':e['channel_title'],
                'category_id': e['category_id'],
                'publish_time':iso.parse_date(e['publish_time']),
                'tags':e['tags'],
                'views':e['views'],
                'likes':e['likes'],
                'dislikes':e['dislikes'],
                'country':e['country']
            }
        model.addVideo(catalog, ee)
        model.addVideoCountry(catalog,ee,contador)
        model.addVideoCategory(catalog,ee,contador)
        contador+=1
    model.verP(catalog)



def req1(country,category,num,catalog):
    video =model.videosTrending(country,category,catalog)
    sList = model.sortViews(video,'shellsort')
    lst = model.newSList(sList,1,int(num))
    model.presentacion(lst)

def req2(country,catalog):
    lr=model.duracionTen(country,catalog)
    print(model.presentacionReq2(lr))

def req3(category,catalog):
    lr=model.contVidsCat(category,catalog)
    print(model.presentacionReq3(lr))


def req4(country,tag,num,catalog):
    video=model.tagsEsp(country,tag,catalog)
    sList = model.sortLikes(video,'shellsort')
    lst = model.newSList(sList,1,int(num))
    model.presantacionTag(lst)
# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
