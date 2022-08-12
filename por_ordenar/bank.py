import pytz
import timezone

class bank:
    interest_rate= 10

    def __init__(self,id,first,last,balance=0):
        self.id = id
        self._first = first
        self._last = last
        self._balance = balance

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self,first):
        self._first = first

    @property
    def last(self):
        return self._first

    @last.setter
    def last(self, last):
        self._last = last

    def fullname(self):
        return self._first +" "+ self._last #esto debe ser con return o con print


    #method for fullname
    @property
    def balance(self):
        return self._balance

    def deposit(self,value):
        if value >= 1:
            self._balance = self.balance + value #necesito saber como convertir esto a un entero y sumarselo

    def withdrawals(self,value):
        if value > self.balance:
            return f"Insuficient Founds"
        else:
            self._balance -= value
            return f"your new balance is {self._balance}"
        #porque no puedo usar una variable global aqui

class Timezone:
    
p=bank("ab","juan","perez","100")
p.last = "Olachea"
p.first = "Juan"
p.deposit(550)
print(p.deposit)
print(p.balance)
print(p.fullname())


