import genetic

class EightQueens(object):
	def test(self,size):
		geneset = [i for i in range(size)]

		def fnDisplay(candidate):
			display(candidate, size)

		def fnGetFitness(genes):
			return get_fitness(genes, size)

		optimalFitness = Fitness(0)
		best,mutations = genetic.get_best(fnGetFitness, 2*size,
			optimalFitness, geneset, fnDisplay)
		print(not optimalFitness > best.Fitness,'\t', mutations)

class Board(object):
	def __init__(self,genes,size):
		board =[['.']*size for _ in range(size)]
		for index in range(0, len(genes), 2):
			row = genes[index]
			column = genes[index+1]
			board[row][column] = 'Q'
		self._board = board

	def print_board(self):
		for i in range(0, len(self._board)):
			print(' '.join(self._board[i]))

	def get(self,row,column):
		return self._board[column][row]


class Fitness(object):
	Total = None

	def __init__(self,total):
		self.Total = total

	def __gt__(self, other):
		return self.Total < other.Total

	def __str__(self):
		return str(self.Total)

def display(candidate, size):
	board = Board(candidate.Genes, size)
	board.print_board()
	print(candidate.Genes, candidate.Fitness)


def get_fitness(genes, size):
	board = Board(genes, size)
	rowswithQueens = set()
	colswithQueens = set()
	top_right_bottom_left_diagonal = set()
	top_left_bottom_right_diagonal = set()
	for row in range(size):
		for col in range(size):
			if board.get(row,col) == 'Q':
				rowswithQueens.add(row)
				colswithQueens.add(col)
				top_right_bottom_left_diagonal.add(row+col)
				top_left_bottom_right_diagonal.add(size -1 - row + col)

	total = 4*size - (len(rowswithQueens)+len(colswithQueens)
		+ len(top_left_bottom_right_diagonal)+ len(top_right_bottom_left_diagonal))
	return Fitness(total)

queens = EightQueens()
queens.test(4)