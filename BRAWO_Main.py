# -*- coding: UTF-8 -*-

#-----Essentiell---
#TODO RSB Mapping
#-----Wichtig-----
#TODO Instructions
#TODO Lose condition
#TODO Win condition
#TODO Winscreen
#----Wenn Zeit ist-----
#TODO Timer
#TODO Menu
#TODO Kommentare changen
#TODO Pause nutzbar machen
#----Kosmetik----
#TODO try to Change Color of the Player
#TODO Steine hinzufugen und random erscheinen lassen
#TODO Grass hinzufugen und random erscheinen lassen
#TODO Boxen rollen lassen
#TODO change direction of the brain





# Pygame Modul importieren.

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,100)


import pygame
from pygame.locals import *

import time
import logging

import rsb

# Unser Tilemap Modul ebenfalls importieren.
import Tilemap

def handle(event):
    print("Received event: %s" % event)
    print("Received text: %s" % event.getData())
    map.rsbCall(event.getData())

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

map = None

def main():
    # Initialisieren aller Pygame-Module und 
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()

    mouseon = 1
    keyson = 0
    screenbreite = 800
    screenhoehe = 672
    screen = pygame.display.set_mode((screenbreite, screenhoehe))
    
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Brawo: Neurofeedback Game")
    pygame.mouse.set_visible(mouseon)
    pygame.key.set_repeat(1, 30)

    # Clock Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()
    
    # Wir erstellen eine Tilemap.
    global map
    map = Tilemap.Tilemap()

    pygame.mouse.set_pos(128,112)  #(screenbreite/3.0,screenhoehe/3.0)

    logging.basicConfig()
    ###counter=0
    ###sizerandom = 0
    ###with rsb.createRemoteServer('/example/serverr') as server:
    with rsb.createListener("/example/informer") as listener:

        listener.addHandler(handle)
        # Die Schleife, und damit unser Spiel, läuft solange running == True.
        running = True
        while running:
            # Framerate auf 30 Frames pro Sekunde beschränken.
            # Pygame wartet, falls das Programm schneller läuft.
            clock.tick(30)
            ###if counter%30 == 29:
            ###    counter = 0
                ###print 'server replied to synchronous call: "%s"' % server.echo('bla')
                ###sizerandom = sizerandom + 1
                ###map.changeSize(server.echo(sizerandom))
            ###counter = counter+1

            #print counter

            # screen Surface mit Schwarz (RGB = 0, 0, 0) füllen.
            screen.fill((0, 0, 0))

            # Alle aufgelaufenen Events holen und abarbeiten.
            for event in pygame.event.get():
                # Spiel beenden, wenn wir ein QUIT-Event finden.
                if event.type == pygame.QUIT:
                    running = False

                # Wir interessieren uns auch für "Taste gedrückt"-Events.
                if event.type == pygame.KEYDOWN:
                    # Wenn Escape gedrückt wird posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

                    # Alle Tastendrücke auch der Tilemap mitteilen.
                    map.handleInput(event.key,keyson)

                if event.type == MOUSEMOTION and mouseon == 1:
                    # If the mouse moves, move the player where the cursor is.
                    map.handleMouse(event.pos[0],event.pos[1])

            map.moveScript()

            # Die Tilemap auf die screen-Surface rendern.
            map.render(screen)

            # Inhalt von screen anzeigen
            pygame.display.flip()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':


    # Unsere Main-Funktion aufrufen
    main()