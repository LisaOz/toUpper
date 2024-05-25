# This is a sample Python script.
import turtle

# Set the turtle shape to 'turtle'
turtle.shape('turtle')

# define the number of sides of the polygon
num_sides = 36

# define the length of each side
side_length = 20

# Loop to draw the circle
for _ in range (num_sides):
    # move the turtle forward by the side length
    turtle.forward(side_length)

    # turn the turtle by the angle that forms a circle
    turtle.right(360 / num_sides)

