import pygame
import random
import sys

pygame.init()

# Fenêtre
LARGEUR, HAUTEUR = 600, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du pendu")

# Police
font = pygame.font.SysFont(None, 36)

# Chargement des mots
mots = []
with open("test.txt") as fl:
    for l in fl:
        mots.append(l.rstrip("\n"))

mot = random.choice(mots)

lettres = []
faux = 0
trouve = False

corps_plein = ["O", "/", "|", "\\", "/", "\\"]
corps = [" ", " ", " ", " ", " ", " "]

clock = pygame.time.Clock()

def afficher_texte(texte, x, y):
    img = font.render(texte, True, (255, 255, 255))
    fenetre.blit(img, (x, y))

while True:
    fenetre.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not trouve and faux <= 5:
            lettre = event.unicode.lower()

            if lettre.isalpha() and lettre not in lettres:
                lettres.append(lettre)

                if lettre not in mot:
                    corps[faux] = corps_plein[faux]
                    faux += 1

    # Affichage du mot
    affichage_mot = ""
    trouve = True
    for l in mot:
        if l in lettres:
            affichage_mot += l + " "
        else:
            affichage_mot += "_ "
            trouve = False

    afficher_texte(affichage_mot, 50, 300)

    # Affichage des lettres déjà jouées
    afficher_texte("Lettres : " + " ".join(lettres), 50, 340)

    # Affichage du pendu simple
    afficher_texte("Tête : "    + corps[0], 50, 50)
    afficher_texte("Bras : "    + corps[1] + corps[3], 50, 90)
    afficher_texte("Corps : "   + corps[2], 50, 130)
    afficher_texte("Jambes : "  + corps[4] + corps[5], 50, 170)

    # en cas de victoire et defaite
    if trouve:
        afficher_texte("TU AS GAGNÉ !", 300, 100)

    if faux > 5:
        afficher_texte("PERDU ! Mot : " + mot, 300, 100)

    pygame.display.flip()
    clock.tick(30)
