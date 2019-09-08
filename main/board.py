#tracks board details
class Board:

    def __init__(self):
        #coordinates of legal spaces on board at 750x750 in order
        # relative to the 2d array
        self.XYPoints = [(54,52),(375,52),(697,52),
                         (160,160),(375,160),(590,160),
                         (268,265),(375,265),(483,265),
                         (54,372),(163,372),(269,372),
                         (482,372),(590,372),(697,372),
                         (269,480),(375,480),(482,480),
                         (162,586),(375,586),(589,586),
                         (54,694),(375,694),(696,694)]

        #Reference
        self.NumPoints = [[1,0,0,2,0,0,3],
                          [0,4,0,5,0,6,0],
                          [0,0,7,8,9,0,0],
                          [10,11,12,0,13,14,15],
                          [0,0,16,17,18,0,0],
                          [0,19,0,20,0,21,0],
                          [22,0,0,23,0,0,24]]

        self.Pieces = []
    