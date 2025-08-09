class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}"
        )

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit of ${amount} is complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self, amount, account):
        try:
            print("\n*********\n\nBeginning Transfer... 🚀")
            # Check if the balance is sufficient to carryout the transfer :
            self.viableTransaction(amount)

            # Deduction of amount from the sender's account :
            self.withdraw(amount)

            # Addition of amount to the receiver's account :
            account.balance = account.balance + amount
            print(f"\nTransfer of ${amount} is complete.")
            account.getBalance()

            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted : {error}")


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")
