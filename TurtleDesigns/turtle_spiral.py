import turtle

def draw_spiral():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Spiral Design")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.width(2)
    t.hideturtle()

    # Colors for the design
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

    # Draw a spiral of squares
    for i in range(150):
        t.color(colors[i % len(colors)])  # Cycle through colors
        t.forward(i * 2)  # Forward step increases each iteration
        t.right(91)  # Slightly offset angle for a spiral effect

    # Finish
    screen.mainloop()

draw_spiral()
