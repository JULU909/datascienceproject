class gamestate:
    whitetomove = True
    castlingw = False
    castlingb = False
    def __init__(self):
        self.board = [
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]]
        self.movelog = []
        self.whitekingpositon = []
        self.blackkingposition = []

        
            
class information:
    def __init__(self):
        self.whitetomove = True



class heuristics :
    pawn = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-4, 68, 61, 47, 47, 49, 45, -1],
        [6, 16, 25, 33, 24, 24, 14, -6],
        [0, -1, 9, 28, 20, 8, -1, 11],
        [6, 4, 6, 14, 14, -5, 6, -6],
        [-1, -8, -4, 4, 2, -12, -1, 5],
        [5, 16, 16, -14, -14, 13, 15, 8],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    knight = [
        [-55, -40, -30, -28, -26, -30, -40, -50 ],
        [-37, -15, 0, -6, 4, 3, -17, -40 ],
        [-25, 5, 16, 12, 11, 6, 6, -29] ,
        [-24, 5, 21, 14, 18, 9, 11, -26] ,
        [-36, -5, 9, 23, 24, 21, 2, -24] ,
        [-32, -1, 4, 19, 20, 4, 11, -25] ,
        [-38, -22, 4, -1, 8, -5, -18, -34] ,
        [-50, -46, -32, -24, -36, -25, -34, -50]
    ]

    bishop = [
        [-14, -13, -4, -7, -14, -9, -16, -20],
        [-11, 6, 3, -6, 4, -3, 5, -4],
        [-11, -3, 5, 15, 4, -1, -5, -10],
        [-7, -1, 11, 16, 5, 11, 7, -13],
        [-4, 4, 10, 16, 6, 12, 4, -16],
        [-4, 4, 11, 12, 10, 7, 7, -12],
        [-11, 7, 6, 6, -3, 2, 1, -7],
        [-15, -4, -11, -4, -10, -10, -6, -17],
    ]

    rook=[
        [5, -6, 1, -4, -4, -6, 6, -3],
        [-6, 4, 2, 5, -1, 3, 4, -15],
        [-15, 3, 3, 0, -1, -6, 5, -9],
        [-16, 6, 0, -6, -3, -3, -4, -4],
        [-15, 6, 2, -6, 6, 0, -6, -10],
        [-6, -1, 3, -2, 6, 5, 0, -15],
        [-8, -4, 1, -4, 3, -5, -6, -5],
        [1, 0, -2, 1, 1, 4, 2, 0],
    ]

    queen =[
        [-21, -7, -6, 1, -8, -15, -10, -16],
        [-4, -5, 3, -4, 2, 6, 3, -10],
        [-13, -2, 7, 2, 6, 10, -4, -6],
        [-1, -4, 3, 1, 8, 8, -2, -2],
        [0, 6, 8, 1, -1, 1, 0, -3],
        [-11, 10, 6, 3, 7, 9, 4, -10],
        [-12, -6, 5, 0, 0, -5, 4, -10],
        [-20, -6, -7, -7, -4, -12, -9, -20]
    ]

    king = [
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -37, -43, -49, -50, -39, -40, -30],
        [-32, -41, -40, -46, -49, -40, -46, -30],
        [-32, -38, -39, -52, -54, -39, -39, -30],
        [-20, -33, -29, -42, -44, -29, -30, -19],
        [-10, -18, -17, -20, -22, -21, -20, -13],
        [14, 18, -1, -1, 4, -1, 15, 14],
        [21, 35, 11, 6, 1, 14, 32, 22]
    ]

