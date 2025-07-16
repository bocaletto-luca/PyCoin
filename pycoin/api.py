# pycoin/api.py
from fastapi import FastAPI, HTTPException
from pycoin.blockchain import Blockchain
from pycoin.transaction import Transaction
from pydantic import BaseModel

app = FastAPI(title="PyCoin API")
chain = Blockchain()

class TxModel(BaseModel):
    sender: str
    recipient: str
    amount: float
    signature: bytes

@app.get("/chain")
def get_chain():
    return {"length": len(chain.chain), "chain": [blk.__dict__ for blk in chain.chain]}

@app.post("/transactions/new")
def new_transaction(tx: TxModel):
    transaction = tx.dict()
    # qui potresti verificare firma con Transaction.verify()
    chain.add_new_transaction(transaction)
    return {"message": "Transaction will be added to Block " + str(chain.last_block.index + 1)}

@app.get("/mine")
def mine(miner_address: str):
    block = chain.mine(miner_address)
    if not block:
        raise HTTPException(400, "No transactions to mine")
    return {"message": "New Block Forged", "index": block.index, "hash": block.hash}
