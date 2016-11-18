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


def graphSearch(problem, frontier):
    
    '''
    General search function that implements graph search. The frontier that
    is passsed determines the kind of search to be carried on
    '''
    
    #Elements will have the format state: [position, action, cost, pathToCurrentNode]
    explored = []
    
    startNode = problem.getStartState()
    frontier.push([startNode,"Stop",0, []])
    
    while(not frontier.isEmpty()):
        
        searchNode = frontier.pop()
        state = searchNode[0]
        path = searchNode[-1]
        
        #if goal is fulfilled return the path
        if(problem.isGoalState(state)):
            return path
        
        if(state not in explored):
            explored.append(state)
            
            #for every syccessor we append their whole state plus the path
            #to reach it (list of actions to that node)
            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    successorPath = path[:]
                    successorPath.append(successor[1])
                    state = successor[0]
                    action = successor[1]
                    cost = successor[2]
                    frontier.push([state,action,cost,successorPath])
                    
    return []
    

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
    "*** YOUR CODE HERE ***"
    
    #Initilize an empty frontier stack.
    frontier = util.Stack()
    #call graphSearch with a stack frontier
    return graphSearch(problem, frontier)
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Initialize the frotier with a PriorityQueue
    #Priority is determined by the length of the path array leading to 
    #that particular node. Path is in the state of the agent as an array
    #the shorter the path the hgiher the priority
    frontier = util.PriorityQueueWithFunction(len)
    
    #call the general search with a priority queue frontier
    return graphSearch(problem,frontier)


    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    #function to be used for calculating the priority
    #it get the cost of the path of the node which can be accessed through
    #the state of the node
    def priorityFunction(item):
        return problem.getCostOfActions(item[-1])   
    
    #create a frontier with a PQ with the specified function
    #the less costly the path to the node, the higher its priority
    frontier = util.PriorityQueueWithFunction(priorityFunction)
    
    return graphSearch(problem, frontier)   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    #function that returns the cost of the path to the node plus the 
    #hueristic associated with the node
    def priorityFunction(item):
        return problem.getCostOfActions(item[-1]) + heuristic(item[0], problem)
    
    #create a frontier with the PR
    #the shorter cost+heursitic of the path, the higher the priority
    frontier = util.PriorityQueueWithFunction(priorityFunction)
    return graphSearch(problem, frontier)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
