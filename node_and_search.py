'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue


class Node:
    '''
    This class defines nodes in search trees. It keep track of: 
    state, cost, parent, action, and depth 
    '''

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def goal_state(self):
        return self.state.check_goal()

    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:
            child = self.state.move(action)
            if child != None:
                childNode = Node(child, self.cost + 1, self, action)
                successors.put(childNode)
        return successors

    def pretty_print_solution(self, verbose=False):
        if self.parent != None:
            self.parent.pretty_print_solution(verbose)

        if verbose:
            self.state.pretty_print()
        print("action: " + str(self.action))

        return


class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''

    def __init__(self, problem):
        self.start = Node(problem)
        self.visitedStates = set()

    def bfs(self):
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.goal_state():
                stop = True
                # Statistics print
                return curr_node

            successors = curr_node.successor()
            while not successors.empty():
                successor = successors.get()
                if successor.state not in self.visitedStates:
                    frontier.put(successor)
                    self.visitedStates.add(successor.state)
