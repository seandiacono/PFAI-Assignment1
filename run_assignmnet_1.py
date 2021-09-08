'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
from eight_puzzle import EightPuzzle

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]

init_state_8puzzle = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state_8puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]


def main():
    mc = MissionariesAndCannibals(init_state, goal_state)
    sa = SearchAlgorithm(mc)
    print('BFS')
    print('Start state: ')
    mc.pretty_print()
    goal_node = sa.bfs(statistics=True, visited_states=False)
    print('goal state: ')
    goal_node.state.pretty_print()
    # goal_node.pretty_print_solution(verbose=True)
    # print('DFS')
    # print('Start state: ')
    # mc.pretty_print()
    # goal_node = sa.dfs(statistics=True, visited_states=True)
    # print('goal state: ')
    # goal_node.state.pretty_print()
    # print('IDS')
    # print('Start state: ')
    # mc.pretty_print()
    # goal_node = sa.ids(statistics=True, visited_states=True)
    # print('goal state: ')
    # goal_node.state.pretty_print()
    # goal_node.pretty_print_solution(verbose=True)

    eight_puzzle = EightPuzzle(init_state_8puzzle, goal_state_8puzzle)
    sa = SearchAlgorithm(eight_puzzle)
    # print('8-Puzzle Greedy Search')
    # print('Start state:')
    # eight_puzzle.pretty_print()
    # goal_node = sa.greedy_search(
    #     statistics=True, visited_states=True, heuristic_method='h_2')
    # print('Goal state: ')
    # goal_node.state.pretty_print()

    # print('8-Puzzle BFS')
    # print('Start state:')
    # eight_puzzle.pretty_print()
    # goal_node = sa.bfs(
    #     statistics=True, visited_states=True)
    # print('Goal state: ')
    # goal_node.state.pretty_print()

    print('8-Puzzle A*')
    print('Start state:')
    eight_puzzle.pretty_print()
    goal_node = sa.a_star(
        statistics=True, visited_states=True, heuristic_method='h_2')
    print('Goal state: ')
    goal_node.state.pretty_print()


if __name__ == "__main__":
    main()
