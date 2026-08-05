import pygame
import os
from datetime import datetime


class CalendarPage:
    def __init__(self):
        # Font path — same project_root pattern as spotify_page.py
        project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
        font_path = os.path.join(project_root, "fonts", "ArchivoBlack-Regular.ttf")
        self.font_path = font_path

        self.all_day_font = pygame.font.Font(font_path, 20)
        self.time_font = pygame.font.Font(font_path, 22)
        self.empty_font = pygame.font.Font(font_path, 24)

        # Colors — same palette as weather_page.py
        self.WHITE = (255, 255, 255)
        self.GREY = (60, 60, 60)
        self.BLUE_GREY = (30, 40, 60)
        self.GOLD = (255, 190, 80)

        # Layout constants
        self.MARGIN = 10
        self.GAP = 10
        self.SCREEN_W = 800
        self.SCREEN_H = 480
        self.ALL_DAY_HEIGHT = 40
        self.MIN_CARD_HEIGHT = 60

        # Cache — only rebuild title surfaces when the event list actually changes
        self.cached_events = None
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

    def format_time(self, iso_string):
        # Timed events look like "2026-08-01T14:00:00-04:00"
        dt = datetime.strptime(iso_string[:19], "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%-I:%M %p")

    def update(self, data):
        events = data.get("calendar", [])

        if events != self.cached_events:
            self.cached_events = events
            self.title_surfaces = []
            card_width = self.SCREEN_W - (self.MARGIN * 2)

            for event in events:
                title = event.get("title", "Untitled")
                surface = self.render_fit(self.font_path, title, card_width - 30, 24, self.WHITE)
                self.title_surfaces.append(surface)

    def draw(self, screen, data):
        events = data.get("calendar", [])

        all_day_events = [e for e in events if e.get("all_day")]
        timed_events = [e for e in events if not e.get("all_day")]
        timed_titles = [
            self.title_surfaces[i] for i, e in enumerate(events) if not e.get("all_day")
        ]

        y = self.MARGIN
        card_width = self.SCREEN_W - (self.MARGIN * 2)

        # All-day strip(s) at the top
        for event in all_day_events:
            rect = (self.MARGIN, y, card_width, self.ALL_DAY_HEIGHT)
            pygame.draw.rect(screen, self.BLUE_GREY, rect, border_radius=12)

            title = event.get("title", "Untitled")
            text_surface = self.all_day_font.render(f"All-day: {title}", True, self.GOLD)
            text_rect = text_surface.get_rect(left=self.MARGIN + 15, centery=y + self.ALL_DAY_HEIGHT // 2)
            screen.blit(text_surface, text_rect)

            y += self.ALL_DAY_HEIGHT + self.GAP

        # Nothing timed today — show a simple message and stop
        if not timed_events:
            msg_surface = self.empty_font.render("No events tomorrow", True, self.GREY)
            msg_rect = msg_surface.get_rect(centerx=self.SCREEN_W // 2, centery=(y + self.SCREEN_H) // 2)
            screen.blit(msg_surface, msg_rect)
            return

        # Dynamic card height so events fill the remaining space evenly
        available_height = self.SCREEN_H - y - self.MARGIN
        num_events = len(timed_events)
        total_gap_height = self.GAP * (num_events - 1)
        card_height = (available_height - total_gap_height) / num_events
        card_height = max(card_height, self.MIN_CARD_HEIGHT)

        for i, event in enumerate(timed_events):
            card_y = y + i * (card_height + self.GAP)
            rect = (self.MARGIN, card_y, card_width, card_height)
            pygame.draw.rect(screen, self.BLUE_GREY, rect, border_radius=20)

            start_raw = event.get("start", "")
            end_raw = event.get("end", "")
            try:
                time_text = f"{self.format_time(start_raw)} - {self.format_time(end_raw)}"
            except (ValueError, TypeError):
                time_text = ""

            time_surface = self.time_font.render(time_text, True, self.GOLD)
            time_rect = time_surface.get_rect(left=self.MARGIN + 15, top=card_y + 10)
            screen.blit(time_surface, time_rect)

            title_surface = timed_titles[i]
            title_rect = title_surface.get_rect(left=self.MARGIN + 15, top=time_rect.bottom + 8)
            screen.blit(title_surface, title_rect)
