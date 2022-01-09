import json
import math
import time

from src.Agent import Agent
from src.DiGraph import DiGraph
from src.Pokemon import Pokemon

eps = 0.000001


class TheGame:
    def __init__(self) -> None:
        self.AgentsList = {}
        self.graph = DiGraph()
        self.PokeList = []

    def setNewVal(self, agents=None, graph=None, pokemons=None) -> None:
        if agents is not None:
            newAgents = json.loads(agents)
            for agent in newAgents["Agents"]:
                Id = int(agent['Agent']['id'])
                if Id in self.AgentsList:
                    self.AgentsList[Id].update(agent['Agent'])
                else:
                    self.AgentsList[Id] = Agent(agent['Agent'])

        if graph is not None:
            self.graph = DiGraph()
            newGraph = json.loads(graph)
            for n in newGraph["Nodes"]:
                Id = int(n["id"])
                if "pos" in n:
                    self.graph.add_node(Id, n["pos"])
                else:
                    self.graph.add_node(Id)
            for edge in newGraph["Edges"]:
                self.graph.add_edge(int(edge["src"]), int(edge["dest"]), float(edge["w"]))

        if pokemons is not None:
            self.PokeList = []
            newPokemons = json.loads(pokemons)
            for pokemon in newPokemons['Pokemons']:
                currPokemon = Pokemon(pokemon['Pokemon'])
                self.findPokeEdge(currPokemon)
                self.PokeList.append(currPokemon)

    def findPokeEdge(self, currPokemon: Pokemon):
        for firstNode in self.graph.nodes:
            for secondNode in self.graph.nodes:
                nodesDist = math.sqrt(
                    math.pow(float(self.graph.nodes[firstNode].pos.x) - float(self.graph.nodes[secondNode].pos.x),
                             2) + math.pow(
                        float(self.graph.nodes[firstNode].pos.y) - float(self.graph.nodes[secondNode].pos.y), 2))
                pokeDist = math.sqrt(
                    math.pow(float(self.graph.nodes[firstNode].pos.x) - float(currPokemon.pos.x), 2) + math.pow(
                        float(self.graph.nodes[firstNode].pos.y) - float(currPokemon.pos.y), 2)) + math.sqrt(
                    math.pow(float(self.graph.nodes[secondNode].pos.x) - float(currPokemon.pos.x), 2) + math.pow(
                        float(self.graph.nodes[secondNode].pos.y) - float(currPokemon.pos.y), 2))
                if abs(nodesDist - pokeDist) <= eps:
                    str1 = str(firstNode)
                    str2 = str(secondNode)
                    str3 = ","
                    stri = str1 + str3 + str2
                    if stri in self.graph.nodes[firstNode].edges:
                        if currPokemon.type > 0:
                            currPokemon.des = max(firstNode, secondNode)
                            currPokemon.src = min(firstNode, secondNode)
                        else:
                            currPokemon.des = min(firstNode, secondNode)
                            currPokemon.src = max(firstNode, secondNode)
                        return

    def allocateAgent(self, agent: Agent, preference=0) -> None:
        t_list = []
        for p in self.PokeList:
            if p.src == agent.src:
                t_list.append((p, (0, (0, []))))
            d = self.shortest_path(agent.src, p.src)
            t = (d[0] / agent.speed)
            t_list.append((p, (t, d)))
        t_list.sort(key=lambda x: x[1][0])
        NEXT = t_list[preference][0]
        t = t_list[preference][1][0]
        if NEXT.agent is not None:
            next_agent = NEXT.agent
            if t > next_agent.time:
                self.allocateAgent(agent, preference + 1)
                return
            else:
                NEXT.agent = agent
                agent.preference = preference
                agent.time = t
                route = t_list[preference][1][1][1]
                route.append(NEXT.des)
                if len(route) > 1:
                    agent.Next = route[1]
                else:
                    agent.Next = route[0]
                self.allocateAgent(next_agent, next_agent.preference + 1)
                return
        NEXT.agent = agent
        agent.time = t
        agent.preference = preference
        route = t_list[preference][1][1][1]
        route.append(NEXT.des)
        if len(route) > 1:
            agent.Next = route[1]
        else:
            agent.Next = route[0]

    def sleep(self):
        maxTime = -1
        for i in self.AgentsList:
            if self.AgentsList.get(i).speed > maxTime:
                maxTime = self.AgentsList.get(i).speed
        if maxTime > 5:
            maxTime = maxTime / 100
            if maxTime <= 0:
                maxTime = 0
            return time.sleep(maxTime)
        else:
            return time.sleep(0.087)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        (d, prev) = self.dikjestra(id1)
        l = {}
        i = id2
        l[0] = id2
        x = 1
        while i != id1:
            if i == -1:
                return None
            l[x] = prev[i]
            i = l[x]
            x += 1
        res = []
        x -= 1
        index = 0
        while x != -1:
            res.append(l[x])
            x -= 1
            index += 1

        return d[id2], res

    def dikjestra(self, src: int) -> (list, list):
        finishedNodes = 0
        INFINITY = 1000000
        prev = {}
        distance = {}
        visited = {}
        for i in self.graph.nodes:
            prev[i] = -1
            distance[i] = INFINITY
            visited[i] = False

        distance[src] = 0
        prev[src] = 0
        for i in self.graph.nodes.get(src).edges:
            if self.graph.nodes.get(src).edges.get(i).src == src:
                if self.graph.nodes.get(src).edges.get(i).w < distance[self.graph.nodes.get(src).edges.get(i).des]:
                    distance[self.graph.nodes.get(src).edges.get(i).des] = self.graph.nodes.get(src).edges.get(i).w
                    prev[self.graph.nodes.get(src).edges.get(i).des] = self.graph.nodes.get(src).edges.get(i).src

        visited[src] = True
        finishedNodes += 1
        while finishedNodes != self.graph.v_size():
            min = INFINITY
            result = 0
            for i in self.graph.nodes:
                if distance[i] < min and visited[i] == False:
                    min = distance[i]
                    result = i

            for i in self.graph.nodes.get(result).edges:
                if self.graph.nodes.get(result).edges.get(i).src == result:
                    if distance[self.graph.nodes.get(result).edges.get(i).src] + self.graph.nodes.get(result).edges.get(
                            i).w < distance[self.graph.nodes.get(result).edges.get(i).des]:
                        distance[self.graph.nodes.get(result).edges.get(i).des] = distance[self.graph.nodes.get(
                            result).edges.get(i).src] + self.graph.nodes.get(result).edges.get(i).w
                        prev[self.graph.nodes.get(result).edges.get(i).des] = self.graph.nodes.get(result).edges.get(
                            i).src

            visited[result] = True
            finishedNodes += 1

        return distance, prev
