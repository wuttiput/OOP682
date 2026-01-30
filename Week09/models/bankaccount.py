class Bankaccount:
    def __init__(self,balance):
        self.balance = balance
        
    def __sub__(self,other):
        if isinstance(other, Bankaccount):
            New_ba = self.balance - other.balance
            New_ac = Bankaccount(New_ba)
            return New_ac
        return NotImplemented
    
    def __add__(self,other):
        if isinstance(other, Bankaccount):
            New_ba = self.balance + other.balance
            New_ac = Bankaccount(New_ba)
            return New_ac
        return NotImplemented

    def __str__(self):
        return (f'Bankaccount: {self.balance:.2f} THB')