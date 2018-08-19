import random
import statistics
import time

def _generate_gene(length,geneset):
	genes = []
	while len(genes) < length:
		sample = min(length - len(genes), len(geneset))
		a,b = random.sample(geneset,sample)
		genes.extend(str(a)+str(b))

	return ''.join(genes)

def _mutate(parent,geneset):
	childgene = list(parent)
	index = random.randrange(0,len(parent))
	newgene, alternative_gene = random.sample(geneset,2)
	childgene[index] = str(alternative_gene) if str(newgene)==childgene[index] else str(newgene)
	return ''.join(childgene)

def get_best(fitness_gene, targetlength, optimalfitness,geneset,display):
	random.seed()
	bestparent = _generate_gene(targetlength,geneset)
	fitness = fitness_gene(bestparent)
	display(bestparent)
	if fitness >= optimalfitness:
		return bestparent

	while True:
		child = _mutate(bestparent,geneset)
		childfitness = fitness_gene(child)
		if fitness >= childfitness:
			continue

		display(child)
		if childfitness>= optimalfitness:
			return child
		fitness = childfitness
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
