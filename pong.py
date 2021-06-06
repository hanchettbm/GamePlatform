# Pong Game Using Arcade
# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 625
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Pong!"
SPRITE_SCALING = 0.5
SPEED = 6


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None


def create_ball():
    ball = Ball()
    # Size of the ball
    ball.size = 12
    
    # Starting position of the ball within the Game
    ball.x = SCREEN_WIDTH / 2
    ball.y = SCREEN_HEIGHT / 2 
 
    # Set initial speed and direction of ball.
    ball.change_x = random.randrange(-2, 3)
    # Make sure it doesn't just go straight horizontal
    if ball.change_x == 0:
        ball.change_x = 1
    ball.change_y = random.randrange(-2, 3)
    # Make sure it doesn't just go straight vertical
    if ball.change_y == 0:
        ball.change_y = 1
 
    # Set ball color
    ball.color = arcade.color.RED
 
    return ball


class Paddles(arcade.Sprite): 
    
    def update(self):
         # Move player
         self.center_x += self.change_x
         self.center_y += self.change_y
 
         # Check for out-of-bounds and stop
         if self.left < 0:
             self.left = 0
         elif self.right > SCREEN_WIDTH - 1:
             self.right = SCREEN_WIDTH - 1
 
         if self.bottom < 0:
             self.bottom = 0
         elif self.top > SCREEN_HEIGHT - 1:
             self.top = SCREEN_HEIGHT - 1
             

class PongGame(arcade.Window):

     def __init__(self, width, height, title):

         # Call the parent class initializer
         super().__init__(width, height, title)
         self.left_text = 0
         self.right_text = 0
         
         self.ball_list = []
         ball = create_ball()
         self.ball_list.append(ball)
 
        # initialize the sprite list
         self.paddle_list = None
 
         # initialize the paddles
         self.left_paddle_sprite = None
         self.right_paddle_sprite = None
 
         # Set the background color
         arcade.set_background_color(arcade.color.NAVY_BLUE)
         
     def setup(self):
        # Initialize Pong sound effect  
        self.collision_sound = arcade.load_sound("Pong_Sound.mp3") 
 
        # Create sprite Paddle list
        self.paddle_list = arcade.SpriteList()
 
         # Set up the left Paddle
        self.left_paddle_sprite = Paddles("Screen Shot 2021-06-04 at 9.52.59 PM.png", SPRITE_SCALING) 
        self.left_paddle_sprite.center_x = 50
        self.left_paddle_sprite.center_y = 300
        self.paddle_list.append(self.left_paddle_sprite)
        
        # Set up the right Paddle
        self.right_paddle_sprite = Paddles("Screen Shot 2021-06-04 at 9.52.59 PM.png", SPRITE_SCALING) 
        self.right_paddle_sprite.center_x = 575
        self.right_paddle_sprite.center_y = 300
        self.paddle_list.append(self.right_paddle_sprite)
        
        
     def on_draw(self):

        # Start to draw
        arcade.start_render()
        
        # Draw the ball
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color) 
            
        # Draw all the sprite Paddles
        self.paddle_list.draw()
        
        # Set up text and quit info 
        arcade.draw_text("Player 1 (S/W)", 10, 575, arcade.color.WHITE, 15)
        arcade.draw_text("Player 2 (UP/DWN)", 450, 575, arcade.color.WHITE, 15)
        arcade.draw_text("Press Space bar to quit", 225, 20, arcade.color.WHITE, 14)
        # Score count
        arcade.draw_text(str(self.left_text), 10, 525, arcade.color.WHITE, 30)
        arcade.draw_text(str(self.right_text), 590, 525, arcade.color.WHITE, 30)


     def on_update(self, delta_time):
        
        # Updates ball movment
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Check for right player score (ball leaves left screen)
            if ball.x < ball.size:
                
                # Add a point 
                self.right_text += 1
                
                # Reset ball position
                ball.x = SCREEN_WIDTH / 2
                ball.y = SCREEN_HEIGHT / 2 
                ball.change_x = random.randrange(-2, 3)
                if ball.change_x == 0:
                    ball.change_x = 1
                ball.change_y = random.randrange(-2, 3)
                if ball.change_y == 0:
                    ball.change_y = 1
 
            # Reverse ball if hits top 
            if ball.y < ball.size:
                ball.change_y *= -1
 
            # Check for left player score (ball leaves right screen)
            if ball.x > SCREEN_WIDTH:
                
                # Add a point
                self.left_text += 1
                
                # Reset ball position
                ball.x = SCREEN_WIDTH / 2
                ball.y = SCREEN_HEIGHT / 2 
                ball.change_x = random.randrange(-2, 3)
                if ball.change_x == 0:
                    ball.change_x = 1
                ball.change_y = random.randrange(-2, 3)
                if ball.change_y == 0:
                    ball.change_y = 1    
 
            # Reverse ball if hits bottom
            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1

            # Check for left paddle collision and then reverse ball
            if self.left_paddle_sprite.collides_with_point([ball.x, ball.y]):
                # Play sound on collision
                arcade.play_sound(self.collision_sound)
                ball.change_x *= -1.5
            
            # Check for right paddle collision and then reverse ball
            if self.right_paddle_sprite.collides_with_point([ball.x, ball.y]):
                # Play sound on collision
                arcade.play_sound(self.collision_sound)
                ball.change_x *= -1.5   
      
        # Move the player
        self.paddle_list.update()
     
     
     def on_key_press(self, key, modifiers):
         
        # If the player presses a key, move the paddle accordingly
        if key == arcade.key.UP:
            self.right_paddle_sprite.change_y = SPEED
        elif key == arcade.key.DOWN:
            self.right_paddle_sprite.change_y = -SPEED
            
        if key == arcade.key.W:
            self.left_paddle_sprite.change_y = SPEED
        elif key == arcade.key.S:
            self.left_paddle_sprite.change_y = -SPEED
        
        # Close with spacebar
        if key == arcade.key.SPACE:
            arcade.close_window()
            

     def on_key_release(self, key, modifiers):

         # Stops Paddle movement when not pressing keys.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.right_paddle_sprite.change_y = 0
        
        if key == arcade.key.W or key == arcade.key.S:
            self.left_paddle_sprite.change_y = 0
            

# Runs the game
def main():
    window = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
 
if __name__ == "__main__":
    main()