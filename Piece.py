class Piece(object):
    """Representation of a Hive Piece"""
    def __init__(self, color, kind, number):
        self.color = color      # 'b' or 'w'
        self.kind = kind        # different Pieces: ['A', 'B', 'G', 'Q', 'S']
        self.number = number    # how many played [1, 2, 3]
    def __repr__(self):
        return "%s%s%s" % (self.color, self.kind, self.number)