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

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0

    def update(self):
        self.velocity -= GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, BIRD_RADIUS, arcade.color.YELLOW)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # Draw top pipe
        arcade.draw_rectangle_filled(
            self.x, self.gap_y + PIPE_GAP / 2 + PIPE_HEIGHT / 2,
            PIPE_WIDTH, PIPE_HEIGHT, arcade.color.GREEN
        )
        # Draw bottom pipe
        arcade.draw_rectangle_filled(
            self.x, self.gap_y - PIPE_GAP / 2 - PIPE_HEIGHT / 2,
            PIPE_WIDTH, PIPE_HEIGHT, arcade.color.GREEN
        )

class FlappyBirdGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.pipes = []
        self.score = 0
        self.game_over = False
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.spawn_pipe()

    def spawn_pipe(self):
        self.pipes.append(Pipe(SCREEN_WIDTH))

    def on_draw(self):
        arcade.start_render()
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.RED, 40, anchor_x="center")

    def on_update(self, delta_time):
        if not self.game_over:
            self.bird.update()

            for pipe in self.pipes:
                pipe.update()
                if pipe.x < -PIPE_WIDTH:
                    self.pipes.remove(pipe)
                    self.spawn_pipe()
                    self.score += 1

            if self.bird.y < 0 or self.bird.y > SCREEN_HEIGHT:
                self.game_over = True

            for pipe in self.pipes:
                if abs(self.bird.x - pipe.x) < PIPE_WIDTH / 2 + BIRD_RADIUS:
                    if not (pipe.gap_y - PIPE_GAP / 2 < self.bird.y < pipe.gap_y + PIPE_GAP / 2):
                        self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and not self.game_over:
            self.bird.flap()

def main():
    game = FlappyBirdGame()
    arcade.run()

if __name__ == "__main__":
    main()