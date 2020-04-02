from graph import Graph
from graph import Node
import math

def calculate(g):
    norm = 0
    for node in g.nodeList:
        for inNode in node.inList:
            node.auth += inNode.hub
            pass
        norm += math.pow(node.auth, 2)
        pass
    norm = math.sqrt(norm)
    for node in g.nodeList:
        node.auth /= norm
        pass
    norm = 0
    for node in g.nodeList:
        for outNode in node.outList:
            node.hub += outNode.auth
            pass
        norm += math.pow(node.hub, 2)
        pass
    norm = math.sqrt(norm)
    for node in g.nodeList:
        node.hub /= norm
        pass
    pass

def check(g):
    old_auths = []
    old_hubs = []
    for node in g.nodeList:
        old_auths.append(node.auth)
        old_hubs.append(node.hub)
        pass
    calculate(g)
    i = 0
    change = 0
    for node in g.nodeList:
        change += (abs(node.auth-old_auths[i])+abs(node.hub-old_hubs[i]))
        i += 1
        pass
    if change<g.delta:
        return True
    else:
        return False
    pass

def getHits(g):
    while (not check(g)):
        pass
    auths = []
    hubs = []
    for node in g.nodeList:
        auths.append(node.auth)
        hubs.append(node.hub)
        pass
    return auths, hubs
    pass


if __name__=='__main__':
    g = Graph().loadGraph()
    auths, hubs = getHits(g)
    print(auths, "\n", hubs)