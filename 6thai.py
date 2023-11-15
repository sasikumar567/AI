class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.total_dirty = sum(row.count('D') for row in grid)

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def clean(self, x, y):
        if self.is_valid(x, y) and self.grid[x][y] == 'D' and (x, y) not in self.visited:
            self.visited.add((x, y))
            self.grid[x][y] = 'C'  # Mark as cleaned
            self.total_dirty -= 1

    def move_left(self, x, y):
        return x, y - 1

    def move_right(self, x, y):
        return x, y + 1

    def move_up(self, x, y):
        return x - 1, y

    def move_down(self, x, y):
        return x + 1, y

    def clean_entire_room(self):
        x, y = 0, 0  
        cleaned = 0

        while cleaned < self.total_dirty:
            self.clean(x, y)
            if self.grid[x][y] == 'C':
                cleaned += 1

            if cleaned == self.total_dirty:
                break

            if self.move_right(x, y) not in self.visited and self.is_valid(x, y + 1):
                y += 1
            elif self.move_down(x, y) not in self.visited and self.is_valid(x + 1, y):
                x += 1
            elif self.move_left(x, y) not in self.visited and self.is_valid(x, y - 1):
                y -= 1
            elif self.move_up(x, y) not in self.visited and self.is_valid(x - 1, y):
                x -= 1
            else:
                break  

        if cleaned == self.total_dirty:
            print("Room cleaned!")
        else:
            print("Unable to clean entire room.")


room = [
    ['D', 'C', 'D', 'D'],
    ['D', 'C', 'C', 'D'],
    ['C', 'D', 'D', 'C'],
    ['D', 'C', 'D', 'D']
]

vacuum = VacuumCleaner(room)
vacuum.clean_entire_room()
