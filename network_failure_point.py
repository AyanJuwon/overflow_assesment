class Node:
    # this represents a router
    def __init__(self, label):
        self.label = label
        self.inbound_links = 0
        self.outbound_links = 0

    def __repr__(self):
        return str(self.label)


class DirectedGraph:
    # connection graph
    def __init__(self):
        self.nodes = {}

    def add_node(self, label):
        node = Node(label)
        self.nodes[label] = node

    def add_connection(self, start, end):
        self.nodes[start].outbound_links += 1
        self.nodes[end].inbound_links += 1

    def identify_critical_router(self):
        max_connections = 0
        max_routers = []

        for label, node in self.nodes.items():
            total_connections = node.inbound_links + node.outbound_links
            if total_connections > max_connections:
                max_connections = total_connections
                max_routers = [node.label]
            elif total_connections == max_connections:
                max_routers.append(node.label)

        return max_routers


# Test cases
graph1 = DirectedGraph()
graph1.add_node(1)
graph1.add_node(2)
graph1.add_node(3)
graph1.add_node(5)
graph1.add_connection(1, 2)
graph1.add_connection(2, 3)
graph1.add_connection(3, 5)
graph1.add_connection(5, 2)
graph1.add_connection(2, 1)
print("Test case 1:", graph1.identify_critical_router())

graph2 = DirectedGraph()
graph2.add_node(1)
graph2.add_node(2)
graph2.add_node(3)
graph2.add_node(5)
graph2.add_node(6)
graph2.add_node(4)
graph2.add_connection(1, 3)
graph2.add_connection(3, 5)
graph2.add_connection(5, 6)
graph2.add_connection(6, 4)
graph2.add_connection(4, 5)
graph2.add_connection(5, 2)
graph2.add_connection(2, 6)
print("Test case 2:", graph2.identify_critical_router())

graph3 = DirectedGraph()
graph3.add_node(2)
graph3.add_node(4)
graph3.add_node(6)
graph3.add_node(5)
graph3.add_connection(2, 4)
graph3.add_connection(4, 6)
graph3.add_connection(6, 2)
graph3.add_connection(2, 5)
graph3.add_connection(5, 6)
print("Test case 3:", graph3.identify_critical_router())
