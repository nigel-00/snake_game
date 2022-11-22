#import the turtle module 
from turtle import Turtle
#set alignement to center 
ALIGNMENT = "center"
#set font size 
FONT = ("Courier", 20, "normal")
#scoreboard class that keeps track of the score and updates it everytime the snake eats food
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
    #updates the score board
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    #displays the game over screen
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)
    #increases the score and clears the previous score everytime the snake eats the food 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       
