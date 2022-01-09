from src.position import position


class Agent:
    def __init__(self, AgentDict: dict):
        self.id = int(AgentDict['id'])
        self.value = float(AgentDict['value'])
        self.speed = float(AgentDict['speed'])
        self.time = float('inf')
        self.src = int(AgentDict['src'])
        self.dest = int(AgentDict['dest'])
        self.Next = None
        self.pos = position(AgentDict['pos'])
        self.preference = 0

    def update(self, AgentDict: dict) -> None:
        self.value = float(AgentDict['value'])
        self.speed = float(AgentDict['speed'])
        self.time = float('inf')
        self.src = int(AgentDict['src'])
        self.dest = int(AgentDict['dest'])
        coordinates = str(AgentDict['pos']).split(',')
        self.pos = []
        for n in coordinates:
            self.pos.append(float(n))
        self.preference = 0

    def __repr__(self) -> str:
        return str((self.src, self.dest))