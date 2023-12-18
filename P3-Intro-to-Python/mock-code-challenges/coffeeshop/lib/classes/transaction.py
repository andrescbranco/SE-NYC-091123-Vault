class Transaction:
    counter, catalog = 0, []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Transaction.counter += 1
        Transaction.catalog.append(self)

        coffee.access_current_transactions(self)
        coffee.access_current_customers(customer)

        customer.access_current_coffees(coffee)
        customer.access_current_transactions(self)
        

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price > 50 or price < 1:
            raise Exception
        self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer (self,customer):
        from classes.customer import Customer
        if not isinstance(customer, Customer):
            raise Exception
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee (self,coffee):
        from classes.coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise Exception
        self._coffee = coffee
    

    def __repr__(self):
        return f"{self.customer.name} ordered a {self.coffee.name} for ${self.price}."