def solve(self, algorithm='DFS'):
    """Finds a solution to maze, if one exists."""
    self.num_explored = 0
    start = Node(state=self.start, parent=None, action=None)

    # Choose the appropriate frontier based on the algorithm
    if algorithm == 'DFS':
        frontier = StackFrontier()
    elif algorithm == 'BFS':
        frontier = QueueFrontier()
    else:
        raise Exception("Invalid algorithm specified")

    frontier.add(start)
    self.explored = set()

    while True:
        if frontier.empty():
            raise Exception("no solution")

        node = frontier.remove()
        self.num_explored += 1

        if node.state == self.goal:
            actions = []
            cells = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            self.solution = (actions, cells)
            return

        self.explored.add(node.state)

        for action, state in self.neighbors(node.state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)