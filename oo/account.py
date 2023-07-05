class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print('Saldo do titular {} é de {}'.format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value):
        available_value = self.__balance + self.__limit
        return value <= available_value

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print('O valor {} ultrapassou seu limite!'.format(value))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    def get_balance(self):
        return self.__balance
    
    def get_holder(self):
        return self.__holder
    
    def get_limit(self):
        return self.__limit
    
    def set_limit(self, limit):
        self.__limit = limit

    @staticmethod
    def code_bank(self):
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
