import pygame

pygame.init()

surface = pygame.Surface((50, 40))
surface.fill((230, 230, 230))

# Alien body.
pygame.draw.ellipse(surface, (0, 180, 0), (8, 5, 34, 28))

# Eyes.
pygame.draw.circle(surface, (255, 255, 255), (18, 15), 5)
pygame.draw.circle(surface, (255, 255, 255), (32, 15), 5)

# Pupils.
pygame.draw.circle(surface, (0, 0, 0), (18, 15), 2)
pygame.draw.circle(surface, (0, 0, 0), (32, 15), 2)

# Save the image.
pygame.image.save(surface, "images/alien.bmp")

pygame.quit()

print("Alien image created successfully!")
