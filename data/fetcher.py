#imports
import io
import pygame
import threading
import requests
import time


class Fetcher:

    
    def __init__(self):                                                                 #fetcher part of the file
       
#empty categories

        self.lock = threading.Lock()

        self.old_song_url = None
        self.old_song_surface = None

        self.base_url = "http://Nicolass-MacBook-air.local:5001"

        self.data = {
                "weather": {},
                "spotify": {},
                "calendar": {},
                "tasks": {},
                "performance": {}
                }

        self.intervals = {
                "weather": 1800,
                "spotify": 1,
                "calendar": 300,
                "tasks": 300,
                "performance": 1
                }

        self.last_fetch = {
                "weather": 0,
                "spotify": 0,
                "calendar": 0,
                "tasks": 0,
                "performance": 0
                }


    def update(self):                                                                   #update part of the file

#check if i need to get the data and then getting it

        for category in self.intervals:
            elapsed = time.time() - self.last_fetch[category]

            if elapsed <= self.intervals[category]:
                pass

            else:
                self.last_fetch[category] = time.time()

                if category == "weather":
                    threading.Thread(target = self.fetch_weather).start()

                elif category == "spotify":
                    threading.Thread(target = self.fetch_spotify).start()

                elif category == "calendar":
                    threading.Thread(target = self.fetch_calendar).start()

                elif category == "tasks":
                    threading.Thread(target = self.fetch_tasks).start()

                elif category == "performance":
                    threading.Thread(target = self.fetch_performance).start()




                


    def get_data(self):                                                                 #get_data part of the file
        with self.lock:
            return dict(self.data)


    def fetch_weather(self):
        
        try:
            url = self.base_url + "/weather"

            response = requests.get(url)

            data = response.json()

            with self.lock: 
                self.data["weather"] = data

        except Exception as e:
            print(f"Weather fetch failed: {e}")
            self.last_fetch["weather"] = time.time() - self.intervals["weather"] + 30


    def fetch_spotify(self):
        
        try:

            url = self.base_url + "/spotify"

            response = requests.get(url)

            data = response.json()

            art = data.get("art", None)

            if art != self.old_song_url and art is not None:
                image_bytes = requests.get(art).content
                image_file = io.BytesIO(image_bytes)
                surface = pygame.image.load(image_file)

                self.old_song_url = art
                self.old_song_surface = surface

            elif art is None:
                surface = None
                self.old_song_url = None
                self.old_song_surface = None

            else:
                surface = self.old_song_surface

            with self.lock: 
                self.data["spotify"] = data
                self.data["spotify"]["art_surface"] = surface

        except Exception as e:
            print(f"Spotify fetch failed: {e}")
            self.last_fetch["spotify"] = time.time() - self.intervals["spotify"] + 30


    def fetch_calendar(self):

        try:
            url = self.base_url + "/calendar"

            response = requests.get(url)

            data = response.json()

            with self.lock: 
                self.data["calendar"] = data

        except Exception as e:
            print(f"Calendar fetch has failed: {e}")
            self.last_fetch["calendar"] = time.time() - self.intervals["calendar"] + 30



    def fetch_tasks(self):

        try:
            url = self.base_url + "/tasks"

            response = requests.get(url)

            data = response.json()

            with self.lock: 
                self.data["tasks"] = data

        except Exception as e:
            print(f"Task fetch has failed: {e}")
            self.last_fetch["tasks"] = time.time() - self.intervals["tasks"] + 30



    def fetch_performance(self):

        try:
            url = self.base_url + "/performance"

            response = requests.get(url)

            data = response.json()

            with self.lock: 
                self.data["performance"] = data

        except Exception as e:
            print(f"Performance fetch has failed: {e}")
            self.last_fetch["performance"] = time.time() - self.intervals["performance"] + 30
           
