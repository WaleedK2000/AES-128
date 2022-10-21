# Flattens array, then converts it into grid of 16
def getGridsof16(arr):
    ret_grids = []
    flatList = arr
    count_f_l = 0

    print(len(arr) // 16, 'wow')
    print(flatList, 'fl')

    for i in range(len(arr) // 16):
        print('w')
        grid = []
        for j in range(0, 4):
            gridj = []
            for k in range(0, 4):
                # print(flatList[count_f_l], 'ahah')
                gridj.append( flatList[count_f_l])

                count_f_l += 1

            grid.append(gridj)

        ret_grids.append(grid)

    print(ret_grids, 'rrrrrrrrrrrr')

    return ret_grids


# function roates list left by n
def rotateRowLeft(row, n):
    return row[n:] + row[:n]
