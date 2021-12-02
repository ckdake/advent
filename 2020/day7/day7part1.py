#!/usr/bin/env python
""" 2020 code advent, day 7 part 1 """

import csv
import re
import networkx as nx


def howmanysuccessors(bag_graph, current_node, depth=0, visited=set()):
    the_count = 1
    visited.add(current_node)

    # print(depth, ":", current_node, bag_graph[current_node].items())

    for (node, attrs) in bag_graph[current_node].items():
        if node not in visited:
            the_count += howmanysuccessors(bag_graph, node, depth + 1)
    return the_count


def doit():
    """ Does the work """

    color_graph = nx.DiGraph()

    # build a graph consisting of dag edges (a,b) where a is a type of bag that is in b
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
                color_graph.add_edge(found_color, first_color, weight=the_weight)

            for another_bag in row[1 : len(row)]:
                match = re.match(r"^ (\d) (.*) bag", another_bag)
                found_color = match.group(2)
                the_weight = match.group(1)
                color_graph.add_edge(found_color, first_color, weight=the_weight)

    shiny_gold_graph = nx.dfs_successors(color_graph, "shiny gold")

    bags = set()
    for key in shiny_gold_graph.keys():
        bags.add(key)
        for value in shiny_gold_graph[key]:
            bags.add(value)
    print(len(bags) - 1)
    print(howmanysuccessors(color_graph, "shiny gold") - 1)

    # its not 4 or 5. 5 is immediate parents, need to go up the graph
    # 175 is too low
    # 338 is wrong, includes 'shiny gold', so 337?


doit()
