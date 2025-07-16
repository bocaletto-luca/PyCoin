# tests/test_node.py
import pytest
import asyncio
from pycoin.node import Node

@pytest.mark.asyncio
async def test_register_and_broadcast(tmp_path):
    node = Node(host='127.0.0.1', port=6790)
    # registra un peer fittizio
    await node.register_peer("ws://127.0.0.1:6791")
    assert "ws://127.0.0.1:6791" in node.peers

    # broadcast vuoto non fallisce
    await node.broadcast({"type":"test","payload":{}})
