from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard object."""
        super().__init__()
        self.score = 0
        with open("snake_game_score_data.txt") as score_file:   
            self.high_score = int(score_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game_score_data.txt",mode="w") as score_file:   
                score_file.write(f"{self.high_score}")
        self.score = 0
        # self.update_scoreboard()
    
    def game_over(self):
        """Display the game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score and update the scoreboard."""
        self.score += 1
        #self.clear()
        self.update_scoreboard()
