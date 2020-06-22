# repeating key xor

import binascii

val = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
new_val = ""
index = 0

for c in val:
    new_val += chr(ord(key[index%3]) ^ ord(c))
    index += 1

print binascii.hexlify(new_val)

