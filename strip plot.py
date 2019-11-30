import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("tips.csv")
print(data)

sns.stripplot(x = data["tip"] , color="red")
plt.show()

sns.stripplot(x = data["day"] ,y =data["total_bill"] , jitter=0)
plt.show()

sns.stripplot(x = data["day"] , y = data["total_bill"] , hue = data["sex"] , jitter=False , size=10)
plt.show()