#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# In[2]:


G = 6.67 * (10**(-11)) #Newtons const [m^3][kg^-1][s^-2]
M = 2 * (10**(41)) #average mass of spiral galaxy [kg]
#4.63 * (10**(20)) #average radius of spiral galaxy [m]
rho_0 = 10**(-21) #average central mass density of a spiral galaxy [kg][m^-3]


# In[3]:


# Define the parameters
char_raddii = [10, 1000, 1000000, 1]  # Example values for r_d


# In[ ]:


# Define the function
def v_vs_r(r, r_d):
    return np.sqrt((G*M)/(r) + (G * M * r * (np.log(r_d)/r_d)) * np.exp(-np.log(r_d)/r_d * r))

# Generate r values
# np.linspace(min, max, steps)
r_values = np.linspace(0.1, 10000000, 100000000)

# Plot the function for each r_d
for r_d in char_raddii:
    v_values = v_vs_r(r_values, r_d)
    plt.plot(r_values, v_values, label=f'r_d = {r_d}' + (' (Keplarian)' if r_d==1 else ''), linestyle=(0, (4, 5)) if r_d==1 else '-', color='black' if r_d==1 else None)

# # plot newtonian for comparision
# v_values = v_vs_r(r_values, 0, 1)
# plt.plot(r_values, v_values, label=f'r_d = 1 (Newtonian)', linestyle=(0, (4, 5)), color='black')

plt.yscale('log')  # Set the y-axis to logarithmic scale
plt.xscale('log')  # Set the x-axis to logarithmic scale

plt.xlabel('r (m)')
plt.ylabel('Orbital Velocities (m/s)')
plt.title('Orbital Velocites vs. r')
plt.legend(title="Characteristic Radii (m)", loc="lower left")
plt.grid(True)

plt.savefig('figures/graph_orbvelVr.png', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:


import subprocess
subprocess.call("jupyter nbconvert --to script velocity_curves.ipynb")

