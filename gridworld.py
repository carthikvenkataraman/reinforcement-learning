# Grid world program

import numpy as np

NUM_COLS = 4
NUM_ROWS = 4
GRID_START = (1,2)
GRID_TERMINAL = [(0,0), (3,3)]
ACTION_SET = ["up", "right", "down", "left"]
REWARD_PER_STEP = -1
GAMMA = 1.0

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

    def getPolicy(self, action):
        if action in ACTION_SET:
            policy = 1/len(ACTION_SET)
        return policy

    def getValue(self, state):
        return self.values[state]

    def getActionValue(self, state, action):
        return self.getReward(state) + GAMMA * self.getValue(self.getNextPosition(state, action))

    def getReward(self, state):
        if state in GRID_TERMINAL:
            reward = 0.0
        else:
            reward = REWARD_PER_STEP
        return reward

    def getAction(self, state):
        maxActionValue = -float("inf")
        optimalAction = ACTION_SET[0]
        for action in ACTION_SET:
            actionValue = self.getActionValue(state, action)
            if actionValue >= actionValue:
                maxActionValue = actionValue
                optimalAction = action
        return optimalAction

    def evaluatePolicy(self):
        newValues = self.values.copy()
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                state = (row, col)
                updatedValue = 0.0                
                for action in ACTION_SET:
                    updatedValue += self.getPolicy(action) * self.getActionValue(state, action)
                newValues[row, col] = updatedValue
        self.values = newValues
        print(self.values)

    #def iterateValues(self):

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
        for _ in range(10):
            self.grid.evaluatePolicy()

if __name__== "__main__":
    player = Agent()
    #player.autoplay()
    player.evaluatePolicy()