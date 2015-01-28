# -*- coding: UTF-8 -*-

import pygame

import Utils
import TileType

# Verwaltet die Tileset Grafik und eine Liste mit Tile-Typen.
class Tileset(object):
    # Im Konstruktor laden wir die Grafik
    # und erstellen ein leeres Dictionary für die Tile-Typen.
    def __init__(self, image, colorkey, tileWidth, tileHeight):
        self.__image = Utils.loadImage(image, colorkey)
        self.__tileWidth = tileWidth
        self.__tileHeight = tileHeight

        self.__tileTypes = dict()
        
    def getImage(self):
        return self.__image

    def setImage(self, image, colorkey):
        self.__image = Utils.loadImage(image, colorkey)
        
    def getTileWidth(self):
        return self.__tileWidth

    def getTileHeight(self):
        return self.__tileHeight

    def getTileSize(self):
        return (self.__tileWidth, self.__tileHeight)
    
    # Neuen Tile-Typ hinzufügen.
    def addTile(self, name, startX, startY):
        self.__tileTypes[name] = TileType.TileType(name, startX, startY, self.__tileWidth, self.__tileHeight)
        
    # Versuchen, einen Tile-Type über seinen Name in der Liste zu finden.
    # Falls der Name nicht existiert, geben wir None zurück.
    def getTile(self, name):
        try:
            return self.__tileTypes[name]
        except KeyError:
            return None