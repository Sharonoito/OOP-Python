class Account:
    def __init__(self,accountnumber,pin,balance):
        self.accountnumber=accountnumber
        self.pin=pin
        self.balance=balance
    def withdraw(self):
        return f"My account number is {self.accountnumber},pin number is {self.pin} and I have a balance of {self.balance}"   
    def deposit(self):
        return f"I deposited 8000 in my account,my account balance is {self.balance}"    
    def loan(self):
        return f"My bank of accountnumber {self.accountnumber} is having a loan"