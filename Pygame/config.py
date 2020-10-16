import pygame

pygame.init()

win = pygame.display.set_mode((1000,550))

#variables
x = 300
y = 450
width = 20
height = 20
vel = 10
lives=0
level=0
player=0
score1=0
score2=0
end=0
livesfor=3
livesleft=3

#music
pygame.mixer.music.load('./Pokémon Red & Blue Music Opening Theme.ogg')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
