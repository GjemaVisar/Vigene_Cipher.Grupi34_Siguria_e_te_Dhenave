import hashlib

def generate_keystream(seed, message_length):

if isinstance(seed, str):
seed=seed.encode('utf-8')
seed=int.from_bytes(hashlib.sha256(seed).digest(),byteorder='big')
keystream=[]
#Per keystream-in e perdorim XOR-shift
for i in range(message_length):
  seed^=seed<<13
  seed^=seed>>17
  seed^=seed<<5
  num=seed&0x7fffffff
  keystream.append(num%26)
  return keystream
  
  
  def vigenere_encrypt(message, seed):
    message = message.upper()
    keystream = generate_keystream(seed, len(message))
    encrypted_message = ''
    #Enkriptojme mesazhin duke shtuar secilin karakter te mesazhot me karakterin perkates te keystream-it
  
