import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.sound('assets/sounds/click.ogg'),
            'game_over': pygame.mixer.sound('assets/sounds/game_over.ogg'),
            'meteorite': pygame.mixer.sound('assets/sounds/meteorite.ogg'),
            'tir': pygame.mixer.sound('assets/sounds/tir.ogg'),
        }

    def play(self, name):
        self.sounds[name].play()
