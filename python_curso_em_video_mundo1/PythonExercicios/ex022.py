# Faça um programa em python que abra e reproduza o aúdio de um arquivo em MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()

