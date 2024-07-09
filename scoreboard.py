from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
