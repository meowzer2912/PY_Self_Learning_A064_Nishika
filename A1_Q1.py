import turtle
import easygui

# functions to draw each shape
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)

def draw_concentric_circles(t, radius):
    # drawing 3 circles with spacing
    for i in range(3):
        current_radius = radius - (i * 20)
        if current_radius > 0:
            t.circle(current_radius)

def draw_star(t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)

# taking inputs through dialog boxes
shape_options = ["Square", "Equilateral Triangle", "Concentric Circles", "Custom Star"]
choice = easygui.buttonbox("Choose a shape to draw:", "Pattern Studio", choices=shape_options)

size = easygui.integerbox("Enter dimension or radius:", "Size Input", default=100, lowerbound=50, upperbound=250)
fill_color = easygui.enterbox("Enter  fill color ", "Color Input")

# setting up turtle screen
s = turtle.Screen()
t = turtle.Turtle()
t.speed(3)

# start filling color
t.fillcolor(fill_color)
t.begin_fill()

if choice == "Square":
    draw_square(t, size)
elif choice == "Equilateral Triangle":
    draw_triangle(t, size)
elif choice == "Concentric Circles":
    draw_concentric_circles(t, size)
elif choice == "Custom Star":
    draw_star(t, size)
t.end_fill()
# completion alert and exit
easygui.msgbox("Drawing completed successfully!", "Done")
turtle.bye()