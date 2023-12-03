from turtle import Turtle,Screen

class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        with open("data.txt",mode="r") as data: #read from the data file for the save the resulte of the high level
            self.high_point = int(data.read())

        self.high_point = 0
        self.color("black")
        self.penup()
        self.goto(-20,270)
        self.writeScorePage()
        self.hideturtle()

    def currentScore(self):
        self.point = self.point + 1
        return self.point
    
    def writeScorePage(self):
        self.clear()
        self.highScore()
        self.write(f"SCORE: {self.point}   HIGH SCORE: {self.high_point}",align="center",font=("Arial",16,"normal"))

    def writeResulte(self):
        self.clear()
        self.goto(-20,10)
        self.write(f"Game Over! YOUR SCORE:  {self.point}",align="center",font=("Arial",18,"normal"))

    def highScore(self):
        if self.point > self.high_point:
            self.high_point = self.point
            with open("data.txt",mode= "w") as data:
                data.write(f"{self.high_point}")
        
    def reset(self):
        self.point = 0
        self.writeScorePage()
