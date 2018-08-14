import turtle
from random import randint
from tkinter import *

root = Tk()
root.title("Death Race")
canvas = Canvas(root, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.speed(0)
t.penup()
t.goto(-140, 140)

for step in range(15):
  t.write(step, align='center')
  t.right(90)
  for num in range(8):
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(10)

  t.penup()
  t.backward(160)
  t.left(90)
  t.forward(20)

red = turtle.RawTurtle(canvas)
red.color('red')
red.shape('turtle')

red.penup()
red.goto(-160, 100)
red.pendown()

for turn in range(10):
  red.right(36)

blue = turtle.RawTurtle(canvas)
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-160, 70)
blue.pendown()

for turn in range(72):
  blue.left(5)

green = turtle.RawTurtle(canvas)
green.shape('turtle')
green.color('yellow')

green.penup()
green.goto(-160, 40)
green.pendown()

for turn in range(60):
  green.right(6)

yellow = turtle.RawTurtle(canvas)
yellow.shape('turtle')
yellow.color('turquoise')

yellow.penup()
yellow.goto(-160, 10)
yellow.pendown()

for turn in range(30):
  yellow.left(12)

def go():
  red.goto(-160, 100)
  blue.goto(-160,70)
  green.goto(-160,40)
  yellow.goto(-160,10)
  for moves in range(100):
    red.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    green.forward(randint(1, 5))
    yellow.forward(randint(1, 5))
  return

btn = Button(root, text="Go", command=go).pack()
btn = Button(root, text="Exit", command=root.destroy).pack()

mainloop()
