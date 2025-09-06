# banking app
import random
from datetime import datetime

class BankAccount:
    promo_prize = 1000

    def __init__(self, acc_name, balance, isadmin=False, isfreezed=False, email=False, sms=False):
        self.account_name = acc_name
        self.acc_number = random.randint(1000000000, 9999999999)  
        self.total_balance = balance  
        self.isAdmin = isadmin
        self.isFreezed = isfreezed 
        self.email = email
        self.sms = sms

    def get_details(self):  
        if self.isFreezed:
            return f"account is frozen you cannot get details"
        return f"Account Name: {self.account_name}, Account Number: {self.acc_number}, Balance: {self.total_balance}"

    def apply_promo(self):  
        if self.isFreezed:
            return f"account is frozen you cannot apply promo"
        self.total_balance += self.promo_prize
        return f"Promo of {self.promo_prize} applied. New balance: {self.total_balance}"
        
    def deposit(self, amount):
        if self.isFreezed:
            return f"your account is frozen you cannot deposit"
        if amount > 0:
            self.total_balance += amount
            if self.sms:
                self.sms_Alert_CR(amount)
            if self.email:
                self.email_Alert_CR(amount)
            return f"you deposited {amount} to your account your new balance is {self.total_balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        if self.isFreezed:
            return f"your account is frozen you cannot withdraw"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount <= self.total_balance:
            self.total_balance -= amount
            if self.sms:
                self.sms_Alert_DR(amount)
            if self.email:
                self.email_Alert_DR(amount)
            return f"you withdrawed {amount} from your bank account, your new balance is {self.total_balance}"
        else:
            return "Insufficient funds"
        
    def transfer(self, amount, target_account):
        if self.isFreezed:
            return f"your account is frozen you cannot transfer"
        if amount <= 0:
            return "Transfer amount must be positive"
        if amount > self.total_balance:
            return "Insufficient balance for transfer"
        
        self.total_balance -= amount
        target_account.total_balance += amount
        
        if self.sms:
            self.sms_Alert_DR(amount)
        if self.email:
            self.email_Alert_DR(amount)
            
        return f"you transfered {amount} to {target_account.account_name} your new balance is {self.total_balance}"
    
    def freeze_account(self, requester):
        if not requester.isAdmin:
            return "Only admins can freeze accounts."
        if self.isFreezed:
            return f"Account {self.account_name} is already frozen."
        self.isFreezed = True
        return f"Account {self.account_name} is now frozen."

    def unfreeze_account(self, requester):
        if not requester.isAdmin:
            return "Only admins can unfreeze accounts."
        if not self.isFreezed:
            return f"Account {self.account_name} is not frozen."
        self.isFreezed = False
        return f"Account {self.account_name} is now unfrozen."

    def sms_Alert_CR(self, amount):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"""
Acct: **{str(self.acc_number)[-4:]}
Amt: NGN{amount:,.2f} CREDIT
Desc: -TRANSFER TO {self.account_name}-OPAY-{self.account_name}
Avail Bal: NGN{self.total_balance:,.2f}
Date: {time_str}
""")

    def sms_Alert_DR(self, amount):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"""
Acct: **{str(self.acc_number)[-4:]}
Amt: NGN{amount:,.2f} DEBIT
Desc: -TRANSFER FROM {self.account_name}-OPAY-{self.account_name}
Avail Bal: NGN{self.total_balance:,.2f}
Date: {time_str}
""")

    def email_Alert_CR(self, amount):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"""
Dear {self.account_name},
Whatsoever Bank electronic Notification Service (WeNS)
We wish to inform you that a CREDIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{str(self.acc_number)[-4:]}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {time_str}
Remarks : 539983*****2873
Time of Transaction : {time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at {time_str} are as follows;
Current Balance : NGN {self.total_balance:,.2f}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *737*51*1#.

Thank you for choosing Whatsoever Bank Limited""")

    def email_Alert_DR(self, amount):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"""
Dear {self.account_name},
Whatsoever Bank electronic Notification Service (WeNS)
We wish to inform you that a DEBIT transaction occurred on your account with us.

The details of this transaction are shown below:
Transaction Notification
Account Number : **{str(self.acc_number)[-4:]}
Transaction Location : 205
Description : WEB PUR 
Amount : NGN {amount:,.2f}
Value Date : {time_str}
Remarks : 539983*****2873
Time of Transaction : {time_str}
Document Number : {random.randint(1000000000, 90000000000)}

The balances on this account as at {time_str} are as follows;
Current Balance : NGN {self.total_balance:,.2f}

The privacy and security of your Bank Account details is important to us. If you would prefer that we do not display your account balance in every transaction alert sent to you via email please dial *737*51*1#.

Thank you for choosing Whatsoever Bank Limited""")


admin = BankAccount("Admin", 5000, isadmin=True)
joy = BankAccount("Joy", 2000, sms=True, email=True)
aaron = BankAccount("Aaron Black", 3000)

print(joy.get_details()) 
print(joy.apply_promo()) 
print(joy.deposit(2000))
print(joy.withdraw(1000))
print(joy.transfer(500, aaron))

print(admin.freeze_account(admin))  
print(joy.freeze_account(admin))    
print(joy.get_details())            
print(joy.unfreeze_account(admin))  