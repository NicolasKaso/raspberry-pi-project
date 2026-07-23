import pygame
import os


class SpotifyPage:

    def __init__(self):
       
#fonts        
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        self.font_path = font_path
        
        self.top_label_font = pygame.font.Font(font_path, 80)
        self.artist_font = pygame.font.Font(font_path, 30)
        self.text_font = pygame.font.Font(font_path, 20)
        self.number_font = pygame.font.Font(font_path, 15)
        
#colours

        self.GREEN = (29, 185, 84)
        self.DARK_GREY = (18, 18, 18)
        self.GREY = (60, 60, 60)
        self.LIGHT_GREY = (80, 80, 80)
        self.WHITE = (225, 225, 225)

        self.cached_track = None
        self.name_surface = None

        self.cached_artist = None
        self.artist_surface = None

        self.cached_album = None
        self.album_surface = None


    def update(self, data):
        track = data.get("spotify", {}).get("track", "")
        if track != self.cached_track:
            self.cached_track = track
            self.name_surface = self.render_fit(self.font_path, track, 480, 30, self.WHITE)

        artist = data.get("spotify", {}).get("artist", "")
        if artist != self.cached_artist:
            self.cached_artist = artist
            self.artist_surface = self.render_fit(self.font_path, artist, 180, 30, self.WHITE)

        album = data.get("spotify", {}).get("track", "")
        if album != self.cached_album:
            self.cached_album = album
            self.album_surface = self.render_fit(self.font_path, album, 180, 30, self.WHITE)

        
    def draw(self, screen, data):
#static elements


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
        info_artist_surface = self.text_font.render("ARTIST", True, self.GREEN)
        info_artist_rect = info_artist_surface.get_rect(centerx = 670, centery = 175)
        screen.blit(info_artist_surface, info_artist_rect)

        #album name
        info_album_surface = self.text_font.render("ALBUM NAME", True, self.GREEN)
        info_album_rect = info_album_surface.get_rect(centerx = 670, centery = 280)
        screen.blit(info_album_surface, info_album_rect)

        #playing yes or no
        
        info_playing_surface = self.text_font.render("PLAYING STATUS", True, self.GREEN)
        info_playing_rect = info_playing_surface.get_rect(centerx = 670, centery = 385)
        screen.blit(info_playing_surface, info_playing_rect)

        
#changing elements
    
    #song image
        art_surface = data["spotify"].get("art_surface", None)
        
        art_rect = pygame.Rect(0, 0, 200, 200)
        art_rect.centerx = 280
        art_rect.top = 155

        if art_surface is not None:
            art_surface = pygame.transform.scale(art_surface, (160, 160))
            art_rect = art_surface.get_rect(centerx = 280, top = 155)
            screen.blit(art_surface, art_rect)

    #song name
        name_rect = self.name_surface.get_rect(centerx = 280, top = art_rect.bottom + 10)
        screen.blit(self.name_surface, name_rect)


    #progress bar

        progress = data["spotify"].get("progress", 0)
        duration = data["spotify"].get("duration", 1)

        if progress is None or duration is None or duration == 0:
            fraction = 0
        else:
            fraction = progress /duration

        fill_width = int(440 * fraction)


        pygame.draw.rect(screen, self.GREY, (60, 415, 440, 8), border_radius = 4)
        pygame.draw.rect(screen, self.WHITE, (60, 415, fill_width, 8), border_radius = 4)

        
    #progress and duration numbers above bar
        #progress
        total_seconds = progress // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_string_progress = f"{minutes}: {seconds:02d}"

        progress_number_surface = self.number_font.render(time_string_progress, True, self.WHITE)
        progress_number_rect = progress_number_surface.get_rect(left = 60, centery = 400)
        screen.blit(progress_number_surface, progress_number_rect)


        #total duration
        total_seconds_d = duration // 1000
        seconds_d = total_seconds_d % 60
        minutes_d = total_seconds_d // 60
        time_string_duration = f"{minutes_d}:{seconds_d:02d}"

        duration_number_surface = self.number_font.render(time_string_duration, True, self.WHITE)
        duration_number_rect = duration_number_surface.get_rect(right = 500, centery = 400)
        screen.blit(duration_number_surface, duration_number_rect)

    
    #artist name
        artist_rect = self.artist_surface.get_rect(centerx = 670, top = info_artist_rect.bottom + 15)
        screen.blit(self.artist_surface, artist_rect)


    #album
        album_rect = self.album_surface.get_rect(centerx = 670, top = info_album_rect.bottom + 15)
        screen.blit(self.album_surface, album_rect)

    #playing status
        if data["spotify"].get("now_playing", None) == True:
            playing_true_surface = self.artist_font.render("PLAYING", True, self.WHITE)
            playing_true_rect = playing_true_surface.get_rect(centerx = 670, top = info_playing_rect.bottom + 15)
            screen.blit(playing_true_surface, playing_true_rect)

        elif data["spotify"].get("now_playing", None) == None:
            pass


        else:
            playing_false_surface = self.artist_font.render("PAUSED", True, self.WHITE)
            playing_false_rect = playing_false_surface.get_rect(centerx = 670, top = info_playing_rect.bottom + 15)
            screen.blit(playing_false_surface, playing_false_rect)

            
    def render_fit(self, font_path, text, max_width, start_size, color):
        size = start_size
        while size >10:
            font = pygame.font.Font(font_path, size)
            surface = font.render(text, True, color)
            if surface.get_width() <= max_width:
                return surface
            size -= 2
        return surface

