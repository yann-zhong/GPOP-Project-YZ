# Necessary imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import statistics

# DIPLOID SIMULATION: NOT WHAT WE WANT FOR QUESTION 1
# ----- Initialize simulation variables ----- # 

generations = 99                                  # Discrete time step
gen_freq = np.ones(3)                               # XAA, XAB, XBB
gen_freq = np.random.dirichlet(np.ones(3),size=1)   # Numpy dirichlet distribution: generates three elements that sum to 1
gen_freq_list = gen_freq.tolist()                   # Convert to list to be able to use append()

p = gen_freq_list[0][0] + 0.5*gen_freq_list[0][1]   # Allele frequency for A: p = XAA + 0.5*XAa
q = 1 - p                                           # Allele frequency for a: q = 1 - p = Xaa + 0.5*XAa

x1,x2,x3 = [[0],[0],[0]]                               # Lists!
y1,y2,y3 = [[gen_freq_list[0][i]] for i in range(3)]   # Use [] outside the for to avoid error.

# ----- Run simulation  ----- # 

for n in range(generations):

    x1.append(n)        # Increment x axis
    x2.append(n)        
    x3.append(n)        

    new_y1 = y1[0]*y1[0]
    new_y2 = 2*y1[0]*y3[0]
    new_y3 = y3[0]*y3[0]

    y1.append(new_y1)   # Increment y axis
    y2.append(new_y2)
    y3.append(new_y3)

# ----- Figure stuff  ----- # 

fig = plt.figure()
ax1 = plt.axes (xlim=(0,generations),ylim=(0,1))
t = np.arange(0, (generations+1)*10, 10)

plt.plot(t,y1, label = "AA")
plt.plot(t,y2, label = "AB")
plt.plot(t,y3, label = "BB")

plt.xlabel('Time')
plt.ylabel('Genotype frequency')
plt.title('Genotype frequency evolution in time')
plt.grid(True)

plt.show()