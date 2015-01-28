# -*- coding: UTF-8 -*-

import pygame
import Utils
import Animation
import Tileset
from pygame.locals import *
from pygame.color import THECOLORS


class Player(object):
    def __init__(self):
        # Bild laden und erste Animation erstellen: 
        self.__anim_image_right = Utils.loadImage("tileset3.png", (255, 0, 255))
        self.__anim_right = Animation.Animation(self.__anim_image_right, 32, 32, 2, 32, 64, 15)  
        
        # Die Grafik spiegeln und in einer neuen Surface speichern,
        # dann können wir die linke Animation erstellen.
        self.__anim_image_left = pygame.transform.flip(self.__anim_image_right, True, False)
        self.__anim_left = Animation.Animation(self.__anim_image_left, 32, 32, 2, 32, 64, 15)

        self.__anim_right = Animation.Animation(self.__anim_image_right, 32, 32, 2, 32, 64, 15)

        #self.__tileset = Tileset.Tileset("tileset3.png", (255, 0, 255), 32, 32)
        #self.__tileset.addTile("brain", 32, 32)

        self.__playerImage = pygame.image.load("Player_brain.png")


        
        # Start-Position des Players festlegen und
        # merken in welche Richtung wir schauen und ob wir überhaupt laufen.
        self.__posX = 128
        self.__posY = 112
        self.__dir = 0
        self.__walking = False
        self.__radius = 16
        self.__speed = 1
        self.__modus = "size"
        self.__shield = 35
        self.__HP = 100
        self.__angle = 90
        self.__rotated = 0
        self.maxHP = 150


        self.font=pygame.font.Font(None,30)
        self.HPtext= self.font.render("HP:", 1,(255,255,255))
        self.SPEEDtext= self.font.render("Speed:", 1,(255,255,255))
        
    def render(self, screen):
        ## Die Blickrichtung ist links:
        #if self.__dir == -1:
        #    # Wenn der Spieler die linke oder rechte Pfeiltaste gedrückt hat sind wir am laufen,
        #    if self.__walking:
        #        # nur dann die Animation updaten.
        #        self.__anim_left.update()
        #   # Blickrichtung links rendern.
        #    self.__anim_left.render(screen, (self.__posX, self.__posY))
        #else:
        #    # Und das gleiche nochmal für rechts:
        #    if self.__walking:
        #        self.__anim_right.update()
        #    self.__anim_right.render(screen, (self.__posX, self.__posY))

        ## De Laufen-Zustand zurücksetzen, im nächsten Frame bleiben wir stehen.
        #self.__walking = False
        #pygame.draw.circle(screen, (  255,   50, 50), [self.__posX, self.__posY], self.__radius,1)
        #tile = self.__tileset.getTile("brain")
        #if tile is not None:
        #            screen.blit(self.__tileset.getImage(), (self.__posX - self.__radius, self.__posY - self.__radius), tile.getRect())
        self.__playerImage = pygame.transform.scale(self.__playerImage,(self.__radius*2,self.__radius*2))
        screen.blit(self.__playerImage, (self.__posX - self.__radius, self.__posY - self.__radius))
        if self.__modus == "shield":
            pygame.draw.circle(screen, (  50,   50, 255), [self.__posX, self.__posY], self.__shield,self.__shield/5)

        ###Statusbar:
        #pygame.draw.rect(screen, THECOLORS['red'], Rect((65,625), (150,30))) #x-pos,y-pos,breite, hoehe
        pygame.draw.rect(screen, THECOLORS['gray'], Rect((63,623), (152,23)),2)

        if (self.__HP>0):
            pygame.draw.rect(screen, THECOLORS['green'], Rect((65,625), (self.__HP,20)))
        screen.blit(self.HPtext, (20, 624))
        if self.__modus == "speed" or self.__rotated!=0:

            loc = self.__playerImage.get_rect().center
            rot_sprite = pygame.transform.rotate(self.__playerImage, self.__angle)
            rot_sprite.get_rect().center = loc
            self.__playerImage = rot_sprite

            self.__rotated += 1
            if self.__rotated == 4:
                self.__rotated = 0

            screen.blit(self.SPEEDtext, (270, 624))
            pygame.draw.rect(screen, THECOLORS['yellow3'], Rect((350,625), (130,20)),2)
            pygame.draw.rect(screen, THECOLORS['yellow3'], Rect((350,625), (self.__speed*65,20)))
        else:
            self.__playerImage = pygame.transform.scale(self.__playerImage,(self.__radius*2,self.__radius*2))
            screen.blit(self.__playerImage, (self.__posX - self.__radius, self.__posY - self.__radius))
        
    
    def handleInput(self, key):
        # Linke Pfeiltaste wird gedrückt:
        if key == pygame.K_LEFT:
            # x-Position der Spielfigur anpassen,
            # die Blickrichtung festlegen
            # und den Laufen-Zustand einschalten.
            self.__posX -= 1
            self.__dir = -1
            self.__walking = True
        
        # Und nochmal für die rechte Pfeiltaste.
        if key == pygame.K_RIGHT:
            self.__posX += 1
            self.__dir = 1
            self.__walking = True


    def move(self, direction):
        if direction == "left":
            self.__posX -= self.__speed

        if direction == "right":
            self.__posX += self.__speed

        if direction == "up":
            self.__posY -= self.__speed

        if direction == "down":
            self.__posY += self.__speed


    def handleMouse(self,xpos,ypos):
        self.__posX =xpos
        self.__posY =ypos






    def getXPosition(self):
        return self.__posX

    def setXPosition(self,x):
        self.__posX = x

    def setYPosition(self,y):
        self.__posY = y

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

    def setModus(self, modus):
        self.__modus = modus

    def getModus(self):
        return self.__modus

    def setShield(self, shield):
        self.__shield = shield

    def getShield(self):
        return self.__shield

    def setHealth(self, hp):
        if hp > 0:
            self.__HP = hp
        else:
            self.__HP = 0
            #TODO you are dead
            print "you died!!!!!!"

    def getHealth(self):
        return self.__HP
