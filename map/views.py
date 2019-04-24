# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from tree.settings import GOOGLE_API_KEY


def index(request):
    context = {'google_api_key': GOOGLE_API_KEY}
    trees_list = []
    with open('/Users/bertrand/workspace/tree/map/static/points.json') as json_file:
        data = json.load(json_file)
        for p in data:
            genre = p['fields']['genre'].encode('latin1')
            espece = p['fields']['espece'].encode('latin1')
            hauteur = p['fields']['hauteurenm']
            date = p['fields']['dateplantation'].split("-")[0].encode('latin1')
            nom = p['fields']['libellefrancais'].encode('latin1')
            lat = p['fields']['geom_x_y'][0]
            long = p['fields']['geom_x_y'][1]
            trees_list.append([genre, espece, hauteur, date, nom, lat, long])
    context['trees_list'] = trees_list
    return render(request, 'home.html', context)
