graph = {}
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}   # end of graph

infinity = float("inf") # represent infinity in Python
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = [] # to avoid processing the same nodes twice

def find_lowest_cost_node(costs):
    node = find_lowest_cost_node(costs) # find lowest cost nodes not processed yet
    while node is not None: # will complete if all nodes are processed
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # go through neighbors of node
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # if cheaper for this node
                costs[n] = new_cost # update cost with cheaper option
                parents[n] = node   # this node is now parent
        processed.append(node)  # mark node as processed
        node = find_lowest_cost_node(costs) # find next node to process