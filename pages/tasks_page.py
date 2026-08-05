import pygame
import os


class TasksPage:
    def __init__(self):
        # Font path — same project_root pattern as your other pages
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        self.font_path = font_path

        self.empty_font = pygame.font.Font(font_path, 24)

        # Colors — same palette as weather_page.py / calendar_page.py
        self.WHITE = (255, 255, 255)
        self.GREY = (60, 60, 60)
        self.BLUE_GREY = (30, 40, 60)
        self.GOLD = (255, 190, 80)

        # Layout constants
        self.MARGIN = 10
        self.GAP = 10
        self.SCREEN_W = 800
        self.SCREEN_H = 480
        self.MIN_ROW_HEIGHT = 50
        self.CHECKBOX_SIZE = 20

        # Cache — only rebuild title surfaces when the task list actually changes
        self.cached_tasks = None
        self.title_surfaces = []

    def render_fit(self, font_path, text, max_width, start_size, color):
        size = start_size
        font = pygame.font.Font(font_path, size)
        surface = font.render(text, True, color)
        while surface.get_width() > max_width and size > 10:
            size -= 1
            font = pygame.font.Font(font_path, size)
            surface = font.render(text, True, color)
        return surface

    def update(self, data):
        tasks = data.get("tasks", [])

        if tasks != self.cached_tasks:
            self.cached_tasks = tasks
            self.title_surfaces = []
            row_width = self.SCREEN_W - (self.MARGIN * 2)
            max_text_width = row_width - self.CHECKBOX_SIZE - 45

            for task in tasks:
                title = task.get("title", "Untitled")
                surface = self.render_fit(self.font_path, title, max_text_width, 40, self.WHITE)
                self.title_surfaces.append(surface)

    def draw(self, screen, data):
        tasks = data.get("tasks", [])

        # Nothing to do — show a simple message and stop
        if not tasks:
            msg_surface = self.empty_font.render("No tasks", True, self.GREY)
            msg_rect = msg_surface.get_rect(centerx=self.SCREEN_W // 2, centery=self.SCREEN_H // 2)
            screen.blit(msg_surface, msg_rect)
            return

        row_width = self.SCREEN_W - (self.MARGIN * 2)

        row_height = 60

        for i, task in enumerate(tasks):
            row_y = self.MARGIN + i * (row_height + self.GAP)
            rect = (self.MARGIN, row_y, row_width, row_height)
            pygame.draw.rect(screen, self.BLUE_GREY, rect, border_radius=16)

            # Checkbox — just an empty rounded square outline, since
            # showCompleted=False means everything here still needs doing
            checkbox_rect = (
                self.MARGIN + 20,
                row_y + (row_height - self.CHECKBOX_SIZE) / 2,
                self.CHECKBOX_SIZE,
                self.CHECKBOX_SIZE
            )
            pygame.draw.rect(screen, self.GOLD, checkbox_rect, width=2, border_radius=5)

            title_surface = self.title_surfaces[i]
            title_rect = title_surface.get_rect(
                left=self.MARGIN + 20 + self.CHECKBOX_SIZE + 15,
                centery=row_y + row_height / 2
            )
            screen.blit(title_surface, title_rect)
