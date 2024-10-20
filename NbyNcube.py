class Rubikscube:
    def __init__(self, N):
        self.N = N
        self.grid = self.create_grid(N)

    def create_grid(self, N):
        rows = 4 * N
        cols = 3 * N
        grid = [['0' for _ in range(cols)] for _ in range(rows)]
        return grid

# Example usage:
N = 2
rubikscube = Rubikscube(N)
for row in rubikscube.grid:
    print(row)