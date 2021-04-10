import sys 
from pygame.sprite import Group 
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    while True:
        gf.check_events(ai_settings, screen,ship,bullets)
        ship.update_location()
        bullets.update()
        # 把已消失在屏幕的子弹删除，生的占用内存，使游戏变慢
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
