import pygame
import player

play = player.player()
pygame.init()
time = pygame.time.Clock()
key = 0
print("geht")
move = ""
List =[]
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
                tmp = (move, time_elapsed)
                List.extend(tmp)

print('[%s]' % ', '.join(map(str, List)))







