class Category:
    def __init__(self, name: str, parent_category: str = None):
        """
        Represents a category for an account or transaction.
        """
        self.name = name
        self.parent_category = parent_category

    def __repr__(self):
        return f"<Category {self.name} - Parent: {self.parent_category if self.parent_category else 'None'}>"
