import math


# class for node
class Node(object):

    # class constructor
    def __init__(self, new_layout, target_layout, old_node_layout=None, level=0):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost(target_layout, new_layout, self.level)
        self.prev_node_layout = old_node_layout if old_node_layout else None

    # function to print layout
    def __repr__(self):
        r_val = ""
        for i in [0, 3, 6]:
            r_val += "\n" + ("".join(self.layout[i] + self.layout[i + 1] + self.layout[i + 2]))
        return r_val

    # redefined equality function
    def __eq__(self, comp_node):
        return True if self.layout == comp_node.layout else False


# class for 2nd heuristic
class Node2(Node):
    # function to enter layout with checking it for uniqueness and fullness
    def __init__(self, new_layout, target_layout, old_node_layout=None, level=0, ):
        self.layout = new_layout
        self.level = level
        # cost to move 1 tile compared to previous layout
        self.wayCost = count_cost2(target_layout, new_layout, self.level)
        self.prev_node_layout = old_node_layout if old_node_layout else None


# list class expansion to represent nodes
class NodeList(list):

    # magic function to use in "in" clause
    def __contains__(self, key):
        layouts = (o.layout for o in self)
        return key.layout in layouts


# function that counts the cost of way of current node
def count_cost(target_layout, new_layout, level=0):
    sum_of_moves = 0
    for n in new_layout:
        sum_of_moves += abs(new_layout.index(n) % 3 - target_layout.index(n) % 3) + \
                        abs(new_layout.index(n) // 3 - target_layout.index(n) // 3)
    way_cost = sum_of_moves + level
    return way_cost


# function that counts the cost of way of current node (second way)
def count_cost2(target_layout, new_layout, level=0):
    counter = 0
    for n in new_layout:
        if new_layout.index(n) != target_layout.index(n):
            counter += 1
    way_cost = counter + level
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
    lines = ["", "", "", "", ""]
    res = ""
    if lst:
        nodeCounter = 0
        for n in lst:
            digits1 = getCountOfDigits(n.wayCost - n.level)
            digits2 = getCountOfDigits(n.level)
            maxnum = max(digits1, digits2)
            lines[0] += n.layout[:3] + " " * (maxnum + 1)
            lines[1] += n.layout[3:6] + " " * (maxnum + 1)
            lines[2] += n.layout[6:] + " " * (maxnum + 1)
            if digits1 == digits2:
                lines[3] += "g:{}".format(n.level) + " " * 2
                lines[4] += "h:{}".format(n.wayCost - n.level) + " " * 2
            else:
                lines[3] += "g:{}".format(n.level) + " " * (1 + digits1)
                lines[4] += "h:{}".format(n.wayCost - n.level) + " " * (1 + digits2)
            nodeCounter += 1
            if nodeCounter == 30:
                res += "\n".join(lines) + "\n\n"
                lines = ["", "", "", "", ""]
                nodeCounter = 0
        res += "\n".join(lines)
        print(res)
    else:
        print("Empty list")


# this does the same as previous function, but without wayCost
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
