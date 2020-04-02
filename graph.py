import json

class Node:

    def __init__(self, id):
        self.id = id
        self.inList = []
        self.outList = []
        self.inNum = 0
        self.outNum = 0
        self.rank = 1
        self.auth = 1
        self.hub = 1
        pass

    pass

class Graph:

    def __init__(self):
        self.nodeList = []
        self.epsilon = 0.01
        self.delta = 0.001
        self.Map = {}
        pass

    def loadGraph(self):
        # node1 = Node(1)
        # node2 = Node(2)
        # node3 = Node(3)
        # node1.inList.append(node2)
        # node1.inList.append(node3)
        # node1.outList.append(node2)
        # node1.inNum = 2
        # node1.outNum = 1
        # node2.inList.append(node1)
        # node2.inList.append(node3)
        # node2.outList.append(node1)
        # node2.inNum = 2
        # node2.outNum = 1
        # node3.outList.append(node1)
        # node3.outList.append(node2)
        # node3.outNum = 2
        # self.nodeList.append(node1)
        # self.nodeList.append(node2)
        # self.nodeList.append(node3)
        FileName = "test.json"
        file = open(FileName)
        dict = json.load(file)
        for id in dict:
            if (id not in self.Map):
                node = Node(id)
                self.Map.update({id: node})
                pass
            idNode = self.Map[id]
            for share in dict[id]:
                if (share not in self.Map):
                    node = Node(share)
                    self.Map.update({share: node})
                    pass
                shareNode = self.Map[share]
                idNode.inList.append(shareNode)
                idNode.inNum += 1
                shareNode.outList.append(idNode)
                shareNode.outNum += 1
                pass
            self.nodeList.append(idNode)
            pass
        return self
        pass
