import sys 
from pygame.sprite import Group 
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings, screen,stats,play_button,ship,bullets)
        if stats.game_active:
            ship.update_location()
        # bullets.update()
        # 把已消失在屏幕的子弹删除，生的占用内存，使游戏变慢
            gf.update_bullets(ai_settings, screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)
run_game()
