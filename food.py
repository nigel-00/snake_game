#import the turtle module 
from turtle import Turtle 
#import the random module 
import random

#create the food class. It inherits all attributes and methods from the Turtle class 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y  = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()
        
    #refresh method that creates a random food location 
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y  = random.randint(-280, 280)
        self.goto(random_x, random_y)





