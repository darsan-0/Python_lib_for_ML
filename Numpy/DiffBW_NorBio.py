#Difference b/w normal and Binomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Normal":random.normal(loc = 50,scale = 5,size = 1000),
    "Binomial":random.binomial(n=100,p=0.5,size=1000)
}
sns.displot(data,kind="kde")
plt.show()