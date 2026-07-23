import math
import pygame  
import os

project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

class StatsPage:

    def __init__(self):

        font_path_label = os.path.join(project_root, "fonts", "ArchivoNarrow-Bold.ttf")
        self.label_font = pygame.font.Font(font_path_label, 28)
        self.top_label_font = pygame.font.Font(font_path_label, 50)
        self.WHITE = (255, 255, 255)
        self.GREY = (80, 80, 80)
        self.BACK_GREY = (60, 60, 60)
        self.GREEN = (0, 200, 0)
        self.YELLOW = (230, 200, 0)
        self.RED = (240, 40, 40)
        

    def update(self, data):
        pass

    def draw(self, screen, data):

#background card
        
        pygame.draw.rect(screen, self.BACK_GREY, (10, 10, 780, 460), border_radius = 25)

#top text (PERFORMANCE)

        top_text_surface = self.top_label_font.render("STATISTICS", True, self.WHITE)
        top_text_rect = top_text_surface.get_rect(centerx = 400, centery = 80)
        screen.blit(top_text_surface, top_text_rect)


#performance gauges and values

        performance = data["performance"]

    #CPU
        self.draw_gauge(screen, performance.get("cpu",0), 35, 150, "CPU")


    #GPU
        self.draw_gauge(screen, performance.get("gpu",0), 290, 150, "GPU")


    #RAM
        self.draw_gauge(screen, performance.get("memory",0), 545, 150, "MEMORY")


#STORAGE


        
        bar_x = 100
        bar_y = 400
        bar_width = 600
        bar_height = 30
        bar_rect = (bar_x, bar_y, bar_width, bar_height)

        disk_percent = performance.get("disk_used_percentage", 0)
        filled_width = bar_width * (disk_percent / 100)
        
    #text
        storage_text_surface = self.label_font.render("USED STORAGE - " + str(disk_percent) + "%", True, self.WHITE)
        storage_text_rect = storage_text_surface.get_rect(centerx = 400, top = 350)
        screen.blit(storage_text_surface, storage_text_rect)

    #empty bar
        pygame.draw.rect(screen, self.GREY, bar_rect, border_radius = 15)

    #usage bar
        pygame.draw.rect(screen, self.WHITE, (bar_x, bar_y, filled_width, bar_height), border_radius = 15)







    def draw_gauge(self, screen, value, x, y, label):
        
        diameter = 220
        gauge_rect = pygame.Rect(x, y, diameter, diameter)

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
        pygame.draw.arc(screen, self.GREY, gauge_rect, 0, math.radians(180), 35) 

#usage arc
        pygame.draw.arc(screen, self.arc_colour, gauge_rect,  angle_radians, math.radians(180), 35) 


#label for the arcs
        
        text_surface = self.label_font.render(label, True, self.WHITE)
        text_rect = text_surface.get_rect(centerx = gauge_rect.centerx, top = gauge_rect.centery + 10)
        screen.blit(text_surface, text_rect)

# % usage of the resources

        value_text = f"{int(value)}%"
        value_surface = self.label_font.render(value_text, True, self.WHITE)
        value_rect = value_surface.get_rect(centerx=gauge_rect.centerx, centery=gauge_rect.centery - 20)
        screen.blit(value_surface, value_rect)
