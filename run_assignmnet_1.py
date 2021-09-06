'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
import time

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]


def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    start = time.process_time()
    goal_node = sa.bfs()
    end = time.process_time()
    print('goal state: ')
    goal_node.state.pretty_print()
    print('Time: ', end - start)
    goal_node.pretty_print_solution(verbose=True)
    print('DFS')
    print('Start state: ')
    mc.pretty_print()
    start = time.process_time()
    goal_node = sa.dfs()
    end = time.process_time()
    print('goal state: ')
    goal_node.state.pretty_print()
    print('Time: ', end - start)
    goal_node.pretty_print_solution(verbose=True)


if __name__ == "__main__":
    main()
