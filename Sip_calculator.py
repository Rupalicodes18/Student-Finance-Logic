import math

def wealth_planner():
    """
    A tool to calculate the future value of monthly investments (SIP).
    Formula: FV = P * [({(1 + r)^n} - 1) / r] * (1 + r)
    """
    print("\n" + "="*40)
    print("FUTURE WEALTH CALCULATOR (SIP)")
    print("="*40)

    is_active = True
    while is_active:
        # User Inputs
        monthly_invest = float(input("\nMonthly Investment Amount (₹): "))
        annual_rate = float(input("Expected Annual Return % (e.g., 12 or 15): "))
        years = int(input("Time Period (Years): "))

        # Monthly conversion
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12

        # SIP Formula: Future Value
        # FV = P × ((1 + i)^n - 1) / i × (1 + i)
        future_value = monthly_invest * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
        
        total_invested = monthly_invest * months
        wealth_gained = future_value - total_invested

        # --- Report ---
        print("\n" + "-"*15 + " INVESTMENT REPORT " + "-"*15)
        print(f"Total Amount Invested : ₹{total_invested:,.2f}")
        print(f"Estimated Future Value : ₹{future_value:,.2f}")
        print(f" Wealth Gained (Interest): ₹{wealth_gained:,.2f}")
        print("-" * 47)

        # Insight Logic
        if wealth_gained > total_invested:
            print(" Insight: Your interest is more than your investment! That's Compounding.")
        else:
            print(" Insight: Give it more time to see the magic of exponential growth.")

        # Control
        choice = input("\nCalculate another goal? (y/n): ").lower()
        if choice != 'y':
            is_active = False
            print("Keep saving, keep coding! See you soon. ")

if __name__ == "__main__":
    wealth_planner()
      
