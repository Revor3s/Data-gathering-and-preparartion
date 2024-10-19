import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Удаляем дубликаты зарплат, сортируем по убыванию
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Проверяем, есть ли вторая по величине зарплата
    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.iloc[1]  # Вторая по величине зарплата
    else:
        second_highest = None  # Если второй зарплаты нет
    
    # Формируем результат в виде DataFrame
    result = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    
    return result

# Пример данных для таблицы Employee
data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}
employee = pd.DataFrame(data)

# Вызов функции
result = second_highest_salary(employee)
print(result)
