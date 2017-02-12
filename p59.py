#!/usr/bin/env python
from time import clock
from math import sqrt
import itertools
start = clock()

"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text;
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt the message and
find the sum of the ASCII values in the original text.
"""
#####################################################################################################################

# all numbers are base 10 in this file
# ascii values for a to z range from 97 to 122 (base 10)
# ascii values for A to A range from 65 to 90
# run all 3 letter permutations of the set a through z against the file

filename = '/Users/alisheikh/PycharmProjects/AliReelin/p059_cipher.txt'
with open(filename, "rt") as f:
    for line in f:
        cipher_list = line.split(',')
print cipher_list
cipher_list = map(int, cipher_list)
print cipher_list

# create a set
set_lower_case = {a for a in range(90, 127)}
set_upper_case = {a for a in range(65, 91)}
yes = set_lower_case | set_upper_case
print yes


from string import ascii_lowercase
list_of_letters = list(ascii_lowercase)

big = []
for triple in itertools.product(list_of_letters,repeat=3):
    print triple
    possible_key = [ord(c) for c in triple]
    print possible_key
    output = []
    for t in range(1, len(cipher_list)):
        store = cipher_list[t] ^ possible_key[t % len(possible_key)]
        #print cipher_list[t], possible_key[t % len(possible_key)], store
        if store not in yes: # if the xor results in a value outside of the ranges noted above, discard this decryption and move onto the next one
            output = []
            break
        else:
            output.append(chr(store))
    print ''.join(output)
    big.append(''.join(output))



big = filter(None, big)
print big










######################################################################################################################

stop = clock()
print("running time is %s" % (stop-start))
# strict rule: running time < 1 minute
# goal: as efficient as possible


