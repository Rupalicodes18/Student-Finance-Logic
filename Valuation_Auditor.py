# Pure Python Logic to calculate Enterprise Value (EV)

company_a = "Hype_Electric_Scooter"
market_cap_a = 50000000   # ₹5 Crore
debt_a = 40000000         # ₹4 Crore (Heavy Debt!)
cash_a = 2000000          # ₹20 Lakh

company_b = "Cash_Rich_AI"
market_cap_b = 50000000   # ₹5 Crore
debt_b = 5000000          # ₹50 Lakh
cash_b = 25000000         # ₹2.5 Crore (Massive Cash!)

# EV Function using pure arithmetic
def calculate_ev(m_cap, debt, cash):
    return m_cap + debt - cash

ev_a = calculate_ev(market_cap_a, debt_a, cash_a)
ev_b = calculate_ev(market_cap_b, debt_b, cash_b)

print(f"--- Valuation Audit ---")
print(f" {company_a} -> Market Cap: ₹{market_cap_a/10000000}Cr | Real capital (EV): ₹{ev_a/10000000}Cr\n")
print(f" {company_b} -> Market Cap: ₹{market_cap_b/10000000}Cr | Real capital (EV): ₹{ev_b/10000000}Cr\n")

# Decision Matrix
if ev_a > market_cap_a * 1.5:
    print(f" Warning on {company_a}: EV is too high due to massive debt. Avoid or short!")
if ev_b < market_cap_b:
    print(f" Deep Value on {company_b}: Company has more cash than debt. Investors' safety net is huge.")
  
