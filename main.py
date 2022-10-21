from SBox import SBox

import random

def hex_number( count, padded=False ):
    # This currently generates a number of length count hex digits.
    # Pad on the left with 0's if padded is True:
    x = random.randint( 0, 16**count )
    hexdig = "%x" % x
    if padded:
        out = hexdig.zfill( count ) # pad with 0 if necessary
        return out
    else:
        return hexdig
def AESvectors( size, num, padded ):
    # generate num vectors (one per line) of size at most count
    # hex digits
    for i in range( num ):
        print( hex_number( size, padded ) )


def main():
    rcon = [[1, 0, 0, 0]]

    for _ in range(1, 10):
        rcon.append([rcon[-1][0] * 2, 0, 0, 0])
        if rcon[-1][0] > 0x80:
            rcon[-1][0] ^= 0x11b

        print(rcon[-1])



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


