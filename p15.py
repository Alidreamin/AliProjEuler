#!/usr/bin/env python

from time import clock
from math import sqrt
import numpy
start = clock()
"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""
graph_dict = {}
size = 8
graph_array = numpy.zeros((size,size))
print graph_array
it = numpy.nditer(graph_array, flags=['multi_index'])
while not it.finished:
    try:
        print graph_array[it.multi_index[0]+1, it.multi_index[1]], graph_array[it.multi_index[0], it.multi_index[1]+1]
        graph_dict[(it.multi_index[0], it.multi_index[1])] = [(it.multi_index[0]+1, it.multi_index[1]),(it.multi_index[0], it.multi_index[1]+1)]
    except IndexError:
        try:
            # this at the boundary of the grid/graph, where the element is only connected to the right or down but not both
            print graph_array[it.multi_index[0] + 1, it.multi_index[1]]
            graph_dict[(it.multi_index[0], it.multi_index[1])] = [(it.multi_index[0]+1, it.multi_index[1])]
        except IndexError:
            try:
                print graph_array[it.multi_index[0], it.multi_index[1] + 1]
                graph_dict[(it.multi_index[0], it.multi_index[1])] = [(it.multi_index[0], it.multi_index[1]+1)]
            except IndexError:
                print "at the end", graph_array[it.multi_index[0], it.multi_index[1]]
                #graph_dict[(graph_array[it.multi_index[0], it.multi_index[1]])] = []
    it.iternext()

# i'll manually build a 2 by 2 directed graph dictionary

# first test the recursive path finding function


# graph_dict = {
#     (0,0) : [(0,1), (1,0)],
#     (0,1) : [(1,1)],
#     (1,0) : [(1,1)]
# }



print graph_dict
for key, value in graph_dict.iteritems():
     print key, value



def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
                #print paths
    return paths

print len(find_all_paths(graph_dict, (0,0), (size-1,size-1)))

#
# def sum_paths(graph, start, end):
#     if start == end:
#         return 1
#     for node in graph[start]:
#         sum = sum_paths(graph, node, end)
#
#     return sum
#
# print sum_paths(graph_array, (0,0), (19,19))

stop = clock()
print("running time is %s" % (stop-start))

# okay, so this takes soooo long to run for n x n, where n > 15 or so
#  this problem can be solved...ANALYTICALLY!
#  a 20x20 grid as defined by this problem means a 21x21 graph
#  21!/(10!*10!)
#  the number of rights and downs that can be arranged