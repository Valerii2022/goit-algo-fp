import turtle
import math

def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return

    turtle.forward(branch_length)
    
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), level - 1, angle)
    
    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), level - 1, angle)
    
    turtle.left(angle)
    turtle.backward(branch_length)

def setup_turtle():
    turtle.speed(0)  
    turtle.left(90)  
    
def draw_tree(level, angle=45):
    setup_turtle()
    draw_pythagoras_tree(100, level, angle)
    turtle.done()

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    draw_tree(level)


