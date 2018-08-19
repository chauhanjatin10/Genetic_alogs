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

def _mutate(parent,geneset,get_fitness,display,optimalfitness,mutations):
	while True:
		childgene = parent.Genes
		index = random.randrange(0,len(parent.Genes))
		newgene, alternative_gene = random.sample(geneset,2)
		childgene[index] = alternative_gene if newgene==childgene[index] else newgene
		fitness = get_fitness(childgene)
		child = Chromosome(childgene, fitness)
		mutations += 1
		#childfitness = fitness_gene(child)
		if parent.Fitness > child.Fitness:
			continue
		if not child.Fitness > parent.Fitness:
			parent = child

		display(child)
		if not optimalfitness > child.Fitness:
			return child,mutations
		parent = child

def _mutate_custom(parent, custom_mutate, get_fitness,display,optimalfitness,mutations):
	while True:
		childGenes = parent.Genes
		custom_mutate(childGenes)
		fitness = get_fitness(childGenes)
		child = Chromosome(childGenes, fitness)
		mutations += 1
		if parent.Fitness > child.Fitness:
			continue
		if not child.Fitness > parent.Fitness:
			parent = child
		
		display(child)
		if not optimalfitness > child.Fitness:
			return child,mutations
		parent = child

def get_best(get_fitness, targetlength, optimalfitness,
			geneset,display, custom_mutate):
	mutations = 1
	random.seed()
	bestparent = _generate_gene(targetlength,geneset,get_fitness)
	#fitness = fitness_gene(bestparent)
	display(bestparent)
	if not optimalfitness > bestparent.Fitness:
		return bestparent

	if custom_mutate is None:
		def fnMutate(bestparent):
			return _mutate(bestparent,geneset,get_fitness,display,optimalfitness,mutations)
		return fnMutate(bestparent)

	else:
		def fnMutate(bestparent):
			return _mutate_custom(bestparent,custom_mutate,get_fitness,display,optimalfitness,mutations)
		return fnMutate(bestparent)
	

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
