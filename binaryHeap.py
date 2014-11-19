##
# Binary Heap Tree - Data Structure for Personal Educational Purposes and Beyond
# 11/13/14
# Marshall Ehlinger
# Based on tutorial @ "http://interactivepython.org/runestone/static/pythonds/Trees/heap.html"
##

# NOTE: written to work with a sepcific graph data structure, in gridConstruction.py
# Determines order based on each item's second value (priority) @ index [1], as in [nodeName, nodePriorityValue]
# Remove references to the nested elements to make more versitile (remove the the [1] in-> list[x][1])

class BinHeap:
	def __init__(self):
		# Initializes a binary heap tree data structure
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, newItem):
		self.heapList.append(newItem)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def delMin(self):
		smallestVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return smallestVal 

	def empty(self):
		return self.currentSize == 0


	# HELPER FUNCTIONS CALLED INTERNALLY

	def percUp(self, i):
		while i / 2 > 0:
			if self.heapList[i][1] < self.heapList[i / 2][1]: 
				temp = self.heapList[i / 2]
				self.heapList[i/ 2] = self.heapList[i]
				self.heapList[i] = temp
			i = i / 2

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i][1] > self.heapList[mc]:
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = temp
			i = mc

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize: 
			return i * 2
		else:
			if self.heapList[i * 2][1] < self.heapList[i * 2 + 1][1]:
				return i * 2
			else:
				return i * 2  + 1