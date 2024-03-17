# def isAvailable(graph, directions, rows, cols, r, c, letter):
    
#     for dr, dc in directions:
#         nr, nc = r + dr, c + dc

#         if 0 <= nr <= rows and 0 <= nc <= cols:
#             if graph[nr][nc] == letter:
#                 return True
#     return False

# def havePath(graph, rows, cols, phrase):
#     direction = [(-1, 0), (1,0), (0, -1), (0, 1)]

#     for letter in phrase:
#         for i in range(rows):
#             for j in range(cols):
#                 if isAvailable(graph, direction, rows, cols, i, j, letter):
#                     break
#                 else:
#                     return False
#     return True
                
    
                    
# N = int(input())

# rows, cols = map(int, input().split())

# lines = []
# for _ in range(rows):  # Assuming 3 lines of input
#     lines.append(input())

# # Split each line into individual characters and store them in a 2D array
# array = [list(line) for line in lines]

# phrase = "ALLIZZWELL"

# if havePath(array, rows, cols, phrase):
#     print("Yes")
# else:
#     print("No")


