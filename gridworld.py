# Grid world program

import numpy as np

NUM_COLS = 4
NUM_ROWS = 4
GRID_START = (0,0)
GRID_END = (3,3)
TERMINAL_STATES = [(0,0), (3,3)]
ACTION_SET = ["up", "right", "down", "left"]

class Grid:
    def __init__(self):
        self.values = np.zeros([NUM_ROWS, NUM_COLS])
        self.current = GRID_START
    
    def isEndReached(self):
        if self.current == GRID_END:
            return True

    def getNextPosition(self, state, action):
        nextPosition = state
        if action == "up":
            nextPosition = (max(0,self.current[0]-1), self.current[1])
        elif action == "down":
            nextPosition = (min(NUM_ROWS-1, self.current[0]+1), self.current[1])
        elif action == "right":
            nextPosition = (self.current[0], min(NUM_COLS-1, self.current[1]+1))
        elif action == "left":
            nextPosition = (self.current[0], max(0, self.current[1]-1))
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
                for action in ACTION_SET:
                    destPosition = self.getNextPosition((row, col), action)
                    updatedValue += probEachAction * (rewardPerStep + self.values[destPosition])
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
            self.grid.getNextPosition(self.grid.current, self.chooseAction())

    def evaluatePolicy(self):
        rewardPerStep = -1
        for _ in range(1):
            self.grid.updateValues(rewardPerStep)

if __name__== "__main__":
    player = Agent()
    player.autoplay()
    #player.evaluatePolicy()