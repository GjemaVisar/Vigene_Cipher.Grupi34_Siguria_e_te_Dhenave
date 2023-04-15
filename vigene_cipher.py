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
    #Enkriptojme mesazhin duke shtuar secilin karakter te mesazhit me karakterin perkates te keystream-it
    for i in range(len(message)):
      num = (ord(message[i]) - 65 + keystream[i]) % 26
      encrypted_message += chr(num + 65)
    return encrypted_message


  def vigenere_decrypt(encrypted_message, seed):
      encrypted_message = encrypted_message.upper()
      keystream = generate_keystream(seed, len(encrypted_message))
      decrypted_message = ''
      # Dekriptojme mesazhin duke zbritur secilin karakter te mesazhit me karakterin perkates te keystream-it
      for i in range(len(encrypted_message)):
          num = (ord(encrypted_message[i]) - 65 - keystream[i]) % 26
          decrypted_message += chr(num + 65)
      return decrypted_message

message=input('Shkruani tekstin që deshironi të ennkriptoni:')
seed=input('Jepni seed-in si integer ose string: ')
encrypted_message=vigenere_encrypt(message,seed)
print('Mesazhi i enkriptuar: '+encrypted_message)
decrypted_message=vigenere_decrypt(encrypted_message,seed)
print('Mesazhi i dekriptuar: '+decrypted_message)











  
