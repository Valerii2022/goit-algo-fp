import turtle
from collections import deque

class Node:
    def __init__(self, key, position=None):
        self.left = None
        self.right = None
        self.value = key
        self.position = position

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def draw_tree(t, root, x, y, dx):
    if root is not None:
        root.position = (x, y) 
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(20, "#000000")  
        t.write(root.value, align="center", font=("Arial", 12, "normal"))
        
        if root.left:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.goto(x - dx, y - 50)
            draw_tree(t, root.left, x - dx, y - 50, dx / 2)
            
        if root.right:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.goto(x + dx, y - 50)
            draw_tree(t, root.right, x + dx, y - 50, dx / 2)

def dfs_visualize(t, root):
    stack = [(root, 0)]
    colors = ["#FF0000", "#FF7F00", "#FFFF00", "#7FFF00", "#00FF00", "#00FF7F", "#00FFFF", "#007FFF", "#0000FF", "#7F00FF", "#FF00FF", "#FF007F"]
    visited = set()
    
    while stack:
        node, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            color = colors[depth % len(colors)]
            t.penup()
            t.goto(node.position)
            t.pendown()
            t.dot(20, color)
            t.write(node.value, align="center", font=("Arial", 12, "normal"))
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

def bfs_visualize(t, root):
    queue = deque([(root, 0)])
    colors = ["#FF0000", "#FF7F00", "#FFFF00", "#7FFF00", "#00FF00", "#00FF7F", "#00FFFF", "#007FFF", "#0000FF", "#7F00FF", "#FF00FF", "#FF007F"]
    visited = set()
    
    while queue:
        node, depth = queue.popleft()
        if node not in visited:
            visited.add(node)
            color = colors[depth % len(colors)]
            t.penup()
            t.goto(node.position)
            t.pendown()
            t.dot(20, color)
            t.write(node.value, align="center", font=("Arial", 12, "normal"))
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

def main():
    screen = turtle.Screen()
    screen.title("Візуалізація обходу дерева")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  
    
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 6)
    root = insert(root, 8)
    
    draw_tree(t, root, 0, 0, 100)
    
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    
    dfs_visualize(t, root)
    
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    
    bfs_visualize(t, root)
    
    turtle.done()

if __name__ == "__main__":
    main()

