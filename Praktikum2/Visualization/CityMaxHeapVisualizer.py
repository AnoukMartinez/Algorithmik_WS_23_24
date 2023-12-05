import networkx as nx
import random
import math
from typing import List

from CityDataManagement.City import City
from CityDataManagement.CityDataManager import CityDataManager
from Visualization.HeatMapColorCreator import HeatMapColorCreator

from bokeh.models import Circle, MultiLine
from bokeh.plotting import figure, from_networkx, show
from bokeh.models import (BoxSelectTool, Circle, HoverTool, MultiLine, NodesAndLinkedEdges, TapTool, WheelZoomTool)
from bokeh.palettes import Spectral4


class CityMaxHeapVisualizer:
    """
    Class with the responsibility to visualize an array of City objects.
    """

    def create_radial_tree_visualisation(self, amount_of_nodes_to_create: int,
                                         city_heap_array: List[City], unsorted: bool):
        """
        Create a radial tree of a heap structure based on an array.


        Param
        -----
        amountOfNodesToCreate: Number of nodes to be displayed.

        cityHeapArray: List of city objects, the data to be presented. Index 0 = Root, Index 1 = second Child
        """

        if unsorted:
            sorted_city_heap_array = city_heap_array.copy()
            sorted_city_heap_array.sort(reverse=True)
            highest_population = sorted_city_heap_array[0].population
            heat_map_color_creator = HeatMapColorCreator(highest_population)
        else:
            highest_population = city_heap_array[0].population
            heat_map_color_creator = HeatMapColorCreator(highest_population)

        city_heap_array: List[City] = city_heap_array

        # NetworkX
        city_heap_graph = nx.Graph()
        self._create_nodes_and_edges(city_heap_array, city_heap_graph, amount_of_nodes_to_create, heat_map_color_creator,
                                     highest_population)
        plot = self._create_plot(city_heap_array)
        self._add_tools_to_plot(plot)

        # Bokeh
        graph_renderer = self._render_graph(city_heap_graph)
        self._render_nodes(graph_renderer)
        self._render_edges(graph_renderer)
        self._set_policies(graph_renderer)

        plot.renderers.append(graph_renderer)
        show(plot)

    def _set_policies(self, graph_renderer):
        """
        Set the policies for the general handling of the visualisation.
        """
        graph_renderer.selection_policy = NodesAndLinkedEdges()
        # graph_renderer.inspection_policy = EdgesAndLinkedNodes()

    def _render_edges(self, graph_renderer):
        """
        Render the Edges.
        """
        graph_renderer.edge_renderer.glyph = MultiLine(line_color="#000000", line_alpha=0.2, line_width=2)
        graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=2)
        graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=2)

    def _render_nodes(self, graph_renderer):
        """
        Render the Nodes.
        """
        graph_renderer.node_renderer.glyph = Circle(size="nodeSize", fill_color="nodeColor")
        # graph_renderer.node_renderer.selection_glyph = Circle(size=30, fill_color=Spectral4[2])
        graph_renderer.node_renderer.hover_glyph = Circle(size=30, fill_color=Spectral4[1])

    def _render_graph(self, city_heap_graph):
        """
        Render the whole graph (the visualisation as a whole).
        """

        pos = self.hierarchy_pos(city_heap_graph, 0, width=2 * math.pi, xcenter=0)
        new_pos = {u: (r * math.cos(theta), r * math.sin(theta)) for u, (theta, r) in
                   pos.items()}  # hierarchical radial tree
        graph_renderer = from_networkx(city_heap_graph, new_pos, scale=1, center=(0, 0))
        return graph_renderer
        # force directed layout (Fruchterman-Reingold layout)
        # graph_renderer = from_networkx(cityHeapGraph, nx.spring_layout, scale=1, center=(0, 0))

    def _add_tools_to_plot(self, plot):
        """
        Add Bokeh Tools to the visualisation.
        """
        plot.add_tools(TapTool(), BoxSelectTool())
        plot.toolbar.active_scroll = plot.select_one(WheelZoomTool)

    def _create_plot(self, city_heap_array):
        """
        Create the NetworkX Plot.
        """
        plot = figure(width=1000, height=1000, x_range=(-2.0, 2.0), y_range=(-2.0, 2.0),
                      x_axis_location=None, y_axis_location=None, toolbar_location="left",
                      title="My City Max Heap: The City with the highest Population is "
                            + city_heap_array[0].name
                            + " with a Population of "
                            + str(city_heap_array[0].population)
                            + " in "
                            + city_heap_array[0].country
                            + " .",
                      background_fill_color="#efefef",
                      tooltips="@cityName with a Population of @population in @country.")
        plot.grid.grid_line_color = None
        plot.sizing_mode = "scale_height"
        return plot

    def _create_nodes_and_edges(self, city_heap_array: List[City], city_heap_graph, amount_of_nodes_to_create: int,
                                heat_map_color_creator: HeatMapColorCreator, highest_population: int):
        """
        Create the NetworkX Nodes and Edges.

        Param:
        ------
        cityHeapArray : List[City]: Sorted List of all Citys.

        cityHeapGraph: The graph/plot to add nodes and edges to.

        amountOfNodesToCreate: inr: the maximum number of nodes to be displayed.

        heatMapColorCreator: HeatMapColorCreator: Class with the responsibility to generate the colors of nodes for a heatMap.

        highestPopulation: int: Highest population in the visualized spectrum

        """

        current_node_index = 0

        # Creation of Nodes & Edges
        for node in city_heap_array:
            size_of_this_node = 40 * (node.population / highest_population)
            if size_of_this_node < 2: size_of_this_node = 2
            color_of_this_node = heat_map_color_creator.heat_map_color_based_on_max_value(node.population)
            city_heap_graph.add_node(current_node_index, cityName=node.name, country=node.country,
                                     population=node.population, nodeSize=size_of_this_node, nodeColor=color_of_this_node)
            if 2 * current_node_index + 1 < amount_of_nodes_to_create:
                city_heap_graph.add_edge(current_node_index, 2 * current_node_index + 1)
            if 2 * current_node_index + 2 < amount_of_nodes_to_create:
                city_heap_graph.add_edge(current_node_index, 2 * current_node_index + 2)
            if current_node_index + 1 == amount_of_nodes_to_create:
                break
            current_node_index = current_node_index + 1

        root = 0
        nx.to_nested_tuple(city_heap_graph, root)

    def hierarchy_pos(self, G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
        Licensed under Creative Commons Attribution-Share Alike

        If the graph is a tree this will return the positions to plot this in a
        hierarchical layout.

        G: the graph (must be a tree)

        root: the root node of current branch
        - if the tree is directed and this is not given,
        the root will be found and used
        - if the tree is directed and this is given, then
        the positions will be just for the descendants of this node.
        - if the tree is undirected and not given,
        then a random choice will be used.

        width: horizontal space allocated for this branch - avoids overlap with other branches

        vert_gap: gap between levels of hierarchy

        vert_loc: vertical location of root

        xcenter: horizontal location of root
        """

        if not nx.is_tree(G):
            raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

        if root is None:
            if isinstance(G, nx.DiGraph):
                root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
            else:
                root = random.choice(list(G.nodes))

        def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
            """
            see hierarchy_pos docstring for most arguments

            pos: a dict saying where all nodes go if they have been assigned
            parent: parent of this branch. - only affects it if non-directed

            """

            if pos is None:
                pos = {root: (xcenter, vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)
            if len(children) != 0:
                dx = width / len(children)
                nextx = xcenter - width / 2 - dx / 2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                         vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                         pos=pos, parent=root)
            return pos

        return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
