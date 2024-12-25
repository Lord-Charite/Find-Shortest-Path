"""
Lord-Charité Igirimbabazi
Section 1 with Vasanta Lakshmi
Lab4
March8, 2021
winter2021
Purpose: make a map_plot python file that draw the vertices and  their edges on map and allow the user to
select a path using BFS
"""
from cs1lib import *
from vertex import *
from load_graph import *
from bfs import *

vertex_dict = load_graph("dartmouth_graph.txt")
#verify if mouse is pressed
mpressed = False
#vertices object
start_vertex = None
goal_vertex = None
#coord keeps track of the mouse movement
x = 0
y = 0


def main_draw():
    global mpressed, x, y, start_vertex, goal_vertex
    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)
    draw_graph()
    #get the start vertex
    for vertex in vertex_dict:
        v_object = vertex_dict[vertex]
        if mpressed and v_object.check_mouse_in_sqr_area(x, y):
            start_vertex = v_object
            start_vertex.draw_vertices(1, 0, 0)

    #get the goal vetex
    for vertex1 in vertex_dict:
        v_object = vertex_dict[vertex1]
        if not mpressed and v_object.check_mouse_in_sqr_area(x, y):
            goal_vertex = v_object
            goal_vertex.draw_vertices(1, 0, 0)


    #get the path using bfs and start and goal vertex
    if start_vertex != None and goal_vertex != None:
        path = breadth_first_search(start_vertex, goal_vertex)
        for vertex2 in path:
            for vertex3 in path:
                if vertex3 in vertex2.adj_list_:
                    v_object = vertex_dict[vertex2.name]
                    v_object.draw_vertices(1,0,0)
                    v_object.draw_edge(vertex3,1, 0, 0)


def draw_graph():
    draw_vertices()
    draw_edges()


def draw_vertices():
    for vertex in vertex_dict:
        v_object = vertex_dict[vertex]
        v_object.draw_vertices(0, 0, 1)


def draw_edges():
    for vertex in vertex_dict:
        v_object = vertex_dict[vertex]
        v_object.draw_edges(0, 0, 1)


def my_mpress(mx, my):
    global mpressed, x, y
    mpressed = True
    x = mx
    y = my


def my_mrelease(mx, my):
    global mpressed
    mpressed = False


def my_move(mx, my):
    global x, y
    x = mx
    y = my


start_graphics(main_draw, mouse_move=my_move, mouse_press=my_mpress, mouse_release=my_mrelease, width=1012, height=811)
