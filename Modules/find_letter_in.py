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

# 7 vies
corps_plein = ["O", "/", "|", "\\", "/", "\\", "X"]
corps = [" ", " ", " ", " ", " ", " ", " "]

clock = pygame.time.Clock()

# Fonction pour centrer le texte horizontalement
def afficher_texte_centre(texte, y):
    img = font.render(texte, True, (255, 255, 255))
    rect = img.get_rect(center=(LARGEUR // 2, y))
    fenetre.blit(img, rect)

while True:
    fenetre.fill((0, 0, 0))

    # Événements clavier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and not trouve and faux < 7:
            lettre = event.unicode.lower()
            if lettre.isalpha() and lettre not in lettres:
                lettres.append(lettre)
                if lettre not in mot:
                    corps[faux] = corps_plein[faux]
                    faux += 1

    # Affichage du mot à deviner
    affichage_mot = ""
    trouve = True
    for l in mot:
        if l in lettres:
            affichage_mot += l + " "
        else:
            affichage_mot += "_ "
            trouve = False

    afficher_texte_centre(affichage_mot, 300)

    # Lettres déjà jouées
    afficher_texte_centre("Lettres : " + " ".join(lettres), 340)

    # Affichage du pendu symbolique (7 étapes)
    afficher_texte_centre("Tête         : " + corps[0], 50)
    afficher_texte_centre("Cou          : " + corps[1], 90)
    afficher_texte_centre("Bras gauche  : " + corps[2], 130)
    afficher_texte_centre("Bras droit   : " + corps[3], 170)
    afficher_texte_centre("Tronc        : " + corps[4], 210)
    afficher_texte_centre("Jambe gauche : " + corps[5], 250)
    afficher_texte_centre("Jambe droite : " + corps[6], 290)

    # Vies restantes
    afficher_texte_centre(f"Vies restantes : {7 - faux}", 20)

    # Victoire / Défaite
    if trouve:
        afficher_texte_centre("TU AS GAGNÉ !", 120)
    if faux >= 7:
        afficher_texte_centre("PERDU ! Mot : " + mot, 120)

    pygame.display.flip()
    clock.tick(30)
