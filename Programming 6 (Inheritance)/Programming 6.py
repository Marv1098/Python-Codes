class SavingAccount:
    def __init__(self, account_num, interest_rate, balance):
        self.__account_num = account_num
        self.__interest_rate = interest_rate
        self.__balance = balance

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate / 100

    def get_balance(self):
        return self.__balance

    def check_balance(self):
        total = 0
        for item in self.__balance:
            total = total + item.check_balance()

    def apply_interest(self):
        self.__balance = self.__balance * (1 + self.__interest_rate/100)

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print('Error: Insufficient Balance.')

class CDAccount(SavingAccount):
    def __init__(self, account_num, interest_rate, balance, mini_balance):
        SavingAccount.__init__(self, account_num, interest_rate, balance)
        self.__mini_balance = mini_balance

    def get_mini_balance(self):
        return self.__mini_balance

    def CDwithdraw(self, amount):
        if self.get_balance() >= self.__mini_balance + amount:
            self.withdraw(amount)
        else:
            print('Insufficient amount')

def main():
    saving = SavingAccount(123, 1, 1200)
    print('Enter Information For Saving account')
    print('Account Number:', saving.get_account_num())
    print('Interest Rate:', saving.get_interest_rate())
    print('Initial Balance:$', saving.get_balance())
    saving.deposit(600)
    print('Balance After deposit:$', saving.get_balance())
    saving.apply_interest()
    print('Balance after interest rate:', saving.get_balance())
    saving.withdraw(600)
    print('Balance after withdraw:$', saving.get_balance())
    print('\n')

    account = CDAccount(321, 3, 2500, 2000)
    print('Enter Information For CD Account')
    print('Account Number:', account.get_account_num())
    print('Interest Rate:', account.get_interest_rate())
    print('Initial Balance:$', account.get_balance())
    print('Minimum Balance:$', account.get_mini_balance())
    account.deposit(600)
    print('Balance after deposit:$', account.get_balance())
    account.apply_interest()
    print('Balance after interest:$', account.get_balance())
    account.CDwithdraw(800)
    print('Balance after withdraw:$', account.get_balance())

main()
