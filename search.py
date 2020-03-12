# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    from util import Stack
    vertices = Stack()
    visited = []
    startState = problem.getStartState()
    vertices.push((startState, []))
    while not vertices.isEmpty():
        currentState, directions = vertices.pop()
        visited.append(currentState)
        if problem.isGoalState(currentState):
            return directions
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                vertices.push((successor[0], directions + [successor[1]]))
    return None
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    vertices = Queue()
    startState = problem.getStartState()
    vertices.push((startState, []))
    visited = [problem.getStartState()]
    while not vertices.isEmpty():
        currentState, directions = vertices.pop()
        if problem.isGoalState(currentState):
            return directions
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                visited.append(successor[0])
                vertices.push((successor[0], directions + [successor[1]]))
    return None

def uniformCostSearch(problem):
    from util import PriorityQueue
    priorityQueue = PriorityQueue()
    startState = problem.getStartState()
    cost = 0
    priorityQueue.push((startState, [],cost), cost)
    visited = []
    while not priorityQueue.isEmpty():
        currentState, directions, cost= priorityQueue.pop()
        if currentState not in visited:
            visited.append(currentState)
            if problem.isGoalState(currentState):
                return directions
            for successor in problem.getSuccessors(currentState):
                total_cost = cost + successor[2]
                priorityQueue.update((successor[0], directions + [successor[1]], total_cost), total_cost)
    return None
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priorityQueue = PriorityQueue()
    startState = problem.getStartState()
    cost = 0
    priorityQueue.push((startState, [], cost), cost)
    visited = []
    while not priorityQueue.isEmpty():
        currentState, directions, cost = priorityQueue.pop()
        if currentState not in visited:
            visited.append(currentState)
            if problem.isGoalState(currentState):
                return directions
            for successor in problem.getSuccessors(currentState):
                cummulative_cost = cost + successor[2]
                path_cost = cummulative_cost + heuristic(successor[0], problem)
                priorityQueue.update((successor[0], directions + [successor[1]], cummulative_cost), path_cost)
    return None
    # util.raiseNotDefined()
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
