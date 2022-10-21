# from SBox import SBox
from KeyExpansion import expansionAlgorithm, newExpansion
from Util import getGridsof16, rotateRowLeft
from SBox import getVal
import random


def hex_number(count, padded=False):
    # This currently generates a number of length count hex digits.
    # Pad on the left with 0's if padded is True:
    x = random.randint(0, 16 ** count)
    hexdig = "%x" % x
    if padded:
        out = hexdig.zfill(count)  # pad with 0 if necessary
        return out
    else:
        return hexdig


def AESvectors(size, num, padded):
    # generate num vectors (one per line) of size at most count
    # hex digits
    for i in range(num):
        print(hex_number(size, padded))


def main():
    key = '5468617473206D79204B756E67204675'

    # [line[i:i + n] for i in range(0, len(line), n)]

    nkey = [key[i:i + 2] for i in range(0, len(key), 2)]

    print(nkey, 'new key')

    rounds = 11
    byteKey = [int(i, 16) for i in nkey]

    print([hex(i) for i in byteKey], 'byte key')

    newExpansion(byteKey)

    # # print(getGridsof16(byteKey)[0])
    #
    # rcon = [[1, 0, 0, 0]]
    #
    # for _ in range(1, rounds):
    #     rcon.append([rcon[-1][0] * 2, 0, 0, 0])
    #     if rcon[-1][0] > 0x80:
    #         rcon[-1][0] ^= 0x11b
    #
    # key_grid = getGridsof16(byteKey)[0]
    #
    # print(key_grid, 'key_gri4444444444444d')
    #
    # for round in range(rounds):
    #     last_column = [row[-1] for row in key_grid]
    #     last_column_rotate_step = rotateRowLeft(last_column, 1)
    #     last_column_sbox_step = [getVal(b) for b in last_column_rotate_step]
    #     last_column_rcon_step = [last_column_sbox_step[i]
    #                              ^ rcon[round][i] for i in range(len(last_column_rotate_step))]
    #
    #     for r in range(4):
    #         key_grid[r] += bytes([last_column_rcon_step[r]
    #                               ^ key_grid[r][round * 4]])
    #
    #     # Three more columns to go
    #     for i in range(len(key_grid)):
    #         for j in range(1, 4):
    #             key_grid[i] += bytes([key_grid[i][round * 4 + j]
    #                                   ^ key_grid[i][round * 4 + j + 3]])
    #
    # round = 1
    #
    # f = [row[round * 4: round * 4 + 4] for row in key_grid]
    # print('final', f)
    #
    # f_he = [hex(he) for he in f[1]]
    # print('s ', f_he)

    # print(byteKey)
    # print(expansionAlgorithm(byteKey))
    #
    # print('byte len', len(byteKey))
    # print(' len', len(key))
    #
    # str = hex_number(128)[3]
    #
    # print('orf', str)
    # print(type(str))
    #
    # base16INT = int(str, 16)
    #
    # print("value", base16INT)
    #
    # print("value", type(base16INT))
    #
    # hex_value = hex(base16INT)
    #
    # print(hex_value)

    # rcon = [[1, 0, 0, 0]]
    #
    # for _ in range(1, 10):
    #     rcon.append([rcon[-1][0] * 2, 0, 0, 0])
    #     if rcon[-1][0] > 0x80:
    #         rcon[-1][0] ^= 0x11b
    #
    #     print(rcon[-1])
    #

    # v1 = 0b11111000
    #
    # sbox = SBox()
    #
    # print(hex(0b1111))
    # print(hex(0b1000))
    #
    # print(hex(sbox.getVal(v1)))
    #
    # # print(bin(v1))
    # #
    # # # Get First 4 Bits (1st nibble)
    # # row = v1 >> 4
    # # # Get Last 4 Bits (2nd nibble)
    # # col = v1 & 0x0F
    # #
    # # print(0x0F)
    # #
    # # print(bin(row))
    # # print(bin(col))


if __name__ == "__main__":
    main()
