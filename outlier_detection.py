# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("./banknote.csv")

df.head()

"""# New Section"""

sns.boxplot(data=df, x=df["Length"])
plt.title("Boxplot of Swiss Banknote Length")


def boxplot(column):
    sns.boxplot(data=df, x=df[f"{column}"])
    plt.title(f"Boxplot of Swiss Banknote {column}")
    plt.show()


boxplot('Length')
boxplot('Right')
boxplot('Left')
boxplot('Bottom')
boxplot('Top')
boxplot('Diagonal')
