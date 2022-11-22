#Import the screen and Turtle from the turtle module 
from turtle import  Screen
#import the time module
import time 

#import the snake class 
from snake import Snake
#import the food class 
from food import Food
#import the scoreboard class
from score_board import ScoreBoard

#Initialize the screen 
screen = Screen()
#Setup the screen length and width 
screen.setup(width=600, height=600)
#Change screen color 
screen.bgcolor("black")
#Set up the screen title 
screen.title("Snake Game")
#turn off the tracer 
screen.tracer(0)

#create a new snake method 
snake = Snake()
#create the food class 
food = Food()
#create a scoreboard 
score = ScoreBoard()
#use the arrow keys to move the snake 
#listen method
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

#boolean variable that starts the game
game_is_on = True

while game_is_on:
    #update the screen once all the segments have moved forward
    screen.update()
    #have a delay time.Keep track of the speed
    time.sleep(0.1)
    #move the snake by calling the move_snake method from Snake class
    snake.move_snake()
    #detect snake collision with food 
    if snake.head.distance(food) < 14.5:
        food.refresh()
        snake.extend()
        score.increase_score()
    #detect collision with wall 
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_is_on = False
        score.game_over()
    #detect collision with tail 
    #if the head colides with any collisions in the tail trigger game over 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


#Exit the screen  
screen.exitonclick()