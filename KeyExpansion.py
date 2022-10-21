class KeyExpansion:
    def expansionAlgorithm(self, originalKey):

        constants = [1, 0, 0, 0]
        rounds = 11

        for i in range(1, rounds):
            significantConstant = constants[-1][0] * 2
            if significantConstant > 0x80:
                significantConstant ^= 0x11b

