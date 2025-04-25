# Import module for class inheritance of the turtle super class.
from turtle import Turtle

# Define constants for class
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

# Create ScoreBoard class from turtle super class.


class ScoreBoard(Turtle):
    """Keeps track of score and displays game information to user."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("yellow")
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Updates scoreboard upon collision with food objects."""
        self.write(f"Current Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays end game message to user based on collision with tail or wall."""
        self.goto(0, 0)
        self.write("GAME OVER MAN!!!", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases score upon collision with food objects."""
        self.clear()
        self.score += 1
        self.update_scoreboard()
