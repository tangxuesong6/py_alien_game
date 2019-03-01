import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


# start game
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    sb = ScoreBoard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, alien)
    while True:
        """key event"""
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, alien, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, alien, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, sb, alien, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, alien, bullets, play_button)


run_game()
