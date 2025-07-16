# pycoin/wallet.py
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

class Wallet:
    @staticmethod
    def generate_keys(password: bytes = b"") -> (bytes, bytes):
        private_key = ec.generate_private_key(ec.SECP256K1())
        pem_priv = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password)
        )
        pem_pub = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem_priv, pem_pub
