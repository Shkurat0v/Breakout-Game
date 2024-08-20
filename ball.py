import random
from turtle import Turtle

choices = (-1, 1)

class Ball(Turtle):
  def __init__(self):
       super().__init__()
       self.color("white")
       self.shape("circle")
       self.penup()
       self.x_move = 10
       self.y_move = 10
       self.move_speed = 0.1

  def move(self):
     new_x = self.xcor() + self.x_move
     new_y = self.ycor() + self.y_move
     self.goto(new_x, new_y)

  def bounce_y(self):
     self.y_move *= -1

  def bounce_x(self):
     self.x_move *= random.choice(choices)
  def reset_ball(self):
      self.y_move *= -1
      self.move_speed = 0.1