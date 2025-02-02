import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    # Малюємо стовбур
    t.forward(branch_length)
    
    # Ліва гілка
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.right(45)  # Повертаємося
    
    # Права гілка
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    t.left(45)  # Повертаємося
    
    # Повертаємося до основи стовбура
    t.backward(branch_length)

def main():
    # Налаштування вікна Turtle
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    
    # Створюємо об'єкт Turtle
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Початкові налаштування
    branch_length = 100  # Довжина стовбура
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
    
    # Початкова позиція
    t.penup()
    t.goto(0, -200)  # Розміщуємо дерево в нижній частині вікна
    t.pendown()
    t.left(90)  # Повертаємо Turtle вгору
    
    # Малюємо дерево
    draw_pythagoras_tree(t, branch_length, level)
    
    # Завершення
    screen.mainloop()

if __name__ == "__main__":
    main()