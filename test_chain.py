from chain import Blockchain
from key import BitcoinAccount

wallet = BitcoinAccount()
address = wallet.to_address()
difficulty = 4

blockchain = Blockchain(difficulty)
blockchain.create_genesis_block()

print("blockchain: ")
print(blockchain.to_dict())

first_block = blockchain.blocks_list[-1]

print("First block: ")
print(first_block)

blockchain.add_transaction(address, "colas", 10)
blockchain.add_transaction(address, "salim", 30)
blockchain.mine_block()

print("blockchain: ")
print(blockchain.to_dict())
second_block = blockchain.blocks_list[-1]

print("Second block: ")
print(second_block)
