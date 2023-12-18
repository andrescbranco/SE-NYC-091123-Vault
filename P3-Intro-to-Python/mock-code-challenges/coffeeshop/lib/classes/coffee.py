class Coffee:
    def __init__(self, name=str):
        self.name = name
        self.new_transaction = []
        self.new_customers = []


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self, 'name'):
            raise Exception
        self._name = name
        

    def __repr__(self):
        return f"Coffee: {self.name}"

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        if isinstance(new_transaction,Transaction):
            self.new_transaction.append(new_transaction)
        return list(self.new_transaction)


    def access_current_customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer,Customer):
            self.new_customers.append(new_customer)
        return list(set(self.new_customers))


    def calculate_total_number_of_transactions(self):
        return len(self.new_transaction)
    
    def calculate_average_price_across_all_transactions(self):
        total = 0
        for transaction in self.new_transaction:
            total += transaction.price
        return total/(Coffee.calculate_total_number_of_transactions(self))