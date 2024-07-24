import openpyxl

def budget_calculation(Einkommen, Miete, contracts):
    remaining = Einkommen - Miete - contracts
    Essen_fitness = remaining * 0.50
    remaining -= Essen_fitness
    books_education = remaining * 0.10
    remaining -= books_education
    vacation = remaining * 0.10
    remaining -= vacation
    family = remaining * 0.10
    remaining -= family
    savings = remaining
    
    return {
        "Miete": Miete,
        "Contracts": contracts,
        "Essen_fitness": Essen_fitness,
        "Books & Education": books_education,
        "Vacation": vacation,
        "Family": family,
        "Savings": savings
    }

def save_to_excel(data, filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Monthly Budget"
    
    headers = ["Category", "Amount"]
    sheet.append(headers)
    
    for category, amount in data.items():
        sheet.append([category, amount])
    
    workbook.save(filename)

def main():
    income = float(input("Enter your monthly income: "))
    rent = float(input("Enter your rent: "))
    contracts = float(input("Enter your contracts: "))
    
    budget = budget_calculation(income, rent, contracts)
    
    print("\nBudget Summary:")
    for category, amount in budget.items():
        print(f"{category}: {amount:.2f}")
    
    save_to_excel(budget, "Monthly_Budget.xlsx")
    print("\nBudget saved to 'Monthly_Budget.xlsx'")

if __name__ == "__main__":
    main()
