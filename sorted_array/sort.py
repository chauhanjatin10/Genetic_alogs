import genetic
import unittest

class SortedNumbers(unittest.TestCase):
	def test_sort_numbers(self):
		return self.sort_numbers(10)

	def sort_numbers(self,totalNumbers):
		geneset = [i for i in range(100)]

		def fnDisplay(candidate):
			Display(candidate)

		def fnFitness(genes):
			return get_fitness(genes)

		optimalfitness = Fitness(totalNumbers, 0)
		best = genetic.get_best(fnFitness,totalNumbers,
			optimalfitness,geneset,fnDisplay)
		return not optimalfitness < best.Fitness
def get_fitness(genes):
	fitness = 1
	gap = 0
	for i in range(1,len(genes)):
		if genes[i] >= genes[i-1]:
			fitness += 1
		else:
			gap += genes[i-1] - genes[i]
	return Fitness(fitness, gap)

def Display(candidate):
	print(candidate.Genes, candidate.Fitness)

class Fitness:
	NumberInSequenceCount = None
	TotalGap = None

	def __init__(self,numberInSequenceCount,totalGap):
		self.NumberInSequenceCount = numberInSequenceCount
		self.TotalGap = totalGap

	def __gt__(self,other):
		if self.NumberInSequenceCount != other.NumberInSequenceCount:
			return self.NumberInSequenceCount > other.NumberInSequenceCount
		return self.TotalGap < other.TotalGap

	def __str__(self):
		return "{0} Sequential, {1} Total Gap".format(
			self.NumberInSequenceCount,self.TotalGap)


sorted_num = SortedNumbers()
result = sorted_num.test_sort_numbers()
print(result)