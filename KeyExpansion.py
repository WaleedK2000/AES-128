# This file deals with key expansion

from Util import getGridsof16, rotateRowLeft
from SBox import getVal


def getRoundKey(w0, w1, w2, w3, current_round, constants):
    w4 = []
    w5 = []
    w6 = []
    w7 = []

    w3_leftshift = rotateRowLeft(w3, 1)
    w3_sbox = []

    for i in range(0, 4):
        w3_sbox.append(getVal(w3_leftshift[i]))

    for i in range(0, 4):
        w4.append(w0[i] ^ (w3_sbox[i] ^ constants[current_round - 1][i]))

    # w4 = w0 ^

    for i in range(0, 4):
        w5.append(w4[i] ^ w1[i])

    for i in range(0, 4):
        w6.append(w5[i] ^ w2[i])

    for i in range(0, 4):
        w7.append(w6[i] ^ w3[i])

    return w4, w5, w6, w7


def newExpansion(key):
    rounds = 11

    constants = [[1, 0, 0, 0]]

    for i in range(1, rounds):
        last_const = constants[-1]
        significant_constant = last_const[0] * 2
        # Check if constant is greater than 80(16) if it is XOR with 11b(16)
        if significant_constant > 0x80:
            significant_constant ^= 0x11b

        constants.append([significant_constant, 0, 0, 0])

    w0 = key[:4]
    w1 = key[4:8]
    w2 = key[8:12]
    w3 = key[12:16]

    rounds = 11

    for i in range(1, rounds):
        last_const = constants[-1]
        significant_constant = last_const[0] * 2
        # Check if constant is greater than 80(16) if it is XOR with 11b(16)
        if significant_constant > 0x80:
            significant_constant ^= 0x11b

        constants.append([significant_constant, 0, 0, 0])

    keys = []
    keys.append([w0, w1, w2, w3])

    print(keys[0][-4], 'LSFRKF ')

    for i in range(1, rounds):
        w4, w5, w6, w7 = getRoundKey(keys[i - 1][-4], keys[i - 1][-3], keys[i - 1][-2], keys[i - 1][-1], 1, constants)
        keys.append([w4, w5, w6, w7])

        print([hex(i) for i in w4], [hex(i) for i in w5], [hex(i) for i in w6], [hex(i) for i in w7],
              [hex(i) for i in w5],
              'nic')

        print('Round KEy', i, ' --------------- -')

    return keys
