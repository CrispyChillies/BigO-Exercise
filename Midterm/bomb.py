# from queue import PriorityQueue
# import math
# import heapq

# class Cell:
#     def __init__(self):
#         self.parent_i = 0
#         self.parent_j = 0
#         self.f = float('inf')
#         self.g = float('inf')
#         self.g = float('inf')
#         self.h = 0
# class AStar:
#     def __init__(self, matrix, src, des):
#         self.matrix = matrix
#         self.src = src
#         self.des = des

#     def is_valid(self, row, col, max_rows, max_cols):
#         return (row >= 0) and (row < max_rows) and (col >= 0) and (col < max_cols)

#     def is_unblocked(self, grid, row, col):
#         return grid[row][col] == 2 or grid[row][col] == 4 or grid[row][col] == 3 or grid[row][col] == 0

#     def is_destination(self, row, col, dest):
#         return row == dest[0] and col == dest[1]

#     def calculate_h_value(self, row, col, dest):
#         return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5
    
#     def trace_path(self, cell_details, dest):
#         path = []
#         row = dest[0]
#         col = dest[1]
    
#         # Trace the path from destination to source using parent cells
#         while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
#             path.append((row, col))
#             temp_row = cell_details[row][col].parent_i
#             temp_col = cell_details[row][col].parent_j
#             row = temp_row
#             col = temp_col
    
#         # Add the source cell to the path
#         path.append((row, col))
#         # Reverse the path to get the path from source to destination
#         path.reverse()
    
#         return path
    
#     def aStar(self, src, des, R, C):
#         max_rows, max_cols = R, C
#         # Check if the source and destination are valid
#         if not self.is_valid(src[0], src[1], max_rows, max_cols) or not self.is_valid(des[0], des[1], max_rows, max_cols):
#             print("Source or destination is invalid")
#             return
    
#         # Check if the source and destination are unblocked
#         if not self.is_unblocked(self.matrix, src[0], src[1]) or not self.is_unblocked(self.matrix, des[0], des[1]):
#             # print("Source or the destination is blocked")
#             return
    
#         # Check if we are already at the destination
#         if self.is_destination(src[0], src[1], des):
#             # print("We are already at the destination")
#             return
    
#         # Initialize the closed list (visited cells)
#         closed_list = [[False for _ in range(max_cols)] for _ in range(max_rows)]
#         # Initialize the details of each cell
#         cell_details = [[Cell() for _ in range(max_cols)] for _ in range(max_rows)]
    
#         # Initialize the start cell details
#         i = src[0]
#         j = src[1]
#         cell_details[i][j].f = 0
#         cell_details[i][j].g = 0
#         cell_details[i][j].h = 0
#         cell_details[i][j].parent_i = i
#         cell_details[i][j].parent_j = j
    
#         # Initialize the open list (cells to be visited) with the start cell
#         open_list = []
#         heapq.heappush(open_list, (0.0, i, j))

#         # Initialize the flag for whether destination is found
#         found_dest = False
    
#         # Main loop of A* search algorithm
#         while len(open_list) > 0:
#             # Pop the cell with the smallest f value from the open list
#             p = heapq.heappop(open_list)
    
#             # Mark the cell as visited
#             i = p[1]
#             j = p[2]
#             closed_list[i][j] = True
    
#             # For each direction, check the successors
#             directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#             for dir in directions:
#                 new_i = i + dir[0]
#                 new_j = j + dir[1]
    
#                 # If the successor is valid, unblocked, and not visited
#                 if self.is_valid(new_i, new_j, max_rows, max_cols) and self.is_unblocked(self.matrix, new_i, new_j) and not closed_list[new_i][new_j]:
#                     # If the successor is the destination
#                     if self.is_destination(new_i, new_j, des):
#                         # Set the parent of the destination cell
#                         cell_details[new_i][new_j].parent_i = i
#                         cell_details[new_i][new_j].parent_j = j
#                         # print("The destination cell is found")
#                         # Trace and print the path from source to destination
#                         path = self.trace_path(cell_details, des)
#                         found_dest = True 
#                         return path
#                     else:
#                         # Calculate the new f, g, and h values
#                         g_new = cell_details[i][j].g + 1.0
#                         h_new = self.calculate_h_value(new_i, new_j, des)
#                         f_new = g_new + h_new
    
#                         # If the cell is not in the open list or the new f value is smaller
#                         if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
#                             # Add the cell to the open list
#                             heapq.heappush(open_list, (f_new, new_i, new_j))
#                             # Update the cell details
#                             cell_details[new_i][new_j].f = f_new
#                             cell_details[new_i][new_j].g = g_new
#                             cell_details[new_i][new_j].h = h_new
#                             cell_details[new_i][new_j].parent_i = i
#                             cell_details[new_i][new_j].parent_j = j
    
#         # If the destination is not found after visiting all cells
#         if not found_dest:
#             print("Failed to find the destination cell")

    
# R,C = map(int, input().split())

# bombs = int(input())

# grid = [[0] * C for _ in range(R)]

# for _ in range(bombs):
#     info = list(map(int, input().split()))
#     row = info[0]
#     bomb = info[1]
#     index = 2
#     for _ in range(bomb):
#         col = info[index]
#         grid[row][col] = 1
#         index += 1

# start = list(map(int, input().split()))
# end = list(map(int, input().split()))
# trial = map(int, input().split())


# searchPath = AStar(grid, start, end)
# path = searchPath.aStar(start, end, R, C)

# print(len(path) - 1)

from queue import PriorityQueue
import math
import heapq

class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.g = float('inf')
        self.h = 0

class AStar:
    def __init__(self, matrix, src, des):
        self.matrix = matrix
        self.src = src
        self.des = des

    def is_valid(self, row, col, max_rows, max_cols):
        return (row >= 0) and (row < max_rows) and (col >= 0) and (col < max_cols)

    def is_unblocked(self, grid, row, col):
        return grid[row][col] != 1

    def is_destination(self, row, col, dest):
        return row == dest[0] and col == dest[1]

    def calculate_h_value(self, row, col, dest):
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5
    
    def trace_path(self, cell_details, dest):
        path = []
        row = dest[0]
        col = dest[1]
    
        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col
    
        # Add the source cell to the path
        path.append((row, col))
        # Reverse the path to get the path from source to destination
        path.reverse()
    
        return path
    
    def aStar(self, src, des, R, C):
        max_rows, max_cols = R, C
        # Check if the source and destination are valid
        if not self.is_valid(src[0], src[1], max_rows, max_cols) or not self.is_valid(des[0], des[1], max_rows, max_cols):
            print("Source or destination is invalid")
            return
    
        # Check if the source and destination are unblocked
        if not self.is_unblocked(self.matrix, src[0], src[1]) or not self.is_unblocked(self.matrix, des[0], des[1]):
            print("Source or the destination is blocked")
            return
    
        # Check if we are already at the destination
        if self.is_destination(src[0], src[1], des):
            print("We are already at the destination")
            return
    
        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(max_cols)] for _ in range(max_rows)]
        # Initialize the details of each cell
        cell_details = [[Cell() for _ in range(max_cols)] for _ in range(max_rows)]
    
        # Initialize the start cell details
        i = src[0]
        j = src[1]
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j
    
        # Initialize the open list (cells to be visited) with the start cell
        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        # Main loop of A* search algorithm
        while len(open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(open_list)
    
            # Mark the cell as visited
            i = p[1]
            j = p[2]
            closed_list[i][j] = True
    
            # For each direction, check the successors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
    
                # If the successor is valid, unblocked, and not visited
                if self.is_valid(new_i, new_j, max_rows, max_cols) and self.is_unblocked(self.matrix, new_i, new_j) and not closed_list[new_i][new_j]:
                    # If the successor is the destination
                    if self.is_destination(new_i, new_j, des):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        # Trace and return the path from source to destination
                        return self.trace_path(cell_details, des)
                    else:
                        # Calculate the new f, g, and h values
                        g_new = cell_details[i][j].g + 1.0
                        h_new = self.calculate_h_value(new_i, new_j, des)
                        f_new = g_new + h_new
    
                        # If the cell is not in the open list or the new f value is smaller
                        if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                            # Add the cell to the open list
                            heapq.heappush(open_list, (f_new, new_i, new_j))
                            # Update the cell details
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j
    
        # If the destination is not found after visiting all cells
        print("Failed to find the destination cell")
        return None
    
test_cases = []
while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    
    bombs = int(input())

    grid = [[0] * C for _ in range(R)]

    for _ in range(bombs):
        info = list(map(int, input().split()))
        row = info[0]
        bomb = info[1]
        index = 2
        for _ in range(bomb):
            col = info[index]
            grid[row][col] = 1
            index += 1

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    test_cases.append((grid, start, end, R, C))

for grid, start, end, R, C in test_cases:
    searchPath = AStar(grid, start, end)
    path = searchPath.aStar(start, end, R, C)
    print(len(path) - 1)


