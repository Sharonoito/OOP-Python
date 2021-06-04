class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0  
        self.transaction_fee=50
        self.loan=0
        self.loan_limit=10,000
        self.loan_fees=5
        
    def deposit(self,amount):
        if amount <=0:
            return "please deposit a valid amount"
        else:
            self.balance+=amount
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
    def withdraw(self,withdraw_amount):
        total=withdraw_amount+self.transactionfee
        if withdraw_amount<=0:
            return"please input a valid amount"
        elif total<self.balance:
            return"You have sufficient"
        else:
            self.balance-=total
            return f"Hello {self.name}You have successufully withdrawn {withdraw_amount} Your account balance is {self.balance} "   
    def borrow(self,loan_borrow):
        interest=self.loan_fees/100*loan_borrow
        loan_due=loan_borrow+interest
        if loan_borrow<=0:
            return "You cannot borrow less"
        elif self.loan>0:
            return "Kindly repay your loan"
        elif loan_borrow>self.loan_limit:
            return "You have exceded loan limit"
        else:
            return f"You have successfully received your loan of {loan_borrow} and your loan due payment is {loan_due},your new balance is {self.balance+loan_borrow}"    



        

             
            


   