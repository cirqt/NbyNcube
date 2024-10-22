class Rubikscube:
    def __init__(self, N):
        self.N = N
        self.grid = self.create_grid(N)

    def create_grid(self, N):
        rows = 4 * N
        cols = 3 * N
        grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        # Define colors for each face
        colors = {
            'U': 'W',  # Up face - White
            'D': 'Y',  # Down face - Yellow
            'F': 'G',  # Front face - Green
            'B': 'B',  # Back face - Blue
            'L': 'O',  # Left face - Orange
            'R': 'R'   # Right face - Red
        }
        
        # Fill the grid with corresponding colors
        # Up face
        for i in range(N):
            for j in range(N):
                grid[i][N + j] = colors['U']
        
        # Left face
        for i in range(N, 2 * N):
            for j in range(N):
                grid[i][j] = colors['L']
        
        # Front face
        for i in range(N, 2 * N):
            for j in range(N, 2 * N):
                grid[i][j] = colors['F']
        
        # Right face
        for i in range(N, 2 * N):
            for j in range(2 * N, 3 * N):
                grid[i][j] = colors['R']
        
        # Back face
        for i in range(2 * N, 3 * N):
            for j in range(N, 2 * N):
                grid[i][j] = colors['B']
        
        # Down face
        for i in range(3 * N, 4 * N):
            for j in range(N, 2 * N):
                grid[i][j] = colors['D']
        
        return grid

# Example usage:
N = 5
rubikscube = Rubikscube(N)
for row in rubikscube.grid:
    print(row)