# Aperture Clock
# Written By: Trentyne Morgan

# Import Libraries
import pygame, sys
from pygame.locals import *
import datetime

# Load PyGame
pygame.init()

# Screen Resolution
ScreenWidth = 600
ScreenHeight = 600

#RGB Colors
ORANGE = (255, 154,  0)
BLACK  = (  0 ,  0,  0)

# Main Application Window
MainApplicationWindowObj = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Aperture Science Clock")

# Mouse Placement System
def mouseplacement():
    cursorpos = pygame.mouse.get_pos()
    print("Current Mouse Position:", cursorpos)

# Import Font File
try:
    DigitalLCD = pygame.font.Font('digit_lcd.ttf', 23)
except:
   DigitalLCD = pygame.font.Font('digit_lcd.ttf', 23)

# Aperture Background Image
ApertureApplicationBackground = pygame.image.load('ApertureBackground.png').convert()

# Set the Background Image
MainApplicationWindowObj.blit(ApertureApplicationBackground, (0, 0))

# Get the Date and Time
CurrentDateTime = datetime.datetime.now()

# Convert the Time Variable into a readable format   
DateTimeFormatObj = CurrentDateTime.strftime("%Y-%m-%d %H:%M")

# Time Text Object
TimeTextObj = DigitalLCD.render(DateTimeFormatObj, True, ORANGE, BLACK)
TimeTextRectObj = TimeTextObj.get_rect()
TimeTextRectObj.center = (300, 300)

# Main Application/Event Loop
while True:
    CurrentDateTime = datetime.datetime.now()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
         mouseplacement()
        if event.type == QUIT:
         pygame.quit()
         sys.exit()
    MainApplicationWindowObj.blit(TimeTextObj, TimeTextRectObj)
    pygame.display.update()
        
        
        
