# Decrypt using a Vigenere Cipher
# Proof of Concept, Code Golf
# Copyright (c) 2022 TX

msg = 'k tgxs vq ftmfg fghyqek kgkmtwva nt zqtegginrn apalkhwvr'.replace(' ', '')
key = 'CISCOCCNAS'.lower()
m = len(key)
txt = [ord(j) - ord(key[i % m]) for i,j in enumerate(msg)]
print(''.join(map(lambda i: chr(i % 26 + 97), txt)))
