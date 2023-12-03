from turtle import Turtle,Screen
import random

SCREEN = [(200,500), (400,100), (90,550)]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5,0.5)
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

    def x_Food(self):
        return self.xcor()
    
    def y_Food(self):
        return self.ycor()
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
