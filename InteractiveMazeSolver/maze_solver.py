import sys
from collections import deque
import random
import time

def print_maze(maze):
    """Prints the maze grid."""
    for row in maze:
        print("".join(row))
    print()

def generate_maze(rows, cols, density=0.3):
    """Generates a random maze with given dimensions and wall density."""
    maze = [[" " for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if random.random() < density:
                maze[i][j] = "#"
    maze[0][0] = "S"  # Start point
    maze[rows-1][cols-1] = "E"  # End point
    return maze

def solve_maze(maze, start, end):
    """Solves the maze using Breadth-First Search (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # Queue stores current position and path
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # Return the path if the end is reached

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == " " and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None  # No solution found

def solve_maze_dfs(maze, start, end):
    """Solves the maze using Depth-First Search (DFS)."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == " " and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None

def solve_maze_visual(maze, start, end):
    """Solves the maze using BFS with step-by-step visualization."""
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == " " and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
                print_maze(maze)
                time.sleep(0.1)

    return None

def provide_hint(maze, start, end):
    """Provides a hint by showing the next step towards the solution."""
    path = solve_maze(maze, start, end)
    if path and len(path) > 1:
        return path[1]  # Return the next step
    return None

def save_maze(maze, filename):
    """Saves the maze to a file."""
    with open(filename, 'w') as f:
        for row in maze:
            f.write("".join(row) + "\n")

def load_maze(filename):
    """Loads a maze from a file."""
    with open(filename, 'r') as f:
        maze = [list(line.strip()) for line in f]
    return maze

import time

def solve_maze_with_metrics(maze, start, end):
    """Solves the maze and displays performance metrics."""
    start_time = time.time()
    path = solve_maze(maze, start, end)
    end_time = time.time()
    if path:
        print(f"Path found: {path}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        print(f"Steps: {len(path)}")
    else:
        print("No path found.")

def main():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensions must be positive integers.")
        maze = generate_maze(rows, cols)
        print_maze(maze)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()