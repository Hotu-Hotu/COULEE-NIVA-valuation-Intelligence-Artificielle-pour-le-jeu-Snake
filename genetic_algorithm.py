# genetic_algorithm.py
import random
from snake import Snake
from neural_network import NeuralNetwork

class GeneticAlgorithm:
    def __init__(self, size=50):
        self.size = size
        self.population = [Snake() for _ in range(size)]
        self.generation = 1
        self.best_fitness = 0
        self.history = []

    def evaluate(self):
        for s in self.population:
            s.calculate_fitness()

    #Sélection par tournoi (choix plus probable des meilleurs) évité convergence prématurée
    def select(self):
        self.population.sort(key=lambda s: s.fitness, reverse=True)
        self.best_fitness = self.population[0].fitness
        self.history.append(self.best_fitness)

        selected = []
        for _ in range(self.size // 2):
            contenders = random.sample(self.population, 3)
            selected.append(max(contenders, key=lambda s: s.fitness))

        return selected


    def reproduce(self, selected):
        new_pop = selected[:5]  # élitisme

        while len(new_pop) < self.size:
            p1, p2 = random.sample(selected, 2)
            child_net = NeuralNetwork.crossover(p1.network, p2.network)
            child_net.mutate()
            new_pop.append(Snake(child_net))

        self.population = new_pop
        self.generation += 1
