# cs_module.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

def generate_key(key_size):
    """
    Generate a random key of the given size.
    """
    return os.urandom(key_size)

def generate_aes_gcm_key():
    """
    Generate a random AES-GCM key.
    """
    return generate_key(16)

def generate_rsa_key(key_size):
    """
    Generate an RSA key of the given size.
    """
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )

def generate_ecdsa_key(curve):
    """
    Generate an ECDSA key for the given curve.
    """
    return ec.generate_private_key(curve)

def encrypt_aes_gcm(key, data):
    """
    Encrypt data using AES-GCM.
    """
    nonce = os.urandom(12)
    cipher = AESGCM(key)
    ciphertext, tag = cipher.encrypt_and_digest(nonce, data, associated_data=b"")
    return nonce + ciphertext + tag

def decrypt_aes_gcm(key, encrypted_data):
    """
    Decrypt data using AES-GCM.
    """
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:-16]
    tag = encrypted_data[-16:]
    cipher = AESGCM(key)
    plaintext = cipher.decrypt_and_verify(nonce, ciphertext, tag, associated_data=b"")
    return plaintext

def encrypt_rsa(key, data):
    """
    Encrypt data using RSA.
    """
    encryptor = key.encryptor(
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    encrypted_data = encryptor.encrypt(data)
    return encrypted_data

def decrypt_rsa(key, encrypted_data):
    """
    Decrypt data using RSA.
    """
    decryptor = key.decryptor(
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plaintext = decryptor.decrypt(encrypted_data)
    return plaintext

def sign_ecdsa(key, data):
    """
    Sign data using ECDSA.
    """
    signer = key.signer(
        ec.ECDSA(hashes.SHA256())
    )
    signature = signer.sign(data)
    return signature

def verify_ecdsa(key, data, signature):
    """
   Verify data using ECDSA.
    """
    verifier = key.verifier(
        ec.ECDSA(hashes.SHA256()),
        signature
    )
    verifier.verify(data)

# Example usage
aes_gcm_key = generate_aes_gcm_key()
data = b"This is a secret message."
encrypted_data = encrypt_aes_gcm(aes_gcm_key, data)
decrypted_data = decrypt_aes_gcm(aes_gcm_key, encrypted_data)
print("Original Data: ", data)
print("Decrypted Data: ", decrypted_data)

rsa_key = generate_rsa_key(2048)
data = b"This is a secret message."
encrypted_data = encrypt_rsa(rsa_key, data)
decrypted_data = decrypt_rsa(rsa_key, encrypted_data)
print("Original Data: ", data)
print("Decrypted Data: ", decrypted_data)

ecdsa_key = generate_ecdsa_key(ec.SECP384R1())
data = b"This is a secret message."
signature = sign_ecdsa(ecdsa_key, data)
verified = verify_ecdsa(ecdsa_key, data, signature)
print("Signature Verified: ", verified)
