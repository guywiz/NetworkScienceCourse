'''
Created on 7 dec. 2010

@author: melancon
'''

from tulip import *
from random import *
import time

class KMeans:

    def __init__(self, graph, k):
        self.graph = graph
        self.k = k
        self.gravitors = []
        self.colors = []
        
        self.red = tlp.Color(255, 50, 25, 255)
        self.clearblue = tlp.Color(117, 225, 255, 255)
        self.blue = tlp.Color(50, 100, 255, 255)
        self.green = tlp.Color(75, 255, 75, 255)
        self.yellow = tlp.Color(255, 255, 50, 255)
        self.orange = tlp.Color(255, 125, 75, 255)
        self.purple = tlp.Color(120, 0, 180, 255)
        self.cyan = tlp.Color(255, 85, 255, 255)
        self.greengold = tlp.Color(152, 152, 0, 255)
        self.fullColorSet = [self.clearblue, self.greengold, self.blue, self.green, self.cyan, self.yellow, self.orange, self.red, self.purple]
        self.epsilon = -1
        ''' used as stopping criterion, will be initialized when calling run() '''
        
    def run(self, stop = 0.01):
        viewColor = self.graph.getColorProperty("viewColor")
        layout = self.graph.getLayoutProperty("viewLayout")
        nodes = self.graph.getNodes()    
            
        self.randomPick(layout)
        for g in self.gravitors:
            self.epsilon += g.norm()
        while self.epsilon > stop: # should be changed to use a stopping criterion
            nodes = self.graph.getNodes()
            while nodes.hasNext():
                node = nodes.next()
                viewColor.setNodeValue(node, self.colors[self.selectGravitor(layout.getNodeValue(node))])
                time.sleep(0.01)
                updateVisualization()
            self.epsilon = self.updateGravitors(self.graph, viewColor, layout)
                    
        
    def randomPick(self, layout):
        # pick k nodes at random and use them as gravitors
        pick = [-1] * self.k
        pick[0] = randint(0, self.graph.numberOfNodes() - 1)
        for i in range(1, self.k):
            r = randint(0, self.graph.numberOfNodes() - 1)
            while r in pick:
                r = randint(0, self.graph.numberOfNodes() - 1)
            pick[i] = r
        pick = sorted(pick)
        i = 0
        g = 0
        nodes = self.graph.getNodes()
        while i <= pick[self.k - 1]:
            node = nodes.next()
            if i in pick:
                self.gravitors.append(layout.getNodeValue(node))
                self.colors.append(self.fullColorSet[g])
                g += 1
            i += 1

    def selectGravitor(self, coord):
        closest = self.gravitors[0]
        closestIndex = 0
        dist2closest = coord.dist(closest)
        for i in range(1, len(self.gravitors)):
            if coord.dist(self.gravitors[i]) < dist2closest:
                dist2closest = coord.dist(self.gravitors[i])
                closest = self.gravitors[i]
                closestIndex = i
        return closestIndex

    def computeGravitor(self, coordList):
        x = 0
        y = 0
        z = 0
        nbCoords = len(coordList) + 0.0
        for i in range(len(coordList)):
            x += coordList[i].getX()
            y += coordList[i].getY()
            z += coordList[i].getZ()
        return tlp.Coord(x / nbCoords, y / nbCoords, z / nbCoords)

    def sameColor(self, c1, c2):
        if c1.getR() != c2.getR():
            return False
        elif c1.getG() != c2.getG():
            return False
        elif c1.getB() != c2.getB():
            return False
        else:
            return True

    def updateGravitors(self, graph, nodeColors, layout):
        epsilon = 0.0
        for i in range(self.k):
            selectedCoords = []
            nodes = graph.getNodes()
            while nodes.hasNext():
                node = nodes.next()
                if self.sameColor(nodeColors.getNodeValue(node), self.colors[i]):
                    selectedCoords.append(layout.getNodeValue(node))
            newGravitor = self.computeGravitor(selectedCoords)
            epsilon += newGravitor.dist(self.gravitors[i])
            self.gravitors[i] = newGravitor
        return epsilon

    def inertia_intra(self):
        layout = self.graph.getLayoutProperty("viewLayout")
        tot_inertia = 0.0
        for i in range(len(self.gravitors)):
            inertia_i = 0.0
            for n in self.graph.getNodes():
                coord = layout[n]
                if self.selectGravitor(coord) == i:
                    inertia_i += coord.dist(self.gravitors[i])**2
            tot_inertia += inertia_i
        return tot_inertia

def main(graph):
    inertia = []
    for k in range(2, 3):
        km = KMeans(graph, k)
        km.run()
        inertia.append((k, km.inertia_intra()))
        print((k, km.inertia_intra()))
    print(inertia)
    
