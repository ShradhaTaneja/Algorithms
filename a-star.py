graph = {
        'S' : [('A', 1), ('B', 4)],
        'A' : [('B', 2), ('C', 5), ('D', 12)],
        'B' : [('C', 2)],
        'C' : [('D', 3)],
        'D' : []
        }

heuristics = {
        'S' : 7,
        'A' : 6,
        'B' : 2,
        'C' : 1,
        'D' : 0
        }

class priority_queue():
    def __init__(self):
        self.items = []

    def pop(self):
        sorted_items = sorted(self.items, key = lambda x:x[1])
#        print 'sorted is : ', sorted_items
        min_value = sorted_items.pop(0)
#        print 'min value is : ', min_value
        self.items = sorted_items
#        print 'new items ', self.items
        return min_value

    def insert(self, value):
        self.items.append(value)
        return self.items

    def get(self):
        return self.items

    def is_empty(self):
        return len(self.items) == 0

    def len(self):
        return len(self.items)


def get_children(graph, node):
    children = []
    for child in graph[node]:
        children.append(child[0])
    return children

def get_cost(graph, start, end):
#    print '>>>>>>>>> cost : ', start, '-', end
    if start == end:
        return 0
    for children in graph[start]:
        if children[0] == end:
#            print '=', children[1]
            return children[1]
    return None

def get_manhattan_distance(graph, path):
#    path = ['S', 'A', 'B', 'C', 'D']
#    print '\n \n _____________inside path cost = ', path
#    print 'getting cost for path = ', path
    total_cost = 0
    for index, node in enumerate(path):
#        print path[index], path[index+1], ' !!!!!!!!!!!!!!!!!!!!!! gonna get path cost for this'
        if (index+1 < len(path)):
#            print '%s(%d) - %s(%d)'% (path[index], index, path[index+1], index+1), get_cost(graph, path[index], path[index+1])
#            print path[index], path[index+1], '@@'
            total_cost += get_cost(graph, path[index], path[index+1])
#        print total_cost

#    print 'returning ; ', total_cost
    return total_cost




def a_star(graph, heuristics, start, end):
    open_paths = priority_queue()
    used_paths = priority_queue()
    goal_paths = priority_queue()

#    open_paths.insert(2)
#    open_paths.insert(3)
#    open_paths.insert(0)
#    open_paths.insert(40)
#    print open_paths.pop()

    start_node = ([start], heuristics[start[-1]])
    open_paths.insert(start_node)

    while (not open_paths.is_empty()):
        current_value = open_paths.pop()

        used_paths.insert(current_value)
        current_path = current_value[0]
#        print '\n popped out ________', current_path
        last_visited_node = current_path[-1]

        for child in get_children(graph, last_visited_node):
#            print ' >> CHILD ------------------------------------------------ ', child
            new_path = current_path + [child]
            new_path_cost = get_manhattan_distance(graph, new_path)
            new_total_cost = new_path_cost + heuristics[child]
            print '-'.join(new_path), ' (' , new_path_cost, ' + ', heuristics[child], ' ) = ', new_total_cost
            new_data = (new_path, new_total_cost)
            open_paths.insert(new_data)
            if end in new_path:
                goal_paths.insert(new_data)

#    print used_paths.get(), '-- used paths', used_paths.len()
#    print goal_paths.get(), '-- goal paths '
#    print open_paths.get(), '-- open paths'

    shortest_path = goal_paths.pop()
    print '\n Total Paths evaluated : ', used_paths.len()
    print '\n \n Shortest Path : ', '-'.join(shortest_path[0]), ' Cost : ', shortest_path[1]


a_star(graph, heuristics, 'S', 'D')
