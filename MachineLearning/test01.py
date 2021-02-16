import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = load_boston()
x, t = dataset.data, dataset.target
columns = dataset.feature_names

df = pd.DataFrame(x, columns=columns)
df['Target'] = t

t = df['Target'].values
x = df.drop(labels=['Target'], axis=1).values

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, t_train)

# plt.figure(figsize=(10, 7))
# plt.bar(x=columns, height=model.coef_)
# plt.show()

y = model.predict(x_test)

print(f'予測値: {y[0]}')
print(f'目標値: {t_test[0]}')