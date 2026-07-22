import pygame
import os


class SpotifyPage:

    def __init__(self):
       
#fonts        
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        
        self.top_label_font = pygame.font.Font(font_path, 80)
        self.artist_font = pygame.font.Font(font_path, 60)
        self.text_font = pygame.font.Font(font_path, 20)

#colours

        self.GREEN = (29, 185, 84)
        self.DARK_GREY = (18, 18, 18)
        self.GREY = (60, 60, 60)
        self.LIGHT_GREY = (80, 80, 80)
        self.WHITE = (225, 225, 225)

    def update(self):
        pass

    def draw(self, screen, data):
        
#background card
        pygame.draw.rect(screen, self.GREY, (10, 10, 780, 460), border_radius = 25)

#top text 
        label_text_surface = self.top_label_font.render("SPOTIFY", True, self.GREEN)
        label_text_rect = label_text_surface.get_rect(centerx = 400, centery = 80)
        screen.blit(label_text_surface, label_text_rect)


#spotify now playing card
        pygame.draw.rect(screen, self.DARK_GREY, (20, 140, 520, 320), border_radius = 25) #main card
        pygame.draw.rect(screen, self.GREEN, (20, 140, 520, 320), width=4, border_radius = 25) #green outline for the card


#track information
    #artist
        info_artist_surface = self.text_font.render("ARTIST", True, self.WHITE)
        info_artist_rect = info_artist_surface.get_rect(centerx = 670, centery = 175)
        screen.blit(info_artist_surface, info_artist_rect)

    #album name
        info_album_surface = self.text_font.render("ALBUM NAME", True, self.WHITE)
        info_album_rect = info_album_surface.get_rect(centerx = 670, centery = 280)
        screen.blit(info_album_surface, info_album_rect)

    #release date
        info_date_surface = self.text_font.render("RELEASE DATE", True, self.WHITE)
        info_date_rect = info_date_surface.get_rect(centerx = 670, centery = 385)
        screen.blit(info_date_surface, info_date_rect)

        


