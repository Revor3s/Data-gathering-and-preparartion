import pandas as pd

# Загрузка данных
df = pd.read_csv('C:\\Data Preparation\\Assignment 4\\bank.csv')
# Первичный обзор данных
print("Первые 5 строк:")
print(df.head())
print("\nИнформация о данных:")
print(df.info())
print("\nПроверка пропущенных значений:")
print(df.isnull().sum())

# Общая информация
total_clients = df.shape[0]
print(f"\nОбщее количество клиентов: {total_clients}")

# 1. Процент клиентов, оформивших депозит
deposit_rate = df['deposit'].value_counts(normalize=True)['yes'] * 100
print(f"Процент клиентов, оформивших депозит: {deposit_rate:.2f}%")

# 2. Средний возраст клиентов
average_age = df['age'].mean()
print(f"Средний возраст клиентов: {average_age:.2f} лет")

# 3. Средний баланс
average_balance = df['balance'].mean()
print(f"Средний баланс на счёте: ${average_balance:.2f}")

# 4. Клиенты с отрицательным балансом
negative_balance_count = df[df['balance'] < 0].shape[0]
print(f"Клиенты с отрицательным балансом: {negative_balance_count}")

# 5. Процент клиентов с жилищным кредитом
housing_loan_rate = df['housing'].value_counts(normalize=True)['yes'] * 100
print(f"Процент клиентов с жилищным кредитом: {housing_loan_rate:.2f}%")

# 6. Процент клиентов с потребительским кредитом
personal_loan_rate = df['loan'].value_counts(normalize=True)['yes'] * 100
print(f"Процент клиентов с потребительским кредитом: {personal_loan_rate:.2f}%")

# 7. Средняя длительность звонков
average_call_duration = df['duration'].mean()
print(f"Средняя длительность звонков: {average_call_duration:.2f} секунд")

# 8. Общая длительность всех звонков
total_call_duration = df['duration'].sum()
print(f"Общая длительность всех звонков: {total_call_duration / 3600:.2f} часов")

# 9. Эффективность звонков по дням недели
if 'day_of_week' in df.columns:
    day_effectiveness = df.groupby('day_of_week')['deposit'].value_counts(normalize=True)[:, 'yes'] * 100
    print("\nЭффективность звонков по дням недели:")
    print(day_effectiveness)

# 10. Распределение звонков по месяцам
monthly_calls = df['month'].value_counts()
print("\nРаспределение звонков по месяцам:")
print(monthly_calls)

# 11. Конверсия по возрастным группам
bins = [18, 30, 40, 50, 60, 100]
labels = ['18-30', '31-40', '41-50', '51-60', '60+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

age_group_conversion = df.groupby('age_group')['deposit'].value_counts(normalize=True)[:, 'yes'] * 100
print("\nКонверсия по возрастным группам:")
print(age_group_conversion)

# 12. Среднее количество контактов для успешных подписок
average_contacts_successful = df[df['deposit'] == 'yes']['campaign'].mean()
print(f"\nСреднее количество контактов для успешных подписок: {average_contacts_successful:.2f}")

# 13. Распределение профессий среди подписавших депозит
job_distribution_successful = df[df['deposit'] == 'yes']['job'].value_counts()
print("\nРаспределение профессий среди подписавших депозит:")
print(job_distribution_successful)

# 14. Длительность успешных и неуспешных звонков
successful_calls = df[df['deposit'] == 'yes']['duration'].mean()
unsuccessful_calls = df[df['deposit'] == 'no']['duration'].mean()
print(f"\nСредняя длительность успешных звонков: {successful_calls:.2f} секунд")
print(f"Средняя длительность неуспешных звонков: {unsuccessful_calls:.2f} секунд")

# 15. Конверсия среди клиентов с высоким балансом
high_balance_clients = df[df['balance'] > df['balance'].quantile(0.75)]
high_balance_conversion = high_balance_clients['deposit'].value_counts(normalize=True)['yes'] * 100
print(f"\nКонверсия среди клиентов с высоким балансом: {high_balance_conversion:.2f}%")

# 16. Эффективность звонков в зависимости от предыдущих контактов
previous_effectiveness = df.groupby('previous')['deposit'].value_counts(normalize=True)[:, 'yes'] * 100
print("\nЭффективность звонков в зависимости от количества предыдущих контактов:")
print(previous_effectiveness)

# 17. Количество клиентов с несколькими кредитами
multiple_loans = df[(df['housing'] == 'yes') & (df['loan'] == 'yes')].shape[0]
print(f"\nКоличество клиентов с жилищным и потребительским кредитами: {multiple_loans}")

# 18. Эффективность звонков по типу контакта
contact_effectiveness = df.groupby('contact')['deposit'].value_counts(normalize=True)[:, 'yes'] * 100
print("\nЭффективность звонков по типу контакта:")
print(contact_effectiveness)

# 19. Успешные подписки после 4+ звонков
high_contact_conversion = df[(df['campaign'] > 4) & (df['deposit'] == 'yes')].shape[0]
print(f"\nКлиенты, подписавшие депозит после более 4 звонков: {high_contact_conversion}")

# 20. Конверсия клиентов с разным уровнем образования
education_conversion = df.groupby('education')['deposit'].value_counts(normalize=True)[:, 'yes'] * 100
print("\nКонверсия клиентов с разным уровнем образования:")
print(education_conversion)
