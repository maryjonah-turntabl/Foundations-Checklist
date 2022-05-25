# The Account class has the generic methods
# It is available to be extended to new classes that include their specialized implementation
# Kiddies takes an extra argument which provides an education_policy for all account holders, it also
# In the same vein, CorporateAccount is also takes the current_account argument which makes all corporate accounts current accounts


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


class CorporateAccount(Account):
    def __init__(self, account_number, current_account=True):
        super().__init__(account_number)
        self.current_account = current_account

    def get_details(self):
        return f"This corporate account has a client relationship manager.\nCall 111-222-333 for more details."


kiddie_account = KiddiesAccount(123)
print(kiddie_account.get_details())
print(kiddie_account.withdraw(100))

corporate_account = CorporateAccount(321)
print(corporate_account.withdraw(1))
print(corporate_account.get_details())
