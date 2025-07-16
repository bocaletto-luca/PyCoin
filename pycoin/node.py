# pycoin/node.py
import asyncio
import json
import websockets
from typing import Set
from pycoin.blockchain import Blockchain, Block

class Node:
    def __init__(self, host: str = 'localhost', port: int = 6789):
        self.blockchain = Blockchain()
        self.peers: Set[str] = set()
        self.host = host
        self.port = port

    async def register_peer(self, peer_uri: str):
        self.peers.add(peer_uri)

    async def broadcast(self, message: dict):
        if not self.peers:
            return
        data = json.dumps(message)
        await asyncio.wait([self._send(peer, data) for peer in self.peers])

    async def _send(self, peer_uri: str, data: str):
        try:
            async with websockets.connect(peer_uri) as ws:
                await ws.send(data)
        except Exception as e:
            print(f"Failed to send to {peer_uri}: {e}")

    async def handler(self, websocket, path):
        async for msg in websocket:
            msg = json.loads(msg)
            t = msg.get("type")
            payload = msg.get("payload")
            if t == "transaction":
                self.blockchain.add_new_transaction(payload)
                print("Received tx:", payload)
            elif t == "block":
                # ricostruisci un Block da dict
                blk = Block(**payload)
                proof = payload.get("hash")
                added = self.blockchain.add_block(blk, proof)
                print("Block added:", added)
            elif t == "register":
                peer = payload.get("peer")
                await self.register_peer(peer)
                print("Registered peer:", peer)

    def start(self):
        loop = asyncio.get_event_loop()
        server = websockets.serve(self.handler, self.host, self.port)
        print(f"P2P server listening on ws://{self.host}:{self.port}")
        loop.run_until_complete(server)
        loop.run_forever()


if __name__ == "__main__":
    node = Node()
    node.start()
