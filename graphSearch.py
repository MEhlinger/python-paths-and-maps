###########################
# GRAPH SEARCH ALGORITHMS #
###########################

# Written by Marshall Ehlinger
# Based on the tutorials @ redblobgames.com
# Includes A* for pathfinding and Breadth-First for procedural generation, etc

###########
# IMPORTS #
###########

from binaryHeap import *
from gridConstruction import *

#############
# FUNCTIONS #
#############

def fScore(activeNode, goalNode, gScore):
	# Determines heuristic first (hscore)
	deltaX = abs(goalNode[0] - activeNode[0])
	deltaY = abs(goalNode[1] - activeNode[1])
	hScore =  (deltaX + deltaY)
	return gScore + hScore



def breadthFirst(graph, start, expandDistance):
	# Expand distance is how many steps away from start the algorithm will traverse.
	# This particular implementation returns all traversed nodes as dict 'node' : distance. 
	# Optimized for procedural map generation.
	frontier = BinHeap()
	distance = {}
	distance[start] = 0
	frontier.insert((start, distance[start]))

	currentNode = start
	while distance[currentNode] <= expandDistance and not frontier.empty():
		currentNode = frontier.delMin()[0]
		for next in graph.neighbors(currentNode):
			if next not in distance:
				distance[next] = 1 + distance[currentNode]
				frontier.insert((next, distance[next]))
	return distance



def aStar(graph, start, goalNode):
	# diagonals takes a boolen value
	frontier = BinHeap()
	frontier.insert((start, 0))

	cameFrom = {}
	cumCost = {}

	cameFrom[start] = None
	cumCost[start] = 0

	while not frontier.empty():
		currentNode = frontier.delMin()[0]

		if currentNode == goalNode:
			return reconstructPath(cameFrom, start, goalNode)

		for next in graph.neighbors(currentNode):
			newCost = cumCost[currentNode] + graph.edgeCost(currentNode, next) 
			if next not in cumCost or newCost < cumCost[next]:
				cumCost[next] = newCost
				priority = fScore(next, goalNode, newCost)
				frontier.insert((next, priority))
				cameFrom[next] = currentNode
	return 'Failure'

def aStarTunnel(graph, start, goalNode):
	# diagonals takes a boolen value
	frontier = BinHeap()
	frontier.insert((start, 0))

	cameFrom = {}
	cumCost = {}

	cameFrom[start] = None
	cumCost[start] = 0

	while not frontier.empty():
		currentNode = frontier.delMin()[0]

		if currentNode == goalNode:
			return reconstructPath(cameFrom, start, goalNode)

		for next in graph.neighbors(currentNode):
			newCost = cumCost[currentNode] + 1
			if next not in cumCost or newCost < cumCost[next]:
				cumCost[next] = newCost
				priority = fScore(next, goalNode, newCost)
				frontier.insert((next, priority))
				cameFrom[next] = currentNode
	return 'Failure'


def reconstructPath(cameFrom, start, goingTo):
	current = goingTo
	path = [current]
	while current != start:
		current = cameFrom[current]
		if current != start:
			path.append(current)
	return path
