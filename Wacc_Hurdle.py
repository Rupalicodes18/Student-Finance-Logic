# Pure Python Logic - WACC Calculator
company = "Future AI-Med Startup"

# 1. Capital Structure Inputs
equity = 700000        # ₹7 Lakhs from Angel Investors
debt = 300000          # ₹3 Lakhs Bank Loan
total_value = equity + debt

# 2. Cost of Capital Rates (as decimals)
cost_of_equity = 0.15  # Investors expect 15% return
cost_of_debt = 0.09    # Bank charges 9% interest
tax_rate = 0.25        # 25% Corporate Tax

# 3. Weights Calculation
weight_of_equity = equity / total_value
weight_of_debt = debt / total_value

# 4. WACC Formula Execution
wacc = (weight_of_equity * cost_of_equity) + (weight_of_debt * cost_of_debt * (1 - tax_rate))

print(f"--- {company} Capital Audit ---")
print(f"Weight of Equity: {weight_of_equity * 100:.1f}%")
print(f"Weight of Debt:   {weight_of_debt * 100:.1f}%")
print(f"Your WACC (Hurdle Rate): {wacc * 100:.2f}%\n")

# 5. Strategic Parameter Check
project_expected_return = 0.11  # New project returns 11%

if project_expected_return > wacc:
    print("GREEN LIGHT: Project creates value. Capital structure can sustain this.")
else:
    print("RED LIGHT: Reject project. Return is lower than cost of capital — value destruction.")
