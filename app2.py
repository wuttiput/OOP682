from models.bankaccount import Bankaccount

my_account = Bankaccount(1000)
your_account = Bankaccount(500)

our_account = my_account + your_account
our_account2 = my_account - your_account
print(our_account2)
print(our_account)