'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    node: Any = field(compare=False)


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
        self.elapsed_time = 0.0
        self.nodes = 0

    # =======
    def statistics(self, curr_node):
        print('----------------------------')
        print('Elapsed time (s): {:.4f}'.format(self.elapsed_time))
        print('Solution found at depth: ', curr_node.depth)
        print('Number of nodes explored: ', self.nodes)
        print('Cost of solution: ', curr_node.cost)
        print('Estimated effective branching factor: ',
              self.nodes**(1 / curr_node.depth))
        print('----------------------------')
    # =======*

    def bfs(self, statistics=False, visited_states=True):
        self.nodes = 0
        start_time = time.process_time()
        frontier = queue.Queue()
        self.nodes += 1
        frontier.put(self.start)
        if visited_states:
            visitedStates = set()
            visitedStates.add(str(self.start.state.state))
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.goal_state():
                stop = True
                # =======
                self.elapsed_time = time.process_time() - start_time
                if statistics:
                    self.statistics(curr_node)
                # =======*
                return curr_node

            successors = curr_node.successor()
            while not successors.empty():
                successor = successors.get()
                if visited_states:
                    if str(successor.state.state) not in visitedStates:
                        frontier.put(successor)
                        # =======
                        self.nodes += 1
                        # =======*
                        visitedStates.add(str(successor.state.state))
                else:
                    frontier.put(successor)
                    # =======
                    self.nodes += 1
                    # =======*

    def dfs(self, statistics=False, visited_states=True, max_depth=None):
        self.nodes = 0
        start_time = time.process_time()

        frontier = []
        self.nodes += 1
        frontier.append(self.start)

        if visited_states:
            visitedStates = set()
            visitedStates.add(str(self.start.state.state))

        stop = False
        while not stop:
            if not frontier:
                return None
            curr_node = frontier.pop()
            if curr_node.goal_state():
                stop = True
                self.elapsed_time = time.process_time() - start_time
                if statistics:
                    self.statistics(curr_node)
                return curr_node
            elif max_depth != None and curr_node.depth > max_depth:
                continue

            successors = curr_node.successor()
            while not successors.empty():
                successor = successors.get()
                if visited_states:
                    if str(successor.state.state) not in visitedStates:
                        frontier.append(successor)
                        # =======
                        self.nodes += 1
                        # =======*
                        visitedStates.add(str(successor.state.state))
                else:
                    frontier.append(successor)
                    # =======
                    self.nodes += 1
                    # =======*

    def ids(self, statistics=False, visited_states=False):
        start_time = time.process_time()
        depth = 0
        while True:
            result = self.dfs(False, visited_states, depth)
            if result != None:
                self.elapsed_time = time.process_time() - start_time
                if statistics:
                    self.statistics(result)
                return result
            else:
                depth += 1

    def greedy_search(self, statistics=False, visited_states=True, heuristic_method='h1'):
        self.nodes = 0
        start_time = time.process_time()

        frontier = queue.PriorityQueue()
        self.nodes += 1
        if heuristic_method == 'h1':
            frontier.put(PrioritizedItem(
                self.start.state.h_1(self.start.state), self.start))
        else:
            frontier.put(PrioritizedItem(
                self.start.state.h_2(self.start.state), self.start))

        if visited_states:
            visitedStates = set()
            visitedStates.add(str(self.start.state.state))

        stop = False
        while not stop:
            if not frontier:
                return None
            curr_node = frontier.get().node
            if curr_node.goal_state():
                stop = True
                self.elapsed_time = time.process_time() - start_time
                if statistics:
                    self.statistics(curr_node)
                return curr_node

            successors = curr_node.successor()
            while not successors.empty():
                successor = successors.get()
                if visited_states:
                    if str(successor.state.state) not in visitedStates:
                        if heuristic_method == 'h1':
                            frontier.put(PrioritizedItem(
                                successor.state.h_1(successor.state), successor))
                        else:
                            frontier.put(PrioritizedItem(
                                successor.state.h_2(successor.state), successor))
                        # =======
                        self.nodes += 1
                        # =======*
                        visitedStates.add(str(successor.state.state))
                else:
                    if heuristic_method == 'h1':
                        frontier.put(PrioritizedItem(
                            successor.state.h_1(successor.state), successor))
                    else:
                        frontier.put(PrioritizedItem(
                            successor.state.h_2(successor.state), successor))
                    # =======
                    self.nodes += 1
                    # =======*

    def a_star(self, statistics=False, visited_states=True, heuristic_method='h1'):
        self.nodes = 0
        start_time = time.process_time()

        frontier = queue.PriorityQueue()
        self.nodes += 1
        if heuristic_method == 'h1':
            frontier.put(PrioritizedItem(
                self.start.state.h_1(self.start.state), self.start))
        else:
            frontier.put(PrioritizedItem(
                self.start.state.h_2(self.start.state), self.start))

        if visited_states:
            visitedStates = set()
            visitedStates.add(str(self.start.state.state))

        stop = False
        while not stop:
            if not frontier:
                return None
            curr_node = frontier.get().node
            if curr_node.goal_state():
                stop = True
                self.elapsed_time = time.process_time() - start_time
                if statistics:
                    self.statistics(curr_node)
                return curr_node

            successors = curr_node.successor()
            while not successors.empty():
                successor = successors.get()
                if visited_states:
                    if str(successor.state.state) not in visitedStates:
                        if heuristic_method == 'h1':
                            frontier.put(PrioritizedItem(
                                successor.state.h_1(successor.state) + successor.cost, successor))
                        else:
                            frontier.put(PrioritizedItem(
                                successor.state.h_2(successor.state) + successor.cost, successor))
                        # =======
                        self.nodes += 1
                        # =======*
                        visitedStates.add(str(successor.state.state))
                else:
                    if heuristic_method == 'h1':
                        frontier.put(PrioritizedItem(
                            successor.state.h_1(successor.state) + successor.cost, successor))
                    else:
                        frontier.put(PrioritizedItem(
                            successor.state.h_2(successor.state) + successor.cost, successor))
                    # =======
                    self.nodes += 1
                    # =======*
