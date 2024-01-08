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
from prompt_toolkit.search import SearchState

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
    return [s, s, w, s, w, w, s, w]


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
    "*** YOUR CODE HERE ***"

    #    print("Start:", problem.getStartState())
    #    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    def dfs_helper(currentNode, visited):
        node_stack = util.Stack()
        node_stack.push(currentNode)

        while not node_stack.isEmpty():
            current_node = node_stack.pop()
            current_state = current_node[0]
            current_direction = current_node[1]

            if problem.isGoalState(current_state):
                return [current_direction]

            for element in reversed(problem.getSuccessors(current_state)):
                state, direction, distance = element
                if state not in visited and element not in [node for node in node_stack.list]:
                    # print(state, direction, distance)
                    visited.add(state)
                    node_stack.push(element)
                    result = dfs_helper(element, visited)
                    if result:
                        # print("ENDE::::: ", [direction] + result)
                        return [direction] + result

    # [State(x,y), direction, value], start,state
    return dfs_helper((problem.getStartState(), '', 0), {problem.getStartState()})


'''
    
    nodes_stack = util.Stack()

    visited_fields = set()

    visited_fields.add(problem.getStartState())

    nodes_stack.push(problem.getSuccessors(problem.getStartState())[0])
    visited_fields.add(problem.getStartState())

    while len(visited_fields) > 0 or not problem.isGoalState(visited_fields.pop()):

        for element in nodes_stack.list:
            print("ELEMENT", element)
            state, direction, distance = element
            if element not in nodes_stack.list:
                nodes_stack.push(element)
            if problem.isGoalState(state):
                return True
            print(len(visited_fields))
            while len(nodes_stack.list) > 0:
                if state not in visited_fields:
                    print("state ", state)
                    visited_fields.add(state)
                    print("visited_fields ", visited_fields)
                    node = nodes_stack.pop()
                    note_nigh = problem.getSuccessors(state)
                    print("note_nigh ", note_nigh)
                    print("length 1", len(nodes_stack.list))
                    visited_fields.add(node[0])

                    return [direction]
                else:
                    print("length 2", len(nodes_stack.list))
'''

'''
    Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    (x,y) Richtung, 1
    

    if problem.isGoalState(problem.getStartState()):
        return True
    else:
        nodes_stack.push(problem.getStartState())
        if problem.getStartState() not in visited_fields:
            visited_fields.add(problem.getStartState())
        for element in problem.getSuccessors(problem.getStartState()):
            print("ELEMENT", element)
            nodes_stack.push(element)
            state, direction, distance = element
            if state not in visited_fields:
                visited_fields.add(state)
                return depthFirstSearch(state)

        else:
            return False
    '''

    # while len(nodes_stack.list) > 0:

    # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
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
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
