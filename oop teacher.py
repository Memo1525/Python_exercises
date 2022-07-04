# timezone
import numbers
from collections import namedtuple
from datetime import timedelta, datetime
import itertools


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Timezone no puede ser vacia")
        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):  # numbers.integral clase de los numeros
            raise ValueError("hora debe de ser un entero ")
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError("Minute offset must be an integer")
        if offset_minutes< -59 or offset_minutes >59:
            raise ValueError("Minutes offset must be between -59 and 59 (inclusive)")

        offset = timedelta(hours=ofset_hours, minutes=offfset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("offset must be between -12:00 and +14:00")

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f'TimeZone(name={self.name}',
                f'offset_hours ={self._offset_hours}',
                f'offset_minutes={self._offset_minutes}')
    #checar las validaciones de los atributos


# this class is not neccesary
class TransactionID:
    def __init__(self, start_id):
        self._start_id = start_id

    def next(self):  # own method of next
        self._start_id += 1
        return self._start_id


class Account:
    #global variables
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5

    _transaction_code = {
        'deposit': 'D',
        'withdrad': 'W',
        'interest':'I',
        'rejected':'X'

    }

    def __init__(self, account_number, first_name, last_name, timezone=None,initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = float(initial_balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self.first_name = validate_name(value, "First Name")
        # if len(str(value).strip())==0:
        #  raise ValueError("first name must not be empty")
        self.first_name = value

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        self.last_name = validate_name(value, "Last Name")
        # if len(str(value).strip())==0:
        #  raise ValueError("last name must not be empty")
        self.last_name = value

    @classmethod
    def validate_name(cls, value, field_title):
        if len(str(value).strip()) == 0 or value is None:
            raise ValueError(f"{field_title} cannot be empty")
        return str(value).strip()

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError("Timezone must be a valid object")
        self._timezone = value

    @classmethod
    def set_interest_rate(cls , value):
        if not isinstance(value,numbers.Real):
            raise ValueError('Interest rate must be a real number ')
        if value < 0:
            raise ValueError('Interest rate cannot be negative')
        cls._interest_rate = value

    def validate_and_set_name(self,property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError (f'{field_title} cannot be empty')
        setattr(self, property_name , value)
    @staticmethod
    def validate_real_num(value,min_value=None):
        if not isinstance(value,numbers.Real):
            raise ValueError('interest rate must be a real number')

    def deposit(self,value):
        if not isinstance(value,numbers.Real):
            raise ValueError('Deposit must be a real number')
        if value <=0:
            raise ValueError('Deposit value must be a positive number')

        transaction_code = Account._transaction_codes['deposit']

        conf_code = self.generate_confirmation_code(transaction_code)


    transaction_counter = TransactionID(100)


    def make_transaction(self):
        new_trans_id = Account.trasaction_counter.next()

    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')

        return f'{transaction_code}-{self.account_number}-{dt_str}-{next{transaction_id}}'

    def transaction_id(start_id):
        while true:
            start_id += 1
            yield start_id
            # we have a built in library that makes this for us the lines from 68 to 72 are simply
            itertools.count(100)





# confirmation code whenever a transcation is made


print(generate_confirmation_code(123, 100 - 'A'))



