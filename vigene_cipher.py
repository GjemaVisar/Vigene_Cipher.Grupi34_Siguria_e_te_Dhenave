import hashlib

def generate_keystream(seed, message_length):

if isinstance(seed, str):
seed=seed.encode('utf-8')
seed=int.from_bytes(hashlib.sha256(seed).digest(),byteorder='big')
keystream=[]
