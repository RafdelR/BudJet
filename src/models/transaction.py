class Transaction:
    def __init__(
        self,
        amount: float,
        date: str,
        source: str,
        category: str,
        description: str = "",
    ):
        """
        Represents a financial transaction.
        """
        self.amount = amount
        self.date = date
        self.source = source
        self.category = category
        self.description = description

    def __repr__(self):
        type_of_transaction = "Income" if self.amount > 0 else "Expense"
        return f"<Transaction {type_of_transaction} - {self.amount} on {self.date} ({self.category})>"
