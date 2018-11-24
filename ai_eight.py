import node
import algorithms

start_layout = node.input_layout("Enter starting layout: ")
target_layout = node.input_layout("Enter target layout: ")
start_node = node.Node(start_layout, target_layout)
target_node = node.Node(target_layout, target_layout, level=10000)
print("\nChoose algorithm:")
print("1 - Manhattan ways")
print("2 - Tiles not on their position")
if input() == "1":
    algorithms.find_solution_informed_manhattan(start_node, target_node)
else:
    algorithms.find_solution_informed_tiles(start_node, target_node)