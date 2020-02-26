import math

## Find PI to the Nth Digit ##

# def find_pi():
#     while True:
#         try: 
#             num = int(input('How many decimals would you like?: '))
#         except ValueError:
#             print('Integers only!')
#         else:
#             if num > 25 or num < 0:
#                 print('You cannot have an integer larger than 25!!!')
#             else:   
#                 print(round(math.pi, num))
#                 break
# find_pi()

## Prime Number Generator
# answer = input("Would you like the next prime number (y/n)?: ")
# current = 1

# def is_prime(x):
#     if x == 2:
#         return False
#     if x % 2 == 0:
#         return False
#     for i in range(3, int((x**0.5)+1), 2):
#         if x % i == 0:
#             return False 
#     return True

# while answer.lower() == 'y':
#     current += 1
#     while is_prime(current) == False:
#         current += 1
#     print("Next prime is " +str(current))
#     answer = input("Would you like the next prime number (y/n)?: ")

## Change Generator (quarters, dimes, nickels, pennies)

# def change_gen():
#     quarters = 0
#     dimes = 0
#     nickels = 0
#     pennies = 0
#     try:
#         num = float(input('Enter an amount to convert to change: '))
#     except ValueError:
#         print('Numbers only!')
#     while num > 0: 
#         if num >= 0.25:
#             num -= 0.25
#             quarters += 1
#         elif num > 0.09:
#             num -= 0.10
#             dimes += 1
#         elif num > 0.04:
#             num -= 0.05
#             nickels += 1
#         else:
#             num -= 0.01
#             pennies += 1
#     return f'Your amount has been converted to {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies}  pennies'
# change_gen()

## Bank Account Manager

class Account:
    def __init__(self, acct_number, balance):
        self.acct_number = acct_number
        self.balance = balance     

    def __str__(self):
        return f'${self.balance:.2f}'
    
    def deposit(self, dep_amt):
        self.balance += dep_amt
        
    def withdraw(self, withdraw_amt):
        if self.balance > withdraw_amt:
            self.balance -= withdraw_amt
        else:
            print('You do not have sufficient funds available!')

class CheckingAccount(Account):
    def __init__(self, acct_number, balance):
        super().__init__(acct_number, balance)
        
    def __str__(self):
        return f'Checking Account #{self.acct_number}\nBalance: {Account.__str__(self)}'
    
    
class SavingsAcount(Account):
    def __init__(self, acct_number, balance):
        super().__init__(acct_number, balance)
        
    def __str__(self):
        return f'Savings Account #{self.acct_number}\nBalance: {Account.__str__(self)}'

class BusinessAccount(Account):
    def __init__(self, acct_number, balance):
        super().__init__(acct_number, balance)

    def __str__(self):
        return f'Business Account #{self.acct_number}\nBalance: {Account.__str__(self)}'
    
class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN