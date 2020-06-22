# single byte xor cipher

import binascii

val = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    score = 0
    for c in s.lower():
        if c in freq:
            score += freq[c]
    return score

def decode(encoded):
    encoded = binascii.unhexlify(encoded)
    max_score = 0
    phrase = ""
    for key in range(256):
        decoded = ''.join(chr(ord(b) ^ key) for b in encoded)
        d_score = score(decoded)
        if d_score > max_score:
            max_score = d_score 
            phrase = decoded 
        
    return phrase

print(decode(val))

# Cooking MC's like a pound of bacon