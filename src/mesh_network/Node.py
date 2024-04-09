import uuid
import time
from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            neighbor.neighbors.append(self)

    def send_message(self, message, origin=None):
        print(f"Node {self.name} received message: {message}")
        for neighbor in self.neighbors:
            if neighbor is not origin:
                neighbor.send_message(message, origin=self)

class MeshNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def display_network(self):
        for node in self.nodes:
            print(f"Node {node.name} with neighbors: {[neighbor.name for neighbor in node.neighbors]}")

# Example usage
if __name__ == "__main__":
    # Creating nodes
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    # Adding nodes to the mesh network
    mesh_network = MeshNetwork()
    mesh_network.add_node(node_a)
    mesh_network.add_node(node_b)
    mesh_network.add_node(node_c)
    mesh_network.add_node(node_d)

    # Connecting nodes
    node_a.add_neighbor(node_b)
    node_b.add_neighbor(node_c)
    node_c.add_neighbor(node_d)
    node_d.add_neighbor(node_a)  # Creating a simple loop for demonstration

    # Displaying the network
    mesh_network.display_network()

    # Sending a message through the network
    print("\nSending a message from Node A through the mesh network:")
    node_a.send_message("Hello, HyperMesh!")
