import turtle

# Създаване на прозорец и настройка на черепахата
window = turtle.Screen()
window.bgcolor("white")
window.title("Pulsating Heart")

turtle.speed(1)  # Настройка на скоростта на черепахата

# Рисуване на сърцето
def draw_heart():
    turtle.begin_fill()
    turtle.color("pink")
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Напис "I Love You" във сърцето
def write_text():
    turtle.penup()
    turtle.goto(-70, -50)
    turtle.color("red")
    turtle.write("I", align="center", font=("Arial", 24, "bold"))
    turtle.goto(0, -50)
    turtle.write("Love", align="center", font=("Arial", 24, "bold"))
    turtle.goto(70, -50)
    turtle.write("You", align="center", font=("Arial", 24, "bold"))

# Рисуване на сърцето и написа "I Love You"
draw_heart()
write_text()

# Пулсиращо сърце
while True:
    turtle.pensize(3)
    turtle.pencolor("red")
    turtle.setheading(0)
    turtle.right(20)
    for _ in range(15):
        turtle.forward(10)
        turtle.right(5)
    turtle.right(5)
    for _ in range(15):
        turtle.forward(10)
        turtle.right(5)

turtle.done()