import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Mandala pattern
colors = ["cyan", "magenta", "yellow", "white"]
for i in range(36):
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.left(10)
    for _ in range(4):
        t.forward(50)
        t.right(90)

t.hideturtle()
screen.mainloop()
