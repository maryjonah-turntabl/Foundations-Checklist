# Only corporate accounts need to be taxed so all CorporateAccount inherit from both Taxable and Account classes
# KiddiesAccount is not taxed, so it inherits the Account class only

from abc import ABC, abstractmethod


class Taxable(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass


class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def get_details(self):
        return f"The account {self.account_number} currently has ${self.balance}"

    def deposit(self):
        pass

    def withdraw(self, amount):
        if self.balance < amount:
            return f"Sorry, you cannot withdraw an amount higher than your balance ${self.balance}"


class KiddiesAccount(Account):
    def __init__(self, account_number, education_policy=True):
        super().__init__(account_number)
        self.education_policy = education_policy

    def get_details(self):
        return f"This is a kiddie account and is eligible for an education policy"


class CorporateAccount(Account, Taxable):
    def __init__(self, account_number, current_account=True):
        super().__init__(account_number)
        self.current_account = current_account

    def calculate_tax(self):
        return f"Tax to be paid: " + str(self.balance * 0.01)

    def get_details(self):
        return f"This corporate account has a client relationship manager.\nCall 111-222-333 for more details."


kiddie_account = KiddiesAccount(123)
print(kiddie_account.get_details())

corporate_account = CorporateAccount(321)
print(corporate_account.calculate_tax())
print(corporate_account.get_details())
