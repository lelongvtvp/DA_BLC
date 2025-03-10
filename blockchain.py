from gettext import translation
import hashlib
import json
import time
import random
#khởi tạo lớp block
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp = None, nonce = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.hash = self.calculate_hash()
    def calculate_hash (self):            
        # self.__dict__: Trả về tất cả thuộc tính của đối tượng (self) dưới dạng một từ điển (dictionary).
        # json.dumps(..., sort_keys=True): Chuyển đổi dictionary thành chuỗi JSON.
        # sort_keys=True giúp sắp xếp thứ tự các khóa để đảm bảo tính nhất quán khi hash dữ liệu.
             block_data = json.dumps(self.__dict__, sort_keys=True)
        #chuyển chuỗi block_data về dạng bytes vì sha-256 chỉ nhận bytes
             return hashlib.sha256(block_data.encode()).hexdigest()
    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:20]}, prev_hash = {self.previous_hash[:20]})"
# block = Block(0, "0", [], time.time())
# print(block)
#khởi tạo lớp blockchain
class Blockchain:
     def __init__(self):
          self.chain = [self.create_genesis_block()]
          self.pending_transactions = []
          self.difficulty = 3 #điều chỉnh độ khó PoW
    #tạo block gốc
     def create_genesis_block(self):
        return Block(0,"0",[], time.time())
    #tạo giao dịch
     def add_transaction(self, transaction):
          self.pending_transactions.append(transaction)
    #đào block
     def mine_block(self, miner_address):
          new_block = Block(len(self.chain), self.chain[-1].hash, self.pending_transactions)
          self.proof_of_work(new_block)
          self.chain.append(new_block)
          self.pending_transactions = [{"sender": "network", "receiver": miner_address, "amount": 1}] #phần thưởng block
     def proof_of_work(self, block):
        while not block.hash.startswith("0" * self.difficulty) :
            block.nonce += random.randint(1,10) #tăng nonce theo bước ngẫu nhiên
            block.hash = block.calculate_hash()
     def is_valid_chain(self, chain):
          for i in range(1, len(chain)):
               if chain[i].previous_hash != chain[i-1].hash:
                    return False
          return True
     def save_blockchain(self):
          with open("res_blockchain.txt", "w") as file:
               json.dump([block.__dict__ for block in self.chain], file, indent=4)
# blockchain = Blockchain()
# blockchain.add_transaction({"sender": "A", "receiver": "B", "amount": 10})
# blockchain.mine_block("miner1")
# print(blockchain.chain)

