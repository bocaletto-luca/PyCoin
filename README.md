# PyCoin

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> A lightweight, Python-native cryptocurrency designed for education and rapid experimentation with consensus protocols.  
> Built by **Bocaletto Luca**.

---

## Table of Contents

1. [Features](#features)  
2. [Architecture](#architecture)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Wallet Generation](#wallet-generation)  
   - [Running the P2P Node](#running-the-p2p-node)  
   - [Starting the API Server](#starting-the-api-server)  
   - [Launching the Block Explorer](#launching-the-block-explorer)  
4. [Command-Line Interface](#command-line-interface)  
5. [REST API](#rest-api)  
6. [P2P Networking](#p2p-networking)  
7. [Docker & Docker Compose](#docker--docker-compose)  
8. [Testing & Linting](#testing--linting)  
9. [Contributing](#contributing)  
10. [License](#license)  
11. [Contact](#contact)

---

## Features

- Pure-Python implementation of a blockchain with Proof-of-Work  
- Modular design to experiment with PoW, PoS, and other consensus algorithms  
- ECDSA key-pair wallet generation (secp256k1)  
- Peer-to-peer networking using WebSockets  
- RESTful API powered by FastAPI for chain queries, mining, and transactions  
- Minimal CLI with Typer for wallet and node management  
- Simple browser-based block explorer  
- Dockerized setup for multi-node testing  
- Comprehensive test suite (unit & integration)

---

## Architecture

```
pycoin/
├── docs/                  
│   └── whitepaper.md      # Project overview & protocol design
├── pycoin/                
│   ├── __init__.py        
│   ├── blockchain.py      # Block, Chain & Proof-of-Work  
│   ├── transaction.py     # Transaction model, sign & verify  
│   ├── wallet.py          # ECDSA key-pair generation  
│   ├── node.py            # P2P network via WebSockets  
│   └── api.py             # FastAPI REST endpoints  
├── explorer/              
│   └── index.html         # Simple block explorer  
├── cli.py                 # Typer-based CLI  
├── tests/                 
│   ├── test_blockchain.py  
│   ├── test_transaction.py 
│   ├── test_wallet.py     
│   └── test_node.py       
├── Dockerfile             
├── docker-compose.yml     
├── README.md              
└── requirements.txt       
```

---

## Getting Started

### Prerequisites

- Python 3.10 or newer  
- Git  
- (Optional) Docker & Docker Compose  

### Installation

```bash
git clone https://github.com/bocaletto-luca/pycoin.git
cd pycoin

# Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
.\.venv\Scripts\activate     # Windows

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Wallet Generation

Generate a new key pair (encrypted with an optional password):

```bash
python cli.py create-wallet --password "yourPassword"
```

This produces:
- `private.pem` (your encrypted private key)  
- `public.pem`  (your public key)

### Running the P2P Node

Start a peer-to-peer node (default ws://localhost:6789):

```bash
python pycoin/node.py
```

### Starting the API Server

Run the FastAPI-powered REST interface:

```bash
uvicorn pycoin.api:app --reload --port 8000
```

Available endpoints:

- `GET  /chain` – retrieve the full blockchain  
- `POST /transactions/new` – submit a new transaction  
- `GET  /mine?miner_address=<your_address>` – mine a new block  

### Launching the Block Explorer

Open `explorer/index.html` in your browser (ensure the API URL matches your server port).

---

## Command-Line Interface

```bash
# Create or decrypt a wallet
python cli.py create-wallet --password "..."

# Run an API node on a custom port
python cli.py run-node --port 8001
```

---

## REST API

```http
GET  /chain
POST /transactions/new
GET  /mine?miner_address=<address>
```

Use tools like `curl` or `httpx` to interact programmatically.

---

## P2P Networking

Peers communicate over WebSockets:

- Broadcast transactions:  
  ```json
  { "type": "transaction", "payload": { sender, recipient, amount, signature } }
  ```
- Broadcast blocks:  
  ```json
  { "type": "block", "payload": Block.__dict__ }
  ```
- Register peers:  
  ```json
  { "type": "register", "payload": { "peer": "ws://host:port" } }
  ```

---

## Docker & Docker Compose

Build and run two nodes for testing:

```bash
docker-compose up --build
```

- Node1 API → `http://localhost:8001`  
- Node2 API → `http://localhost:8002`  
- WS Peers on ports 6789 & 6790  

---

## Testing & Linting

Run test suite and style checks:

```bash
pytest -q
flake8 .
black --check .
```

---

## Contributing

1. Fork the repo  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add awesome feature"
   ```  
4. Push to your fork and open a Pull Request  

Please follow the code style (`black`, `flake8`) and write tests for new features.

---

## License

Distributed under the GPL License. See `LICENSE` for details.

---

## Contact

**Bocaletto Luca**  
– GitHub: [@bocaletto-luca](https://github.com/bocaletto-luca)  

---
