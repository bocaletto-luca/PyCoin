# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from pycoin.api import app

client = TestClient(app)

def test_get_chain_empty():
    res = client.get("/chain")
    assert res.status_code == 200
    data = res.json()
    assert "chain" in data
    assert data["length"] == len(data["chain"]) >= 1

def test_transaction_and_mine():
    tx = {"sender":"A","recipient":"B","amount":1.5,"signature":b""}
    res = client.post("/transactions/new", json=tx)
    assert res.status_code == 200
    # ora miniamo
    res2 = client.get("/mine?miner_address=miner1")
    assert res2.status_code in (200, 400)
