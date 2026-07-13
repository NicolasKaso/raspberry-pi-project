import pygame

from pages.main_page import MainPage
from pages.stats_page import StatsPage
from pages.spotify_page import SpotifyPage
from pages.tasks_page import TasksPage
from pages.calendar_page import CalendarPage
from pages.weather_page import WeatherPage
from data.fetcher import Fetcher


pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
running = True
BLACK = (0, 0, 0)


# file instances

page = MainPage()


stats = StatsPage()


spotify = SpotifyPage()


task = TasksPage()


calendar = CalendarPage()


weather = WeatherPage()


fetcher = Fetcher()


# Active page tracker

current_page = page


# main loop

while running:
    for event in pygame.event.get():


# keyboard press  detection

        mods = pygame.key.get_mods()
        if event.type == pygame.KEYDOWN and mods  & pygame.KMOD_META and mods & pygame.KMOD_ALT:

            if event.key == pygame.K_1:
                current_page = page

            elif event.key == pygame.K_2:
                current_page = calendar

            elif event.key == pygame.K_3:
                current_page = task

            elif event.key == pygame.K_4:
                current_page = spotify

            elif event.key == pygame.K_5:
                current_page = stats


# quit command

        if event.type == pygame.QUIT:
            running = False

    
#getting and drawing the data 
    screen.fill(BLACK)
    fetcher.update()
    data = fetcher.get_data() 
    current_page.update()
    current_page.draw(screen, data)


# display script on screen
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
