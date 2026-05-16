def professional_tax_calculator():
    print("==================================================")
    print("🏛️   FINTECH LOGIC: INDIAN INCOME TAX ENGINE (FY 2025-26) ")
    print("==================================================")
    
    gross_income = float(input("Enter Gross Annual Income (₹): "))
    
    # 1. Applying Standard Deduction under New Tax Regime
    standard_deduction = 75000
    taxable_income = max(0.0, gross_income - standard_deduction)
    
    # 2. Tax Rebate Check (Section 87A)
    # Under New Tax Regime, if taxable income <= ₹7,00,000, tax is fully rebated
    if taxable_income <= 700000:
        print("\n---TAX REPORT ---")
        print(f"Gross Annual Income:    ₹{gross_income:,.2f}")
        print(f"Standard Deduction:     ₹{standard_deduction:,.2f}")
        print(f"Taxable Income:         ₹{taxable_income:,.2f}")
        print("--------------------------------------------------")
        print("Tax Rebate (Sec 87A):   Eligible (100% Tax Relief)")
        print("Net Tax Payable:        ₹0.00")
        print("==================================================")
        return

    # 3. Progressive Tax Computation Layers
    base_tax = 0.0
    
    if taxable_income > 1500000:
        base_tax += (taxable_income - 1500000) * 0.30
        taxable_income = 1500000
    if taxable_income > 1200000:
        base_tax += (taxable_income - 1200000) * 0.20
        taxable_income = 1200000
    if taxable_income > 900000:
        base_tax += (taxable_income - 900000) * 0.15
        taxable_income = 900000
    if taxable_income > 600000:
        base_tax += (taxable_income - 600000) * 0.10
        taxable_income = 600000
    if taxable_income > 300000:
        base_tax += (taxable_income - 300000) * 0.05

    # 4. Adding 4% Health & Education Cess
    cess = base_tax * 0.04
    total_tax = base_tax + cess
    
    print("\n---TAX REPORT ---")
    print(f"Gross Annual Income:    ₹{gross_income:,.2f}")
    print(f"Standard Deduction:     ₹{-standard_deduction:,.2f}")
    print(f"Taxable Net Income:     ₹{gross_income - standard_deduction:,.2f}")
    print("--------------------------------------------------")
    print(f"Base Income Tax:        ₹{base_tax:,.2f}")
    print(f"Education/Health Cess:  ₹{cess:,.2f}")
    print("--------------------------------------------------")
    print(f"Total Tax Payable:      ₹{total_tax:,.2f}")
    print("==================================================")

if __name__ == "__main__":
    professional_tax_calculator()
      
