import turtle
# 12 legs
turtle.shape('turtle')

# Define the initial side length
legs_length = 90

# Define the number of legs
num_legs = 12

for i in range(num_legs):
    turtle.forward(legs_length)
    turtle.stamp()
    turtle.backward(legs_length)
    turtle.right(360/12)