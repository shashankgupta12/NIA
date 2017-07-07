#-------------------------------------------------------------
#       Part - II: GA--> Crossover, Mutation
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------



#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random
from copy import deepcopy



#-------------------------------------------------------------
# Step 2: Problem parameters
#-------------------------------------------------------------
D       = 5         # Problem Dimension
LB      = -30       # Set Size Lower Bound
UB      = 30        # Set Size Upper Bound



#-------------------------------------------------------------
# Step 4: Functions Definations
#-------------------------------------------------------------
# Function 1: Fitness Function
def FitnessFunction(x):
    s=(x[4] - x[3]**2)**2 + (x[3] - x[2]**2)**2 + (x[2] - x[1]**2)**2 + (x[1] - x[0]**2)**2
    return round(s,2)


#-------------------------------------------------------------
# Step 3: Crossover
#-------------------------------------------------------------

# Choose a crossover point 
pt = random.randint(1,D-2)

# Choose Parents
p1=[6.161, -2.325, 11.094, -8.654, -6.864]
p2=[-17.53, 11.272, 7.352, -23.524, 0.899]

p1Fitness=FitnessFunction(p1)
p2Fitness=FitnessFunction(p2)

# Generate new childs 
c1=p1[0:pt] + p2[pt:]
c2=p2[0:pt] + p1[pt:]

c1Fitness=FitnessFunction(c1)
c2Fitness=FitnessFunction(c2)

print "********* Crossover *********"
print "pt: ", pt
print "\np1: ", p1, "\tFitness: ", p1Fitness
print "p2: ", p2, "\tFitness: ", p2Fitness
print "\nc1: ", c1, "\tFitness: ", c1Fitness
print "c2: ", c2, "\tFitness: ", c2Fitness




#-------------------------------------------------------------
# Step 4: Mutation
#-------------------------------------------------------------

pt = random.randint(0, D-1)

p=[6.161, -2.325, 11.094, -8.654, -6.864]
pFitness=FitnessFunction(p)

c=deepcopy(p)

c[pt] = round(random.uniform(LB,UB),3)
cFitness=FitnessFunction(c)

print "\n\n********* Mutation *********"
print "pt: ", pt
print "\np: ", p, "\tFitness: ", pFitness
print "c: ", c, "\tFitness: ", cFitness
print "\n"



