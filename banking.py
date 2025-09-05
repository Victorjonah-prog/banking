# banking app
import random

class BankAccount:
    promo_prize = 1000

    def __init__(self, acc_name, balance,isadmin=False, isfreezed=False):
        self.account_name = acc_name
        self.acc_number = random.randint(1000000000, 9999999999)  
        self.total_balance = balance  
        self.isAdmin = isadmin
        self.isFreezed = isfreezed 

    def get_details(self):  
        if self.isFreezed:
            return f"account is frozen you cannot get details"
        return f"Account Name: {self.account_name}, Account Number: {self.acc_number}, Balance: {self.total_balance}"

    def apply_promo(self):  
        if self.isFreezed:
            return f"account is frozen you cannot apply promo"
        self.total_balance += self.promo_prize
        return f"Promo of {self.promo_prize} applied. New balance: {self.total_balance}"
    def deposit(self,amount,):
        if self.isFreezed:
            return f"your account is frozen you cannot deposit"
        if amount > 0:
            self.total_balance += amount
            return f"you deposited {amount} to your account your new balance is {self.total_balance} "
    
    def withdraw(self, amount):
        if self.isFreezed:
            return f"your account is frozen you cannot withdraw"
        if amount < self.total_balance:
            self.total_balance -= amount
            return f"you withdrawed {amount} from your bank account, your new balance is {self.total_balance}"
        
    def transfer(self,amount,target_account):
        if amount <= 0:
            return "Transfer amount must be positive"
        if amount > self.total_balance:
            return "Insufficient balance for transfer"
        self.total_balance -= amount
        target_account += amount
        return f" you transfered {amount} to {target_account} your new balance is {self.total_balance}"
    
    
    def freeze_account(self, requester):
        if not requester.isAdmin:
            return "Only admins can freeze accounts."
        if self.isFreezed:
            return f"Account {self.account_name} is already frozen."
        self.isFreezed = True
        self._send_notification("Account Frozen", f"Your account {self.acc_number} has been frozen.")
        return f"Account {self.account_name} is now frozen."

    
    def unfreeze_account(self, requester):
        if not requester.isAdmin:
            return "Only admins can unfreeze accounts."
        if not self.isFreezed:
            return f"Account {self.account_name} is not frozen."
        self.isFreezed = False
        self._send_notification("Account Unfrozen", f"Your account {self.acc_number} has been unfrozen.")
        return f"Account {self.account_name} is now unfrozen."

    
    def _send_notification(self, method, sms, email):
        if method == "email":
            return email

        elif method == "sms":
            return sms
        else:
            return "Invalid notification method. Use 'email' or 'sms'."

        
       

admin = BankAccount("Admin", 5000, isadmin=True)
joy = BankAccount("joy", 2000)
print(joy.get_details()) 
joy.apply_promo()
print(joy.apply_promo()) 
joy.deposit(2000)
print(joy.deposit(2000))
joy.withdraw(1000)
print(joy.withdraw(1000))

joy.transfer(500,9383822446)
print(joy.transfer(500,9383822446))

joy.freeze_account(admin)
print(joy.freeze_account(admin))

joy._send_notification(sms,email,"withdrawal succesful","deposited successfully")
print(joy._send_notification(sms,"withdrawal suceesful","deposited successfully"))


# implement freeze, sms, mail  add a new flag isadmin = false and isfreezed = false and only an admin can freeze and unfreez, there should be a methode for freeze and unfreeeze
#message should take mail or sms