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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    perimeter = util.Stack()
    visited = set()

    perimeter.push((problem.getStartState(), [])) # [] = Aktionsliste, um zur Node zu kommen

    while len(perimeter.list) > 0: # perimeter.isEmpty ist bei mir irgendwie immer true
        currentFrom, actionList = perimeter.pop()

        if problem.isGoalState(currentFrom):
            return actionList

        if currentFrom not in visited:
            for successor, action, distance in problem.getSuccessors(currentFrom):
                if successor not in visited:
                    nextActions = actionList + [action]
                    perimeter.push((successor, nextActions))
            visited.add(currentFrom)

    return [] # Keine Lösung gefunden: Return Leere Aktionsliste

def depthFirstSearchRecursive(problem : SearchProblem, currentNode, visited, actions):
    if problem.isGoalState(currentNode):
        if problem.isGoalState(problem.getStartState()):
            return actions
        actions.insert(0, currentNode[1]) # current Richtung an erster Stelle einfügen (gehen rekursiv zurück)
        return

    visited.add(currentNode)

    for successor, action, distance in problem.getSuccessors(currentNode):
        if successor not in visited:
            depthFirstSearchRecursive(problem, successor, visited, actions)

    return actions

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    perimeter = util.Queue()
    visited = set()

    perimeter.push((problem.getStartState(), []))
    visited.add(problem.getStartState())

    while len(perimeter.list) > 0:
        currentFrom, actionList = perimeter.pop()

        if problem.isGoalState(currentFrom):
            return actionList # Kann leer sein, wenn Start = Ziel

        for successor, action, distance in problem.getSuccessors(currentFrom):
            currentTo = successor
            if currentTo not in visited:
                nextAction = actionList + [action]
                perimeter.push((currentTo, nextAction))
                visited.add(currentTo)

    return [] # Wenn kein Pfad gefunden wird

def breadthFirstSearchRecursive():
    """ WORK IN PROGRESS """
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
bfsr = breadthFirstSearchRecursive
dfs = depthFirstSearch
dfsr = depthFirstSearchRecursive
astar = aStarSearch
ucs = uniformCostSearch