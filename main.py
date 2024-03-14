import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
# tim.shape("turtle")
# tim.fillcolor("teal")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# for _ in range(15):
# 	tim.forward(10)
# 	tim.penup()
# 	tim.forward(10)
# 	tim.pendown()

# import turtle

#
#
# # Function to draw a polygon with a given number of sides and length
# def draw_polygon(sides, length):
# 	for _ in range(sides):
# 		turtle.forward(length)
# 		turtle.left(360 / sides)
#
#
# # Function to draw a shape with a random color
# def draw_shape_with_random_color(sides, length):
# 	# Set a random color using RGB values
# 	turtle.pencolor(random.random(), random.random(), random.random())
#
# 	# Draw the polygon with the specified number of sides and length
# 	draw_polygon(sides, length)
#
#
# # Set up the turtle window
# turtle.speed(2)  # Set the drawing speed (adjust as needed)
# turtle.bgcolor("white")  # Set the background color
#
# # Draw shapes with sides from 3 to 10
# for sides in range(3, 11):
# 	draw_shape_with_random_color(sides, 100)
#
# # Close the turtle graphics window when clicked
# turtle.done()
#
# screen = Screen()
# screen.exitonclick()


# is a list containing eight color names.
# colours = ["Cornflowerblue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "slateGray", "SeaGreen", "wheat"]
#
# #draw_shape is a function that takes the number of sides (num_sides) as an argument and uses a loop to draw a shape with that number of sides. It calculates the angle needed for each turn based on the number of sides and then moves the turtle (tim) forward and turns right in a loop.
# def draw_shape(num_sides):
# 	angle = 360 / num_sides
# 	for _ in range(num_sides):
# 		tim.forward(100)
# 		tim.right(angle)
#
#
# # iterates over the range from 3 to 10, inclusive (the number of sides for your shapes).
# for shape_side_n in range(3, 11):
# 	#sets the turtle's color to a randomly chosen color from the colours list.
# 	tim.color(random.choice(colours))
# 	#calls the draw_shape function with the current number of sides.
# 	draw_shape(shape_side_n)

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	random_color = (r, g, b)
	return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)


for _ in range(200):
	# tim.color(random.choice(colours))
	tim.color(random_color())
	tim.forward(30)
	tim.setheading(random.choice(directions))
	tim.speed(4)  # Set the drawing speed (adjust as needed)



# Close the turtle graphics window when clicked
turtle.done()