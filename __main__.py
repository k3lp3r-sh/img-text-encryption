from PIL import Image
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2



width = 400
height = 300

cipher_img = Image.new(mode = 'RGB', size = (width, height))

raw_text = "The quick brown fox jumped over the lazy dog."
print("raw_text: ", raw_text)

'''
p = getPrime(1024)
q = getPrime(1024)
'''

with open(r'privatekeys.txt', 'r') as privkeys:
    l = privkeys.readlines()

p = int(l[0])
q = int(l[1])

privkeys.close()

n = p * q

e = 65537

phin = (p-1)*(q-1)

assert GCD(e, phin) == 1

d = inverse(e,phin)

message = bytes(raw_text, 'utf-8') 

message = bytes_to_long(message)

ciphertext = pow(message, e, n)

print(ciphertext)

#cipher_img.show()

