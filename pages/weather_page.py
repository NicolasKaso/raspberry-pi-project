import pygame
import os
from datetime import datetime


class WeatherPage:

    def __init__(self):                                             #INIT PART OF THE CODE
        
#variables
        self.WHITE = (255, 255, 255)
        self.GREY = (60, 60, 60)
        self.BLUE_GREY = (30, 40, 60)
        self.GOLD = (255, 190, 80)

        now = datetime.now()
        self.day = now.strftime("%A")
        

#fonts
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf") 
        self.week_day_font = pygame.font.Font(font_path, 50)
        self.current_weather_font = pygame.font.Font(font_path, 50)
        self.current_feels_like_font = pygame.font.Font(font_path, 30)
        self.feels_like_text_font = pygame.font.Font(font_path, 20)
        self.info_text_font = pygame.font.Font(font_path, 30)
        self.current_condition_font = pygame.font.Font(font_path, 30)
        self.current_wind_speed_font = pygame.font.Font(font_path, 40)
        self.current_humidity_font = pygame.font.Font(font_path, 40)
        self.forecast_day_font = pygame.font.Font(font_path, 40)
        self.forecast_temp_font = pygame.font.Font(font_path, 30)
        self.forecast_condition_font = pygame.font.Font(font_path, 30)


    def update(self, data):                                         #UPDATE PART OF THE CODE
        
#day of the week for the current weather update
        
        now = datetime.now()

        current_day = now.strftime("%A")
        if current_day != self.day:
            self.day = current_day




    def draw(self, screen, data):                                   #DRAW PART OF THE CODE
        
#static elements
        
    #current weather background card
        pygame.draw.rect(screen, self.BLUE_GREY, (10, 10, 320, 260), border_radius = 25)


    #current weather info background card
        pygame.draw.rect(screen, self.BLUE_GREY, (340, 10, 450, 260), border_radius = 25)


    #forecast weather background card
        pygame.draw.rect(screen, self.BLUE_GREY, (10, 280, 780, 190), border_radius = 25)


    #condition info text
        condition_info_surface = self.info_text_font.render("CONDITON:", True, self.WHITE)
        condition_info_rect = condition_info_surface.get_rect(left = 350, centery = 53)    
        screen.blit(condition_info_surface, condition_info_rect)  


    #wind speed info text
        wind_speed_info_surface = self.info_text_font.render("WIND SPEED:", True, self.WHITE)
        wind_speed_info_rect = wind_speed_info_surface.get_rect(left = 350, centery = 135)
        screen.blit(wind_speed_info_surface, wind_speed_info_rect)


    #humididy info text
        humidity_info_text_surface = self.info_text_font.render("HUMIDITY:", True, self.WHITE)
        humidity_info_text_rect = humidity_info_text_surface.get_rect(left = 350, centery = 217)
        screen.blit(humidity_info_text_surface, humidity_info_text_rect)


#changing elements

    #day for the current_weather

        current_day_surface = self.week_day_font.render(self.day, True, self.WHITE)
        current_day_rect = current_day_surface.get_rect(centerx = 170, centery = 60)
        screen.blit(current_day_surface, current_day_rect)
    
    #current weather
        current_weather = data["weather"].get("temp", 0)

        current_weather_surface = self.current_weather_font.render(str(current_weather) + "°C", True, self.GOLD)
        current_weather_rect = current_weather_surface.get_rect(centerx = current_day_rect.centerx, top = current_day_rect.bottom + 5)
        screen.blit(current_weather_surface, current_weather_rect)

    #feels_like text
        feels_like_text_surface = self.feels_like_text_font.render("FEELS LIKE", True, self.WHITE)
        feels_like_text_rect = feels_like_text_surface.get_rect(centerx = current_weather_rect.centerx, top = current_weather_rect.bottom + 10)
        screen.blit(feels_like_text_surface, feels_like_text_rect)


    #current feels like
        current_feels_like = data["weather"].get("feels_like", 0)

        current_feels_like_surface = self.current_feels_like_font.render(str(current_feels_like) + "°C", True, self.GOLD)
        current_feels_like_rect = current_feels_like_surface.get_rect(centerx = feels_like_text_rect.centerx, top = feels_like_text_rect.bottom + 5)
        screen.blit(current_feels_like_surface, current_feels_like_rect)    
        

    #current condition
        current_condition = data["weather"].get("condition", None)

        current_condition_surface = self.current_condition_font.render(str(current_condition), True, self.GOLD)
        current_condition_rect = current_condition_surface.get_rect(left = condition_info_rect.right + 10, centery = condition_info_rect.centery)
        screen.blit(current_condition_surface, current_condition_rect)  


    #current wind speed
        current_wind_speed = data["weather"].get("wind_speed", 0)

        current_wind_speed_surface = self.current_wind_speed_font.render(str(current_wind_speed) + " km/h", True, self.GOLD)
        current_wind_speed_rect = current_wind_speed_surface.get_rect(left = wind_speed_info_rect.right + 10, centery = wind_speed_info_rect.centery)
        screen.blit(current_wind_speed_surface, current_wind_speed_rect)


    #current humidity
        current_humidity = data["weather"].get("humidity", 0)

        current_humidity_surface = self.current_humidity_font.render(str(current_humidity) + " %", True, self.GOLD)
        current_humidity_rect = current_humidity_surface.get_rect(left = humidity_info_text_rect.right + 10, centery = humidity_info_text_rect.centery)
        screen.blit(current_humidity_surface, current_humidity_rect)


#forecast
        
        forecast_days = data.get("forecast", {}).get("forecast", [])[1:]
        for i, day in enumerate(forecast_days):
            day_name = day.get("date", "")
            avg_temp = day.get("avgtemp_c", "")
            condition = day.get("condition", "")

            day_x = 205 + (i * 390)

    #dates
            day_name_surface = self.forecast_day_font.render(day_name, True, self.WHITE)
            day_name_rect = day_name_surface.get_rect(centerx = day_x, top = 290)
            screen.blit(day_name_surface, day_name_rect)


    #average temp
            avg_temp_surface = self.forecast_temp_font.render(str(avg_temp) + "°C", True, self.GOLD)
            avg_temp_rect = avg_temp_surface.get_rect(centerx=day_x, top=day_name_rect.bottom + 10)
            screen.blit(avg_temp_surface, avg_temp_rect)


    #condition
            condition_surface = self.forecast_condition_font.render(condition, True, self.GOLD)
            condition_rect = condition_surface.get_rect(centerx=day_x, top=avg_temp_rect.bottom + 10)
            screen.blit(condition_surface, condition_rect)
        
