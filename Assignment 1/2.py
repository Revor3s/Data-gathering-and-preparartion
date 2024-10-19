import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

print(df.head())
print(df.info())

# Проверка на пропущенные значения
print(df.isnull().sum())

# Статистическое описание
print(df.describe())

# Заполнение пропусков
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Визуализация данных
# Распределение возраста
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], kde=True)
plt.title('Распределение возраста пассажиров')
plt.show()

# Взаимосвязь между классом и выживаемостью
plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='survived', data=df)
plt.title('Класс и вероятность выживания')
plt.show()

# Корреляционная матрица
corr_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Корреляционная матрица признаков')
plt.show()
