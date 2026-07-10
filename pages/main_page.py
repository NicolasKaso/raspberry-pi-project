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
        self.BLACK = (0, 0, 0)

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


    def update(self):                                                                               #UPDATE PART OF THE CODE
        
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


    def draw(self, screen, data):                                                       #drawing part of the code


#12 hour logic current hour

        display_hour = self.hour % 12

        if display_hour == 0:
            display_hour = 12


#am/pm logic

        am_pm = "am" if self.hour < 12 else "pm"


#12 hour logic next hour

        display_next_hour = self.next_hour % 12

        if display_next_hour ==0:
            display_next_hour = 12

#strings

        hour_time_string = f"{display_hour:02d}"
        minute_time_string = f"{self.minute:02d}"
        next_hour_time_string = f"{display_next_hour:02d}"
        next_minute_time_string = f"{self.next_minute:02d}"
        date_string = f"{MONTH_NAMES[self.month -1]} {self.day}, {self.year}"


#hour clock numbers current

        hour_surface = self.hour_font.render(hour_time_string, True, self.WHITE)
        hour_rect = hour_surface.get_rect()


#minute clock numbers current

        minute_surface = self.minute_font.render(minute_time_string, True, self.WHITE)
        minute_rect = minute_surface.get_rect()


#hour clock numbers next 

        next_hour_surface = self.hour_font.render(next_hour_time_string, True, self.WHITE)
        next_hour_rect = next_hour_surface.get_rect()


#minute clock numbers next

        next_minute_surface = self.minute_font.render(next_minute_time_string, True, self.WHITE)
        next_minute_rect = next_minute_surface.get_rect()

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
        minute_rect.centery = minute_card.centery



#hour clock card

        pygame.draw.rect(screen, self.GREY, hour_card, border_radius = 25)


#minute clock card

        pygame.draw.rect(screen, self.GREY, minute_card, border_radius = 25)


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














# ANIMATION
    
    #hour
        if self.hour_animation_start is None:
            screen.blit(hour_surface, hour_rect)

        else:
            
            #phase 1
            elapsed = pygame.time.get_ticks() - self.hour_animation_start
            half_duration = FLIP_DURATION_MS / 2

            if elapsed < FLIP_DURATION_MS // 2:
                progress = elapsed / half_duration
                scale = 1 - progress

                original_height = hour_rect.height // 2
                new_height = int(original_height * scale)

                top_half_surface = hour_surface.subsurface((0, 0, hour_rect.width, original_height))
                squished_surface = pygame.transform.scale(top_half_surface, (hour_rect.width, new_height))

            #top part of the clock in phase 1
                blit_y = hour_card.centery - new_height
                screen.blit(squished_surface, (hour_rect.left, blit_y))

            #bottom part of the clock in phase 1
                bottom_half_surface = hour_surface.subsurface((0, original_height, hour_rect.width, hour_rect.height - original_height))
                screen.blit(bottom_half_surface, (hour_rect.left, hour_card.centery))

                
            #phase 2
            else:
                progress = (elapsed - half_duration) / half_duration
                scale = progress

                original_height = next_hour_rect.height // 2
                new_height = int(original_height * scale)

                bottom_half_surface = next_hour_surface.subsurface((0, original_height, next_hour_rect.width, next_hour_rect.height - original_height))

                top_half_surface = next_hour_surface.subsurface((0, 0, next_hour_rect.width, original_height))
                squished_surface = pygame.transform.scale(top_half_surface, (next_hour_rect.width, new_height))


                blit_y = hour_card.centery - new_height
                screen.blit(squished_surface, (hour_rect.left, blit_y))

                screen.blit(bottom_half_surface, (hour_rect.left, hour_card.centery))





    #minute
        if self.minute_animation_start is None:
            screen.blit(minute_surface, minute_rect)

        else:
            
            #phase 1
            elapsed = pygame.time.get_ticks() - self.minute_animation_start
            half_duration = FLIP_DURATION_MS / 2

            if elapsed < FLIP_DURATION_MS // 2:
                progress = elapsed / half_duration
                scale = 1 - progress

                original_height = minute_rect.height // 2
                new_height = int(original_height * scale)

                top_half_surface = minute_surface.subsurface((0, 0, minute_rect.width, original_height))
                squished_surface = pygame.transform.scale(top_half_surface, (minute_rect.width, new_height))

            #top part of the clock in phase 1
                blit_y = minute_card.centery - new_height
                screen.blit(squished_surface, (minute_rect.left, blit_y))

            #bottom part of the clock in phase 1
                bottom_half_surface = minute_surface.subsurface((0, original_height, minute_rect.width, minute_rect.height - original_height))
                screen.blit(bottom_half_surface, (minute_rect.left, minute_card.centery))

                
            #phase 2
            else:
                progress = (elapsed - half_duration) / half_duration
                scale = progress

                original_height = next_minute_rect.height // 2
                new_height = int(original_height * scale)

                bottom_half_surface = next_minute_surface.subsurface((0, original_height, next_minute_rect.width, next_minute_rect.height - original_height))

                top_half_surface = next_minute_surface.subsurface((0, 0, next_minute_rect.width, original_height))
                squished_surface = pygame.transform.scale(top_half_surface, (next_minute_rect.width, new_height))


                blit_y = minute_card.centery - new_height
                screen.blit(squished_surface, (minute_rect.left, blit_y))
    
                screen.blit(bottom_half_surface, (minute_rect.left, minute_card.centery))







#blit on the screen

        screen.blit(date_surface, date_rect)
        screen.blit(am_pm_surface, am_pm_rect)


#horizontal line hour

        pygame.draw.line(screen, self.BLACK, (hour_card.left, hour_card.centery), (hour_card.right, hour_card.centery), width = 7)


#horizontal line minute

        pygame.draw.line(screen, self.BLACK, (minute_card.left, minute_card.centery), (minute_card.right, minute_card.centery), width = 7)



