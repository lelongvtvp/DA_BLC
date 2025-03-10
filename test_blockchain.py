import pytest
from blockchain import Blockchain
@pytest.fixture
def blockchain ():
    return Blockchain()

def test_genesis_block(blockchain):
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    assert blockchain.chain[0].previous_hash == "0"

def test_add_transaction (blockchain):
    blockchain.add_transaction({"sender": "Alice", "receiver": "Bob", "amount": 10})
    assert len(blockchain.pending_transactions) == 1

def test_mine_block(blockchain):
    blockchain.add_transaction({"sender": "Alice", "receiver": "Bob", "amount" :10})
    blockchain.mine_block("miner1")
    assert len(blockchain.chain) == 2
    assert blockchain.chain[-1].transactions[0]['sender'] == "Alice"


