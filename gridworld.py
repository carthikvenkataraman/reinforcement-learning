# Grid world program

import numpy as np

NUM_COLS = 4
NUM_ROWS = 4
GRID_START = (0,0)
GRID_END = (4,4)
ACTION_SET = ["up", "right", "down", "left"]

class Grid:
    def __init__(self):
        self.values = np.zeros([NUM_ROWS, NUM_COLS])
        self.current = GRID_START
    
    def isEndReached(self):
        if self.current == GRID_END:
            return True

    def update(self, action):
        print(self.current)
        print(action)
        if action == "up":
            self.current = (max(0,self.current[0]-1), self.current[1])
        elif action == "down":
            self.current = (min(NUM_ROWS, self.current[0]+1), self.current[1])
        elif action == "right":
            self.current = (self.current[0], min(NUM_COLS, self.current[1]+1))
        elif action == "left":
            self.current = (self.current[0], max(0, self.current[1]-1))
        else:
            print("Invalid action")

class Agent:
    def __init__(self):
        self.grid = Grid()
        self.action = self.chooseAction()

    def chooseAction(self):
        return np.random.choice(ACTION_SET)

    def play(self):
        while not self.grid.isEndReached():
            self.grid.update(self.chooseAction())

if __name__== "__main__":
    player = Agent()
    player.play()