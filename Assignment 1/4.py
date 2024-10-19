# Function for graphical representation with annotations for three price situations

def annotated_collar_strategy_graph(put_strike, call_strike, premium_put, premium_call):
    price_range = np.linspace(60, 80, 100)
    payoff_put = np.maximum(put_strike - price_range, 0) - premium_put
    payoff_call = -(np.maximum(price_range - call_strike, 0)) + premium_call
    total_payoff = payoff_put + payoff_call

    plt.figure(figsize=(8,6))
    plt.plot(price_range, total_payoff, label="Collar Strategy", color="purple")
    plt.axhline(0, color="black",linewidth=0.5)

    # Annotate key price points
    plt.annotate('Spot < Put Strike (Max Profit)', xy=(62, total_payoff[5]), xytext=(63, total_payoff[5] + 2),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot between Strikes (Loss: Premium)', xy=(70, total_payoff[40]), xytext=(71, total_payoff[40] - 2),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot > Call Strike (Capped Profit)', xy=(75, total_payoff[80]), xytext=(76, total_payoff[80] - 3),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xlabel("Crude Oil Price ($/barrel)")
    plt.ylabel("Payoff ($/barrel)")
    plt.title("Annotated Collar Strategy (Put and Call Combination)")
    plt.legend()
    plt.grid(True)
    plt.show()

def annotated_calendar_spread_graph(short_premium, long_premium):
    price_range = np.linspace(60, 80, 100)
    payoff_short = np.maximum(69.0 - price_range, 0) - short_premium  # 1M put option payoff
    payoff_long = np.maximum(69.0 - price_range, 0) - long_premium  # 3M put option payoff
    spread_payoff = payoff_long - payoff_short

    plt.figure(figsize=(8,6))
    plt.plot(price_range, spread_payoff, label="Calendar Spread Strategy", color="orange")
    plt.axhline(0, color="black",linewidth=0.5)

    # Annotate key price points
    plt.annotate('Spot < Strike (Moderate Profit)', xy=(62, spread_payoff[5]), xytext=(63, spread_payoff[5] + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot between Strikes (Neutral)', xy=(70, spread_payoff[40]), xytext=(71, spread_payoff[40] + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot > Strike (Loss: Premium)', xy=(75, spread_payoff[80]), xytext=(76, spread_payoff[80] + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xlabel("Crude Oil Price ($/barrel)")
    plt.ylabel("Payoff ($/barrel)")
    plt.title("Annotated Calendar Spread Strategy")
    plt.legend()
    plt.grid(True)
    plt.show()

def annotated_strangle_strategy_graph(put_strike, call_strike, premium_put, premium_call):
    price_range = np.linspace(60, 80, 100)
    payoff_put = np.maximum(put_strike - price_range, 0) - premium_put
    payoff_call = np.maximum(price_range - call_strike, 0) - premium_call
    total_payoff = payoff_put + payoff_call

    plt.figure(figsize=(8,6))
    plt.plot(price_range, total_payoff, label="Strangle Strategy", color="darkred")
    plt.axhline(0, color="black",linewidth=0.5)

    # Annotate key price points
    plt.annotate('Spot < Put Strike (Profit)', xy=(62, total_payoff[5]), xytext=(63, total_payoff[5] + 1),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot between Strikes (Loss: Premiums)', xy=(70, total_payoff[40]), xytext=(71, total_payoff[40] - 1),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Spot > Call Strike (Profit)', xy=(75, total_payoff[80]), xytext=(76, total_payoff[80] + 1),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xlabel("Crude Oil Price ($/barrel)")
    plt.ylabel("Payoff ($/barrel)")
    plt.title("Annotated Strangle Strategy (Put and Call Out of the Money)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Drawing all strategies with annotations
annotated_collar_strategy_graph(put_strike=69.0, call_strike=73.0, premium_put=2.60, premium_call=2.10)
annotated_calendar_spread_graph(short_premium=2.60, long_premium=3.90)
annotated_strangle_strategy_graph(put_strike=67.0, call_strike=75.0, premium_put=1.30, premium_call=0.60)
