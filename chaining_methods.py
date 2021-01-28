class User:
    def __init__(self, name, email):
        self.name =  name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self

jason = User("Jason", "jason@python.com")
agnes = User("Agnes", "agnes@python.com")
deku = User("Deku", "deku@python.com")

jason.make_deposit(1000).make_deposit(500).make_deposit(50).make_withdrawl(200).display_user_balance()

agnes.make_deposit(2000).make_deposit(100).make_withdrawl(50).make_withdrawl(50).display_user_balance()

deku.make_deposit(1000).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_user_balance()

jason.transfer_money(deku,1000).display_user_balance()
deku.display_user_balance()

