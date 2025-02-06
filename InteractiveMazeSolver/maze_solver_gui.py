import tkinter as tk
from maze_solver import solve_maze, generate_maze, print_maze

def draw_maze(canvas, maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            color = "black" if cell == "#" else "white"
            canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color)

def main():
    root = tk.Tk()
    root.title("Maze Solver")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    maze = generate_maze(20, 20)
    draw_maze(canvas, maze)

    root.mainloop()

if __name__ == "__main__":
    main()