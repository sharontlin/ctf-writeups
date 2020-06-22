# break repeating-key xor

# code written by gipi
def hamming_distance(a,b):
    result = 0
    for x, y in zip(bytearray(a), bytearray(b)):
        # we create a string removing the '0b' part
        bx = bin(x)[2:]
        by = bin(y)[2:]

        lenbx = len(bx)
        lenby = len(by)

        if lenbx < lenby:
            bx, by = by, bx

        # bx > by
        # we add a number of "0" much as missing
        for count in range(abs(lenbx - lenby)):
            by = '0' + by

        for _bx, _by in zip(bx, by):
            if _bx != _by:
                result += 1

    return result

def find_keysize(source, start=2, end=41):
    lowest_hd = float("inf")
    lowest_ks = 0
    for ks in range(start,end):
        hd = hamming_distance(source[:ks], source[ks:ks+ks])/ks
        if hd < lowest_hd:
            lowest_hd = hd 
            lowest_ks = ks 

    return lowest_ks

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

# print(hamming_distance('this is a test','wokka wokka!!!'))  
# keysize: 38

ciphertext = ""

with open('s1c6.txt') as f:
    for line in f: 
        ciphertext += line
    
ciphers = [ ciphertext[i:i+38] for i in range(0, len(ciphertext), 38) ]


print(ciphers)
        