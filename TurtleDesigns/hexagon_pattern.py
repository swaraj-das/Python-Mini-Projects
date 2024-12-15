import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.color("purple")

# Hexagon function
def draw_hexagon(size, depth):
    if depth == 0:
        return
    for _ in range(6):
        t.forward(size)
        draw_hexagon(size / 2, depth - 1)
        t.right(60)

# Draw recursive hexagons
t.penup()
t.goto(-150, 150)
t.pendown()
draw_hexagon(100, 3)

t.hideturtle()
screen.mainloop()
