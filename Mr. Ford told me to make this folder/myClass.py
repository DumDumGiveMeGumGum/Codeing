class  Account:
    def __init__ (self,owner,balance,password) :
        self.owner = owner
        self.balance = balance
        self.password = password

    def __str__ (self) :
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance} '

    def deposit (self,dep_amt) :
        self.balance += dep_amt
        print ('Deposit Acceptid')

    def withdrawl (self, wd_amt) :
        if wd_amt < self.balance:
            self.balance -=wd_amt
            print ('Withdrawl Accepted -- Thank you: ',  self.owner)
        elif wd_amt == self.balance:
            self.balance -= wd_amt
            print ("Account Closed -- Thank you:", self.owner)
        else:
            print ('Funds Unavalible --check your math:', self.owner)
