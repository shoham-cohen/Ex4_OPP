import json
import pygame
from pygame import Color, display, gfxdraw, image, transform, mouse
from pygame.constants import RESIZABLE
from src.TheGame import TheGame
from src.client import Client

WIDTH, HEIGHT = 1200, 600
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=15, flags=RESIZABLE)
time = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 15, bold=True)
radius = 1000
back = 'backk.png'
ash = 'ash.png'
type1 = 'pikachu.png'
type2 = 'charmender.png'


class gui():
    def __init__(self, thegame: TheGame, client: Client) -> None:
        self.client = client
        self.game = thegame
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        self.background = image.load(back)
        self.ashPhoto = image.load(ash)
        self.ashPhoto = pygame.transform.scale(self.ashPhoto, (40, 40))
        self.PH_type1 = image.load(type1)
        self.PH_type1 = pygame.transform.scale(self.PH_type1, (30, 30))
        self.PH_type2 = image.load(type2)
        self.PH_type2 = pygame.transform.scale(self.PH_type2, (30, 30))
        self.minx = 100000.0
        self.maxx = 0.0
        self.miny = 100000.0
        self.maxy = 0.0
        self.edges = {}
        self.Bquit = CreatBotton((220, 220, 220), 2, 2, 65, 24, 'STOP')
        self.Btime = CreatBotton((220, 220, 220), 2 + 1 * 65, 2, 65, 24, 'TIME')
        self.Bmove = CreatBotton((220, 220, 220), 2 + 2 * 65, 2, 65, 24, 'MOVES')
        self.Bgrade = CreatBotton((220, 220, 220), 2 + 3 * 65, 2, 65, 24, 'GRADE')
        for i in self.game.graph.nodes:
            if float(self.game.graph.nodes.get(i).pos.x) < self.minx:
                self.minx = float(self.game.graph.nodes.get(i).pos.x)
            if float(self.game.graph.nodes.get(i).pos.x) > self.maxx:
                self.maxx = float(self.game.graph.nodes.get(i).pos.x)
            if float(self.game.graph.nodes.get(i).pos.y) < self.miny:
                self.miny = float(self.game.graph.nodes.get(i).pos.y)
            if float(self.game.graph.nodes.get(i).pos.y) > self.maxy:
                self.maxy = float(self.game.graph.nodes.get(i).pos.y)
            for j in self.game.graph.nodes.get(i).edges:
                if j not in self.edges:
                    self.edges[j] = self.game.graph.nodes.get(i).edges.get(j)

    def scale(self, point, minS, maxS, minPoint, maxPoint):
        return int(((point - minPoint) / (maxPoint - minPoint)) * (maxS - minS) + minS)

    def NodeDrawer(self):
        for i in self.game.graph.nodes:
            x = self.scale(float(self.game.graph.nodes.get(i).pos.x), 60, screen.get_width() - 60, self.minx, self.maxx)
            y = self.scale(float(self.game.graph.nodes.get(i).pos.y), 60, screen.get_height() - 60, self.miny,
                           self.maxy)
            gfxdraw.filled_circle(screen, x, y, 10, Color(255, 255, 255))
            j = FONT.render(str(i), True, pygame.Color(0, 0, 0))
            k = j.get_rect(center=(x, y))
            screen.blit(j, k)

    def EdgeDrawer(self):
        for i in self.edges:
            sX = self.scale(float(self.game.graph.nodes[self.edges[i].src].pos.x), 60, screen.get_width() - 60,
                            self.minx,
                            self.maxx)
            sY = self.scale(float(self.game.graph.nodes[self.edges[i].src].pos.y), 60, screen.get_height() - 60,
                            self.miny,
                            self.maxy)
            dX = self.scale(float(self.game.graph.nodes[self.edges[i].des].pos.x), 60, screen.get_width() - 60,
                            self.minx,
                            self.maxx)
            dY = self.scale(float(self.game.graph.nodes[self.edges[i].des].pos.y), 60, screen.get_height() - 60,
                            self.miny,
                            self.maxy)
            pygame.draw.line(screen, Color(25,25,112), (sX, sY), (dX, dY), width=4)

    def PokeDrawer(self):
        for i in self.game.PokeList:
            x = self.scale(float(i.pos.x), 50, screen.get_width() - 75, self.minx, self.maxx)
            y = self.scale(float(i.pos.y), 50, screen.get_height() - 75, self.miny,
                           self.maxy)
            if i.type < 0:
                self.screen.blit(self.PH_type1, (x, y))
            else:
                self.screen.blit(self.PH_type2, (x, y))

    def AgentDrawer(self):
        for i in self.game.AgentsList:
            x = self.scale(float(self.game.AgentsList[i].pos[0]), 50, screen.get_width() - 75, self.minx, self.maxx)
            y = self.scale(float(self.game.AgentsList[i].pos[1]), 50, screen.get_height() - 75, self.miny,
                           self.maxy)
            self.screen.blit(self.ashPhoto, (x, y))

    def drawAll(self):
        background = transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, [0, 0])
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.Bquit.stopped(mouse.get_pos()):
                    pygame.quit()
                    exit(0)
            elif e.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        self.ButtonsDrawer()
        self.EdgeDrawer()
        self.NodeDrawer()
        self.PokeDrawer()
        self.AgentDrawer()
        display.update()

    def ButtonsDrawer(self) -> None:
        self.Bquit.drawBotton(self.screen, (0, 0, 0))
        info = json.loads(self.client.get_info())["GameServer"]
        self.Bmove.text = 'MOVES: ' + str(info['moves'])
        self.Bmove.drawBotton(self.screen, (0, 0, 0))
        self.Btime.text = 'TIME: ' + str(int(float(self.client.time_to_end()) / 1000))
        self.Btime.drawBotton(self.screen, (0, 0, 0))
        self.Bgrade.text = 'GRADE: ' + str(info["grade"])
        self.Bgrade.drawBotton(self.screen, (0, 0, 0))


class CreatBotton():
    def __init__(self, color, x_axis, y_axis, width, height, text=''):
        self.color = color
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.width = width
        self.height = height
        self.text = text

    def drawBotton(self, Screen, OL=None):
        if OL:
            pygame.draw.rect(Screen, OL, (self.x_axis - 2, self.y_axis - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(Screen, self.color, (self.x_axis, self.y_axis, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Arial', 10)
            text = font.render(self.text, 1, (0, 0, 0))
            Screen.blit(text, (
                self.x_axis + (self.width / 2 - text.get_width() / 2), self.y_axis + (self.height / 2 - text.get_height() / 2)))

    def stopped(self, mouseCoordinents):
        if self.x_axis < mouseCoordinents[0] < self.x_axis + self.width:
            if self.y_axis < mouseCoordinents[1] < self.y_axis + self.height:
                return True

        return False
