# PyCoin Whitepaper

## 1. Introduction  
PyCoin is a lightweight, Python-native cryptocurrency designed for education and rapid experimentation with consensus algorithms.

## 2. Architecture  
- **Blockchain Core**: Block, Chain, Proof-of-Work (SHA-256)  
- **P2P Network**: WebSocket gossip protocol  
- **Wallet**: ECDSA keypairs (SECP256K1)  
- **API**: FastAPI REST endpoints

## 3. Consensus  
PoW with adjustable difficulty.  
Block time target: 2 minutes.  
Halving every 210 000 blocks.

## 4. Transaction Model  
UTXO-inspired: each tx has `sender`, `recipient`, `amount`, `signature`.  
Fees determinati dall’utente.

## 5. Security  
- Firma ECDSA SHA-256  
- Veriﬁca integrità blocchi e catena  
- Meccanismi base anti-double-spend

## 6. Roadmap  
1. PoW MVP  
2. P2P Networking  
3. Wallet CLI/GUI  
4. Smart-contracts Python  
5. Staking & PoS experiment  
