# Interactive Maze Solver 🎯

A Python-based interactive maze solver where you can draw your own mazes in the terminal and watch the program solve them using Breadth-First Search (BFS).

## How It Works
1. Draw your maze row by row in the terminal:
   - Use `#` for walls.
   - Use spaces (` `) for paths.
   - Use `S` for the start point.
   - Use `E` for the end point.
2. Type `DONE` when you're finished drawing the maze.
3. Watch the program solve the maze and display the solution!

## Example Input

## New Features

### 1. Maze Generation
- Automatically generate random mazes with specified dimensions and wall density.
- Example usage:
  ```python
  maze = generate_maze(20, 20, 0.3)
  ```
 Multiple Solving Algorithms
Added support for Depth-First Search (DFS) in addition to BFS.
Example usage:
path = solve_maze_dfs(maze, start, end)
 Maze Saving and Loading
Save mazes to a file and load them later.
Example usage:
save_maze(maze, 'maze.txt')
loaded_maze = load_maze('maze.txt')
Graphical User Interface (GUI)
Simple GUI using Tkinter to visualize the maze and the solving process.
Example usage:
python maze_solver_gui.py
Maze Validation
Validate the maze to ensure it has a valid start and end point.
Example usage:
is_valid = validate_maze(maze, start, end)
Step-by-Step Visualization
Visualize the solving process step-by-step.
Example usage:
path = solve_maze_visual(maze, start, end)
Customizable Maze Size
Specify the dimensions of the maze when generating it.
Example usage:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
maze = generate_maze(rows, cols)
Hints and Pathfinding Assistance
Provide hints by showing the next step towards the solution.
Example usage:
next_step = provide_hint(maze, start, end)
Performance Metrics
Display performance metrics such as time taken and number of steps.
Example usage:
solve_maze_with_metrics(maze, start, end)
User Input Error Handling
Improved error handling for user input.
Example usage:
try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    if rows <= 0 or cols <= 0:
        raise ValueError("Dimensions must be positive integers.")
    maze = generate_maze(rows, cols)
    print_maze(maze)
except ValueError as e:
    print(f"Invalid input: {e}")
    python maze_solver.py
    python maze_solver_gui.py
    