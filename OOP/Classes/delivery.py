from geopy.distance import geodesic
import numpy as np
import osmnx as ox
import networkx as nx

class Delivery_Boy():
    
    def __init__(self):
        pass
    
    def distance_matrix(self,locations):
        nlocations = len(locations)
        matrix = np.zeros((nlocations,nlocations))
        graph = ox.graph_from_place("Viña del Mar, Chile", network_type="all_private")

        for i,origin in enumerate(locations):
            for j,destination in enumerate(locations):
                origin_node = ox.distance.nearest_nodes(graph, X=origin[1], Y=origin[0])
                destination_node = ox.distance.nearest_nodes(graph, X=destination[1], Y=destination[0])
                shortest_path = nx.shortest_path(graph, origin_node, destination_node, weight="length")
                total_length_meters = sum(ox.utils_graph.get_route_edge_attributes(graph, shortest_path, "length"))
                matrix[i,j] = total_length_meters
        return matrix

        

    def distance(self,l1,l2): #l1,l2 are tuples, latitude,longitude
        return geodesic(l1,l2).kilometers