from ortools.constraint_solver import pywrapcp
import numpy as np
import osmnx as ox
import networkx as nx
from ortools.constraint_solver import routing_enums_pb2


class TSP():

    def preprocessing(self,addresses):
        locations = []
        for address in addresses:
            locations.append(ox.geocode(address))
        nlocations = len(locations)
        matrix = np.zeros((nlocations,nlocations))
        graph = ox.graph_from_place("Viña del Mar, Chile", network_type="all_private")

        for i,origin in enumerate(locations):
            for j,destination in enumerate(locations):
                origin_node = ox.distance.nearest_nodes(graph, X=origin[1], Y=origin[0])
                destination_node = ox.distance.nearest_nodes(graph, X=destination[1], Y=destination[0])
                shortest_path = nx.shortest_path(graph, origin_node, destination_node, weight="length")
                total_length_meters = sum(ox.utils_graph.get_route_edge_attributes(graph, shortest_path, "length"))
                matrix[i,j] = int(total_length_meters)
        return matrix

    def create_data_model(self,distances):
        data = {}
        data["distance_matrix"] = distances
        data["num_vehicles"] = 1
        data["depot"] = 0
        return data

    def solve(self,addresses):
        distances = self.preprocessing(addresses)
        data = self.create_data_model(distances)
        manager = pywrapcp.RoutingIndexManager(len(data["distance_matrix"]), data["num_vehicles"], data["depot"])
        routing = pywrapcp.RoutingModel(manager)
        
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]


        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            return self.process_solution(manager, routing, solution)
        else:
            return None
        
    def process_solution(self, manager, routing, solution):
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            index = solution.Value(routing.NextVar(index))
        return route