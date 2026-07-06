#INFO: Everything with "Debug" after it only exists in the development script, not in precompiled binaries nor the standard source
#Imports
import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
import string
import secrets
import socket #Needed later when establishing comms with server
#TODO: import socket, secrets and string only if set up in Desktop + Mobile mode. No need to do that if you're going fully local.

#Initiate Pygame and UI prerequisites
pygame.init()
screen = pygame.display.set_mode((1366, 768))
width, height = screen.get_size()
screen.fill((234, 235, 237))
font = pygame.font.Font('SFPRODISPLAYREGULAR.OTF', 72)
print("Display initiated") #Debug

#Display welcome screen and its widgets
text = font.render('Welcome to mommy.ai!', True, (0,105,137))
textRect = text.get_rect()
textRect.center = (width // 2, height // 3)
screen.blit(text, textRect)

Beginbutton = pygame.transform.scale(pygame.image.load("Begin.png"), (width/3, width*3/16))
screen.blit(Beginbutton, ((width/2)-(width/3)/2,(height/3*2)-(width*3/16)/2)) #Math mess to blit the button correctly (I'm terrible at math and I have absolutely no clue how I managed to make this crap work.)

#Create ID
alphabet = string.ascii_letters + string.digits
userID = ''.join(secrets.choice(alphabet) for _ in range(24))

print("ID created:", userID) #Debug

'''
Abandon hope, all ye who enter here.
'''

def output():
    global name
    name = textbox.getText()

def nameentry(screen, font):
	width, height = screen.get_size()
	text = font.render('What should the AI refer to you as?', True, (0,105,137))
	textRect = text.get_rect()
	textRect.center = (width // 2, height // 3)
	screen.blit(text, textRect)
	
	global textbox
	textbox = TextBox(screen, (width/2)-(width/3)/2,(height/3*2)-(width*3/16)/2, width/3, 80, fontSize=50,borderColour=(0,105,137), textColour=(0,105,137),onSubmit=output, radius=10,borderThickness=5)
#Pygame sys stuff and main event loop, put last because the docs said to
pygame.display.flip()

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Beginbutton_rect = Beginbutton.get_rect(topleft = ((width/2)-(width/3)/2,(height/3*2)-(width*3/16)/2))
            if Beginbutton_rect.collidepoint(event.pos):
            	screen.fill((234, 235, 237))
            	nameentry(screen, font)
            	pygame_widgets.update(events)
            	pygame.display.flip()		
#I'd spent 1,5 days getting this bullshit to work. If someone DARES to refactor the button logic, I'll track them down and fucking RIP THEM APART. The fruit of my labor and wasted time should NOT be touched. Ever.
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:  
                running = False

pygame.quit()