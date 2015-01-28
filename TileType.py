# -*- coding: UTF-8 -*-

import pygame

# Speichert die Daten eines Tile-Typs:
class TileType(object):
    # Im Konstruktor speichern wir den Namen
    # und erstellen das Rect (den Bereich) dieses Typs auf der Tileset-Grafik.
    def __init__(self, name, startX, startY, width, height):
        self.__name = name
        self.__rect = pygame.rect.Rect(startX, startY, width, height)

    def getName(self):
        return self.__name

    def getRect(self):
        return self.__rect