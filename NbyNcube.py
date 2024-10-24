class Rubikscube:
    def __init__(self, N):
        self.N = N
        self.grid = self.create_grid(N)

    def create_grid(self, N):
        """
        Creates a 2D grid representation of an NxN Rubik's cube.
        Args:
            N (int): The size of each face of the Rubik's cube.
        Returns:
            list: A 2D list representing the grid of the Rubik's cube with each face colored.
        The grid is organized as follows:
        - The grid has 4*N rows and 3*N columns.
        - Each face of the cube is represented by a specific color:
            'U' (Up face) - White ('W')
            'D' (Down face) - Yellow ('Y')
            'F' (Front face) - Green ('G')
            'B' (Back face) - Blue ('B')
            'L' (Left face) - Orange ('O')
            'R' (Right face) - Red ('R')
        The layout of the grid is:
            [   U   ][   O   ]
            [ L F R ][ G W B ]
            [   B   ][   Y   ]
            [   D   ][   R   ]
        Example:
            For N=2, the grid will look like:
            [
            [' ', ' ', 'W', 'W', ' ', ' '],
            [' ', ' ', 'W', 'W', ' ', ' '],
            ['O', 'O', 'G', 'G', 'R', 'R'],
            ['O', 'O', 'G', 'G', 'R', 'R'],
            [' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', 'Y', 'Y', ' ', ' '],
            [' ', ' ', 'Y', 'Y', ' ', ' ']
            ]
        """
        rows = 4 * N
        cols = 3 * N
        grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        # Define colors for each face
        colors = {
            'U': 'O',  # Up face - ORANGE
            'D': 'R',  # Down face - RED
            'F': 'W',  # Front face - WHITE
            'B': 'Y',  # Back face - YELLOW
            'L': 'G',  # Left face - GREEN
            'R': 'B'   # Right face - BLUE
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
    
    def rotate_row(self, row_index, direction):
        """
        Rotates a row of the Rubik's cube grid in the specified direction.
        Args:
            row_index (int): The index of the row to rotate.
            direction (str): The direction to rotate ('left' or 'right').
        """
        if direction not in ['left', 'right']:
            raise ValueError("Direction must be 'left' or 'right'")
        temp = self.grid[self.N-row_index-1][self.N:2*(self.N)]
        print(temp)
        for i in range(0,self.N):
            self.grid[self.N-row_index][self.N+i] = self.grid[2*self.N-i-1][self.N-row_index]
            self.grid[2*self.N-i-1][self.N-row_index] = self.grid[self.N*2+row_index-1][self.N*2-i-1]
            self.grid[self.N*2+row_index-1][self.N*2-i-1] = self.grid[self.N+i][self.N*2+row_index-1]
            self.grid[self.N+i][self.N*2+row_index-1] = temp[i]

        
    #def rotate_column(self, col_index, direction):

# Example usage:
N = 5
rubikscube = Rubikscube(3)
user_input = input("Enter a command: ")
commands = user_input.split()
for command in commands:
    if command[0] == 'H':
        row_index = int(command[1:])
        rubikscube.rotate_row(row_index, 'right')
    elif command[0] == 'V':
        col_index = int(command[1:])
        rubikscube.rotate_column(col_index, 'down')
for row in rubikscube.grid:
    print(row)