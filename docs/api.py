from flask import Flask, request, jsonify
from blockchain import Blockchain
from mesh_network import MeshNetwork
from quantum_security import QuantumSecurity

app = Flask(__name__)

# Initialize the functionalities
blockchain = Blockchain()
mesh_network = MeshNetwork()
quantum_security = QuantumSecurity()

@app.route('/blockchain/new_transaction', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Add the new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mesh_network/send_message', methods=['POST'])
def send_message():
    values = request.get_json()
    required = ['message', 'destination']
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Send the message
    success = mesh_network.send_message(values['message'], values['destination'])
    response = {'message': 'Message sent successfully'} if success else {'message': 'Failed to send message'}
    return jsonify(response), 200

@app.route('/quantum_security/encrypt', methods=['POST'])
def encrypt_message():
    values = request.get_json()
    required = ['message']
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Encrypt the message
    encrypted_message = quantum_security.encrypt(values['message'])
    response = {'encrypted_message': encrypted_message}
    return jsonify(response), 200

@app.route('/quantum_security/decrypt', methods=['POST'])
def decrypt_message():
    values = request.get_json()
    required = ['encrypted_message']
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Decrypt the message
    decrypted_message = quantum_security.decrypt(values['encrypted_message'])
    response = {'decrypted_message': decrypted_message}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
