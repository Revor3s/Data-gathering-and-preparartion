from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')


mean_age = df['age'].mean()
median_age = df['age'].median()
mode_age = df['age'].mode()[0]


print(f"Средний возраст: {mean_age}")
print(f"Медианный возраст: {median_age}")
print(f"Модальный возраст: {mode_age}")


# Сравнение возраста выживших и невыживших пассажиров
survived_age = df[df['survived'] == 1]['age']
not_survived_age = df[df['survived'] == 0]['age']

# Проведение t-теста
t_stat, p_val = stats.ttest_ind(survived_age.dropna(), not_survived_age.dropna())
print(f"T-статистика: {t_stat}, P-значение: {p_val}")

# 3. Визуализация результатов
plt.figure(figsize=(10, 6))
sns.histplot(survived_age, color='green', label='Выжившие', kde=True)
sns.histplot(not_survived_age, color='red', label='Невыжившие', kde=True)
plt.title('Сравнение возраста выживших и невыживших пассажиров')
plt.legend()
plt.show()

# Группировка по классу и подсчет среднего возраста
grouped_by_class = df.groupby('pclass')['age'].mean()
print(grouped_by_class)
