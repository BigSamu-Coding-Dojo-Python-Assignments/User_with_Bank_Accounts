import random
import string

class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_number = ''.join(random.choices(string.digits,k = 10))
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info(self,name):
        print(f"Name: {name} Account: {self.account_number} Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+self.int_rate)
        else:
            print("Account overdrwan: No interests given")
        return self
    

class User:		# here's what we have so far
    # Constructor
    def __init__(self, name, email, number_of_accounts=1,init_rate=0,balance=0):
        self.name = name
        self.email = email
        self.number_of_accounts = number_of_accounts
        self.account = []
        for i in range(number_of_accounts):
            self.account.append(BankAccount(init_rate,balance))
    # adding the deposit method
    def make_deposit(self, amount, accountNumber):	
        self.account[self.account_index(accountNumber)].deposit(amount)
        return self
    
    # adding the withdrawal method
    def make_withdrawal(self, amount, accountNumber):	
        self.account[self.account_index(accountNumber)].withdraw(amount)
        return self
    
    # adding the display method
    def display_user_balance(self,accountNumber):
        self.account[self.account_index(accountNumber)].display_account_info(self.name)
        return self

    def transfer_money(self, amount, account_number_origin,user_recipient,account_number_destinatary): 
        self.make_withdrawal(amount, account_number_origin)
        user_recipient.make_deposit(amount, account_number_destinatary)
        print(f"Origin: {self.name} - Destinatary: {self.name} - Amount: {amount}")
        print(f"Origin Account: {account_number_origin} - Destinatary_Account: {account_number_destinatary}")

        return self

    def account_index(self,accountNumber):
        for i in range(self.number_of_accounts):
            if self.account[i].account_number == accountNumber:
                return i


# Create Two users, both of them with two accounts
guido = User("Guido van Rossum", "guido@python.com",number_of_accounts=2,init_rate=0,balance=0)
monty = User("Monty Python", "monty@python.com",number_of_accounts=2,init_rate=0,balance=0)

# We extract the account numbers of both users

#GUIDO INFO
print("\n","GUIDO INFO\n")

# Account Numbers of Guido
guido_account_number_1 = guido.account[0].account_number
guido_account_number_2 = guido.account[1].account_number

# We make a deposit of 100 and 200 on accounts 1 and 2 of Guido
guido.account[guido.account_index(guido_account_number_1)].deposit(100)
guido.account[guido.account_index(guido_account_number_2)].deposit(200)

# We get the status of accounts 1 and 2 of Guido
guido.display_user_balance(guido_account_number_1)
guido.display_user_balance(guido_account_number_2)

print("\n","*"*100,"\n")

#MONTI INFO
print("MONTI INFO\n")

# Account Numbers of Monty
monty_account_number_1 = monty.account[0].account_number
monty_account_number_2 = monty.account[1].account_number

# We make a deposit of 50 and 80 on accounts 1 and 2 of Monty
monty.account[monty.account_index(monty_account_number_1)].deposit(50)
monty.account[monty.account_index(monty_account_number_2)].deposit(80)

# We get the status of accounts 1 and 2 of Monty
monty.display_user_balance(monty_account_number_1)
monty.display_user_balance(monty_account_number_2)

print("\n","*"*100,"\n")

#TRANSFERENCES
print("TRANSFERS INFO\n")
guido.transfer_money(40,guido_account_number_1,monty,monty_account_number_1)

guido.display_user_balance(guido_account_number_1)
guido.display_user_balance(guido_account_number_2)
monty.display_user_balance(monty_account_number_1)
monty.display_user_balance(monty_account_number_2)

print("\n","*"*100,"\n")