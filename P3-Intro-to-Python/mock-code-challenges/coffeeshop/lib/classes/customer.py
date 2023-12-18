class Customer:    
    def __init__(self, name):
        self.name = name
        self.new_transaction = []
        self.new_coffee = []

    @property
    def name(self):
        return str(self._name)
    
    @name.setter
    def name(self, name):
        if len(name)<1 or len(name)>15 or not isinstance(name, str):
            raise Exception
        self._name = name

    def __repr__(self):
        return f"Customer: {self.name}"

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        if isinstance(new_transaction,Transaction):
            self.new_transaction.append(new_transaction)
        return list(self.new_transaction)
    
    def access_current_coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self.new_coffee.append(new_coffee)
        return list(set(self.new_coffee))

    def place_order(self, name_of_coffee=str, price=int):
        from classes.transaction import Transaction
        from classes.coffee import Coffee
        return (Transaction(self, Coffee(name_of_coffee), price))


    def calculate_total_money_spent(self):
        spent = 0
        for transaction in self.new_transaction:
            spent += transaction.price
        return spent

    def retrieve_coffees_within_price_range(self, min_price=0, max_price=999):
        filtered_coffees = []
        for transaction in self.new_transaction:
            if transaction.price > min_price and transaction.price <max_price:
                filtered_coffees.append(transaction.coffee)
        return filtered_coffees