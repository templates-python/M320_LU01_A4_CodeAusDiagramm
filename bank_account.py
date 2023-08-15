class BankAccount:

    def __init__(self, max_overdraft, customer):
        self.__balance   = 0.0
        self.__overdraft = max_overdraft
        self.__customer  = customer

    @property
    def balance(self):
        return self.__balance

    @property
    def overdraft(self):
        return self.__overdraft

    @property
    def customer(self):
        return self.__customer


    def booking(self, amount):
        self.__balance += amount

    def get_money(self, amount):
        if (self.__balance + self.__overdraft) > amount:
            self.__balance -= amount
            return amount
        else:
            return 0.0




