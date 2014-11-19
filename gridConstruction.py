###
# Class for graph for pathfinding. Rectangular graphs only, punk.
# Written by Marshall Ehlinger, based on redblobgames tutorials
###

class Graph:
	def __init__(self, width, height):
		self.allNodes = [(x,y) for y in range(width) for x in range(height)]
		self.inhabitants = {} # Stores agents in the graph as 'name' : (tuplex, tupley), 
		self.inhabitants['walls'] = [] # Should be list of tuples for wall coordinates

	def neighbors(self, node):
		edges = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
		result = []
		for edge in edges:
			neighbor = tuple(sum(x) for x in zip(node, edge))
			if neighbor in self.allNodes:
				result.append(neighbor)
		return result

	def edgeCost(self, parentNode, neighborNode):
		if neighborNode not in self.inhabitants['walls']:
			if (abs(neighborNode[0] - parentNode[0]), abs(neighborNode[1] - parentNode[1])) == (1,1):
				return 1.40
			else:
				return 1.00
		else:
			return 999.99

	def edgeCostTunnel(self, parentNode, neighborNode):
		# Retrieves edge costs with a less-weighted wall weight for tunneling during map generation
		if neighborNode not in self.inhabitants['walls']:
			if (abs(neighborNode[0] - parentNode[0]), abs(neighborNode[1] - parentNode[1])) == (1,1):
				return 1.40
			else:
				return 1.00
		else:
			return 25

	def perimeter(self):
		perimeter = []
		for node in self.allNodes:
			if len(self.neighbors(node)) < 8:
				perimeter.append(node)
		return perimeter