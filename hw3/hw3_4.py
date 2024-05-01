class Wallet:
    payment_system = "Koshel"

    def __init__(self, name: str, currency: str, balance: float):
        self.name = name
        self.currency = currency
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Баланс {self.name} пополнен на {amount} {self.currency}.")

    def pay(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Списание: {amount} {self.currency} .")
        else:
            print("Недостаточно средств для оплаты.")

    def get_balance_info(self):
        print(f"Баланс {self.name}: {self.balance} {self.currency}.")

    def close_account(self):
        print(f"Кошелек {self.name} закрыт.")
        del self

my_wallet = Wallet("Koshel", "USD", 1000.0)
my_wallet.deposit(500.0)
my_wallet.get_balance_info()
my_wallet.pay(700.0)
my_wallet.get_balance_info()
my_wallet.pay(1000.0)
my_wallet.close_account()