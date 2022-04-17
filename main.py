"""
    Shayanekat
    Programme principal du jeu
"""

# ===== Imports =====
import pygame

# ===== variables globales =====
WIDTH = 800
HEIGHT = 500

# ===== fonctions =====
def render():
    """
        Fonction pour l'affichage d'une frame
    """
    pass

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
    
    # boucle d'evenement
    for event in pygame.event.get():
        # fermeture du jeu
        if event.type == pygame.QUIT:
            running = False