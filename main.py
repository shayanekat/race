"""
    Shayanekat
    Programme principal du jeu
"""

# ===== Imports =====
import pygame
from module.variables import *

# ===== variables globales =====


# ===== fonctions =====
def render():
    """
        Fonction pour l'affichage d'une frame
    """
    # reset l'écran
    screen.fill((0, 0, 0))
    
    # le décor
    pygame.draw.rect(screen, SkyColor, (0, 0, WIDTH, SkyHeight)) # le ciel
    pygame.draw.rect(screen, GrassColor, (0, SkyHeight, WIDTH, HEIGHT)) # le sol
    pygame.draw.polygon(screen, RoadColor, [(WIDTH//2, SkyHeight), (WIDTH//2 + NearRoadWidth//2, HEIGHT), (WIDTH//2 - NearRoadWidth//2, HEIGHT)]) # la route
    
    # test en dessinant les lignes de la route
    pygame.draw.line(screen, (255, 255, 255), (WIDTH//2, SkyHeight), (WIDTH//2 - NearRoadWidth//2, HEIGHT), WhiteLineWidth)
    pygame.draw.line(screen, (255, 255, 255), (WIDTH//2, SkyHeight), (WIDTH//2 + NearRoadWidth//2, HEIGHT), WhiteLineWidth)
    
    pygame.display.flip()

# ===== frontend =====
# initialisation de la fenêtre
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Game")


# boucle de jeu principale
running = True
while running:
    # MàJ de l'écran
    pygame.display.flip()
    
    # partie principale
    render()
    
    # boucle d'evenement
    for event in pygame.event.get():
        # fermeture du jeu
        if event.type == pygame.QUIT:
            running = False