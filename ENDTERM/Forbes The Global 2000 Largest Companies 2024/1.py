import pandas as pd

file_path = r'C:\Data Preparation\Endterm\Forbes The Global 2000 Largest Companies 2024\Largest-Companies.csv'

try:
    df = pd.read_csv(file_path, encoding='utf-8')  
except UnicodeDecodeError:
    print("Failed with utf-8. Trying 'latin1' encoding...")
    df = pd.read_csv(file_path, encoding='latin1')  


df_cleaned = df.dropna()  
df_cleaned = df_cleaned.drop_duplicates()  



# 1.
total_companies = len(df_cleaned)

# 2. 
average_sales = df_cleaned['Sales'].mean()

# 3.
top_companies_profit = df_cleaned.nlargest(5, 'Profit')[['Name', 'Profit']]

# 4. 
top_industry = df_cleaned['Industry'].value_counts().idxmax()

# 5. 
market_value_by_industry = df_cleaned.groupby('Industry')['Market Value'].mean().sort_values(ascending=False).head(5)

# 6.
top_country = df_cleaned['Country'].value_counts().idxmax()

# 7. 
total_employees = df_cleaned['Employees'].sum()

# 8.
highest_sales_company = df_cleaned.loc[df_cleaned['Sales'].idxmax()]

# 9.
average_profit_by_country = df_cleaned.groupby('Country')['Profit'].mean().sort_values(ascending=False).head(5)

# 10.
frequent_hq = df_cleaned['Headquarters'].value_counts().idxmax()

# 11. 
companies_before_1900 = len(df_cleaned[df_cleaned['Founded'] < 1900])

# 12.
average_employees = df_cleaned['Employees'].mean()

# 13.
companies_above_trillion = len(df_cleaned[df_cleaned['Market Value'] > 1000])

# 14. 
top_countries_sales = df_cleaned.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(5)

# 15. 
companies_high_profit_margin = len(df_cleaned[df_cleaned['Profit'] / df_cleaned['Sales'] > 0.3])

# 16.
average_assets_by_industry = df_cleaned.groupby('Industry')['Assets'].mean().sort_values(ascending=False).head(5)

# 17. 
most_employees_company = df_cleaned.loc[df_cleaned['Employees'].idxmax()]

# 18. 
small_industries = df_cleaned['Industry'].value_counts()[df_cleaned['Industry'].value_counts() < 5]

# Вывод результатов для проверки
print(f"Total companies: {total_companies}")
print(f"Average sales: {average_sales}")
print("Top 5 companies by profit:")
print(top_companies_profit)
print(f"Top industry by count: {top_industry}")
print("Top industries by market value:")
print(market_value_by_industry)
print(f"Country with most companies: {top_country}")
print(f"Total employees: {total_employees}")
print(f"Highest sales company: {highest_sales_company['Name']}")
print("Top 5 countries by profit:")
print(average_profit_by_country)
print(f"Most frequent headquarters: {frequent_hq}")
print(f"Companies founded before 1900: {companies_before_1900}")
print(f"Average employees per company: {average_employees}")
print(f"Companies with market value > $1T: {companies_above_trillion}")
print("Top 5 countries by total sales:")
print(top_countries_sales)
print(f"Companies with profit margin > 30%: {companies_high_profit_margin}")
print("Average assets by industry:")
print(average_assets_by_industry)
print(f"Company with most employees: {most_employees_company['Name']}")
print("Industries with fewer than 5 companies:")
print(small_industries)
