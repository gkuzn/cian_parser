# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 08:32:33 2016

@author: Artem
"""
#Маленькие буквы в градусах. Большие в километрах.
def dist(lat,lon):
    y0=55.753345
    x0=37.621253
    dy=lat-y0
    dx=lon-x0
    ky=40075.7/360
    kx=62.394
    dX=dx*kx
    dY=dy*ky
    dist=(dX**2+dY**2)**0.5
    return dist
print (dist(55.753345, 38.6252553))
