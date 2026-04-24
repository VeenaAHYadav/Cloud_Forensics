import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from blockchain.web3_client import store_hash, get_hash, get_count

print("Storing...")
store_hash("hello123")

count = get_count()
print("Count:", count)

value = get_hash(0)
print("Stored Hash:", value)