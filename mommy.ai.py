#INFO: Everything with "Debug" after it only exists in the development script, not in precompiled binaries nor the standard source
#Imports
import pygame
import string
import secrets
import socket #Needed later when establishing comms with server
#TODO: import socket, secrets and string only if set up in Desktop + Mobile mode.

#Initiate Pygame and UI prerequisites
pygame.init()
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
width, height = screen.get_size()
screen.fill((234, 235, 237))
font = pygame.font.Font('SFPRODISPLAYREGULAR.OTF', 72)

print("Display initiated") #Debug

#Display welcome screen
text = font.render('Welcome to mommy.ai!', True, (0,105,137))
textRect = text.get_rect()
textRect.center = (width // 2, height // 3)
screen.blit(text, textRect)

#Create ID
alphabet = string.ascii_letters + string.digits
userID = ''.join(secrets.choice(alphabet) for _ in range(24))

print("ID created:", userID) #Debug
#TODO: Make the name entry page

#Pygame sys stuff, put last because the docs said to
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:  
                running = False

pygame.quit()