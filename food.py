# Import modules for food class using turtle super class.
from turtle import Turtle
import random

# Create food class to inherit turtle super class.


class Food(Turtle):
    """Creates food objects that populate in random areas on the screen."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Populates food in random locations on the screen."""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)