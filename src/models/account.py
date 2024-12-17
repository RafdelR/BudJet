class Account:
    def __init__(
        self, name: str, account_type: str, balance: float, bank_name: str
    ) -> None:
        """
        Represents a bank account.
        """
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.bank_name = bank_name

    def update_balance(self, new_balance: float):
        """Updates the balance of the account."""
        self.balance = new_balance

    def __repr__(self):
        return f"<Account {self.name} ({self.account_type}) - Balance: ${self.balance:.2f}>"
