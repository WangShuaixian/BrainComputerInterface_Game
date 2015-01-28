# -*- coding: UTF-8 -*-

import pygame
import random
import Tileset
import Player
import Finishline
import MovingBoxes
import time
from pygame.locals import *
from pygame.color import THECOLORS


fadeCounter = 10000
# Die Tilemap Klasse verwaltet die Tile-Daten, die das Aussehen der Karte beschreiben.
class Tilemap(object):


    def __init__(self):
        # Wir erstellen ein neues Tileset.
        # Hier im Tutorial fügen wir manuell vier Tile-Typen hinzu.
        self.__tileset = Tileset.Tileset("tileset4.png", (255, 0, 255), 32, 32)
        self.__tileset.addTile("grass", 0, 0)
        self.__tileset.addTile("mud", 32, 0)
        self.__tileset.addTile("water", 64, 0)
        self.__tileset.addTile("blockCircleGrass", 96, 0)
        self.__tileset.addTile("block", 0, 32)
        self.__tileset.addTile("stoneCircle", 32, 32)
        self.__tileset.addTile("blockCircle", 64, 32)
        self.__tileset.addTile("stoneCircleGrass", 96, 32)
        self.__tileset.addTile("grassToMud", 0, 64)
        self.__tileset.addTile("coin", 32, 64)
        self.__tileset.addTile("stone", 96, 64)

        self.__direct = "right"
        self.__runningDirection = "right"
        self.t1 = 0
        self.t2 = 0
        self.moving = 0

        # Festlegen der Startposition der Kamera.
        self.__cameraX = 0
        self.__cameraY = 0


        self.font=pygame.font.Font(None,30)


        # Die Größe der Maps in Tiles.
        self.__width = 65
        self.__height = 19

        # Erstellen einer leeren Liste für die Tile Daten.
        self.__tiles = list()
        
        # Manuelles Befüllen der Tile-Liste:
        # Jedes Feld bekommt ein zufälliges Tile zugewiesen.
        for i in range(0, self.__height): # i = zeilen
            self.__tiles.append(list())
            for j in range(0, self.__width): # j = spalten
                #Abfrage wann Steine gesetzt werden.1.Zeile Rand 2.Randweg1 3. Randweg2 4.Treppe
                if i == 0 or i == 18 or ((i == 6) and (60>=j<=63)) or j == 0 or j == 64 or ((i == 12) and (2<=j>=4))\
or ( ((7 <= j <= 15) or (19 <= j <= 23) or (26 <= j <= 32)) and ((i == 1) or  (i==5)))\
or ( ((13 <= j <= 13) or (21 <= j <= 22) or (28 <= j <= 31)) and ((i == 2) or (i == 4)))\
or ((40 <= j <= 60) and (i==5)) or ((44 <= j <= 60) and (i==4)) or ((50 <= j <= 60) and (i==3)):
                    self.__tiles[i].append("stoneCircleGrass")

                else:
                    self.__tiles[i].append("grass")



                #x = random.randint(1, 101)
                #if x < 90:
                #    self.__tiles[i].append("grass")
                #elif x < 94:
                #    self.__tiles[i].append("water")
                #elif x < 99:
                #    self.__tiles[i].append("mud")
                #else:
                #    self.__tiles[i].append("block")
        self.__player = Player.Player()
        self.__finishLine = None
        self.__boxOpponents = []
                    
    
    # Hier rendern wir den sichtbaren Teil der Karte.
    def render(self, screen):
        # Zeilenweise durch die Tiles durchgehen.
        for y in range(0, int(screen.get_height() / self.__tileset.getTileHeight()) + 1):
            # Die Kamera Position mit einbeziehen.
            ty = y + self.__cameraY
            if ty >= self.__height or ty < 0:
                continue
            # Die aktuelle Zeile zum einfacheren Zugriff speichern.
            line = self.__tiles[ty]
            # Und jetzt spaltenweise die Tiles rendern.
            for x in range(0, int(screen.get_width() / self.__tileset.getTileWidth()) + 1):
                # Auch hier müssen wir die Kamera beachten.
                tx = x + self.__cameraX
                if tx >= self.__width or tx < 0:
                    continue
                # Wir versuchen, die Daten des Tiles zu bekommen.
                tilename = line[tx]
                tile = self.__tileset.getTile(tilename)
                # Falls das nicht fehlschlägt können wir das Tile auf die screen-Surface blitten.
                if tile is not None:
                    screen.blit(self.__tileset.getImage(), (x * self.__tileset.getTileWidth(), y * self.__tileset.getTileHeight()), tile.getRect())
                if "stone" in tilename or "block" in tilename:
                    #if (((x * self.__tileset.getTileWidth()) <= self.__player.getXPosition() <= ((x+1) * self.__tileset.getTileWidth()))
                    #    and (y * self.__tileset.getTileHeight()) <= self.__player.getYPosition()<= ((y+1) * self.__tileset.getTileHeight()) ):
                    x1 = self.__player.getXPosition()
                    y1 = self.__player.getYPosition()
                    x2 =  (x * self.__tileset.getTileWidth()) + 16
                    y2 =  (y * self.__tileset.getTileHeight()) + 16
                    r1 = self.__player.getRadius()
                    r2 = 16 #radius eines Steins

                    dsqrd = (y2-y1) * (y2-y1) + (x2-x1) * (x2-x1);
                    if (dsqrd < (r1+r2)*(r1+r2)):
                        pygame.mouse.set_visible(0)
                        self.__player.setHealth(self.__player.getHealth() - 0.5)
                        print ("Don't touch the wall!")

                    #print ((x *self.__tileset.getTileWidth()))
                    #print ("Player Y-Pos:"+str(self.__player.getYPosition()))
                    #print ("Player X-Pos:"+str(self.__player.getXPosition()))
        #print ("next")

        x1 = self.__player.getXPosition()
        y1 = self.__player.getYPosition()
        r1 = self.__player.getShield()


        if self.__finishLine is not None:
            self.__finishLine.render(screen)
            x2 = self.__finishLine.getXPosition()
            y2 = self.__finishLine.getYPosition()
            r2 = self.__finishLine.getRadius()
            r1 = self.__player.getRadius()

            dsqrd = (y2-y1) * (y2-y1) + (x2-x1) * (x2-x1)
            if (dsqrd < (r1+r2)*(r1+r2)):
                print ("You got it!")

                if self.__player.maxHP < (self.__player.getHealth() + self.__finishLine.HPgranted):
                    self.__player.setHealth(self.__player.getHealth() + self.__finishLine.HPgranted)
                else:
                    self.__player.setHealth(self.__player.maxHP)

                self.__finishLine.setXPosition(-10000)

        if self.__boxOpponents is not []:
            for box in self.__boxOpponents:
                box.render(screen)
                x2 = box.getXPosition()
                y2 = box.getYPosition()
                r2 = box.getRadius()

                dsqrd = (y2-y1) * (y2-y1) + (x2-x1) * (x2-x1)
                if (dsqrd < (r1+r2)*(r1+r2)):
                    print ("Your shield got hit.")
                    if (0 <= (self.__player.getShield() - (13-box.getNummer()))):#zur Vermeidung wenn ein Schield negativ würde
                        self.__player.setShield(self.__player.getShield()- (13-box.getNummer()))
                    else:
                        self.__player.setShield(0)
                    box.setXPosition(-1000)
                else:
                    r1 = self.__player.getRadius()
                    if (dsqrd < (r1+r2)*(r1+r2)):
                        print ("Ouch, a box hit you!!")
                        self.__player.setHealth(self.__player.getHealth() - (10))
                        box.setXPosition(-1000)
                        #TODO get DMG
                    r1 = self.__player.getShield()
        self.__player.render(screen)

        if self.moving:
            if(self.__player.getHealth() > 0):
                self.t2 = time.time()
            #self.timer = self.font.render("%.2f" %(self.t2-self.t1), 1,(255,255,255))
            self.timer = self.font.render(time.strftime("%M:%S", time.gmtime(self.t2-self.t1)), 1,(255,255,255))
            screen.blit(self.timer, (700, 624))



    
    # Tastendrücke verarbeiten:
    def handleInput(self, key, keyson):
        if(keyson == 1):
            if key == pygame.K_LEFT:
                self.__cameraX += 1
            if key == pygame.K_RIGHT:
                self.__cameraX -= 1

            # Und das gleiche nochmal für die y-Position.
            if key == pygame.K_UP:
                self.__cameraY += 1
            if key == pygame.K_DOWN:
                self.__cameraY -= 1

        if key == pygame.K_SPACE:
            self.moving = 1
            self.t1 = time.time()

        if ((key == pygame.K_p) and  (self.__direct is not "left") and  (self.__direct is not "right2")):
            self.moving = 0

        #self.__player.handleInput(key)   # Bewegung des Brains duch Keydruck




    # beschreibt die Bewegung im Game + Kamerabewegung
    def moveScript(self):
        if self.moving == 1:


            global fadeCounter

            if self.__direct == "right":
                self.__runningDirection = "right"
                global fadeCounter
                if (fadeCounter < 20):
                    self.__player.setXPosition(self.__player.getXPosition() - 32)
                    self.__cameraX += 1
                    fadeCounter += 1
                elif self.__player.getXPosition() - self.__cameraX  >  650:
                    fadeCounter = 0
                    if self.__cameraX == 40:
                        self.__direct = "down"
                elif ((self.__cameraX == 20) and (self.__player.getXPosition())) == 460:
                    self.__player.setModus("height")
                    self.__player.setRadius(16)




            elif self.__direct == "down":
                if (self.__player.getXPosition() == 720):
                    self.__runningDirection = "down"
                    print self.__player.getYPosition()
                if (self.__player.getYPosition() == 300):
                    self.__runningDirection = "left"
                    self.__direct = "left"
                    self.__finishLine = Finishline.Opponents()
                    self.__player.setModus("speed")
            elif self.__direct == "left":
                    if self.__player.getXPosition() - self.__cameraX  <  400:
                        self.__player.setXPosition(self.__player.getXPosition() + 32)
                        self.__finishLine.setXPosition(self.__finishLine.getXPosition() + 32)
                        self.__cameraX -= 1
                    if (self.__cameraX == 0):
                        self.__direct = "down2"
                        self.__finishLine = None

            elif self.__direct == "down2":
                    if (self.__player.getXPosition() < 2.5*32):
                        self.__runningDirection = "down"
                    if (self.__player.getYPosition() == 496):
                        fadeCounter = 10000
                        self.__direct = "right2"
                        self.__player.setModus("shield")
                        self.__player.setSpeed(1)
                        for i in xrange(12):
                            self.__boxOpponents.append(MovingBoxes.Opponents(i+1))
            elif self.__direct == "right2":
                self.__runningDirection = "right"

                if (fadeCounter < 20):
                    self.__player.setXPosition(self.__player.getXPosition() - 32)
                    for box in self.__boxOpponents:
                        box.setXPosition(box.getXPosition() - 32)
                    self.__cameraX += 1
                    fadeCounter += 1

                elif self.__player.getXPosition() - self.__cameraX  >  650:
                    fadeCounter = 0
                    if self.__cameraX == 40:
                        print "Game Over. You win."

            self.__player.move(self.__runningDirection)



    def handleMouse(self, xpos,ypos):
        self.__player.handleMouse(xpos,ypos)

    def rsbCall(self,rsbValue):
        if self.__player.getModus() == "size": #16
            self.__player.setRadius(rsbValue)
        elif self.__player.getModus() == "height": #112
            self.__player.setYPosition(rsbValue)
        elif self.__player.getModus() == "speed": #1
            self.__player.setSpeed(rsbValue)
        elif self.__player.getModus() == "shield":#35
            self.__player.setShield(self.__player.getShield() + (rsbValue))

