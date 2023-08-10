#THIS CODE IS FOR SKETCH USING CANVAS
from sketchpy import canvas

obj = canvas.sketch_from_svg("C:\\Users\\asus\\sketch.svg", scale=250)
obj.draw()

#THIS CODE IS FOR SKETCH USING LIBRARY
from sketchpy import library

obj = library.apj()
obj.draw()

#THIS CODE IS FOR SKETCH USING TURTLE
import turtle

m = turtle.Screen()
m.title("pattern PROJECT BY Prince Yadav ")
turtle.bgcolor('black')
turtle.speed(20)
turtle.pensize(1)
colors = ('blue', 'orange', 'yellow', 'dark', 'green', 'red')
for i in range(200):
  turtle.fd(i * 4)
  turtle.right(90)
  turtle.color(colors[i % 5])
  for j in range(3):
    turtle.fd(j * 4)
    turtle.right(90)
    for k in range(2):
      turtle.fd(k * 4)
      turtle.right(90)
      for l in range(739):
        turtle.fd(l * 4)
        turtle.right(891)
