"""
N rooks problem

    every rook in every column and row can not attack each other

"""

def placeR(board, r):
    n = len(board)
    if r == n:
        print(board)
    else:
        for j in range(n):
            legal = True
            for i in range(r):
                if board[i] == j:
                    legal = False
            if legal:
                board[r] = j
                placeR(board, r+1)

if __name__ == "__main__":
    placeR([0 for _ in range(8)],0)
