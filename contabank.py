class BankAcount:
    def __init__(self, person, balance):
        self._person = person
        self._balance = balance

    @property
    def person(self):
        return self._person
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def see_extract(self):
        print(f'Person: {self._person}')
        print(f'Balance: {self._balance}')
    
    def deposit(self, valor):
       self._balance += valor
       return f'Balance: {self._balance}'
        
    def withdraw(self, valor):
        if self._balance < valor: 
            print('Invalid, not enough balance')
        else:
            self._balance -= valor
            return f'Balance: {self._balance}'

jose = BankAcount('Jose', 10000)
jose.deposit(34000)
jose.withdraw(10000)
print(jose.balance)