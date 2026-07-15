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

        performance = data["performance"]

#CPU
        self.draw_gauge(screen, performance["cpu"], 100, 150, "CPU")

#GPU
        self.draw_gauge(screen, performance["gpu"], 350, 150, "GPU")

#RAM
        self.draw_gauge(screen, performance["memory"], 600, 150, "MEMORY")

#STORAGE


    def draw_gauge(self, screen, value, x, y, label):

        angle_degrees = 180 - (value / 100) * 180
        angle_radians = math.radians(angle_degrees)

#differant colours depending on use %
        if value < 25:
            self.arc_colour = self.GREEN

        elif value > 75:
            self.arc_colour = self.RED

        else:
            self.arc_colour = self.YELLOW

#background arc(empty)
        pygame.draw.arc(screen, self.GREY, (x, y, 100, 100), 0, math.radians(180), 20) 

#usage arc
        pygame.draw.arc(screen, self.arc_colour, (x, y, 100, 100), angle_radians, math.radians(180), 20) 

