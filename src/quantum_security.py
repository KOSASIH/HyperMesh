from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from numpy.random import randint
import numpy as np

# Constants
n = 100  # Number of qubits / bits in the key

# Step 1: Alice generates random bits
alice_bits = randint(2, size=n)

# Step 2: Alice generates random basis
alice_bases = randint(2, size=n)

# Step 3: Alice encodes her bits in the chosen basis
def encode_message(bits, bases):
    message = []
    for i in range(n):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0:  # Prepare qubit in Z basis
            if bits[i] == 0:
                pass  # |0>
            else:
                qc.x(0)  # |1>
        else:  # Prepare qubit in X basis
            if bits[i] == 0:
                qc.h(0)  # |+>
            else:
                qc.x(0)
                qc.h(0)  # |->
        qc.barrier()
        message.append(qc)
    return message

alice_message = encode_message(alice_bits, alice_bases)

# Step 4: Bob generates random basis
bob_bases = randint(2, size=n)

# Step 5: Bob measures Alice's qubits
def measure_message(message, bases):
    backend = Aer.get_backend('qasm_simulator')
    measurements = []
    for qc, basis in zip(message, bases):
        if basis == 1:
            qc.h(0)
        qc.measure(0, 0)
        result = execute(qc, backend, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

bob_measurements = measure_message(alice_message, bob_bases)

# Step 6: Alice and Bob share their basis
alice_bases_shared = alice_bases
bob_bases_shared = bob_bases

# Step 7: Alice and Bob discard mismatched basis bits
alice_key = []
bob_key = []
for i in range(n):
    if alice_bases_shared[i] == bob_bases_shared[i]:
        alice_key.append(alice_bits[i])
        bob_key.append(bob_measurements[i])

# Step 8: Verify the key
print("Alice's key: ", alice_key)
print("Bob's key:  ", bob_key)
print("Key match: ", np.array_equal(alice_key, bob_key))
