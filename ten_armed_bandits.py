import random
import matplotlib.pyplot as plt
import numpy as np

class tenBandits():
	def __init__(self):
		self.values = [random.gauss(0, 1) for i in range(10)]
		self.qvalues = dict()

		# Init Q values
		for i in range(len(self.values)):
			self.qvalues[i] = (0, 1)

	def getRewards(self, action):
		# Gets Rt
		return random.gauss(self.values[action], 1)

	def greedyAction(self):
		return max(self.qvalues, key=self.qvalues.get)

	def epsilonGreedyAction(self, epsilon):
		prob = random.random()
		if prob<=epsilon:
			return random.randrange(0, 10, 1)
		else:
			#print("max bandit", max(self.qvalues, key=self.qvalues.get))
			return max(self.qvalues, key=self.qvalues.get)

	def updateQValue(self, Qvalue_index, reward):
		print(self.qvalues[Qvalue_index], Qvalue_index)
		input()
		v, t = self.qvalues[Qvalue_index]
		self.qvalues[Qvalue_index] = ((t-1)*v/t + reward/t, t+1)


bandits = tenBandits()
default_values = bandits.values
default_qvalues = bandits.qvalues.copy()

print(default_qvalues)

def exp1(epsilon=0, steps=1000):

	print(bandits.values)

	total1 = np.zeros(1000)
	total2 = np.zeros(1000)
	total3 = np.zeros(1000)
	for j in range(2000):
		values = list()
		for i in range(steps):
			action = bandits.epsilonGreedyAction(0)
			reward = bandits.getRewards(action)
			bandits.updateQValue(action, reward)

			values.append(reward)
		total1 += np.asarray(values)
		bandits.values = default_values
		bandits.qvalues = default_qvalues

	for j in range(2000):
		values = list()
		for i in range(steps):
			action = bandits.epsilonGreedyAction(0.1)
			reward = bandits.getRewards(action)
			bandits.updateQValue(action, reward)

			values.append(reward)
		total2 += np.asarray(values)
		bandits.values = default_values
		bandits.qvalues = default_qvalues


	for j in range(2000):
		values = list()
		for i in range(steps):
			action = bandits.epsilonGreedyAction(0.01)
			reward = bandits.getRewards(action)
			bandits.updateQValue(action, reward)

			values.append(reward)
		total3 += np.asarray(values)
		bandits.values = default_values
		bandits.qvalues = default_qvalues


	plt.plot(range(1000), total1/2000)
	plt.plot(range(1000), total2/2000)
	plt.plot(range(1000), total3/2000)

	plt.show()
