import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cross_decomposition import PLSRegression

df = pd.read_csv('regression_pls.csv')
t = df['Target'].values
x = df.drop('Target', axis=1).values

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, t_train)

# print(f'train: {model.score(x_train, t_train)}')
# print(f'test: {model.score(x_test, t_test)}')

df_corr = df.corr()

plt.figure(figsize=(12,8))
sns.heatmap(df_corr.iloc[:20, :20], annot=True)
sns.jointplot(x='x1', y='x16', data=df)
# plt.show()

pls = PLSRegression(n_components=11)
pls.fit(x_train, t_train)

print(f'train: {pls.score(x_train, t_train)}')
print(f'test: {pls.score(x_test, t_test)}')
