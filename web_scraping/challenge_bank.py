"""
Challenge: Simulate Bank Transactions
You have been given the task of simulating bank transactions using the BankAccount class. Your goal is to complete the code and test various scenarios to ensure the proper functioning of the bank operations.
Requirements:
Implement the __init__ method to initialize private attributes (name and balance).
Implement the get_balance method to retrieve the current balance.
Implement the check_balance method to display a summary of the account information.
Implement the deposit method to handle deposit operations and display the updated balance.
Implement the withdraw method to handle withdrawal operations with proper validation and display the updated balance.
Implement the appreciation method to display a thank-you message.
Challenge Task:
Create an instance of the BankAccount class with a starting balance.
Perform a series of transactions such as deposits and withdrawals to test the functionality.
Display the account information after each transaction.
Note: Make sure to handle edge cases, such as attempting to withdraw more than the current balance, and ensure that the class methods provide meaningful outputs.
"""

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance
      
    def deposit(self):
        amount = float (input ("Enter amount to deposit: "))
        if amount > 1:
            return (amount)   
        else:
           return ('please deposit higher amount')

    def withdraw(self):
            amount = float (input ("Enter amount to withdraw: "))       
            if self.balance >= amount:
                self.balance -= amount
                return ('withdrawn', amount)
            else:
                return ('Insufficient amount')

    def appreciation (self):
        return ('Thank you for banking with us')

acc_1 = BankAccount('James Bond',3000)

 
print (acc_1.deposit())   
print (acc_1.withdraw())    
print (acc_1.get_balance())
print (acc_1.appreciation())












