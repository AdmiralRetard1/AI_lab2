import math


# class for node
class Node(object):

    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, target_layout, old_node=None, level=0, ):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost(target_layout, new_layout, old_node)
        self.prev_node_layout = old_node.layout if old_node else None

    # function to print layout
    def __repr__(self):
        r_val = ""
        for i in [0, 3, 6]:
            r_val += "\n" + ("".join(self.layout[i] + self.layout[i + 1] + self.layout[i + 2]))
        return r_val

    # redefined equality function
    def __eq__(self, comp_node):
        return True if self.layout == comp_node.layout else False


# class for 2nd euristic
class Node2(Node):
    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, target_layout, old_node=None, level=0, ):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost2(target_layout, new_layout, old_node)
        self.prev_node_layout = old_node.layout if old_node else None


# list class expansion to represent nodes
class NodeList(list):

    # magic function to use in "in" clause
    def __contains__(self, key):
        layouts = (o.layout for o in self)
        return key.layout in layouts


# function that counts the cost of way of current node
def count_cost(target_layout, new_layout, old_node=None):
    sum_of_moves = 0
    for n in new_layout:
        sum_of_moves += abs(new_layout.index(n) % 3 - target_layout.index(n) % 3) + \
                        abs(new_layout.index(n) // 3 - target_layout.index(n) // 3)
    way_cost = old_node.level + old_node.wayCost + sum_of_moves if old_node else 0
    return way_cost


# function that counts the cost of way of current node
def count_cost2(target_layout, new_layout, old_node=None):
    counter = 0
    for n in new_layout:
        if new_layout.index(n) != target_layout.index(n):
            counter += 1
    way_cost = old_node.wayCost + counter if old_node else 0
    return way_cost


# function to check correctness of input
def input_layout(message):
    while True:
        layout = input(message)
        if (len(layout) != 8) and (len(layout) != 9):
            print("Invalid number of elements! Please enter again")
        else:
            # checking uniqueness
            checked = ""
            legal = True
            for ch in layout:
                if ch not in checked:
                    checked += ch
                else:
                    print("Numbers should not repeat! Try again")
                    legal = False
                    break
            # if everything is ok, check if we have only 8 elements - then the last is empty and we need
            # to fill it with space
            if legal:
                if len(layout) == 8:
                    layout += " "
                break
    return layout


# universal func to print our lists without braces and with wayCost under layout
def print_nodes(lst):
    lines = ["", "", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            digits = getCountOfDigits(n.wayCost)
            lines[0] += n.layout[:3] + " " * (digits + 1)
            lines[1] += n.layout[3:6] + " " * (digits + 1)
            lines[2] += n.layout[6:] + " " * (digits + 1)
            lines[3] += "w:{}".format(n.wayCost) + " " * 2
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


# this does the same as previou function, but without wayCost
def print_list(lst):
    lines = ["", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            lines[0] += n[:3] + "  "
            lines[1] += n[3:6] + "  "
            lines[2] += n[6:] + "  "
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


def getCountOfDigits(number):
    return 1 if number == 1 or number == 0 else round(math.log10(number) + 0.50000001)
