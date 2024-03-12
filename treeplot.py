import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("Root")
G.add_node("Child1")
G.add_node("Child2")
G.add_node("Grandchild1")
G.add_node("Grandchild2")

# Add edges
G.add_edge("Root", "Child1")
G.add_edge("Root", "Child2")
G.add_edge("Child1", "Grandchild1")
G.add_edge("Child1", "Grandchild2")

# Draw the graph
pos = nx.spring_layout(G)  # Positions nodes using the spring layout algorithm
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")

# Show plot
plt.title("Tree Plot Example")
plt.show()
