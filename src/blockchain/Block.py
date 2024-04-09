import hashlib
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        self.nonce = 0
        while self.compute_hash()[:difficulty] != '0' * difficulty:
            self.nonce += 1
        self.hash = self.compute_hash()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        self.difficulty = 4  # Difficulty of our PoW algorithm

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.proof_of_work(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, block):
        block.previous_hash = self.last_block.hash
        block.proof_of_work(self.difficulty)
        self.chain.append(block)

    @property
    def last_block(self):
        return self.chain[-1]

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.compute_hash():
                print("Current block's hash is incorrect")
                return False

            if current.previous_hash != previous.hash:
                print("Previous block's hash doesn't match current block's previous hash")
                return False

        return True

# Example Usage
if __name__ == "__main__":
    hypermesh_blockchain = Blockchain()

    # Adding blocks
    block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
    block_two_transactions = {"sender": "Bob", "receiver": "Charlie", "amount": "25"}

    new_block = Block(index=1, transactions=block_one_transactions, timestamp=time.time(), previous_hash=hypermesh_blockchain.last_block.hash)
    hypermesh_blockchain.add_block(new_block)

    new_block = Block(index=2, transactions=block_two_transactions, timestamp=time.time(), previous_hash=hypermesh_blockchain.last_block.hash)
    hypermesh_blockchain.add_block(new_block)

    # Verifying blockchain
    print("Blockchain valid?", hypermesh_blockchain.is_valid())
