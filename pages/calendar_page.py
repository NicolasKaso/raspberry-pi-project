import pygame
import os


class CalendarPage:

    def __init__(self):
        
#variables
        self.WHITE = (225, 225, 225)
        self.GREY = (60, 60, 60)


#fonts
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        self.page_name_font = pygame.font.Font(project(font_path, 50))

    def update(self, data):
        pass    

    def draw(self, screen, data):
        
#static elements
        
    #background card
        pyagme.draw.rect(screen, self.GREY, (10, 10, 780, 460))


    #page name(calendar)
        page_name_surface = self.page_name_font.render("CALENDAR", True, self.WHITE)
        page_name_rect = page_name_surface.get_rect(centerx = 400, centery = 40)
        screen.blit(page_name_surface, page_name_rect)
