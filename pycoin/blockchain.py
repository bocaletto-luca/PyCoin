# pycoin/blockchain.py
import hashlib
import json
import time
from typing import List, Optional

class Block:
    def __init__(self,
                 index: int,
                 timestamp: float,
                 transactions: List[dict],
                 previous_hash: str,
                 nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 4  # numero zeri iniziali richiesti

    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[dict] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, time.time(), [], "0")
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, block: Block) -> str:
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith("0" * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block: Block, proof: str) -> bool:
        if proof != block.compute_hash():
            return False
        if block.previous_hash != self.last_block.hash:
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def add_new_transaction(self, transaction: dict):
        self.pending_transactions.append(transaction)

    def mine(self, miner_address: str) -> Optional[Block]:
        if not self.pending_transactions:
            return None
        block = Block(
            index=self.last_block.index + 1,
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=self.last_block.hash
        )
        proof = self.proof_of_work(block)
        self.add_block(block, proof)
        # Ricompensa miner
        reward_tx = {"from": "NETWORK", "to": miner_address, "amount": 1}
        self.pending_transactions = [reward_tx]
        return block
