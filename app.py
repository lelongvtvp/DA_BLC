from flask import Flask, request, jsonify, send_from_directory
from blockchain import Blockchain
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json
import requests
app = Flask(__name__)
CORS(app)
socketIO = SocketIO(app)
nodes = set()
blockchain = Blockchain()
@app.route("/")
def serve_frontend():
    return send_from_directory('static', 'index.html')
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)
@app.route('/mine', methods = ['GET'])
def mine():
    blockchain.mine_block("miner1")
    return jsonify({"message": "Block mined!", "chain": [block.__dict__ for block in blockchain.chain]})
@app.route('/transactions/new', methods = ['POST'])
def new_transaction():
    data = request.get_json()
    blockchain.add_transaction(data)
    return jsonify({"message": "Transaction added!", "pending_transactions": blockchain.pending_transactions})
@app.route('/chain', methods = ['GET'])
def get_chain():
    blockchain_data = json.dumps([block.__dict__ for block in blockchain.chain], indent=4)

    with open("blockchain.txt", "w") as file:
        file.write(blockchain_data)
    return jsonify({"message": "Blockchain saved to blockchain.txt"})
@app.route('/register_node', methods=['POST'])
def register_node():
    node_address = request.json['node']
    if node_address.startswith("http://127.0.0.1"):
        nodes.add(node_address)
        return jsonify({"message": "Node registered", "node": list(nodes)})
    return jsonify({"error": "Invalid node"}),
@socketIO.on('sync_blockchain')
def sync_blockchain(data):
    global blockchain
    blockchain = data
    emit('blockchain_updated', blockchain, broadcast=True)

if __name__ == '__main__':
    socketIO.run(app, port=5000)