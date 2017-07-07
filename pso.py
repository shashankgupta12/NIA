import random

pb = []
pb_particles = []

def best(ptls):
	global pb
	global particles
	updatedPB = []
	updatedParticles = []
	newPB = [sum(particle) for particle in ptls]
	n1 = [abs(i - 0) for i in newPB] #because subset sum has to be zero
	n2 = [abs(i - 0) for i in pb]
	for index, a in enumerate(zip(n1, n2)):
		if a[0] < a[1]:
			updatedPB.append(n1[index])
			updatedParticles.append(ptls[index])
		else:
			updatedPB.append(n2[index])
			updatedParticles.append(particles[index])
	for index, i in enumerate(updatedPB):
		pb[index] = i
	for index, i in enumerate(updatedParticles):
		particles[index] = i
	gbest = max(pb)

def pso(particles, velocities):
	gbest, pbest = best(particles)
	return []

def optimize(A, subSize):
	global pb
	global pb_particles
	populationSize = 10
	particles = [random.sample(A, subSize) for i in range(populationSize)]
	velocities = [[0]*5 for _ in range(populationSize)]
	for particle in particles:
		pb.append(sum(particle))
	for particle in particles:
		pb_particles.append(particle)
	lst = pso(particles, velocities)
	return lst

if __name__ == '__main__':
	A = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
	subSize = 5
	lst = optimize(A, subSize)
	print('Total subsets: {}'.format(len(lst)))
	for subset in lst:
		print(subset)