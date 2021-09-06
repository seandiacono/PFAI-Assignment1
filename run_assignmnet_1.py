'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]


def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs(statistics=True, visited_states=True)
    print('goal state: ')
    goal_node.state.pretty_print()
    # goal_node.pretty_print_solution(verbose=True)
    # print('DFS')
    # print('Start state: ')
    # mc.pretty_print()
    # goal_node = sa.dfs(statistics=True, visited_states=True)
    # print('goal state: ')
    # goal_node.state.pretty_print()
    print('IDS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.ids(statistics=False, visited_states=True)
    print('goal state: ')
    goal_node.state.pretty_print()
    # goal_node.pretty_print_solution(verbose=True)


if __name__ == "__main__":
    main()
