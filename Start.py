import pygame
import Player
import Movement
import json


play = Player.Player()
pygame.init()
time = pygame.time.Clock()
key = 0
print("geht")
move = ""
List = []
a = True
pygame.display.set_mode((100, 100))
while a is True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            time_down = pygame.time.get_ticks()
            if event.key == pygame.K_LEFT:
                move = "l"
                print('LINKS')
            elif event.key == pygame.K_RIGHT:
                move = "r"
                print('RECHTS')
            elif event.key == pygame.K_DOWN:
                move = "d"
                print('UNTEN')
            elif event.key == pygame.K_UP:
                move = "u"
                print('OBEN')
            elif event.key == pygame.K_ESCAPE:
                move = "h"
                break
            else:
                move = "e"
        if move == "h":
            a = False
            break
        elif move == "e":
            if event.type == pygame.KEYUP:
                print("ungültig")
        else:
            play.handlerevent(event)
            if event.type == pygame.KEYUP:
                key += 1
                time_elapsed = (pygame.time.get_ticks() - time_down) / 1000.0
                print("Nummer: ", key, "Zeit: ", time_elapsed)
                path = Movement.Movement(key, move, time_elapsed)
                List.append(path)

for tmp in List:
    print(tmp.id, tmp.move, tmp.time)

s = json.dumps([ob.__dict__ for ob in List], indent=3)
print(s)
with open('file.json', 'w') as file:
    file.write(s)
