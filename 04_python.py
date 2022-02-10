'''
Your task for this exercise is to complete the code for the class below.
You'll start by creating the graph specified below and storing it as a dict, 
you can also lookup what a defaultdict is and use that instead.



your graph/dictionary (key:values) must look like this when printed
{
('a', ['b'])
('b', ['a', 'c'])
('c', ['b'])
}
'''

from collections import defaultdict

class Graph():
	def __init__(self):
		'''
		Initialize the dictionary with the (key:values) specified above.
		'''
		

	def __str__(self):
		'''
		print the dictionary as described in the example above.
		'''

	def isConnected(self, person1, person2):
		'''
		The arguments of this function are two people and it returns a boolean
		whether those two people are connected in the graph or not.

		Hint: try to use some search technique
		'''
		


if __name__ == "__main__":
	g = Graph()

	print("---------Testing __str__ ---------")
	print(str(g))
	print(str(g) == "{\n('a', ['b'])\n('b', ['a', 'c'])\n('c', ['b'])\n}")

	print("---------Testing isConnected ---------")
	connectivity = [g.isConnected('a', 'b'), g.isConnected('c', 'a'), g.isConnected('c', 'b')]
	print(connectivity == [True, True, True])

