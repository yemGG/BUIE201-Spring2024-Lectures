import pygame
import random
import sys


class Game:
    def __init__(self):
        pygame.init()

        # Set the window dimensions
        self.width = 400
        self._height = 400
        self.window = pygame.display.set_mode((self.width, self._height))

        self._WHITE = (255, 255, 255)       
        self._shapes = []

        pygame.display.set_caption("Shapes Drop")

    def IsyVisible(self, y):
        return y < self._height

    def runGameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill(self._WHITE)  # Clear the window

            # Generate new shape
            if random.random() < 0.1:  # Adjust this probability as needed
                if random.random() < 0.5:
                    new_shape = Circle(self)
                else:
                    new_shape = Rectangle(self)

                self._shapes.append(new_shape)

            # Update and draw shapes
            for shape in self._shapes:
                shape.move()
                shape.draw()

            # Remove shapes that have fallen off the screen
            self._shapes = [shape for shape in self._shapes if shape.isVisible()]

            pygame.display.flip()
            pygame.time.Clock().tick(60)  # Limit frame rate to 60 FPS


# Shape class
class Shape:
    def __init__(self, game):
        self._game = game
        self._x = random.randint(0, game.width)  # Random x-coordinate
        self._y = 0  # Start from the top
        self._size = random.randint(10, 30)  # Random size
        self._color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        
    def draw(self):
        pass

    def move(self):
        self._y += 1  # Move downwards

    def isVisible(self):
        return game.IsyVisible(self._y)

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(self._game.window, self._color, (self._x, self._y), self._size)  
    
class Rectangle(Shape):
    def draw(self):
        pygame.draw.rect(self._game.window, self._color, (self._x, self._y, self._size, self._size))  


game = Game()
game.runGameLoop()

