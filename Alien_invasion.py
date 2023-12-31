import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assests and behaviors"""

    def __init__(self):
        """Intialize the game, and create game resourses"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)) 
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
           
    def _check_events(self):
        """Respond to keypresses and mouse event"""
         # Watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
            

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """update the possition of bullets and get rid of old bullets"""
        #Update bullet position
        self.bullets.update()

        """Get rid of bullets that have dissapered"""
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0 :
                    self.bullets.remove(bullet)
        print(len(self.bullets))

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and find the number of alien in a 
        #spacing between each alien is to one alien width
        alien = Alien(self)
        alien_width = alien.rect.width
        avaible_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = avaible_space_x // (2 * alien_width)

        #create the first row of alien
        for alien_number in range(number_alien_x):
            #create an alien and place it in the row
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)
    
    def _fire_bullet(self):
        """Create a new bullet and add it ti the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Make the most recently deawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #Make a gemw instance, and run the game
    ai = AlienInvasion()
    ai.run_game()