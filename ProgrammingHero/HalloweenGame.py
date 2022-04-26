import pygame
from time import  sleep

pygame.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(8)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(1)
image = pygame.image.load('halloween.png')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)



