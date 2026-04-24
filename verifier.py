# verification/verifier.py
from hashing.hasher import generate_hash
from blockchain.web3_client import get_hash

def verify(logs):
    results = []

    for i, log in enumerate(logs):
        local_hash = generate_hash(log)
        chain_hash = get_hash(i)

        if local_hash == chain_hash:
            results.append("OK")
        else:
            results.append("TAMPERED")

    return results