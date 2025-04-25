# Import module for making snake from turtle class.
from turtle import Turtle

# Create constants for repetitive variables and flexibility.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SHAPE = "square"
SNAKE_COLOR = "green"

# Create Snake class from turtle objects, define attributes and methods.


class Snake:
    """Snake class made from turtle objects."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Iterates through starting positions constant to instantiate the snake objects."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds new segment to snake."""
        new_segment = Turtle(SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Detects collision with food objects to add segment to snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Continuously moves snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Using the onkey method to listen for user input to change direction of snake."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Using the onkey method to listen for user input to change direction of snake."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Using the onkey method to listen for user input to change direction of snake."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Using the onkey method to listen for user input to change direction of snake."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)