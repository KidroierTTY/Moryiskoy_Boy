class Field:
    def __init__(self, size, ships):
        self.size = int(size)
        self.ships = int(ships)
        self.ships_alive = ships
        self.grid = [[None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None]]