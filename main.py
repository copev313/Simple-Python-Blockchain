# main.py

from pprint import pprint
from blockchain import Blockchain

bc = Blockchain()

t1 = bc.new_transaction("Satoshi", "Mike", "5 BTC")
t2 = bc.new_transaction("Mike", "Satoshi", "1 BTC")
t3 = bc.new_transaction("Satoshi", "Hal Finney", "5 BTC")
bc.new_block(12345)

t4 = bc.new_transaction("Mike", "Alice", "1 BTC")
t5 = bc.new_transaction("Alice", "Bob", "0.5 BTC")
t6 = bc.new_transaction("Bob", "Mike", "0.5 BTC")
bc.new_block(6789)

print("Genesis Block: \n")
for block in bc.chain:
    pprint(block, indent=2)
