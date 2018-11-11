import node
import algorithms

start_layout = node.input_layout("Enter starting layout: ")
target_layout = node.input_layout("Enter target layout: ")
start_node = node.Node(start_layout, target_layout)
target_node = node.Node(target_layout, target_layout, level=10000)
algorithms.find_solution_informed(start_node, target_node)
