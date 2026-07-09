import pygame
import os
from datetime import datetime
FLIP_DURATION_MS = 400

project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
font_path_clock = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
font_path_am_pm = os.path.join(project_root, "fonts", "ArchivoNarrow-Bold.ttf")
font_path_date = os.path.join(project_root, "fonts", "ArchivoNarrow-Bold.ttf")

MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class MainPage: 

    def __init__(self): #INIT PART OF THE CODE

#variables

        self.WHITE = (255, 255, 255)
        self.GREY = (60, 60, 60)

        now = datetime.now()
        
        self.hour_animation_start = None
        self.hour = now.hour
        
        self.minute_animation_start = None
        self.minute = now.minute

        self.day = now.day

        self.month = now.month

        self.year = now.year

        self.next_hour = self.hour
        self.next_minute = self.minute


#fonts

        self.hour_font = pygame.font.Font(font_path_clock, 230)
        self.minute_font = pygame.font.Font(font_path_clock, 230)
        self.colon_font = pygame.font.Font(font_path_clock, 230)
        self.am_pm_font = pygame.font.Font(font_path_am_pm, 60)
        self.date_font = pygame.font.Font(font_path_date, 40)


    def update(self): #UPDATE PART OF THE CODE
        
        now = datetime.now()

#hours
        current_hour = now.hour
        if current_hour != self.hour:
            if self.hour_animation_start is None:
                self.hour_animation_start = pygame.time.get_ticks()
                self.next_hour = current_hour

            else:
                if pygame.time.get_ticks() - self.hour_animation_start >= FLIP_DURATION_MS:
                    self.hour_animation_start = None
                    self.hour = current_hour

    
#minutes
        current_minute = now.minute
        if current_minute != self.minute:
            if self.minute_animation_start == None:
                self.minute_animation_start = pygame.time.get_ticks()
                self.next_minute = current_minute

            else:
                if pygame.time.get_ticks() - self.minute_animation_start >= FLIP_DURATION_MS:
                    self.minute_animation_start = None
                    self.minute = current_minute


#date_day

        current_day = now.day
        if current_day != self.day:
            self.day = current_day


#date_month

        current_month = now.month
        if current_month != self.month:
            self.month = current_month


#date_year

        current_year = now.year
        if current_year != self.year:
            self.year = current_year


    def draw(self, screen, data): #drawing part of the code

#am/pm logic

        display_hour = self.hour % 12

        if display_hour == 0:
            display_hour = 12

        am_pm = "am" if self.hour < 12 else "pm"

#strings

        hour_time_string = f"{display_hour:02d}"
        minute_time_string = f"{self.minute:02d}"
        date_string = f"{MONTH_NAMES[self.month -1]} {self.day}, {self.year}"


#hour clock numbers

        hour_surface = self.hour_font.render(hour_time_string, True, self.WHITE)
        hour_rect = hour_surface.get_rect()


#minute clock numbers

        minute_surface = self.minute_font.render(minute_time_string, True, self.WHITE)
        minute_rect = minute_surface.get_rect()


#card placement and size
        
        hour_card = pygame.Rect(0, 0, 0, 0)
        minute_card = pygame.Rect(0, 0, 0, 0)

        hour_card.width = hour_rect.width + 40
        minute_card.width = minute_rect.width + 40

        hour_card.height = hour_rect.height + 40
        minute_card.height = minute_rect.height + 40

        card_total_width = hour_card.width + minute_card.width + 20

        card_start_x = (800 - card_total_width) // 2

        hour_card.left = card_start_x
        hour_card.centery = 230

        minute_card.left = hour_card.right + 20
        minute_card.centery = 230


#clock surface placement

    #hour
        hour_rect.centerx = hour_card.centerx
        hour_rect.centery = hour_card.centery
    
    #minute
        minute_rect.centerx = minute_card.centerx
        minute_rect.centery = hour_card.centery



#hour clock card

        hour_card_surface = pygame.draw.rect(screen, self.GREY, hour_card, border_radius = 25)


#minute clock card

        minute_card_surface = pygame.draw.rect(screen, self.GREY, minute_card, border_radius = 25)


#date 

        date_surface = self.date_font.render(date_string, True, self.WHITE)
        date_rect = date_surface.get_rect()
        date_rect.centerx = 400
        date_rect.centery = 445


#AM/PM

        am_pm_surface = self.am_pm_font.render(am_pm, True, self.WHITE)
        am_pm_rect = am_pm_surface.get_rect()
        am_pm_rect.left = minute_rect.right - 65
        am_pm_rect.top = hour_rect.bottom - 60


#blit on the screen

        screen.blit(hour_surface, hour_rect)
        screen.blit(minute_surface, minute_rect)
        screen.blit(date_surface, date_rect)
        screen.blit(am_pm_surface, am_pm_rect)

