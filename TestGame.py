# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()








# Basic arcade shooter

# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0

class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include enemies and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()
            
class SpaceShooter(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        
def setup(self):
    """Get the game ready to play
    """

    # Set the background color
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Set up the player
    self.player = arcade.Sprite("images/jet.png", SCALING)
    self.player.center_y = self.height / 2
    self.player.left = 10
    self.all_sprites.append(self.player)
    
    # Spawn a new enemy every 0.25 seconds
    arcade.schedule(self.add_enemy, 0.25)

    # Spawn a new cloud every second
    arcade.schedule(self.add_cloud, 1.0)
    
def add_enemy(self, delta_time: float):
    """Adds a new enemy to the screen

    Arguments:
        delta_time {float} -- How much time has passed since the last call
    """

    # First, create the new enemy sprite
    enemy = arcade.Sprite("images/missile.png", SCALING)

    # Set its position to a random height and off screen right
    enemy.left = random.randint(self.width, self.width + 80)
    enemy.top = random.randint(10, self.height - 10)
    
    # Set its speed to a random speed heading left
    enemy.velocity = (random.randint(-20, -5), 0)

    # Add it to the enemies list
    self.enemies_list.append(enemy)
    self.all_sprites.append(enemy)

def on_key_press(self, symbol, modifiers):
    """Handle user keyboard input
    Q: Quit the game
    P: Pause/Unpause the game
    I/J/K/L: Move Up, Left, Down, Right
    Arrows: Move Up, Left, Down, Right

    Arguments:
        symbol {int} -- Which key was pressed
        modifiers {int} -- Which modifiers were pressed
    """
    if symbol == arcade.key.Q:
        # Quit immediately
        arcade.close_window()

    if symbol == arcade.key.P:
        self.paused = not self.paused

    if symbol == arcade.key.I or symbol == arcade.key.UP:
        self.player.change_y = 5

    if symbol == arcade.key.K or symbol == arcade.key.DOWN:
        self.player.change_y = -5

    if symbol == arcade.key.J or symbol == arcade.key.LEFT:
        self.player.change_x = -5

    if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
        self.player.change_x = 5

def on_key_release(self, symbol: int, modifiers: int):
    """Undo movement vectors when movement keys are released

    Arguments:
        symbol {int} -- Which key was pressed
        modifiers {int} -- Which modifiers were pressed
    """
    if (
        symbol == arcade.key.I
        or symbol == arcade.key.K
        or symbol == arcade.key.UP
        or symbol == arcade.key.DOWN
    ):
        self.player.change_y = 0

    if (
        symbol == arcade.key.J
        or symbol == arcade.key.L
        or symbol == arcade.key.LEFT
        or symbol == arcade.key.RIGHT
    ):
        self.player.change_x = 0
        

def on_update(self, delta_time: float):
    """Update the positions and statuses of all game objects
    If paused, do nothing

    Arguments:
        delta_time {float} -- Time since the last update
    """

    # If paused, don't update anything
    if self.paused:
        return

    # Update everything
    self.all_sprites.update()

    # Keep the player on screen
    if self.player.top > self.height:
        self.player.top = self.height
    if self.player.right > self.width:
        self.player.right = self.width
    if self.player.bottom < 0:
        self.player.bottom = 0
    if self.player.left < 0:
        self.player.left = 0
        
def on_draw(self):
    """Draw all game objects
    """
    arcade.start_render()
    self.all_sprites.draw()