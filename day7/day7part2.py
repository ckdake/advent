#!/usr/bin/env python
""" 2020 code advent, day 7 part 2 """

import csv
import re
import networkx as nx


def weightedchildrencount(bag_graph, current_node, depth=0):
    the_count = 1

    print(depth, ":", current_node, bag_graph[current_node].items())

    for (node, attrs) in bag_graph[current_node].items():
        the_count += int(attrs["weight"]) * weightedchildrencount(
            bag_graph, node, depth + 1
        )
    return the_count


def doit():
    """ Does the work """

    color_graph = nx.DiGraph()
    weights = {}

    # build a graph consisting of dag edges (a,b) where a may be in b
    with open("input.txt", "r") as file_descriptor:
        reader = csv.reader(file_descriptor)
        for row in reader:
            first_color = re.match(r"^(.*) bags contain", row[0]).group(1)
            if re.match(
                r"^(.*) bags contain no other bags", row[0]
            ):  # this is an end node in the graph
                color_graph.add_node(first_color)
            else:  # this contains bags!
                match = re.match(r"^(.*) bags contain (\d) (.*) bag", row[0])
                found_color = match.group(3)
                the_weight = match.group(2)
                color_graph.add_edge(first_color, found_color, weight=the_weight)

            for another_bag in row[1 : len(row)]:
                match = re.match(r"^ (\d) (.*) bag", another_bag)
                found_color = match.group(2)
                the_weight = match.group(1)
                color_graph.add_edge(first_color, found_color, weight=the_weight)

    # 369922 is too high
    print(weightedchildrencount(color_graph, "shiny gold") - 1)


doit()
