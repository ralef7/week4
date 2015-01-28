class BankAccount:

    
    balance = None
        
    

    def deposit(self, cash_in):
        self.balance += cash_in

        


    def withdraw(self, cash_out):
        if cash_out > self.balance:
            return self.balance
        else:
            self.balance -= cash_out

        


    def transfer(self, cash_move, transfer_to):
        if cash_move > self.balance:
            return self.balance
        else:         
            self.balance -= cash_move
            transfer_to.balance += cash_move
        
        
        
      
        
        


            
        
        
