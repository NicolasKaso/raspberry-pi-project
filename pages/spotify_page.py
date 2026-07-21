class SpotifyPage:

    def __init__(self):
       
#fonts        
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        
        self.title_font = pygame.font.Font(font_path, 60)
        self.artist_font = pygame.font.Font(font_path, 40)

#colours

        self.GREEN = (29, 185, 84)
        self.GREY = (60, 60, 60)
        self.LIGHT_GREY = (80, 80, 80)

    def update(self):
        pass

    def draw(self, screen, data):
        
#background card
        pygame.draw.rect(screen, self.GREY, (10, 10, 780, 460), border_radius = 25)

