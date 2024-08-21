import random
from turtle import Turtle, Screen
tom_the_turtle = Turtle()
tom_the_turtle.shape("turtle")
tom_the_turtle.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shapes(num_side):
    angle = 360/ num_side
    for _ in range(num_side):
        tom_the_turtle.forward(100)
        tom_the_turtle.right(angle)
for shape_side_n in range(3,11):
    tom_the_turtle.color(random.choice(colours))
    draw_shapes(shape_side_n)



# tom_the_turtle.circle(50)

# for _ in range(10):
#     tom_the_turtle.forward(10)
#     tom_the_turtle.penup()
#     tom_the_turtle.forward(10)
#     tom_the_turtle.pendown()



screen = Screen()
screen.exitonclick()
