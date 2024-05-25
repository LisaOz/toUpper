import turtle

turtle.shape('turtle')

# Define the parameters
length = 5
angle = 90
increment = 5 # Increase the length in each circle

# Loop to draw the spiral
for _ in range(100):
    turtle.forward(length)
    turtle.right(angle)
    length += increment
