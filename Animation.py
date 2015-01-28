# -*- coding: UTF-8 -*-

import pygame

# Die Klasse kümmert sich um eine einfache Animation:
class Animation(object):
    def __init__(self, image, startX, startY, num, width, height, duration):
        # Die Surface speichern,
        # alle Einzelbilder müssen in einer Reihe liegen.
        self.__image = image
        
        # Dazu müssen wir wissen, an welcher Position die Frames beginnen,
        # wie viele Frames die Animation hat,
        # sowie die Breite und Höhe der Animation kennen.
        self.__startX = startX
        self.__startY = startY
        self.__num = num
        self.__width = width
        self.__height = height
        
        # Und natürlich auch, nach welchem Zeitraum wir das nächsten Frame anzeigen sollen.
        self.__duration = duration
        
        # Die aktuelle Zeit und das aktuellen Frame speichern wir ebenfalls.
        self.__time = 0
        self.__current = 0
        
    
    # Die update-Methode rufen wir einmal pro Frame auf:
    def update(self, time = 1):
        # Die vergangene Zeit addieren
        self.__time += time
        
        # Falls wir den Anzeige-Zeitraum überschreiten, ...
        if self.__time > self.__duration:
            # ... setzten wir die Zeit zurück und gehen zum nächsten Frame.
            self.__time = 0
            self.__current += 1
            # Sicherstellen, dass das aktuelle Frame auch verfügbar ist.
            if self.__current >= self.__num:
                self.__current = 0
                
    
    # Das aktuelle Frame an einer bestimmten Position rendern:
    def render(self, screen, pos):
        # Welchen Bereich aus der Grafik müssen wir anzeigen?
        # Die x-Position können wir aus der Breite und der Start-Position berechnen,
        # die restlichen Werte kennen wir bereits.
        screen.blit(self.__image, pos, pygame.Rect(self.__startX + (self.__width * self.__current), self.__startY, self.__width, self.__height))