import hashlib
import time
from transaction import Transaction
from key import verify_signature


class Block:

    def __init__(self, index, previous_hash, nonce=0, timestamp=0, transactions=[], hashval=None, miner=None):
        self.index = index
        self.nonce = nonce
        self.timestamp = timestamp
        self.transactions = []
        for elem in transactions:
            self.transactions.append(Transaction(elem["sender"], elem["receiver"], elem["amount"], elem["timestamp"],
                                                 elem["tx_number"]))
        self.previous_hash = previous_hash
        self.hashval = hashval
        self.miner = miner

    def hash(self, nonce):
        sha = hashlib.sha256()
        data = ""
        data = str(self.index) + str(self.timestamp) + str(nonce) + str(self.previous_hash)
        for elem in self.transactions:
            data += str(elem.sender) + str(elem.receiver) + str(elem.amount)
        sha.update(data.encode())
        return sha.hexdigest()

    def add_transaction(self, transaction):
        tx = transaction
        tx.tx_number = len(self.transactions)
        self.transactions.append(tx)
        pass

    def to_dict(self):
        block_dict = {}
        block_dict["index"] = self.index
        block_dict["nonce"] = self.nonce
        block_dict["timestamp"] = self.timestamp
        block_dict["miner"] = self.miner
        block_dict["transactions"] = []
        for elem in self.transactions:
            block_dict["transactions"].append(elem.to_dict())
        block_dict["previous_hash"] = self.previous_hash
        block_dict["hashval"] = self.hashval
        return block_dict

    def mine(self, difficulty):
        self.timestamp = time.time()
        nonce = 0
        prefix = "0" * difficulty
        hash_value = self.hash(nonce)
        print("Debut du minage")
        while (hash_value.startswith(prefix) == False):
            nonce += 1
            hash_value = self.hash(nonce)
            print(hash_value)
        print("Le minage est terminé")
        self.hashval = hash_value
        self.nonce = nonce
        self.miner = "밥"

        return nonce
