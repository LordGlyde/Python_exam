import datetime
history = {}

class Account(object):
	def __init__(self):
		self.pin = 1234
		self.

	def checkBalance(self):
		print (('Current balance is ') + str(self.balance) + ' peso(s).')

       
        def withdrawal(self, amount):
        "withdrawal processing"
        self.amount = amount
        if self.amount > BankingCustomer.allCustomers[self.name]:
            print(.format(self.name, self.amount))
        else:
            print("\n{} took {} USD from his account.".format(self.name, self.amount))
            BankingCustomer.allCustomers[self.name] -= self.amount
        print("{}\'s account balance is {} USD.".format(self.name, BankingCustomer.allCustomers[self.name]))

	def withdraw(self, value):
		if value <= self.balance:
			self.balance -= value
			print (('Successfully withdrawn ') + str(value) + ' peso(s) from your account.')
		else:
			print('Not enough balance.')

	def deposit(self, pin, value):
		if self.checkCode(pin):
			self.balance += value
			print (('Successfully deposited ') + str(value) + ' peso(s) from your account.')
		else:
			print ('Wrong pin code. Try again.')


class CheckingAccount(Account):
	def __init__(self):
		super(CheckingAccount, self).__init__()
		self.balance = 50000


checksAcc = CheckingAccount()
def print_menu():
    print ("1. List Account(s)\n2. Open an Account\n3. Close an Account")
    print ("4. Withdraw money\n5. Deposit Money\n6. Quit")
    print

accounts = {}
choice = 0
print_menu()
balance = 0
while True:
    choice = int(input("Input here: "))
    print
    if choice == 1:
        print ("Enter a new Accountnumber")
        number = input("New accountnumber: ")
        accounts[number]=balance
        print ("Accountnumber", number, "opened.")
    elif choice == 3:
        print ("Accounts")
        for x in accounts.keys():
            checksAcc.checkBalance()
        print
    elif choice == 4:
        print ("Withdraw money from Account.")
        asn = input("Amount: ")
        checksAcc.withdraw(awsn)
    elif choice == 5:
        print ("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in accounts:
            deposit = float(input("How much money would you like to deposit? > "))
            balance += deposit
            print ("Your new balance is €", balance)
        else:
            print ("That accountnumber does not exist.")
    elif choice == 6:
        print ("Quit.")
        break
    else:
        print ("Please enter a number between 1 and 6.")
    print
    print_menu()
