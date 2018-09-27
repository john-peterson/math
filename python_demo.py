
# coding: utf-8

# In[2]:


#get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import pandas as pd


# In[4]:


df = pd.read_csv('data.csv')
print(df)


# In[11]:
plt.plot(df['V'], df['I'], marker='o', label="measured data")
plt.xlabel('V [V]')
plt.ylabel('I [A]')
plt.title('quick demo')


# In[9]:
import scipy.stats
slope, intercept, _r, _p, _s = scipy.stats.linregress(df['V'], df['I'])
print(slope)
print(intercept)


# In[12]:
plt.plot(df['V'], slope*df['V']+intercept, label="theory")
plt.legend()


# In[13]:

#plt.savefig("labb_plot.svg")
plt.show()

