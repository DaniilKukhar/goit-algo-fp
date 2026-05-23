import turtle


def draw_tree(branch_length, level):

    if level == 0:
        return

    # Малювання гілки
    turtle.forward(branch_length)

    # Поворот вправо
    turtle.right(30)

    # Права гілка
    draw_tree(branch_length * 0.7, level - 1)

    # Поворот вліво
    turtle.left(60)

    # Ліва гілка
    draw_tree(branch_length * 0.7, level - 1)

    # Повернення у початковий напрямок
    turtle.right(30)

    # Повернення назад
    turtle.backward(branch_length)


def main():

    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштування черепашки
    turtle.speed(0)
    turtle.color("brown")
    turtle.pensize(2)

    # Початкова позиція
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    # Малювання дерева
    draw_tree(100, level)

    # Завершення програми
    turtle.done()


if __name__ == "__main__":
    main()