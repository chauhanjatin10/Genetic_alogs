import genetic 
import random

class Cards:
	def test(self):
		geneset = [i for i in range(1,11)]

		def fnDisplay(candidate):
			display(candidate)
		
		def fnGetFitness(genes):
			return get_fitness(genes)

		def fnMutate(genes):
			mutate(genes,geneset)

		optimalFitness = Fitness(36, 360, 0)
		best,mutations = genetic.get_best(fnGetFitness, 10, optimalFitness,
				geneset, fnDisplay, fnMutate)
		print(not optimalFitness < best.Fitness)

import functools
import operator
def get_fitness(genes):
	sum1 = sum(genes[0:5])
	prod = functools.reduce(operator.mul,genes[5:10])
	duplicateCount = len(genes) - len(set(genes))
	return Fitness(sum1,prod,duplicateCount)

class Fitness:
	def __init__(self,sum1,prod,duplicateCount):
		self.sum1 = sum1
		self.prod = prod
		self.totaldiff = abs(360 - prod) + abs(36-sum1)
		self.duplicateCount = duplicateCount

	def __gt__(self,other):
		if self.duplicateCount != other.duplicateCount:
			return self.duplicateCount < other.duplicateCount
		return self.totaldiff < other.totaldiff
	
	def __str__(self):
		return "sum: {0} prod: {1} dups: {2}".format(
				self.sum1,
				self.prod,
				self.duplicateCount)

def display(candidate):
	print(candidate.Genes[5:10], '  ',candidate.Genes[0:5], candidate.Fitness)

def mutate(genes,geneset):
	if len(genes) == len(set(genes)):
		index1, index2 = random.sample(range(len(genes)), 2)
		genes[index1], genes[index2] = genes[index2], genes[index1]

	else:
		indexA = random.randrange(0, len(genes))
		indexB = random.randrange(0, len(geneset))
		genes[indexA] = geneset[indexB]

card = Cards()
card.test()
