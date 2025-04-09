from collections import deque

# Define directions: up, down, left, right
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs_flood_fill(grid, start_row, start_col, new_color):
    queue = deque([(start_row, start_col)])
    start_color = grid[start_row][start_col]
    visited = set()
    
    while queue:
        row, col = queue.popleft()
        grid[row][col] = new_color
        visited.add((row, col))  # Mark current cell as visited
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and grid[new_row][new_col] == start_color:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))  # Mark new cell as visited
    
    return grid

# Example grid
grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

start_row, start_col = 1, 2  # Starting point
new_color = 2  # New color to fill

filled_grid_bfs = bfs_flood_fill(grid, start_row, start_col, new_color)
for row in filled_grid_bfs:
    print(row)



# Define directions: up, down, left, right
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs_flood_fill(grid, row, col, start_color, new_color, visited):
    if (row, col) in visited or row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != start_color:
        return
    
    grid[row][col] = new_color
    visited.add((row, col))  # Mark current cell as visited
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        dfs_flood_fill(grid, new_row, new_col, start_color, new_color, visited)

# Example grid
grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

start_row, start_col = 1, 2  # Starting point
new_color = 2  # New color to fill
start_color = grid[start_row][start_col]

visited = set()
dfs_flood_fill(grid, start_row, start_col, start_color, new_color, visited)

for row in grid:
    print(row)
