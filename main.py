import turtle as t
import random
from memorial.image_data_extractor import ColorExtractor

# Extract colors and their proportions
color_extractor = ColorExtractor("boni.png", 20)
color_proportions = color_extractor.get_color_proportions()

# Separate colors and their weights
colors, weights = zip(*color_proportions)

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

# Set the starting position
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 100 
dot_size = 20 
spacing = 50  

for dot_count in range(1, number_of_dots + 1):
    # Select a color based on its weight
    color = random.choices(colors, weights)[0]
    turtle.dot(dot_size, color)
    turtle.forward(spacing)

    if dot_count % 10 == 0: 
        turtle.setheading(90)
        turtle.forward(spacing)
        turtle.setheading(180)
        turtle.forward(spacing * 10)
        turtle.setheading(0)

screen.exitonclick()