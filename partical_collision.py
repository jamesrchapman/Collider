import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Particle:
    def __init__(self, x, y, dx, dy, radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

def collide(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance < p1.radius + p2.radius:
        angle = math.atan2(dy, dx)
        p1.dx, p1.dy = math.cos(angle), math.sin(angle)
        p2.dx, p2.dy = -math.cos(angle), -math.sin(angle)

# Initialize Pygame
pygame.init()

# Set the size of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Particle Collision Simulation")

# Create a list of particles
particles = []
for i in range(50):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    dx = random.uniform(-1, 1)
    dy = random.uniform(-1, 1)
    radius = random.randint(5, 20)
    particles.append(Particle(x, y, dx, dy, radius))

# Set the clock
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw particles
    for particle in particles:
        particle.update()
        particle.draw(screen)

    # Check for collisions
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            collide(particles[i], particles[j])

    # Update the screen
    pygame.display.flip()

    # Limit the frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()