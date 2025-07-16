# pycoin/transaction.py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import serialization

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, signature: bytes = b""):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}

    def sign(self, private_key: ec.EllipticCurvePrivateKey):
        tx_str = f"{self.sender}{self.recipient}{self.amount}"
        signature = private_key.sign(
            tx_str.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        self.signature = signature

    def verify(self, public_key_pem: bytes) -> bool:
        public_key = serialization.load_pem_public_key(public_key_pem)
        tx_str = f"{self.sender}{self.recipient}{self.amount}"
        try:
            public_key.verify(
                self.signature,
                tx_str.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False
