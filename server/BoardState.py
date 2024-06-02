class BoardState:
    def __init__(self, computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns):
        self._computerKings = computerKings
        self._computerRooks = computerRooks
        self._computerBishops = computerBishops
        self._computerQueens = computerQueens
        self._computerKnights = computerKnights
        self._computerPawns = computerPawns
        self._humanKings = humanKings
        self._humanRooks = humanRooks
        self._humanBishops = humanBishops
        self._humanQueens = humanQueens
        self._humanKnights = humanKnights
        self._humanPawns = humanPawns

    @property
    def computerKings(self):
        return self._computerKings

    @computerKings.setter
    def computerKings(self, value):
        self._computerKings = value

    @property
    def computerRooks(self):
        return self._computerRooks

    @computerRooks.setter
    def computerRooks(self, value):
        self._computerRooks = value

    @property
    def computerBishops(self):
        return self._computerBishops

    @computerBishops.setter
    def computerBishops(self, value):
        self._computerBishops = value

    @property
    def computerQueens(self):
        return self._computerQueens

    @computerQueens.setter
    def computerQueens(self, value):
        self._computerQueens = value

    @property
    def computerKnights(self):
        return self._computerKnights

    @computerKnights.setter
    def computerKnights(self, value):
        self._computerKnights = value

    @property
    def computerPawns(self):
        return self._computerPawns

    @computerPawns.setter
    def computerPawns(self, value):
        self._computerPawns = value

    @property
    def humanKings(self):
        return self._humanKings

    @humanKings.setter
    def humanKings(self, value):
        self._humanKings = value

    @property
    def humanRooks(self):
        return self._humanRooks

    @humanRooks.setter
    def humanRooks(self, value):
        self._humanRooks = value

    @property
    def humanBishops(self):
        return self._humanBishops

    @humanBishops.setter
    def humanBishops(self, value):
        self._humanBishops = value

    @property
    def humanQueens(self):
        return self._humanQueens

    @humanQueens.setter
    def humanQueens(self, value):
        self._humanQueens = value

    @property
    def humanKnights(self):
        return self._humanKnights

    @humanKnights.setter
    def humanKnights(self, value):
        self._humanKnights = value

    @property
    def humanPawns(self):
        return self._humanPawns

    @humanPawns.setter
    def humanPawns(self, value):
        self._humanPawns = value

    def boardClone(self):
        return BoardState(
            self._computerKings,
            self._computerRooks,
            self._computerBishops,
            self._computerQueens,
            self._computerKnights,
            self._computerPawns,
            self._humanKings,
            self._humanRooks,
            self._humanBishops,
            self._humanQueens,
            self._humanKnights,
            self._humanPawns
        )