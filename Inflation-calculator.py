def inflation_impact():
    print("---PURCHASING POWER CALCULATOR ---")
    
    current_money = float(input("Enter amount today (₹): "))
    inflation_rate = float(input("Average annual inflation % (e.g., 6): "))
    years = int(input("Number of years: "))
    
    # Formula: Purchasing Power = Amount / (1 + r)^n
    buying_power = current_money / ((1 + (inflation_rate/100))**years)
    
    print("-" * 35)
    print(f"Today's ₹{current_money:,.2f} will feel like ₹{buying_power:,.2f} after {years} years.")
    print(f"Advice: You need to earn more than {inflation_rate}% returns to grow wealth!")

inflation_impact()
