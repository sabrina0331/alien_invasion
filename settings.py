class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        # self.bg_color = (105,105,105)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 102,0,102
        self.bullets_allowed = 3
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        # fleet—direction为1 向右移，为-1向左
        self.fleet_direction = 1