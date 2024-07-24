import turtle

def draw_tree(t, branch_length, angle, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    t.right(angle)
    draw_tree(t, branch_length * 0.7, angle, level - 1)
    
    t.left(2 * angle)
    draw_tree(t, branch_length * 0.7, angle, level - 1)
    
    t.right(angle)
    t.backward(branch_length)

def main():
    try:
        screen = turtle.Screen()
        screen.title("Дерево Піфагора")
        screen.bgcolor("white")
        
        t = turtle.Turtle()
        t.speed(0)  
        
        level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
        
        t.left(90) 
        t.penup()
        t.goto(0, -200) 
        t.pendown()
        
        draw_tree(t, 100, 30, level)
        
        turtle.done()
        
    except turtle.Terminator:
        print("Термінатор: Вікно закрито або програма була зупинена.")

if __name__ == "__main__":
    main()

