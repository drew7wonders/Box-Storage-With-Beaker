import beaker

@beaker.box
def accounts():
accounts = {}
def add_account(account_id: str, balance: int):
    if account_id not in accounts:
        accounts[account_id] = balance

def get_balance(account_id: str) -> int:
    if account_id in accounts:
        return accounts[account_id]
    return 0

return {
    "add_account": add_account,
    "get_balance": get_balance
}
def main():
# Initialize the accounts box
accounts_box = accounts()
# Add a few accounts with initial balances
accounts_box.add_account("Alice", 1000)
accounts_box.add_account("Bob", 500)
accounts_box.add_account("Charlie", 250)

# Check the balances of the accounts
print(accounts_box.get_balance("Alice")) # Outputs: 1000
print(accounts_box.get_balance("Bob")) # Outputs: 500
print(accounts_box.get_balance("Charlie")) # Outputs: 250
main()
