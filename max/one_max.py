import datetime
import genetic

def test_phrase():
	target = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
	return guess_phrase(target)

def guess_phrase(target):

	geneset = [0,1]

	def GetFitness(genes):
		return fitness_gene(genes)

	def Display(genes):
		display(genes,target)

	optimalfitness = len(target)
	return genetic.get_best(GetFitness,len(target),optimalfitness,geneset,Display)

def display(guess,target):
	fitness = fitness_gene(guess)
	#guess_truncated = guess[:15] + guess[86:]
	print("{0}   {1}".format(guess,fitness))

def fitness_gene(guess):
	return guess.count("1")

found = test_phrase()
print(found)
#genetic.Benchmark.run(test_phrase)
