# ATM OPERATOR
import os

all_customers = {
    'User1': 1234,
    'User2': 5678,
    'User3': 9101}


class ATM():
    def __init__(self, Username='SAMIKO BANK', Total_amount=100000):
        self.Username = Username
        self.Total_amount = Total_amount
        self.balance = 0
        print('welcome to ' + self.Username + ' you have ' + str(self.Total_amount) + ' Naira')

    def Request_details(self):
        try:
            self.account_name = input('Enter your account Name: ')
            self.account_pin = int(input('Enter your account Pin: '))

            if self.account_name in all_customers.keys() and self.account_pin == all_customers[self.account_name]:
                self.user_interface()

            else:
                print('Sorry the pin or Account name, you entered is incorrect')
                print('Please try Again!!')

        except ValueError:
            self.error()

    def user_interface(self):
        print('Welcome ' + self.account_name + ' What would you like to do? ')
        print('Press (W) for Withdrawal, (D) for Deposit, (C) for customer services, (B) for accout Balance')

        choice_of_operation = input('Enter your Choice: ')

        if choice_of_operation.upper() == 'W':
            self.withdraw()

        elif choice_of_operation.upper() == 'D':
            self.deposit()

        elif choice_of_operation.upper() == 'C':
            self.customer_service()

        elif choice_of_operation.upper() == 'B':
            self.check_balance()

        else:
            self.error()

    def withdraw(self):
        global remaining_balance
        if self.account_name:
            if str(self.account_name + '_account.txt') in os.listdir():
                amount_to_withdraw = int(input('Enter amount to withdraw: '))
                with open(str(self.account_name + '_account.txt'), 'r') as account_balance:
                    remaining_balance = int(account_balance.read()) - amount_to_withdraw
                    print('Success!!, You have withdrawn ' + str(amount_to_withdraw))
                    print('You have ' + str(remaining_balance) + ' Naira, in your account Now')
                account_balance.close()
                with open(str(self.account_name + '_account.txt'), 'w') as updated_balance:
                    updated_balance.write(str(remaining_balance))
                updated_balance.close()
            print()
            do_something_else = input('Would you like to do something else?, Press (Y) for Yes or (N)for No: ')
            if do_something_else.upper() == 'Y':
                print()
                self.user_interface()

            else:
                with open(str(self.account_name + '_account.txt'), 'w') as account_details:
                    amount_to_withdraw = int(input('Enter amount to withdraw: '))
                    if amount_to_withdraw <= self.Total_amount:
                        remaining_balance = self.Total_amount - amount_to_withdraw
                        account_details.write(str(remaining_balance))

                        print('Success!!, You have withdrawn ' + str(amount_to_withdraw))
                        print('You have ' + str(remaining_balance) + ' Naira, in your account Now')
                        self.Total_amount = remaining_balance
                    account_details.close()
                print()
                do_something_else = input('Would you like to do something else?, Press (Y) for Yes or (N)for No: ')
                if do_something_else.upper() == 'Y':
                    print()
                    self.user_interface()

    def check_balance(self):
        if self.account_name:
            with open(str(self.account_name + '_account.txt'), 'r') as account_details:
                account_balance = account_details.read()
                print('Your account Balance is ' + str(account_balance) + ' Naira Only')
            do_something_else = input('Would you like to do something else?, Press (Y) for Yes or (N)for No: ')
            print()
            if do_something_else.upper() == 'Y':
                print()
                self.user_interface()

    def deposit(self):
        global remaining_balance
        if self.account_name:
            amount_to_deposit = input('Enter amount to deposit: ')
            print(f'You have successfully deposited {amount_to_deposit} Naira, into your account')
            print('Thanks for using our service!')
            print()
            with open(str(self.account_name + '_account.txt'), 'r') as account_balance:
                remaining_balance = int(account_balance.read()) + int(amount_to_deposit)
            account_balance.close()

            with open(str(self.account_name + '_account.txt'), 'w') as updated_balance_after_deposit:
                updated_balance_after_deposit.write(str(remaining_balance))
            updated_balance_after_deposit.close()

            do_something_else = input('Would you like to do something else?, Press (Y) for Yes or (N)for No: ')
            if do_something_else.upper() == 'Y':
                print()
                self.user_interface()

    def error(self):
        print('Sorry!, Theres an error in your input, check and try again')
        self.__init_subclass__()

    def customer_service(self):
        print(' \nDialing.... Customer Service')
        print('Hello Welcome to the Internet Banking Customer line.')
        print('Please what is your complaints? \n')
        complaints = input('Enter Complaints here: ')
        print('Thanks for your time and feedback, \nWe would surely get back to You!')
        print()

        do_something_else = input('Would you like to do something else?, Press (Y) for Yes or (N)for No: ')
        if do_something_else.upper() == 'Y':
            print()
            self.user_interface()


ATM().Request_details()
