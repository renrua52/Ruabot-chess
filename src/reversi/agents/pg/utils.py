import torch

def getModelInput(board):
    grid = board.getGrid()
    height, width = board.getSize()
    ret = torch.zeros(3, height, width)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                ret[0][i][j] = 1
            elif grid[i][j] == board.getTurn():
                ret[1][i][j] = 1
            else:
                ret[2][i][j] = 1

    return ret.unsqueeze(0)

