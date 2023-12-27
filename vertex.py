"""
Lord-Charité Igirimbabazi
Section 1 with Vasanta Lakshmi
Lab4 checkpoint
March8, 2021
winter2021
Purpose: create vertex class that takes name of the vertex and its x and y locations
"""
from cs1lib import *

RADIUS = 8
# stroke_width
N = 2

class Vertex:
    # x and y are coordinate of the location
    def __init__(self, name, x, y):
        self.name = name
        self.x_location = int(x)
        self.y_location = int(y)
        self.adj_list_ = []

    def adj_names(self):
        adj_name = ""
        for i in range(len(self.adj_list_)):
            adj_name += self.adj_list_[i].name + ", "
            if i == len(self.adj_list_) - 1:
                adj_name += self.adj_list_[i].name
        return adj_name

    def draw_vertices(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x_location, self.y_location, RADIUS)

    def draw_edge(self, vertex1, r, g, b):
        enable_stroke()
        set_stroke_width(N)
        set_stroke_color(r, g, b)
        draw_line(self.x_location, self.y_location, vertex1.x_location, vertex1.y_location)

    def draw_edges(self, r, g, b):
        enable_stroke()
        for vertex in self.adj_list_:
            self.draw_edge(vertex, r, g, b)

    def check_mouse_in_sqr_area(self, mx, my):
        return self.x_location - RADIUS <= mx <= self.x_location + RADIUS \
               and self.y_location - RADIUS <= my <= self.y_location + RADIUS

    def __str__(self):
        return self.name + "; " + "Location: " + str(self.x_location) + "," + str(
            self.y_location) + "; " + "Adjacent vertices: " + (self.adj_names())
