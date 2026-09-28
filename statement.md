# Problem Statement

**Project:** Simple ATM Simulation
**Author:** Preksha Jain (Reg. No. 26MIM10089)
**Institute:** VIT Bhopal University — 1st Year Integrated M.Tech (AI)
**Course:** Python Essentials

## Problem Statement

Traditional bank branch visits for basic operations such as checking a
balance, depositing or withdrawing cash, or transferring funds are
time-consuming and inconvenient. ATMs solve this by giving customers a
self-service interface for routine banking. This project simulates the
core behavior of a real ATM using Python, applying object-oriented design,
secure authentication, and persistent storage — without requiring any
physical hardware or a real banking backend.

The simulation addresses the need for a lightweight, offline, easy-to-run
demonstration of how an ATM system authenticates a user, safely processes
money movement, and maintains an auditable transaction history, while
reinforcing the Python concepts taught in this course (functions,
control flow, data structures, modules, and OOP).

## Scope of the Project

**In scope:**
- Single-bank simulation with multiple customer accounts
- PIN-based authentication with lockout after repeated failures
- Deposit, withdrawal, and transfer operations with input validation
- Persistent storage of accounts and transaction history in a local
  JSON file
- Command-line interface (menu-driven)
- Unit tests for core account and bank logic

**Out of scope (not implemented, to keep the project appropriately
scoped for a beginner Python Essentials capstone):**
- A graphical user interface (GUI) or web interface
- Multi-bank / interbank transfers
- Real-time integration with an actual banking network or card reader
- Multi-currency support
- Concurrent/multi-user simultaneous access (the app is single-session)

## Target Users

- Bank customers who want a self-service way to check balances, deposit
  or withdraw cash, and transfer funds between accounts.
- In the context of this project: evaluators/reviewers assessing the
  application of Python Essentials concepts (functions, data structures,
  control flow, modules/packages, and OOP) in a realistic, relatable
  problem domain.

## High-Level Features

1. **Account Management** — create an account, log in securely with a
   4-digit PIN, change PIN, automatic lockout after 3 failed attempts.
2. **Transaction Processing** — deposit funds, withdraw funds (with
   insufficient-funds protection), transfer funds between accounts.
3. **Transaction History & Reporting** — mini statement (last 5
   transactions) and full transaction history with timestamps and
   running balance.
4. **Persistence** — all account and transaction data is saved to disk
   (`data/accounts.json`) and reloaded automatically on the next run.
