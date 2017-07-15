
# lab 24: ATM

# version 1
# ATM class containing two attributes: a balance and an interest rate
# a newly created account will have a balance of 0 and an interest rate of 0.1%
# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account


# version 2
# have the ATM maintain a list of transactions
# e.g. every time the user makes a deposit or withdrawal
#     add a string to the list saying 'user deposited $15'
#     or 'user withdrew $15'
# add a new function for printing out the list of transactions

# version 3
# allow the user to enter commands
# e.g. 'what would you like to do? (deposit, withdraw, check balance)'
# the user would then be asked what amount they'd like to withdraw
# e.g. 'how much would you like to deposit?'


class AtmAccount:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('deposited $' + str(amount))

    def check_withdrawal(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append('withdrew $' + str(amount))

    def calc_interest(self):
        return self.balance * self.interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

atm = AtmAccount()

while True:
    command = input('what would you like to do? (deposit, withdraw, balance, transactions, exit) ')
    if command == 'exit':
        print('goodbye!')
        break
    elif command == 'deposit':
        amount = int(input('how much would you like to deposit? $'))
        atm.deposit(amount)
        print('\tdeposited $' + str(amount))
    elif command == 'withdraw':
        amount = int(input('how much would you like to withdraw? $'))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)
            print('\twithdrew $' + str(amount))
        else:
            print('you don\'t have that much money in your account')
    elif command == 'balance':
        print('your balance is: $' + str(atm.check_balance()))
    elif command == 'transactions':
        atm.print_transactions()
    else:
        print('command not recognized')






