# Simple ATM Simulation

**Author:** Preksha Jain
**Registration No.:** 26MIM10089
**Institute:** VIT Bhopal University — 1st Year Integrated M.Tech (AI)
**Course:** Python Essentials

---

## Overview

A command-line ATM simulation built in Python that models the core
functionality of a real ATM/banking system: account creation, secure
PIN-based login, deposits, withdrawals, inter-account transfers, and
transaction history reporting. All account data is persisted to a local
JSON file so balances and history survive between runs.

The project was built as a capstone for the Python Essentials course,
applying core data structures, control flow, functions, modules/packages,
and object-oriented programming (classes, encapsulation) covered across
the syllabus.

## Features

- **Account Management**
  - Create a new account with name, 4-digit PIN, and optional initial deposit
  - Auto-generated unique 6-digit account number
  - Secure login with PIN verification
  - Change PIN (requires current PIN)
  - Account auto-locks after 3 consecutive failed PIN attempts
- **Transaction Processing**
  - Deposit funds
  - Withdraw funds (blocked if it would overdraw the account)
  - Transfer funds to another account by account number
- **Transaction History & Reporting**
  - Mini statement (last 5 transactions)
  - Full transaction history with timestamps and running balance
- **Persistence & Reliability**
  - All data saved to `data/accounts.json` after every change
  - Data reloaded automatically on next run

## Technologies / Tools Used

- **Language:** Python 3.10+
- **Standard library only** — no external dependencies (`hashlib`, `json`,
  `datetime`, `random`, `unittest`)
- **Testing:** `unittest` (Python's built-in test framework)
- **Version control:** Git / GitHub

## Project Structure

```
atm-simulation/
├── main.py                # CLI entry point / menu loop
├── atm/
│   ├── __init__.py        # package exports
│   ├── account.py         # Account class (OOP core: PIN security, deposit/withdraw)
│   ├── bank.py             # Bank class (manages all accounts, transfers)
│   ├── transaction.py      # Transaction data structure
│   ├── auth.py             # Login / authentication flow
│   ├── storage.py          # JSON persistence (save/load)
│   └── validators.py       # Input validation helpers
├── tests/
│   ├── test_account.py     # Unit tests for Account
│   └── test_bank.py        # Unit tests for Bank
├── data/
│   └── accounts.json       # Persisted account data (auto-created/updated)
├── README.md
├── statement.md
└── DESIGN.md               # Architecture, workflow & UML diagrams
```

## How to Install & Run

**Requirements:** Python 3.10 or newer. No external packages needed.

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd atm-simulation

# 2. Run the application (no pip install required)
python main.py
```

On first run, the app starts with no accounts. Use **Option 1** from the
main menu to create an account, note down the generated account number,
then use **Option 2** to log in.

## How to Test

Unit tests cover account security (PIN hashing, lockout), deposits,
withdrawals, insufficient-funds handling, and bank-level transfers.

```bash
# Run all tests
python -m unittest discover tests -v

# Or run a specific test file
python -m unittest tests.test_account -v
python -m unittest tests.test_bank -v
```

All 17 tests pass as of the latest commit.

## Sample Usage

```
=== Main Menu ===
1. Create New Account
2. Login to Existing Account
3. Exit
Choose an option: 1

--- Create New Account ---
Enter your full name: Preksha Jain
Set a 4-digit PIN: 1234
Confirm PIN: 1234
Initial deposit amount (0 for none): 1000

Account created successfully!
Your account number is: 410215
```

## Screenshots

_Add terminal screenshots of account creation, login, deposit/withdrawal,
and mini-statement output here before final submission._

## Design & Security Notes

- PINs are never stored in plain text — they are hashed with SHA-256
  before being written to disk.
- All monetary inputs are validated (positive numbers, max 2 decimal
  places) before any balance is modified.
- Transfers use a withdraw-then-deposit sequence and raise before any
  state changes if the source account has insufficient funds, so a
  failed transfer never leaves balances inconsistent.

See `DESIGN.md` for the system architecture, workflow, and UML diagrams,
and `statement.md` for the problem statement and scope.
