import turtle
import colorsys

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Graphic Design with Turtle")

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()

    num_of_colors = 36
    hue = 0
    colors = [colorsys.hsv_to_rgb(hue + i / num_of_colors, 1, 1) for i in range(num_of_colors)]
    colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]

    for i in range(360):
        turtle_color = colors[i % num_of_colors]
        t.color('#%02x%02x%02x' % turtle_color)
        t.circle(120)
        t.left(10)

    screen.mainloop()

draw_flower()
