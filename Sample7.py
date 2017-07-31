class BankingCustomer:
    "Represents customer with name and balance"

    allCustomers = {}
    def __init__(self, name, balance = 0):
        "Customer initialization"
        self.name = name
        self.balance = balance
        BankingCustomer.allCustomers[self.name] = self.balance
        print("\nCustomer profile for {} has been created.".format(self.name))
        if BankingCustomer.allCustomers[self.name] == 0:
            print("{} hasn't placed any funds as initial deposit".format(self.name))
        else:
            print("{} has made an initial deposit of {} Peso(s)".format(self.name, BankingCustomer.allCustomers[self.name]))

    def deposit(self, amount):
        "Deposit processing"
        self.amount = amount
        print("\n{1} has deposited {0} Peso(s) into bank account.".format(self.amount, self.name))
        BankingCustomer.allCustomers[self.name]+= self.amount
        print("{}\'s new balance is {} Peso(s).".format(self.name, BankingCustomer.allCustomers[self.name]))

    def withdrawal(self, amount):
        "withdrawal processing"
        self.amount = amount
        if self.amount > BankingCustomer.allCustomers[self.name]:
            print("\n{} wants to withdraw {} Peso(s) but doesn't have enough funds to perform this \
transaction.".format(self.name, self.amount))
        else:
            print("\n{} took {} Peso(s) from his account.".format(self.name, self.amount))
            BankingCustomer.allCustomers[self.name] -= self.amount
        print("{}\'s account balance is {} Peso(s).".format(self.name, BankingCustomer.allCustomers[self.name]))

    def balanceCheck(self):
        "Balance check functonality"
        print("\n{1}\'s balance is {0} Peso(s).".format(BankingCustomer.allCustomers[self.name], self.name))
    #class methods
    @classmethod

    def totalCustomers(cls):
        "Prints the current customer base."
        print("Bank has a customer base of {} customers".format(len(cls.allCustomers)))

name = input('What is your name? ')
customer1 = BankingCustomer(name)
customer1.deposit(500)

def print_menu():
    print ("1. Deposit Money\n2. Withdraw Money")
    print ("3. Balance Inquiry\n4. Acount Information\n5. Quit")
    print

accounts = {}
choice = 0
print_menu()
balance = 0
while True:
    choice = int(input("Input here: "))
    print
    if choice == 1:
        print ("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in accounts:
            deposit = float(input("How much money would you like to deposit? > "))
            balance += deposit
            print ("Your new balance is €", balance)
        else:
            print ("That accountnumber does not exist.")
    elif choice == 2:
        print ("Withdraw money from Account.")
        asn = input("Amount: ")
    elif choice == 3:
        customer1.balanceCheck()
    elif choice == 4:
        
    elif choice == 5:
        print ("Quit.")
        break
    else:
        print ("Please enter a number between 1 and 5.")
    print
    print_menu()


