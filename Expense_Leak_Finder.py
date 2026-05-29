import sqlite3
from datetime import datetime

# ========================================================================
# RELATIONAL EXPENSE DATABASE SETUP
# ========================================================================
def init_expense_db():
    conn = sqlite3.connect("expense_core.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            is_essential INTEGER
        )
    """)
    conn.commit()
    return conn

# ========================================================================
# LEAK DETECTION LOGIC ENGINE
# ========================================================================
def analyze_leaks(cursor, monthly_budget):
    cursor.execute("SELECT category, SUM(amount), is_essential FROM expenses GROUP BY category")
    data = cursor.fetchall()
    
    if not data:
        return 0, []
        
    total_spent = 0
    leaks = []
    
    for category, amount, is_essential in data:
        total_spent += amount
        # Condition: If non-essential spending in a single category exceeds 15% of total budget
        if is_essential == 0 and amount > (monthly_budget * 0.15):
            leaks.append((category, amount))
            
    return total_spent, leaks

# ========================================================================
# TERMINAL USER INTERFACE
# ========================================================================
def main():
    conn = init_expense_db()
    cursor = conn.cursor()
    
    # Simple predefined budget line for a student/aspirant
    budget_limit = 5000.0 
    
    while True:
        print("\n" + "="*50)
        print("      STUDENT EXPENSE & LEAK FINDER v1.0 ")
        print("="*50)
        print(f"Current Monthly Target Budget: {budget_limit} INR")
        print("-"*50)
        print("1. Log New Expense/Subscription Vector")
        print("2. Launch Financial Leak Audit")
        print("3. Wipe Expense Log History (Purge)")
        print("4. Close Core Terminal Portal")
        
        choice = input("\nSelect system node (1-4): ")
        
        if choice == "1":
            category = input("Enter Expense Category (e.g., Food, Subscriptions, Books): ").strip()
            try:
                amount = float(input("Enter Amount Spent (INR): "))
                essential_input = input("Is this an absolute essential/survival expense? (y/n): ").strip().lower()
                is_essential = 1 if essential_input == 'y' else 0
                
                current_date = datetime.now().strftime("%Y-%m-%d")
                
                cursor.execute("""
                    INSERT INTO expenses (category, amount, date, is_essential)
                    VALUES (?, ?, ?, ?)
                """, (category, amount, current_date, is_essential))
                conn.commit()
                print("\n Data Matrix Injected Successfully!")
            except ValueError:
                print("\n[X] Format Error: Amount must be numerical.")
                
        elif choice == "2":
            total, leaks = analyze_leaks(cursor, budget_limit)
            print("\n" + "="*45)
            print("        --- FINANCIAL AUDIT REPORT ---")
            print("="*45)
            print(f"Total Aggregated Spending: {total} / {budget_limit} INR")
            
            if total > budget_limit:
                print("[ALERT] SYSTEM OUT OF EQUILIBRIUM: Budget exceeded!")
            else:
                print("Capital boundaries intact within target thresholds.")
                
            print("\n[-] Non-Essential Financial Leaks Detected:")
            if not leaks:
                print("  * None! Allocation behavior is completely optimized.")
            else:
                for cat, amt in leaks:
                    print(f"  * [LEAK] '{cat}' is draining {amt} INR (Critical Limit Cross!)")
                    
        elif choice == "3":
            cursor.execute("DELETE FROM expenses")
            conn.commit()
            print("\n[!] Data history completely purged.")
            
        elif choice == "4":
            print("\nTerminating Connection Core. Safe Exit. ")
            conn.close()
            break
        else:
            print("\n[X] Invalid operational node choice.")

if __name__ == "__main__":
    main()
  
