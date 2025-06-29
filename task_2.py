import turtle

# Налаштування екрана і черепашки:
screen = turtle.Screen()
screen.setup(500, 500)

t = turtle.Turtle()
t.color("darkgreen")
t.speed(7)
t.pensize(3)
t.hideturtle()

# Початкова позиція черепашки:
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()


# Рекурсивна функція побудови дерева:
def tree(t, depth, length, reduction, angle):
    if depth == 0:
        return

    t.forward(length)

    # Позиція та напрямок:
    pos = t.position()
    heading = t.heading()

    # Малюємо ліву та праву гілки:
    for turn in (angle, -angle):
        t.setheading(heading + turn)
        tree(t, depth - 1, length - reduction, reduction, angle)
        t.penup()
        t.setposition(pos)
        t.setheading(heading)
        t.pendown()


# Вибір глибини:
depth = int(input("Enter the depth of the tree: "))
tree(t, depth, 100, 10, 30)

screen.exitonclick()
