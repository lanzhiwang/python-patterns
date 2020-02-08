#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, path=None):
        print('start: %s' % start)
        print('end: %s' % end)
        print('path: %s' % path)
        print()
        """
        start: A
        end: D
        path: None

        start: B
        end: D
        path: ['A']

        start: C
        end: D
        path: ['A', 'B']

        start: D
        end: D
        path: ['A', 'B', 'C']
        """
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath

    def find_all_path(self, start, end, path=None):
        r"""
                 A->D
               /      \
             B->D    C->D
            /   \     \
          C->D D->D  D->D
          /
        D->D
        """
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if node not in path:
                newpaths = self.find_all_path(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path(self, start, end, path=None):
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_shortest_path(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


# example of graph usage
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
         }

# initialization of new graph search object
graph1 = GraphSearch(graph)

print(graph1.find_all_path('A', 'D'))  # [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
