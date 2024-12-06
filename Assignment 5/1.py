import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'C:\Data Preparation\Assignment 5\salesforcourse.csv'
df = pd.read_csv(file_path)

# Step 2: Data cleaning
# Remove rows with missing values
df_cleaned = df.dropna()

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Convert numerical columns to appropriate types
numerical_columns = ['Customer Age', 'Quantity',
                     'Unit Cost', 'Unit Price', 'Cost', 'Revenue']
df_cleaned[numerical_columns] = df_cleaned[numerical_columns].apply(
    pd.to_numeric, errors='coerce')

# Step 3: Data Analysis
descriptive_stats = df_cleaned[numerical_columns].describe()

for col in numerical_columns:
    plt.figure(figsize=(6, 4))
    plt.hist(df_cleaned[col], bins=20, edgecolor='black', alpha=0.7)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

for column in numerical_columns:
    column_mean = df_cleaned[column].mean()
    column_std = df_cleaned[column].std()
    column_min = df_cleaned[column].min()
    column_max = df_cleaned[column].max()
    column_25 = df_cleaned[column].quantile(0.25)
    column_50 = df_cleaned[column].median()
    column_75 = df_cleaned[column].quantile(0.75)

    print(f"=== {column} ===")
    print(f"- Среднее значение: {column_mean:.2f}")
    print(f"- Стандартное отклонение: {column_std:.2f}")
    print(f"- Минимальное значение: {column_min:.2f}")
    print(f"- Максимальное значение: {column_max:.2f}")
    print(f"- 25-й процентиль: {column_25:.2f}")
    print(f"- Медиана: {column_50:.2f}")
    print(f"- 75-й процентиль: {column_75:.2f}")
    print("\n")
