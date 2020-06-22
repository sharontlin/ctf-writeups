# convert hex to base64

import codecs 

val = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_b64(val):
    return codecs.encode(codecs.decode(val, 'hex'), 'base64').decode()

