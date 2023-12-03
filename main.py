from email.mime import image
from turtle import Turtle,Screen
import time
import random
import turtle
from snake import Snake
from Food import Food
from Scoreboard import Scorboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

image_snake = "new_snake_image.gif" #save the image
screen.addshape(image_snake) # add a new shape for the choice 
turtle.shape(image_snake) # choice the new shape 



snake = Snake()
food = Food()
point = Scorboard()
screen.listen()# can to use keyboard
screen.onkey(snake.moveUp,"Up")
screen.onkey(snake.moveDown,"Down")
screen.onkey(snake.moveLeft,"Left")
screen.onkey(snake.moveRight,"Right")

game_over = False
while (game_over != True):
    screen.update() # refresh the screen
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food) < 15):
        food.refresh()
        point.currentScore()
        point.writeScorePage()
        snake.eaten()
    rand = random.randint(1,20) # to increase the move snake
    if(rand == 1):
        snake.speedUp()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        point.highScore()
        point.writeScorePage()
        snake.reset()
        point.reset()

    if (snake.touchHimself()):
        point.highScore()
        point.writeScorePage()
        snake.reset()
        point.reset()

        








screen.exitonclick()