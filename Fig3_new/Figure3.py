#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[11]:


##Skin Friction data____________________________
data = pd.read_csv('fig3_shear.csv')
dt1 =data.sort_values(by='Angle')
np_arr = dt1.values
x_1 = np_arr[:,0]
y_1 = np_arr[:,1]

##Pressure data__________________________________
data2 = pd.read_csv('fig3_pressure.csv')
dt2 =data2.sort_values(by='Angle')
np_arr = dt2.values
x_2 = np_arr[:,0]
y_2 = np_arr[:,1]


# In[19]:


fig_1, (ax1, ax2) = plt.subplots(2, 1, figsize=(9,9), constrained_layout=False)
fig_1.subplots_adjust(hspace=0.5)
fig_1.tight_layout()

#_____________________#FIGURE_3 SHEAR________________________________#

ax1.set_xticks([0, 30, 60, 90, 120, 150, 180])
ax1.set_yticks([-3,-2,-1,0,1,2,3])
ax1.grid(True, color ='0.6', linewidth= 1, dashes=(1,2,1,2))

ax1.set_xlim(0, 180)
ax1.set_ylim(-3, 3)
ax1.set_ylabel(r'($\tau_o / \rho\cup^{2}_\infty)\sqrt{Re}$', fontsize=14)

ax1.set_title("Figure 3 Skin friction and Pressure")
ax1.set_title('Skin friction', loc='left', y=0.80, x=0.50, fontsize='large')
ax1.set_title("$\phi_1$= 78$^\circ$", loc='center', y=0.50, x=0.49, fontsize='large')


ax1.plot(x_1, y_1, color ='navy', alpha=.75, lw=2, ls='-', marker ='o',
                                  markersize=7, markerfacecolor ='r', 
                                  markeredgecolor ='r', markeredgewidth=2)

#_____________________#FIGURE_3 PRESSURE________________________________#

ax2.set_xticks([0, 30, 60, 90, 120, 150, 180])
ax2.set_yticks([-1.5,-1,-0.5,0,0.5,1])
ax2.grid(True, color ='0.6', linewidth= 1, dashes=(1,2,1,2))
ax2.set_ylabel(r'$[p - p_\infty]/(\frac{1}{2}\rho)\cup^{2}_\infty]$', fontsize=14)

ax2.set_xlim(0, 180)
ax2.set_ylim(-2, 1)
#ax2.set_xlabel('Peripheral Angle, (degree)')
ax2.set_title('Pressure', loc='left', y=0.80, x=0.70, fontsize='large')

ax2.plot(x_2, y_2, color ='navy', alpha=.75, lw=2, ls='-', marker ='o',
                                  markersize=7, markerfacecolor ='r', 
                                  markeredgecolor ='r', markeredgewidth=2)






# ##### END OF FIGURE 3
# 

# In[ ]:




