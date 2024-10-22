"""
Cookie Clicker Game

Author: Mike Kohlegger
Date: October 2024
"""

# https://www.youtube.com/watch?v=yD_cn7vJJAA

import pygame, sys


WIDTH = 800
HEIGHT = 600
RADIUS = 150
BASE_COLOR = "#ffffff"
TITLE = "Cookie Clicker by Mike"


class CookieClicker:
    def __init__(self):
        self.cookie_count = 0
        self.cpc = 1
        self.cps = 0

        self.cpc_upgrade_cost = 5
        self.cpc_upgrade_button = pygame.Rect(
            50,
            HEIGHT-100,
            300,
            50,
        )

        self.cps_upgrade_cost = 10
        self.cps_upgrade_button = pygame.Rect(
            400,
            HEIGHT-100,
            300,
            50,
        )

        self.cookie_button = pygame.Rect(
            WIDTH/2-RADIUS,
            HEIGHT/2-RADIUS,
            RADIUS*2,
            RADIUS*2
        )
        self.cookie_color = "#522920"
        self.clicked = False

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()

        if self.cookie_button.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                click_sound.play()
                self.clicked = True
            else:
                if self.clicked:
                    self.cookie_count += self.cpc
                    self.clicked = False

        if self.cpc_upgrade_button.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    if self.cookie_count >= self.cpc_upgrade_cost:
                        cash_sound.play()
                        self.cookie_count -= self.cpc_upgrade_cost
                        self.cpc_upgrade_cost *= 3
                        self.cpc += self.cpc
                self.clicked = False

        if self.cps_upgrade_button.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    if self.cookie_count >= self.cps_upgrade_cost:
                        cash_sound.play()
                        self.cookie_count -= self.cps_upgrade_cost
                        self.cps_upgrade_cost *= 3
                        if self.cps == 0:
                            self.cps = 1
                        else:
                            self.cps += self.cpc
                self.clicked = False

        pygame.draw.rect(
            canvas,
            self.cookie_color,
            self.cookie_button,
            border_radius=150
        )

    def render(self):
        self.click_button()
        self.draw_score()
        if self.cookie_count >= self.cpc_upgrade_cost:
            self.cpc_upgrade()
        if self.cookie_count >= self.cps_upgrade_cost:
            self.cps_upgrade()
        self.draw_rates()

    def draw_score(self):
        self.display_cookies = text_font.render(
            f"Cookies: {str(self.cookie_count)}",
            True,
            BASE_COLOR
        )
        canvas.blit(self.display_cookies, (50, 100))

    def draw_rates(self):
        self.display_cpc = text_font.render(
            f"Current c/c rate: {str(self.cpc)}",
            True,
            BASE_COLOR
        )
        canvas.blit(self.display_cpc, (50, 120))
        self.display_cps = text_font.render(
            f"Current c/s rate: {str(self.cps)}",
            True,
            BASE_COLOR
        )
        canvas.blit(self.display_cps, (50, 140))

    def cpc_upgrade(self):
        self.cpc_upgrade_display = text_font.render(
            f"+{self.cpc} c/c for {str(self.cpc_upgrade_cost)} cookies",
            True,
            BASE_COLOR
        )
        pygame.draw.rect(
            canvas,
            "#000000",
            self.cpc_upgrade_button,
            border_radius=15
        )
        canvas.blit(self.cpc_upgrade_display, (90, HEIGHT-85))

    def cps_upgrade(self):
        if self.cps == 0:
            display_cps = 1
        else:
            display_cps = self.cps

        self.cps_upgrade_display = text_font.render(
            f"+{display_cps} c/s for {str(self.cps_upgrade_cost)} cookies",
            True,
            BASE_COLOR
        )
        pygame.draw.rect(
            canvas,
            "#000000",
            self.cps_upgrade_button,
            border_radius=15
        )
        canvas.blit(self.cps_upgrade_display, (440, HEIGHT-85))

    def get_time_cookies(self):
        self.cookie_count += self.cps

if __name__ == "__main__":

    pygame.init()

    text_font = pygame.font.Font(None, 25)
    title_font = pygame.font.Font(None, 50)

    game = CookieClicker()

    canvas = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    cookie_img = pygame.image.load("static/cookie.gif").convert()
    cookie_img = pygame.transform.scale(cookie_img, (RADIUS*2, RADIUS*2))

    background_img = pygame.image.load("static/bg.jpeg").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    click_sound = pygame.mixer.Sound("static/click.mp3")
    cash_sound = pygame.mixer.Sound("static/cash.mp3")

    pygame.display.set_caption(title=TITLE)
    title = title_font.render(TITLE, True, BASE_COLOR)
    clock = pygame.time.Clock()

    time_counter = 0

    while True:

        time_counter += 1

        canvas.blit(background_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        canvas.blit(title, (50, 50))

        if time_counter == 60:
            game.get_time_cookies()
            time_counter = 0

        game.render()
        canvas.blit(cookie_img, (WIDTH/2-RADIUS, HEIGHT/2-RADIUS))

        pygame.display.update()
        clock.tick(60)
