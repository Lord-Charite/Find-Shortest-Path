
"""
Lord-Charité Igirimbabazi
Section 1 with Vasanta Lakshmi
Lab4
March8, 2021
winter2021
Purpose: define a load graph function to create a vertex object object and add it into a dictionary
"""

from vertex import Vertex


def load_graph(filename):
    vertex_dict = {}
    fp = open(filename, "r")
    for line in fp:
        field_list= line.split(";")
        for i in range(len(field_list)):
            field_list[i] = field_list[i].strip()

        location= field_list[2].split(",")
        vertex_= field_list[0]
        v = Vertex(vertex_, location[0], location[1])
        vertex_dict[field_list[0]] = v

    fp.close()

    fp1 = open(filename, "r")
    for line in fp1:
        field_list = line.split(";")
        for i in range(len(field_list)):
            field_list[i] = field_list[i].strip()
        adj_vertex = field_list[1]
        adj_list = adj_vertex.split(",")
        for i in range(len(adj_list)):
            adj_list[i] = adj_list[i].strip()
        vertex_ = field_list[0]
        v = vertex_dict[vertex_]
        for v_name in adj_list:
            v_obj = vertex_dict[v_name]
            v.adj_list_.append(v_obj)
    fp1.close()
    return vertex_dict
