#imports 
import base64
from Crypto import Random
import random, string
from Crypto.Cipher import AES

# definitions
BlockSize = 128 
char_set = string.lowercase + string.ascii_uppercase + string.digits + string.ascii_letters

#functions 
pad = lambda s: s + (BlockSize - len(s) % BlockSize) * chr(BlockSize - len(s) % BlockSize)# chr 97 -> a 
unpad = lambda s : s[0:-ord(s[-1])]# ord a ->  97 # keys can be 32 24 or 16 
randomword = lambda length: ''.join(random.choice(char_set*6) for i in range(length))
def generate_random_keys(list_length, wordlength): 
    keylist =[]
    for i in range(0,list_length):
        keylist.append(randomword(wordlength))
    return keylist

# lets do aes 
class AESCipher:

    def __init__( self, key ):
        self.key = key 
        AES.block_size =16
        AES.key_size=32
    def encrypt( self, raw ):
        padded_raw = pad(raw)
        #print raw
        iv = Random.new().read( AES.block_size ) #vector 
        ci = AES.new( self.key, AES.MODE_CBC, iv ) #cipher 
        #print cipher 
        return base64.b64encode( iv + ci.encrypt( padded_raw ) ) #prepend iv & encode 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc) #decode 
        iv = enc[:16] # get iv 
        ci = AES.new(self.key, AES.MODE_CBC, iv ) #cipher 
        return unpad(ci.decrypt( enc[16:] )) #decrypt given vector and unpad 
    

## main program 
#
#CHANGE THE FOLLOWING THREE LINES ONLY! 
message = 'ezzmainpassworD123//' # <-- This ur secret message 
keys = generate_random_keys(10, 32) # <-- This generating you a list of keys 
i = 5 # <-- This the key you choose to use index number in the list 
#
AESCIPHER1 = AESCipher(keys[i]) # <-- This the cipher being created DONT CHANGE 
encrypted_message = AESCIPHER1.encrypt(message)# <-- This the message being encrypted DONT CHANGE 
decrypted_message =AESCIPHER1.decrypt(encrypted_message)# <-- This the message being decrypted DONT CHANGE 
#
#display what we have 
print message
print 
print keys[i] 
print 
print encrypted_message
print 
print decrypted_message
