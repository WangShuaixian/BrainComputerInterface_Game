# -*- coding: UTF-8 -*-

import pygame
import random
import Utils
import Animation
import Tileset

# Die Player Klasse verwendet zwei Animationen, um eine steuerbare Spielfigur dazustellen.
class Opponents(object):
    def __init__(self,nummer):

        self.__opponentImage = pygame.image.load("round_box.png")


        self.__nummer = nummer
        self.__posX = ((60-(nummer*2))+6) *32
        self.__posY = (15.5) *32
        self.__dirY = random.choice([-1, 1])
        self.__dirX = -1
        self.__walking = False
        self.__radius = 32 - (nummer*2)
        self.__speed = 0.2 * nummer
        self.__centerY = (15.5) *32
        self.__centerX = ((nummer*5)+6) *32
        self.__opponentImage2 = pygame.transform.scale(self.__opponentImage,(self.__radius*2,self.__radius*2))


    def render(self, screen):



        screen.blit(self.__opponentImage2, (self.__posX - self.__radius, self.__posY - self.__radius))

        if (int(self.__centerY - self.__posY) > (80 - self.__radius)) or (int(self.__centerY - self.__posY) < (-80 + self.__radius)) :
            self.__dirY = self.__dirY*-1
        #if (int(self.__centerY - self.__posY) > 96) or (int(self.__centerY - self.__posY) < -96) :
        #    self.__dirX = self.__dirX*-1
        self.__posY += self.__dirY * self.__speed
        self.__posX += self.__dirX * self.__speed



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

    def getNummer(self):
        return self.__nummer