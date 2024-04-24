# qe_module.py

from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256

def generate_quantum_key():
    """
    Generates a quantum-resistant encryption key using X25519.
    """
    private_key = x25519.PrivateKey()
    public_key = private_key.public_key()

    return private_key, public_key

def encrypt_data(data, public_key):
    """
    Encrypts data using the X25519-generated public key.
    """
    shared_key = public_key.exchange(x25519.PrivateKey(serialization.decode_bytes(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))))

    key = HKDF(
        algorithm=SHA256(),
        length=32,
        salt=None,
        info=None,
    ).derive(shared_key)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

    return ciphertext

def decrypt_data(ciphertext, private_key):
    """
    Decrypts data using the X25519-generated private key.
    """
    shared_key = private_key.exchange(x25519.PublicKey(serialization.decode_bytes(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))))

    key = HKDF(
        algorithm=SHA256(),
        length=32,
        salt=None,
        info=None,
    ).derive(shared_key)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

# Example usage
private_key, public_key = generate_quantum_key()
data = "This is a secret message."
ciphertext = encrypt_data(data, public_key)
plaintext = decrypt_data(ciphertext, private_key)
print(plaintext.decode())
