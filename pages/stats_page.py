import math
import pygame   

class StatsPage:

    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.GREY = (80, 80, 80)
        self.GREEN = (0, 200, 0)
        self.YELLOW = (230, 200, 0)
        self.RED = (240, 40, 40)
        

    def update(self):
        pass

    def draw(self, screen, data):
        
        value = 65
        angle_degrees = 180 - (value / 100) * 180
        angle_radians = math.radians(angle_degrees)

        #background arc(empty)
        pygame.draw.arc(screen, self.GREY, (0, 0, 100, 100), 0, math.radians(180), 20) 

        #differant colours depending on use
        if value < 25:
            self.arc_colour = self.GREEN

        elif value > 75:
            self.arc_colour = self.RED

        else:
            self.arc_colour = self.YELLOW
        
        #usage arc
        pygame.draw.arc(screen, self.arc_colour, (0, 0, 100, 100), angle_radians, math.radians(180), 20) 

