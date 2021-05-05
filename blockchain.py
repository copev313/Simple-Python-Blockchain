# blockchain.py

import hashlib
import json
from time import time


class Blockchain(object):
    '''A simple blockchain object used to demonstrate the data structure.'''

    def __init__(self):
        # The chain we'll add blocks to:
        self.chain = []
        # The list where transactions will sit until approved & added to a new block:
        self.pending_transactions = []
        # Use this method to add each block to the chain:
        self.new_block(proof=10010,
                       prev_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.")
    
    
    def new_block(self, proof, prev_hash=None):
        '''Creates a new block listing of key/value pair block information in a JSON object.
        Resets the list of pending transactions and appends the newest block to the chain.
        '''
        block = {
            # Used to reference an individual block:
            'index': len(self.chain) + 1,

            # Timestamp the block when it's created:
            'timestamp': time(),

            # Any pending transactions will be included in the new block:
            'transactions': self.pending_transactions,

            # Our difficult to find random number for security purposes:
            'proof': proof,

            # Hashed version of the most recent approved block:
            'prev_hash': prev_hash or self.hash(self.chain[-1]),
        }
        # Reset our pending transactions:
        self.pending_transactions = []

        # Add our new block to the chain:
        self.chain.append(block)

        return block
    

    @property
    def last_block(self):
        '''Retreives the block most recently added to the chain.'''
        return self.chain[-1]

    
    def new_transaction(self, sender, recipient, amount):
        '''Creates a new transaction object containing the sender, recipient,
        and amount of currency being sent.'''
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1


    def hash(self, block):
        '''Returns a new hash from a block's key/value pairs.'''
        str_obj = json.dumps(block, sort_keys=True)
        block_str = str_obj.encode()

        raw_hash = hashlib.sha256(block_str)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

