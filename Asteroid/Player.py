import pygame

# Player class
class Player:
    def __init__(self, canvas, sprite, player_speed):
        self.pos = pygame.Vector2(canvas.get_width()/2 - sprite.get_width()/2, canvas.get_height()/2 - sprite.get_height()/2)
        self.velocity = pygame.Vector2(0,0)
        self.canvas = canvas
        self.sprite = sprite
        self.speed = player_speed

    # Update player
    def update(self, dt, keys):
        if keys[pygame.K_w]:
            self.pos.y -= self.speed.y * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed.y * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed.x * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed.x * dt

    # Draw player on canvas
    def draw(self):
        self.canvas.blit(self.sprite, self.pos)

    # Return the player sprite.
    def get_sprite(self):
        return self.sprite

    # Returns position of player
    def get_pos(self):
        return self.pos