import genetic
import random

class Knights():
	def test(self, width, height, num):
		self.find_knight_positions(width, height, num)

	def find_knight_positions(self,width, height, num):
		def fnDisplay(candidate):
			display(candidate,width,height)

		def fnGetFitness(genes):
			return get_fitness(genes, width, height)

		def fnGetRandomPositions():
			return Position(random.randrange(0,width),
						random.randrange(0,height))

		def fnMutate(genes):
			mutate(genes, fnGetRandomPositions)

		def fncreate():
			return create(fnGetRandomPositions, num)

		optimalFitness = width*height
		best, mutations = genetic.get_best(fnGetFitness,
			None, optimalFitness, None, fnDisplay,
			fnMutate, fncreate)
		print(not optimalFitness < best.Fitness)

class Position:
	def __init__(self,X,Y):
		self.X = X
		self.Y = Y
	def __str__(self):
		return self.X, self.Y

	def __eq__(self, other):
		return self.X == other.X and self.Y==other.Y

	def __hash__(self):
		return self.X*1000 + self.Y*10

def get_attacks(location,width,height):
	return [i for i in set(Position(x + location.X,y+location.Y)
			for x in [-2,-1,1,2] if 0 <= x+location.X < width
			for y in [-2,-1,2,2] if 0 <= y+location.Y < height
			and abs(x) != abs(y) )]

def create(get_random_pos, num_knights):
	genes = [get_random_pos() for _ in range(num_knights)]
	return genes

def mutate(genes,get_random_pos):
	index = random.randrange(0, len(genes))
	genes[index] = get_random_pos()

class Board:
	def __init__(self,positions,width,height):
		board = [['.']*width for _ in range(height)]
		for index in range(len(positions)):
			kightposition = positions[index]
			board[kightposition.X][kightposition.Y] = 'K'
		self._board = board
		self._width = width
		self._height = height

	def print_board(self):
		for i in range(len(self._board)):
			print(self._board[i])

def display(candidate, width, height):
	board = Board(candidate.Genes, width, height)
	board.print_board()
	print(candidate.Fitness)

def get_fitness(genes, width, height):
	return len(set(pos 
					for gn in genes
					for pos in get_attacks(gn, width, height)))

kni = Knights()
kni.test(8,8,14)