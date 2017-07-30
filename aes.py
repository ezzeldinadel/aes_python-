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
unpad = lambda s : s[0:-ord(s[-1])]# ord a ->  97
randomword = lambda length: ''.join(random.choice(char_set*6) for i in range(length))


# lets do aes 
class AESCipher:

    def __init__( self, key ):
        self.key = key 

    def encrypt( self, raw ):
        padded_raw = pad(raw)
        #print raw
        iv = Random.new().read( AES.block_size ) #vector 
        ci = AES.new( self.key, AES.MODE_CBC, iv ) #cipher 
        #print cipher 
        return base64.b64encode( iv + ci.encrypt( padded_raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        ci = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(ci.decrypt( enc[16:] ))
    

# main program 
message = 'ezzmainpassworD123//'
key = randomword(32) # keys can be 32 24 or 16 
AESCIPHER1 = AESCipher(key) 
encrypted_message = AESCIPHER1.encrypt(message)

print message
print 
print key 
print 
print encrypted_message
print 
print AESCIPHER1.decrypt(encrypted_message)
