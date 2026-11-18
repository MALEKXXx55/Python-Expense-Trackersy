expenses = []

def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    expenses.append({"description": description, "amount": amount})

def show_expenses():
    for item in expenses:
        print(item)

def show_total():
    print(sum(item["amount"] for item in expenses))

def main():
    while True:
        print("\n1. Add")
        print("2. Show")
        print("3. Total")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            break

main()

