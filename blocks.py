import random
from turtle import Turtle

colors = ['red', 'blue', 'yellow', 'green', 'orange', 'white']

class Blocks(Turtle):
    def __init__(self, offset_x, offset_y):
         super().__init__()

         self.shape("square")
         self.color(random.choice(colors))
         self.shapesize(1, 3)
         self.penup()
         self.goto(random.randint(-350, 350) + offset_x, random.randint(200, 275))




