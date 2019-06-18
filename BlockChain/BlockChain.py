# Stuart Spiegel, Date: 6/17/2019
#This Python class is an implementation of a Block Chain

#We must first define the class Block which is the most basic
#unit of the blockchains implementation.

#library to assign hashes to blocks(transactions)
import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) +
               str(self.timestamp) +
               str(self.data) +
               str(self.previous_hash))
    return sha.hexdigest()

    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    #number of blocks to add to the chain + 1 (Genesis-block)
    num_of_blocks_to_add = 20 #small number of blocks for now (snakeCoin)

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
      block_to_add = next_block(previous_block)
      blockchain.append(block_to_add)
      previous_block = block_to_add
      print "Block #{} has been added to the blockchain!".format(block_to_add.index)
      print "Hash: {}\n".format(block_to_add.hash)
