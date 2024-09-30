
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


def main():
    accounts = {}
    
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter your name: ")
            if name not in accounts:
                accounts[name] = BankAccount(name)
                print(f"Account created for {name}.")
            else:
                print("Account already exists.")

        elif choice == '2':
            name = input("Enter your name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter your name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            name = input("Enter your name: ")
            if name in accounts:
                balance = accounts[name].get_balance()
                print(f"Balance for {name}: ${balance:.2f}")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
