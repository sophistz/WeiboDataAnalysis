from graph import Graph
from graph import Node
import math

def calculate(g):
    for node in g.nodeList:
        rank = 0
        for inNode in node.inList:
            rank += inNode.rank/inNode.outNum
            pass
        rank = 0.5 + 0.5*rank
        node.rank = rank
        pass
    pass

def check(g):
    flag = True
    old_ranks = []
    for node in g.nodeList:
        old_ranks.append(node.rank)
        pass
    calculate(g)
    i = 0
    for node in g.nodeList:
        if abs(old_ranks[i]-node.rank)>g.epsilon:
            flag = False
            pass
        i += 1
        pass
    return flag
    pass

def getPageRank(g):
    while (not check(g)):
        pass
    ranks = []
    for node in g.nodeList:
        ranks.append(node.rank)
        pass
    return ranks
    pass

if __name__=='__main__':
    g = Graph().loadGraph()
    ranks = getPageRank(g)
    print(ranks)