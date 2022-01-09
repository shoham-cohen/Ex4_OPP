from src.position import position


class Pokemon:
    def __init__(self, PokeDict: dict):
        self.src = None
        self.des = None
        self.value = float(PokeDict['value'])
        self.pos = position(PokeDict['pos'])
        self.type = int(PokeDict['type'])
        self.agent = None

    def __repr__(self) -> str:
        return str((self.src, self.des))
