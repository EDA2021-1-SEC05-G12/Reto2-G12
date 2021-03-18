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
    loadVideos(catalog)
#    loadTags(catalog)


def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    contador = 1
    for e in input_file:
        ee={
                'video_id':e['video_id'],
                'trending_date': datetime.strptime(e['trending_date'],'%y.%d.%m').date(),
                'title':e['title'],
                'channel_title':e['title'],
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



def req1(category,num,catalog):
    video =model.findVideos(category,catalog)
    sList = model.sortLikes(video,'shellsort')
    lst = model.newSList(sList,1,int(num))
    model.presentacion(lst)