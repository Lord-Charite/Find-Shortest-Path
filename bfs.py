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
    frontier = deque()
    back_pointer = {}
    frontier.append(start)
    back_pointer[start] = None
    while len(frontier) > 0:
        v = frontier.popleft()
        for neighbour in v.adj_list_:
            if neighbour not in back_pointer:
                frontier.append(neighbour)
                back_pointer[neighbour] = v
            if neighbour == goal.name:
                break

    vertex = goal

    path = []

    while (vertex != None):
        path.append(vertex)
        vertex = back_pointer[vertex]
    return path



