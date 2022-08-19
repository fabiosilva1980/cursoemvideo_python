# Faça um programa que abra e reproduza um audio de um arquivo em mp3

import pygame
pygame.init()
pygame.mixer.music.load('Aula_8_ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
