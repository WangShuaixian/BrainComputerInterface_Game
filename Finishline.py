# -*- coding: UTF-8 -*-

import pygame
import Utils
import Animation
import Tileset

# Die Player Klasse verwendet zwei Animationen, um eine steuerbare Spielfigur dazustellen.
class Opponents(object):
    def __init__(self):

        self.__opponentImage = pygame.image.load("finishline2.png")



        self.__posX = 20.5 *32
        self.__posY = 9.5*32
        self.__dir = 0
        self.__walking = False
        self.__radius = 10
        self.__speed = 1
        self.HPgranted = 50


    def render(self, screen):
        self.__opponentImage = pygame.transform.scale(self.__opponentImage,(16*2,16*2))
        screen.blit(self.__opponentImage, (self.__posX - 16, self.__posY - 16))
        screen.blit(self.__opponentImage, (self.__posX - 16, self.__posY - 16-32))
        screen.blit(self.__opponentImage, (self.__posX - 16, self.__posY - 16-64))
        screen.blit(self.__opponentImage, (self.__posX - 16, self.__posY - 16+32))
        screen.blit(self.__opponentImage, (self.__posX - 16, self.__posY - 16+64))
        self.__posX -= 1.2


    def move(self, direction):
        if direction == "left":
            self.__posX -= self.__speed

        if direction == "right":
            self.__posX += self.__speed

        if direction == "up":
            self.__posY -= self.__speed

        if direction == "down":
            self.__posY += self.__speed



    def getXPosition(self):
        return self.__posX

    def setXPosition(self,x):
        self.__posX = x

    def getYPosition(self):
        return self.__posY

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def setSpeed(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return self.__speed