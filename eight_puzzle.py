from copy import deepcopy


class EightPuzzle():

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.position = [1, 1]
        self.goal = goal
        self.action = ["up", "down", "left", "right"]
        self.no_of_tiles = 0.0
        self.manhattan_dist = 0.0

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    # Number of tiles
    def h_1(self, puzzle):
        return len([j for i, j in zip([item for sublist in self.goal for item in sublist], [
            item for sublist in puzzle.state for item in sublist]) if (i != j and j != 'e' and i != 'e')])

    # Manhattan Distance
    def h_2(self, puzzle):
        dist = 0
        for i in range(0, len(puzzle.state)):
            for j in range(0, len(puzzle.state[i])):
                num = puzzle.state[i][j]
                if (num != 'e'):
                    goal_x = num // 3
                    goal_y = num % 3
                    dist_x = i - goal_x
                    dist_y = j - goal_y
                    dist = dist + abs(dist_x) + abs(dist_y)
        return dist

    def move(self, move):
        if move == "up":
            dc = deepcopy(self)
            if dc.up():
                return dc
        elif move == "down":
            dc = deepcopy(self)
            if dc.down():
                return dc
        elif move == "left":
            dc = deepcopy(self)
            if dc.left():
                return dc
        elif move == "right":
            dc = deepcopy(self)
            if dc.right():
                return dc

    def up(self):
        if self.position[0] != 0:
            # Update number
            self.state[self.position[0]][self.position[1]
                                         ] = self.state[self.position[0] - 1][self.position[1]]
            # Update e
            self.state[self.position[0] - 1][self.position[1]] = 'e'
            # Update position of e
            self.position[0] -= 1

            return True

    def down(self):
        if self.position[0] != 2:
            # Update number
            self.state[self.position[0]][self.position[1]
                                         ] = self.state[self.position[0] + 1][self.position[1]]
            # Update e
            self.state[self.position[0] + 1][self.position[1]] = 'e'
            # Update position of e
            self.position[0] += 1

            return True

    def left(self):
        if self.position[1] != 0:
            # Update number
            self.state[self.position[0]][self.position[1]
                                         ] = self.state[self.position[0]][self.position[1] - 1]
            # Update e
            self.state[self.position[0]][self.position[1] - 1] = 'e'
            # Update position of e
            self.position[1] -= 1

            return True

    def right(self):
        if self.position[1] != 2:
            # Update number
            self.state[self.position[0]][self.position[1]
                                         ] = self.state[self.position[0]][self.position[1] + 1]
            # Update e
            self.state[self.position[0]][self.position[1] + 1] = 'e'
            # Update position of e
            self.position[1] += 1

            return True

    def pretty_print(self):
        print('--------------')
        print(self.state[0][0], ' | ', self.state[0]
              [1], ' | ', self.state[0][2])
        print('--------------')
        print(self.state[1][0], ' | ', self.state[1]
              [1], ' | ', self.state[1][2])
        print('--------------')
        print(self.state[2][0], ' | ', self.state[2]
              [1], ' | ', self.state[2][2])
        print('--------------')
