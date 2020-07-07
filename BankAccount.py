class BankAccount:
    def __init__(self, first_name, last_name, if_active = False, balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.if_active = if_active
        self.balance = balance

    def activate(self):
        self.if_active = True
        return 'Welcome. Your account has been activated.'

    def close(self):
        if self.balance == 0:
            self.if_active = False
            return "Your account has been closed. Good day."
        else:
            return f"You cannot close your account. Withdraw all your money first. You have still {self.balance} $."

    def saldo(self):
        return f"You have {self.balance} $ on your account."

    def deposit(self, amount):
        self.balance += amount
        return f"You deposited {self.balance} $ on your account."

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Your amount have been withdrawn. You have now {self.balance} $ on your account."
        else:
            return f"You don't have enough money on your account to withdraw {amount} $. You can withdraw only {self.balance} $."
        return self.balance

Dorota = BankAccount('Dorota', 'Malinowska')
print(Dorota.activate())
print(Dorota.saldo())
print(Dorota.deposit(300))
print(Dorota.saldo())
print(Dorota.withdrawal(500))
print(Dorota.withdrawal(100))
print(Dorota.close())
print(Dorota.withdrawal(200))
print(Dorota.close())