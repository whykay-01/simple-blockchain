from hashlib import sha256
import datetime
import time
from xmlrpc.client import _iso8601_format

class Block():

    def __init__(self, index, timestamp, data, previous_hash = ''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return sha256((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()).hexdigest()


class Blockchain():
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        t = "06/23/2023"
        ts = _iso8601_format.parse_datetime(t)
        timestamp = str(time.mktime(ts.timetuple()))
        print(timestamp)
        return Block(0, timestamp, 'Genesis Block', '0')

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def print_blockchain(self):
        for i in range(len(self.chain)):
            print("Block " + str(i) + " : " + str(self.chain[i].hash))
    
    def get_blockchain(self):
        return self.chain
    
    def get_block(self, index):

        if index < len(self.chain):
            return self.chain[index]
        else:
            return None

    def get_block_by_hash(self, hash):

        for i in range(len(self.chain)):
            if self.chain[i].hash == hash:
                return self.chain[i]
        
        return None

    def get_block_by_timestamp(self, timestamp):

        for i in range(len(self.chain)):
            if self.chain[i].timestamp == timestamp:
                return self.chain[i]
        
        return None
    
    def get_block_by_data(self, data):

        for i in range(len(self.chain)):
            if self.chain[i].data == data:
                return self.chain[i]
        
        return None

