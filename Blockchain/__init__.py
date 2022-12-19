import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8') + self.previous_hash.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        if len(self.chain) == 0:
            previous_hash = '0x12x21x012'
        else:
            previous_hash = self.chain[-1].hash
        new_block = Block(data, previous_hash)
        self.chain.append(new_block)

blockchain = Blockchain()
blockchain.add_block('Rakib works at Cefalo')
blockchain.add_block('Kazi works at Brain Station')
blockchain.add_block('Siam works at Steamtech')

for block in blockchain.chain:
    print(block.data,  block.hash)
