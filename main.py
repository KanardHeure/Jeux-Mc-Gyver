# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 500))


game = 1
while game:
    game = int(input())