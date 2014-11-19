#######						#######
#  Procedural DUNGEON Generation  #
#######						#######


# Procedural 'dungeon' generation, using the cellular automata approach
# Written by Marshall Ehlinger for educational purposes
#
# This is the MODEL only- 
# Outputs a data structure representing the dungeon as cells/nodes occupied either as empty or being walls.

###########
# IMPORTS #
###########

import os, random, math, graphSearch, gridConstruction

#############
# FUNCTIONS #
#############

def randWeightedLow(minVal, maxVal):
	for i in range(minVal, maxVal):
		if round(random.randint(i, maxVal) / maxVal) == 1: # This is very arbitrary.
			return i



def generateDungeon(widthX, heightY):
	level = gridConstruction.Graph(widthX, heightY)

	for node in level.allNodes:
		level.inhabitants['walls'].append(node)

	roomSeeds = []
	tunnels = []
	toTunnel = []

	perimeter = level.perimeter()

	roomSeedQuant = int(math.ceil(len(level.allNodes) / 180))

	for i in range(roomSeedQuant):
		roomSeeds.append((random.randint(1, widthX-1), random.randint(1, heightY-1)))
	

	for i in range(len(roomSeeds)):
		room = graphSearch.breadthFirst(level, roomSeeds[i], random.randint(2,5))
		try:
			tunnel = graphSearch.aStarTunnel(level, roomSeeds[i], roomSeeds[i+1])
		except IndexError:
			pass
		for cell in room:
			if cell not in perimeter and cell in level.inhabitants['walls']:
				level.inhabitants['walls'].remove(cell)
		for cell in tunnel:
			if cell not in perimeter and cell in level.inhabitants['walls']:
				level.inhabitants['walls'].remove(cell)

	return level

def updateView(graph):
	# Requires graph formatted as in gridConstruction.py
	os.system('cls' if os.name == 'nt' else 'clear')
	prevNode = graph.allNodes[0]
	for node in graph.allNodes:
		if node[1] > prevNode[1]:
			print
		if node in graph.inhabitants['walls']:
			print 'X',
		else:
			print ' ',
		prevNode = node


# TEST

test = generateDungeon(75, 75)
updateView(test)

