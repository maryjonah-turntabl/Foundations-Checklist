# Each class is concerned with a specific task

class Customer:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def get_details(self):
        return f"{self.first_name} {self.last_name} lives at {self.address}"


class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self):
        pass

    def withdraw(self):
        pass


class Bank:
    def _init__(self, branch_name, location):
        self.branch_name = branch_name
        self.location = location


client = Customer("Jane", "Doe", "A301-23, Imaginary Town")
print(client.get_details())

