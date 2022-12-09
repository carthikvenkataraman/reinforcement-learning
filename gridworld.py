# Grid world program

import numpy as np

NUM_COLS = 4
NUM_ROWS = 4
GRID_START = (1,2)
GRID_TERMINAL = [(0,0), (3,3)]
ACTION_SET = ["up", "right", "down", "left"]

class Grid:
    def __init__(self):
        self.values = np.zeros([NUM_ROWS, NUM_COLS])
        self.current = GRID_START
    
    def isEndReached(self):
        if self.current in GRID_TERMINAL:
            return True
        
    def getNextPosition(self, state, action):
        nextPosition = state
        
        if state in GRID_TERMINAL:
            return nextPosition
        
        if action == "up":
            nextPosition = (max(0, state[0]-1), state[1])
        elif action == "down":
            nextPosition = (min(NUM_ROWS-1, state[0]+1), state[1])
        elif action == "right":
            nextPosition = (state[0], min(NUM_COLS-1, state[1]+1))
        elif action == "left":
            nextPosition = (state[0], max(0, state[1]-1))
        else:
            print("Invalid action")
        self.current = nextPosition
        return nextPosition

    def updateValues(self, rewardPerStep):
        probEachAction = 0.25
        newValues = self.values.copy()
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                updatedValue = 0.0                
                if (row, col) in GRID_TERMINAL:
                    reward = 0.0
                else:
                    reward = rewardPerStep
                for action in ACTION_SET:
                    destPosition = self.getNextPosition((row, col), action)
                    updatedValue += probEachAction * (reward + self.values[destPosition])
                newValues[row, col] = updatedValue
        self.values = newValues
        print(self.values)

class Agent:
    def __init__(self):
        self.grid = Grid()
        self.action = self.chooseAction()

    def chooseAction(self):
        return np.random.choice(ACTION_SET)

    def autoplay(self):
        while not self.grid.isEndReached():
            p = self.grid.getNextPosition(self.grid.current, self.chooseAction())
            print(p)

    def evaluatePolicy(self):
        rewardPerStep = -1
        for _ in range(10):
            self.grid.updateValues(rewardPerStep)

if __name__== "__main__":
    player = Agent()
    #player.autoplay()
    player.evaluatePolicy()