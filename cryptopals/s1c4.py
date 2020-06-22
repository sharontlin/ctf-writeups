# detect single character xor

import binascii

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
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
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

with open('s1c4.txt') as f:
    max_score = 0
    phrase = ""
    for line in f: 
        line = line.rstrip() 
        d_line = decode(line)
        d_score = score(d_line)
        if d_score > max_score:
            max_score = d_score
            phrase = d_line

    print phrase 

# Now that the party is jumping