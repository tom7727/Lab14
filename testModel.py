from model.model import Model

m = Model()
m.buildGraph(1, 5)


nodi, archi = m.getGraphDetails()
print(f"Nodi: {nodi}, Archi: {archi}")