import pygame

from keyboards import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# Pygame setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Visualiser")

# creating fonts
mono = pygame.font.SysFont("FreeMono", 25)
bold = pygame.font.SysFont("FreeMono", 25, bold=True)

# Global Variables
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
margins = {"top":200, "bottom":100, "left":100, "right":100}
gap = 80

# Rotor settings
i = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
ii = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
iii = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
iv = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
v = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

# Reflector settings
a = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
b = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
c = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Plugboard settings
pb = Plugboard(["AB", "CD", "EF"])
kb = Keyboard()

enigma = Enigma(b, i, ii, iii, pb, kb)
# print(enigma.encrypt("A"))
enigma.setKey("CAT")
enigma.setRings((1, 1, 1))

# message = "TESTINGTESTINGTESTINGTESTING"
# ciphertext = ""
# for letter in message:
#     ciphertext += enigma.encrypt(letter)
# print(ciphertext)

animating = True
while animating:
    screen.fill("#333333")
    draw(enigma, screen, width, height, margins, gap, bold)
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ii.rotate()