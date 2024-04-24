# bc_module.py

import pysha3
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(block):
    """
    Calculate the hash of a block.
    """
    sha3 = pysha3.Sha3_256()
    sha3.update(
        str(block.index).encode('utf-8') +
        str(block.previous_hash).encode('utf-8') +
        str(block.timestamp).encode('utf-8') +
        str(block.data).encode('utf-8')
    )
    return sha3.hexdigest()

def create_genesis_block():
    """
    Create the genesis block.
    """
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(Block(0, "0", int(time.time()), "Genesis Block", "")))

def create_new_block(previous_block, data):
    """
    Create a new block in the blockchain.
    """
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(Block(index, previous_block.previous_hash, timestamp, data, ""))
    return Block(index, previous_block.previous_hash, timestamp, data, hash)

# Example usage
genesis_block = create_genesis_block()
new_block = create_new_block(genesis_block, "Sample data")
print("Genesis Block: ", genesis_block.hash)
print("New Block: ", new_block.hash)
