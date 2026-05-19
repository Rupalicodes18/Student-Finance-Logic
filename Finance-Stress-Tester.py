def analyze_financial_health(income, fixed_expenses, variable_expenses, current_savings):
    """
    Analyzes monthly survival runway and stress tests personal finances.
    """
    total_expenses = fixed_expenses + variable_expenses
    monthly_savings = income - total_expenses
    
    # 1. Calculate Savings Rate
    savings_rate = (monthly_savings / income) * 100 if income > 0 else 0
    
    # 2. Calculate Survival Runway (How many months can you survive on savings if income drops to 0?)
    runway_months = current_savings / total_expenses if total_expenses > 0 else 0
    
    # 3. Recommended Emergency Fund (Standard 6 Months of mandatory survival expenses)
    recommended_emergency_fund = fixed_expenses * 6
    fund_gap = recommended_emergency_fund - current_savings
    
    return total_expenses, savings_rate, runway_months, recommended_emergency_fund, fund_gap

def main():
    print("==================================================")
    print(" PERSONAL FINANCE STRESS TESTER & RISK ENGINE")
    print("==================================================")
    
    try:
        income = float(input("Enter Monthly Net Income (₹): "))
        fixed_expenses = float(input("Enter Mandatory Fixed Expenses (Rent, Food, Bills) (₹): "))
        variable_expenses = float(input("Enter Variable Expenses (Entertainment, Shopping) (₹): "))
        current_savings = float(input("Enter Current Liquid Savings/Emergency Cash (₹): "))
    except ValueError:
        print("\n[!] Please enter valid numerical values.")
        return

    if fixed_expenses + variable_expenses > income:
        print("\n WARNING: Your monthly expenses exceed your income! You are in a deficit.")

    total_expenses, savings_rate, runway, target_fund, gap = analyze_financial_health(
        income, fixed_expenses, variable_expenses, current_savings
    )
    
    print("\n" + "="*45)
    print("FINANCIAL DIAGNOSTIC REPORT")
    print("="*45)
    print(f"Total Monthly Outflow  : ₹{total_expenses:,.2f}")
    print(f"Monthly Savings Rate   : {savings_rate:.2f}%")
    print(f"Financial Runway       : {runway:.1f} Months of Survival")
    print(f"Target Emergency Fund  : ₹{target_fund:,.2f} (6-Month Base)")
    
    print("-" * 45)
    if gap <= 0:
        print(" STATUS: Secure! Your emergency buffer is fully funded.")
    else:
        print(f" STATUS: Vulnerable! You need ₹{gap:,.2f} more to secure your fund.")
    print("="*45)

if __name__ == "__main__":
    main()
  
