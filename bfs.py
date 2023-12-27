"""
Lord-Charité Igirimbabazi
Section 1 with Vasanta Lakshmi
Lab4
March8, 2021
winter2021
Purpose: define a breadth first search function that takes in start and goal vertex objects as
parameters and return the shortest path between the start and goal vertex
"""
from collections import deque
# BFS

def breadth_first_search(start, goal):
    frontier = deque([start])
    back_pointer = { start : None}
    while len(frontier) > 0:
        v = frontier.popleft()
        for neighbour in v.adj_list_:
            
            if neighbour == goal.name:
                break
                
            if neighbour not in back_pointer:
                frontier.append(neighbour)
                back_pointer[neighbour] = v

    path = reconstruct_path(goal, back_pointer)
    return path

def reconstruct_path(goal, back_pointer):
    path = []
    current_vertex = goal

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = back_pointer[current_vertex]

    return path[::-1]  # Reverse the path to start from the 'start' vertex


