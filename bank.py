from datetime import datetime
class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0  
        self.transaction_fee=50
        self.loan=0
        self.loan_limit=10000
        self.loan_fees=5
        self.transaction=[]
   
    def deposit(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Please enter amount in figures"    
        if amount <=0:
            return "please deposit a valid amount"
        else:
            self.balance+=amount
        transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}  
        self.transaction.append(transaction)  
        return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
    def withdraw(self,withdraw_amount):
        try:
            amount+10
        except TypeError:
            return f"please enter amount in figures"  
        total=withdraw_amount+self.transaction_fee
        if withdraw_amount<=0:
            return"please input a valid amount"
        elif total<self.balance:
            return"You have sufficient"
        else:
            self.balance-=total
            transaction={"amount":withdraw_amount,"balance":self.balance,"narration":"You withdrew","time":datetime.now()}  
        self.transaction.append(transaction)
        return f"Hello {self.name}You have successufully withdrawn {withdraw_amount} Your account balance is {self.balance} "   
    def borrow(self,loan_borrow):
        try:
            amount+10
        except TypeError:
            return "Please enter the amount in figures"    
        interest=self.loan_fees/100*loan_borrow
      
        if loan_borrow <= 0:
            return "You cannot borrow less"
        elif self.loan>0:
            return "Kindly repay your loan"
        elif loan_borrow > self.loan_limit:
            return "You have exceded loan limit"
        else:
            self.loan=loan_borrow+interest
            transaction={"amount":loan_borrow,"balance":self.balance,"narration":"You borrowed","time":datetime.now()}  
        self.transaction.append(transaction)
        return f"You have successfully received your loan of {loan_borrow} and your loan due payment is {self.loan},your new balance is {self.balance+loan_borrow}"  
    def repay(self,loan_return):
        try:
            amount+10
        except TypeError:
            return "Please enter the amount in figures" 
        if loan_return < self.loan:
            self.loan-= loan_return
            transaction={"amount":loan_return,"balance":self.balance,"narration":"You repayed","time":datetime.now()}  
            self.transaction.append(transaction) 
            return f"You have paid {loan_return}Your balance is {self.loan}"
        elif loan_return>self.loan:
             loan_payment=loan_return-self.loan
             self.balance+=loan_payment
             self.loan=0
             transaction={"amount":loan_return,"balance":self.balance,"narration":"You repayed","time":datetime.now()}  
             self.transaction.append(transaction) 
             return "Loan payed succefully {loan_payment}Your balance is {self.balance}" 
        elif loan_return==self.loan:
            transaction={"amount":loan_return,"balance":self.balance,"narration":"You repayed","time":datetime.now()} 
            self.transaction.append(transaction) 
            return "Congratulations you have successfully paid your loan"   
        else:     
            return "You  have not repayed your loan"  
    def transfer(self,amount,account):  
        try:
            amount+10
        except TypeError:
            return f"please enter amount in figures"
        if  amount >=0:
            fee=amount*0.05
            total=amount+fee
            return f"Please enter valid amount"  
        if total >self.balance.account:
            return f"Your balance is {self.balance}you need {total} inorder to transfer {amount}"
        else:
            self.balance-=total
            account.deposit=(amount)
            return f"You transfered {amount} to {account.name},Your new balance is {self.balance}"       
                              
    def get_statement(self): 
        for transaction in self.transaction:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            print(f"{date}...{narration}...{amount}...balance {balance}")

class MobileMoneyAccount(Account):
   
    def __init__(self,name,phone,service_provider): 
        Account.__init__(self,name,phone)
        self.service_provider=service_provider
    def buy_airtime(self,amount):
        try:
            amount+10
        except TypeError:
            return "Please input your value in figures"    
        if amount<=0:
            return f"Enter  a valid amount"
        elif amount>self.balance:
            return f"You have insufficient balance to purchase this credit"
        else:
            #  amount<=self.balance
             self.balance-=amount
             transaction={"amount":amount,"balance":self.balance,"narration":"You bought airtime","time":datetime.now()} 
             self.transaction.append(transaction)            
             return f"You can purchase your airtime"
             
        

   
        

             
            


   