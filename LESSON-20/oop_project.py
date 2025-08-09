from bank_accounts import *

Amith = BankAccount(1000, "Amith")
Vijaya = BankAccount(2000, "Vijaya")

print("_____________________________________________")

Amith.getBalance()
Vijaya.getBalance()

print("_____________________________________________")

Amith.deposit(2500)

print("_____________________________________________")

Vijaya.withdraw(10000)
Vijaya.withdraw(10)

print("_____________________________________________")

# Amith.transfer(10000)
# Amith.transfer(10000, Vijaya)
# Amith.transfer(500, Vijaya)

print("_____________________________________________")

Jim = InterestRewardsAcc(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Amith)

print("_____________________________________________")

Blaze = SavingsAcc(1500, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(150, Vijaya)