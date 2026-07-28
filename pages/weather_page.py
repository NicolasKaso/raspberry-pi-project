import pygame
import os


class WeatherPage:

    def __init__(self):                                             #INIT PART OF THE CODE
        
#variables
        self.WHITE = (255, 255, 255)
        self.GREY = (60, 60, 60)
        

#fonts
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf") 
        self.general_font = pygame.font.Font(font_path, 40)

    def update(self, data):                                         #UPDATE PART OF THE CODE
        pass


    def draw(self, screen, data):                                   #DRAW PART OF THE CODE
        
#static elements
        
    #current weather background card
        pygame.draw.rect(screen, self.GREY, (10, 10, 780, 260), border_radius = 25)


    #forecast weather background card
        pygame.draw.rect(screen, self.GREY, (10, 280, 780, 190), border_radius = 25)


#changing elements
    
#current weather
        
