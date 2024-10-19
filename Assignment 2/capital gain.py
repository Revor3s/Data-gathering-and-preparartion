import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:

    stocks = stocks.sort_values(by=['stock_name', 'operation_day']).reset_index(drop=True)
    
    gain_loss = {}
    
    
    for stock_name in stocks['stock_name'].unique():
        stock_data = stocks[stocks['stock_name'] == stock_name]
        total_gain_loss = 0
        buy_stack = []  
        
        
        for index, row in stock_data.iterrows():
            if row['operation'] == 'Buy':
                buy_stack.append(row['price'])  
            elif row['operation'] == 'Sell' and buy_stack:
                buy_price = buy_stack.pop(0)  
                sell_price = row['price']
                total_gain_loss += (sell_price - buy_price)  

        gain_loss[stock_name] = total_gain_loss

    result = pd.DataFrame(list(gain_loss.items()), columns=['stock_name', 'capital_gain_loss']).sort_values(by='stock_name').reset_index(drop=True)
    
    return result

data = {
    'stock_name': ['Leetcode', 'Corona Masks', 'Leetcode', 'Handbags', 'Corona Masks', 'Corona Masks', 
                   'Corona Masks', 'Corona Masks', 'Handbags', 'Corona Masks'],
    'operation': ['Buy', 'Buy', 'Sell', 'Buy', 'Sell', 'Buy', 'Sell', 'Buy', 'Sell', 'Sell'],
    'operation_day': [1, 2, 5, 17, 3, 4, 5, 6, 29, 10],
    'price': [1000, 10, 9000, 30000, 1010, 1000, 500, 1000, 7000, 10000]
}
stocks = pd.DataFrame(data)

result = capital_gainloss(stocks)
print(result)
