import turtle
# 10 squares
turtle.shape('turtle')

# Define the initial side length
side_length = 200

# Define the number of square
num_squares = 10

# loop to draw 10 squares inside each other
for _ in range(num_squares):
    # Lift the oen before moving to the next square
    turtle.penup()
    # Move to the starting position of the next square
    turtle.goto(-side_length/2, side_length/2)
    # Set the pen down to start drawing the square
    turtle.pendown()
    # Loop to draw a single square
    for _ in range (4):
        turtle.forward(side_length)
        turtle.right(90)

    # Decrease the side length for the next square
    side_length -= 20

    # Adjust the position for the next square
    turtle.penup()
    turtle.goto(-side_length/2, side_length/2)
    turtle.pendown()



