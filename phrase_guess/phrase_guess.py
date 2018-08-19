import datetime
import genetic

def test_phrase():
	target = "hey fells, how's life goin' out there?"
	guess_phrase(target)

def guess_phrase(target):
	geneset = " ,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.?'"

	def GetFitness(genes):
		return fitness_gene(genes,target)

	def Display(genes):
		display(genes,target)

	optimalfitness = len(target)
	genetic.get_best(GetFitness,len(target),optimalfitness,geneset,Display)

def display(guess,target):
	fitness = fitness_gene(guess,target)
	print("{0}   {1}".format(guess,fitness))

def fitness_gene(guess,target):
	return sum(1 for a,b in zip(target,guess) if a==b)

genetic.Benchmark.run(test_phrase)
