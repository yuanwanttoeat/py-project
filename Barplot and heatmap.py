import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns


# Path of the file to read
ign_filepath = "ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col = 'Platform')

# Bar chart showing average score for racing games by platform
sns.barplot(x=ign_data.index, y=ign_data['Racing']) 
plt.ylabel("Rating")

plt.show()
plt.savefig('barplot.png')

# Heatmap showing average game score by platform and genre
sns.heatmap(ign_data, annot=True)

plt.show()
plt.savefig('heatmap.png')