import random
import statistics
import time

class Chromosome:
	Genes = None
	Fitness = None

	def __init__(self,genes,fitness):
		self.Genes = genes
		self.Fitness = fitness

def _generate_gene(length,geneset,get_fitness):
	genes = []
	while len(genes) < length:
		#samples = min(length - len(genes), len(geneset))
		a = random.sample(geneset,1)
		genes.extend(a)
	fitness = get_fitness(genes)
	return Chromosome(genes,fitness)

def _mutate(parent,geneset,get_fitness):
	childgene = parent.Genes
	index = random.randrange(0,len(parent.Genes))
	newgene, alternative_gene = random.sample(geneset,2)
	childgene[index] = alternative_gene if newgene==childgene[index] else newgene
	#print(type(childgene))
	fitness = get_fitness(childgene)
	return Chromosome(childgene,fitness)

def get_best(get_fitness, targetlength, optimalfitness,geneset,display):
	mutations = 1
	random.seed()
	bestparent = _generate_gene(targetlength,geneset,get_fitness)
	#fitness = fitness_gene(bestparent)
	display(bestparent)
	if not optimalfitness > bestparent.Fitness:
		return bestparent

	while True:
		child = _mutate(bestparent,geneset,get_fitness)
		mutations += 1
		#childfitness = fitness_gene(child)
		if bestparent.Fitness > child.Fitness:
			continue
		if not child.Fitness > bestparent.Fitness:
			bestparent = child

		display(child)
		if not optimalfitness > child.Fitness:
			return child,mutations
		bestparent = child

class Benchmark:
	@staticmethod
	def run(function):
		timings = []
		for i in range(10):
			starttime = time.time()
			function()
			seconds = time.time() - starttime
			timings.append(seconds)
			mean = statistics.mean(timings)
			print(1+i," ",mean, " ",statistics.stdev(timings,mean) if i>1 else 0)
