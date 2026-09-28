"""
main.py
--------
Simple ATM Simulation - CLI entry point.

Author : Preksha Jain
Reg No : 26MIM10089
Institute : VIT Bhopal University, 1st Year Integrated M.Tech (AI)

Run with:  python main.py

This module wires together the three functional modules of the project:
  1. Account Management   (create account, login, change PIN)
  2. Transaction Processing (deposit, withdraw, transfer)
  3. Transaction History & Reporting (mini statement, full history)
"""

import sys

from atm.bank import Bank
from atm.auth import login
from atm.storage import load_accounts, save_accounts
from atm.exceptions import ATMError
from atm.validators import validate_account_number, validate_pin, validate_name

DATA_FILE = "data/accounts.json"


# ---------------------------------------------------------------- helpers

def prompt(text):
    return input(text).strip()


def pause():
    input("\nPress Enter to continue...")


# ---------------------------------------------------------- account menus

def create_account_flow(bank):
    print("\n--- Create New Account ---")
    try:
        name = validate_name(prompt("Enter your full name: "))
        pin = validate_pin(prompt("Set a 4-digit PIN: "))
        confirm_pin = validate_pin(prompt("Confirm PIN: "))
        if pin != confirm_pin:
            print("PINs do not match. Account not created.")
            return
        deposit_str = prompt("Initial deposit amount (0 for none): ") or "0"
        account = bank.create_account(name, pin, initial_deposit=deposit_str)
        save_accounts(bank, DATA_FILE)
        print(f"\nAccount created successfully!")
        print(f"Your account number is: {account.account_number}")
        print("Please save this number - you will need it to log in.")
    except (ATMError, ValueError) as e:
        print(f"Error: {e}")
    pause()


def login_flow(bank):
    print("\n--- Login ---")
    try:
        acc_number = validate_account_number(prompt("Account number: "))
        pin = prompt("PIN: ")
        account = login(bank, acc_number, pin)
        print(f"\nWelcome, {account.name}!")
        account_menu(bank, account)
    except (ATMError, ValueError) as e:
        print(f"Error: {e}")
        pause()


# ---------------------------------------------------------- account menu

def account_menu(bank, account):
    while True:
        print(f"\n=== Account Menu ({account.account_number}) ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. Mini Statement (last 5 transactions)")
        print("6. Full Transaction History")
        print("7. Change PIN")
        print("8. Logout")
        choice = prompt("Choose an option: ")

        try:
            if choice == "1":
                print(f"Current balance: {account.balance:.2f}")

            elif choice == "2":
                amount = prompt("Amount to deposit: ")
                txn = account.deposit(amount)
                print(f"Deposit successful. {txn}")
                save_accounts(bank, DATA_FILE)

            elif choice == "3":
                amount = prompt("Amount to withdraw: ")
                txn = account.withdraw(amount)
                print(f"Withdrawal successful. {txn}")
                save_accounts(bank, DATA_FILE)

            elif choice == "4":
                to_number = validate_account_number(prompt("Recipient account number: "))
                amount = prompt("Amount to transfer: ")
                bank.transfer(account.account_number, to_number, amount)
                print(f"Transfer of {float(amount):.2f} to {to_number} successful.")
                save_accounts(bank, DATA_FILE)

            elif choice == "5":
                stmt = account.mini_statement(5)
                if not stmt:
                    print("No transactions yet.")
                for txn in stmt:
                    print(txn)

            elif choice == "6":
                if not account.transactions:
                    print("No transactions yet.")
                for txn in reversed(account.transactions):
                    print(txn)

            elif choice == "7":
                old_pin = prompt("Current PIN: ")
                new_pin = validate_pin(prompt("New PIN: "))
                account.change_pin(old_pin, new_pin)
                save_accounts(bank, DATA_FILE)
                print("PIN changed successfully.")

            elif choice == "8":
                print("Logged out.")
                break

            else:
                print("Invalid option. Please choose 1-8.")

        except (ATMError, ValueError) as e:
            print(f"Error: {e}")

        pause()


# ------------------------------------------------------------- main loop

def main():
    bank = Bank()
    n = load_accounts(bank, DATA_FILE)
    if n:
        print(f"Loaded {n} existing account(s) from {DATA_FILE}.")

    print("=" * 50)
    print("   SIMPLE ATM SIMULATION")
    print("   Preksha Jain | Reg No: 26MIM10089")
    print("   VIT Bhopal University")
    print("=" * 50)

    while True:
        print("\n=== Main Menu ===")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        choice = prompt("Choose an option: ")

        if choice == "1":
            create_account_flow(bank)
        elif choice == "2":
            login_flow(bank)
        elif choice == "3":
            print("Thank you for using Simple ATM Simulation. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose 1-3.")


if __name__ == "__main__":
    main()
