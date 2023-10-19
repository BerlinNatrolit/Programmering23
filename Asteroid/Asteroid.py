import pygame

# Asteroid class
class Asteroid:
    def __init__(self, canvas, sprite, start_pos, velocity):
        self.pos = start_pos
        self.velocity = velocity
        self.canvas = canvas
        self.sprite = sprite

    # Update asteroid
    def update(self, dt):
        self.pos += self.velocity*dt

        # Lets make the asteroid bounce on the edges of the screen
        if self.pos.y < 0:
            self.velocity.y = - self.velocity.y
        elif self.pos.y+self.sprite.get_height() > self.canvas.get_height():
            self.velocity.y = - self.velocity.y

        if self.pos.x < 0:
            self.velocity.x = - self.velocity.x
        elif self.pos.x+self.sprite.get_width() > self.canvas.get_width():
            self.velocity.x = - self.velocity.x

    # Draw asteroid on canvas
    def draw(self):
        self.canvas.blit(self.sprite, self.pos)

    # Return the asteroid sprite
    def get_sprite(self):
        return self.sprite

    # Check if two sprites overlap somewhere.
    def overlaps(self, other):
        rect1 = pygame.Rect(self.pos.x, self.pos.y, self.sprite.get_width(), self.sprite.get_height())
        rect2 = pygame.Rect(other.get_pos().x, other.get_pos().y, other.get_sprite().get_width(), other.get_sprite().get_height())

        return rect1.colliderect(rect2)