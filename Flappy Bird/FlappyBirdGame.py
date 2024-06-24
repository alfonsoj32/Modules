import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Bird"
BIRD_RADIUS = 20
GRAVITY = 0.5
FLAP_STRENGTH = 10
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200
PIPE_SPACING = 300
PIPE_SPEED = 2
FLAP_RATE = 0.1  # Time between flaps in seconds
GROUND_HEIGHT = 50  # Height of the ground

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.textures = [
            arcade.load_texture("Flappy Bird/images/bird1.png"),
            arcade.load_texture("Flappy Bird/images/bird2.png"),
            arcade.load_texture("Flappy Bird/images/bird3.png")
        ]
        self.current_texture_index = 0
        self.time_since_last_flap = 0

    def update(self, delta_time):
        self.velocity -= GRAVITY
        self.y += self.velocity

        # Update the animation frame based on the time since the last frame change
        self.time_since_last_flap += delta_time
        if self.time_since_last_flap >= FLAP_RATE:
            self.current_texture_index = (self.current_texture_index + 1) % len(self.textures)
            self.time_since_last_flap = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self):
        texture = self.textures[self.current_texture_index]
        arcade.draw_texture_rectangle(self.x, self.y, texture.width, texture.height, texture)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)
        self.texture = arcade.load_texture("Flappy Bird/images/pipe.png")

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # Draw top pipe (upside down)
        top_pipe_y = self.gap_y + PIPE_GAP / 2 + self.texture.height / 2
        arcade.draw_texture_rectangle(
            self.x, top_pipe_y,
            PIPE_WIDTH, self.texture.height,
            self.texture,
            180  # Rotate the texture 180 degrees for the top pipe
        )
        # Draw bottom pipe
        bottom_pipe_y = self.gap_y - PIPE_GAP / 2 - self.texture.height / 2
        arcade.draw_texture_rectangle(
            self.x, bottom_pipe_y,
            PIPE_WIDTH, self.texture.height,
            self.texture
        )

class FlappyBirdGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.background = arcade.load_texture("Flappy Bird/images/bg.png")  # Load the background image
        self.ground = arcade.load_texture("Flappy Bird/images/ground.png")  # Load the ground image

        # Preload sounds
        self.flap_sound = arcade.load_sound("Flappy Bird/sounds/flap.wav")
        self.game_over_sound = arcade.load_sound("Flappy Bird/sounds/gameover.wav")
        self.score_sound = arcade.load_sound("Flappy Bird/sounds/point.wav")
        self.background_music = arcade.load_sound("Flappy Bird/sounds/bg.mp3")
        
        # Play background music
        self.music_player = None
        self.play_background_music()

        # Preload first pipe
        self.spawn_pipe()

    def play_background_music(self):
        if self.music_player is not None:
            self.music_player.stop()
        self.music_player = arcade.play_sound(self.background_music, looping=True)

    def spawn_pipe(self):
        if len(self.pipes) == 0 or self.pipes[-1].x < SCREEN_WIDTH - PIPE_SPACING:
            self.pipes.append(Pipe(SCREEN_WIDTH))

    def on_draw(self):
        arcade.start_render()
        # Draw the background image
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Draw the ground image
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, GROUND_HEIGHT, self.ground)

        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.RED, 40, anchor_x="center")
            arcade.draw_text("Press R to Restart", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                             arcade.color.RED, 20, anchor_x="center")

    def on_update(self, delta_time):
        if not self.game_over:
            self.bird.update(delta_time)
            self.spawn_pipe()

            for pipe in self.pipes:
                pipe.update()
                if pipe.x < -PIPE_WIDTH:
                    self.pipes.remove(pipe)
                    self.score += 1
                    arcade.play_sound(self.score_sound)  # Play score sound effect

            if self.bird.y < GROUND_HEIGHT or self.bird.y > SCREEN_HEIGHT:
                self.game_over = True
                arcade.play_sound(self.game_over_sound)

            for pipe in self.pipes:
                if abs(self.bird.x - pipe.x) < PIPE_WIDTH / 2 + self.bird.textures[self.bird.current_texture_index].width / 2:
                    if not (pipe.gap_y - PIPE_GAP / 2 < self.bird.y < pipe.gap_y + PIPE_GAP / 2):
                        self.game_over = True
                        arcade.play_sound(self.game_over_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and not self.game_over:
            self.bird.flap()
            arcade.play_sound(self.flap_sound)
        elif key == arcade.key.R and self.game_over:
            self.restart_game()

    def restart_game(self):
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.spawn_pipe()

def main():
    game = FlappyBirdGame()
    arcade.run()

if __name__ == "__main__":
    main()
