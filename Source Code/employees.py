class Employee:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.daily_transactions = 0

    def transactions_increment(self):
        self.daily_transactions += 1

    def get_transactions(self):
        return self.daily_transactions

    def check_password(self, name,password):
        return self.password == password and self.name == name