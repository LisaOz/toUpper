import turtle

turtle.shape('turtle')

# define the number of sides of the polygon
num_sides = 360
# define the length of each side
angle = 5
length = 5
increment = 0.01 # Increase the length in each circle

# Loop to draw the circle
for _ in range (100):
    # move the turtle forward by the side length
    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(angle)

        # Increment the length fot the next spiral
        length += increment
  
turtle.mainloop()