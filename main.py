from tools import add, subtract, deposit, withdraw


print(add(20, 10))
print(subtract(20, 10))

balance = 500

balance = deposit(balance, 100)
print("After deposit:", balance)

balance = withdraw(balance, 200)
print("After withdraw:", balance)
print("Git practice")
print("Temporary change")
