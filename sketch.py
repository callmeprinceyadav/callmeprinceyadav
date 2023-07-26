# import turtle
# window = turtle.Screen()
# window.bgcolor("white")

# turtle_1 = turtle.ht()
# turtle_1.shape("turtle")
# turtle_1.color("red")

# window.exitonclick()


import turtle

# turtle object
img_turtle = turtle.Turtle()

# registering the image
# as a new shape
turtle.register_shape('example.gif')

# setting the image as cursor
img_turtle.shape('example.gif')
