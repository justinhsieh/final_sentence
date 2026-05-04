"""Audio API built on top of pygame.mixer."""

import pygame

from .paths import audio_path


class AudioManager:
    """Small wrapper around pygame music and sound effects."""

    def __init__(self):
        # Load background music and sound effects.
        pygame.mixer.init()
        self.enabled = True
        self.music_vol = 1.0
        self.sfx_vol = 1.0
        pygame.mixer.music.load(audio_path("bgm.mp3"))
        self.sounds = {
            "type": pygame.mixer.Sound(audio_path("type.wav")),
            "wrong": pygame.mixer.Sound(audio_path("wrong.wav")),
            "spin": pygame.mixer.Sound(audio_path("spin.wav")),
            "click": pygame.mixer.Sound(audio_path("click.wav")),
            "shoot": pygame.mixer.Sound(audio_path("shoot.wav")),
            "tick": pygame.mixer.Sound(audio_path("tick.wav")),
            "type_stats": pygame.mixer.Sound(audio_path("type.wav")),
        }
        self.apply_volumes()

    def apply_volumes(self):
        # Sync pygame channels with current volume values.
        if not self.enabled:
            return
        pygame.mixer.music.set_volume(self.music_vol)
        self.sounds["type"].set_volume(0.3 * self.sfx_vol)
        self.sounds["wrong"].set_volume(1.0 * self.sfx_vol)
        self.sounds["spin"].set_volume(1.0 * self.sfx_vol)
        self.sounds["click"].set_volume(1.0 * self.sfx_vol)
        self.sounds["shoot"].set_volume(1.0 * self.sfx_vol)
        self.sounds["tick"].set_volume(0.15 * self.sfx_vol)
        self.sounds["type_stats"].set_volume(0.1 * self.sfx_vol)

    def set_music_volume(self, percent):
        # Set background music volume from a 0-100 UI value.
        self.music_vol = float(percent) / 100.0
        self.apply_volumes()

    def set_sfx_volume(self, percent):
        # Set sound effect volume from a 0-100 UI value.
        self.sfx_vol = float(percent) / 100.0
        self.apply_volumes()

    def play(self, name):
        # Play a named sound effect if audio is enabled.
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def play_music_loop(self):
        # Start looping the background music.
        if self.enabled:
            pygame.mixer.music.play(-1)

    def stop_music(self):
        # Stop the background music.
        if self.enabled:
            pygame.mixer.music.stop()

    def fadeout_music(self, milliseconds):
        # Fade out the background music over a duration.
        if self.enabled:
            pygame.mixer.music.fadeout(milliseconds)

