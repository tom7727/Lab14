import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._nodi = None
        self._idMapOrder = {}
        self._edges = None

    def buildGraph(self, store_id, max_giorni):
        self._grafo.clear()
        self._nodi = DAO.getAllNodes(store_id)
        self._grafo.add_nodes_from(self._nodi)
        for n in self._nodi:
            self._idMapOrder[n.order_id] = n
        self._edges = DAO.getAllEdges(store_id, max_giorni, self._idMapOrder)
        for e in self._edges:
            self._grafo.add_edge(e.ordine1, e.ordine2, weight = e.peso)


    def getAllStores(self):
        return DAO.getAllStores()




    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)