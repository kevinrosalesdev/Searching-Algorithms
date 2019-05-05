# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
print("======================================[CASO_1]======================================")
print("En Anchura: " + str(search.breadth_first_graph_search(ab).path()))
print("En Profundidad: " + str(search.depth_first_graph_search(ab).path()))
print("Branch & Bound: " + str(search.bab(ab).path()))
print("Branch & Bound con Subestimación: " + str(search.babsub(ab).path()))
print("====================================================================================")

"""
Result:
Nodos visitados:  16
En Anchura: [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
Nodos visitados:  10
En Profundidad: [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]: 101 + 138 + 120 + 75 + 70 + 111 + 118 = 733
Nodos visitados:  24
Branch & Bound: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
Nodos visitados:  6
Branch & Bound con Subestimación: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
"""

af = search.GPSProblem('A', 'F', search.romania)
print("======================================[CASO_2]======================================")
print("En Anchura: " + str(search.breadth_first_graph_search(af).path()))
print("En Profundidad: " + str(search.depth_first_graph_search(af).path()))
print("Branch & Bound: " + str(search.bab(af).path()))
print("Branch & Bound con Subestimación: " + str(search.babsub(af).path()))
print("====================================================================================")

"""
Result:
Nodos visitados:  8
En Anchura: [<Node F>, <Node S>, <Node A>] : 99 + 140 = 239
Nodos visitados:  11
En Profundidad: [<Node F>, <Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 211 + 101 + 138 + 120 + 75 + 70 + 111 + 118 = 944
Nodos visitados:  11
Branch & Bound: [<Node F>, <Node S>, <Node A>] : 99 + 140 = 239
Nodos visitados:  3
Branch & Bound con Subestimación: [<Node F>, <Node S>, <Node A>] : 99 + 140 = 239
"""
np = search.GPSProblem('N', 'P', search.romania)
print("======================================[CASO_3]======================================")
print("En Anchura: " + str(search.breadth_first_graph_search(np).path()))
print("En Profundidad: " + str(search.depth_first_graph_search(np).path()))
print("Branch & Bound: " + str(search.bab(np).path()))
print("Branch & Bound con Subestimación: " + str(search.babsub(np).path()))
print("====================================================================================")

"""
Result:
Nodos visitados:  11
En Anchura: [<Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>] : 101 + 85 + 142 + 92 + 87 = 507
Nodos visitados:  15
En Profundidad: [<Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>] : 97 + 80 + 99 + 211 + 85 + 142 + 92 + 87 = 893
Nodos visitados:  13
Branch & Bound: [<Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>] : 101 + 85 + 142 + 92 + 87 = 507
Nodos visitados:  8
Branch & Bound con Subestimación: [<Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]: 101 + 85 + 142 + 92 + 87 = 507
"""

ce = search.GPSProblem('C', 'E', search.romania)
print("======================================[CASO_4]======================================")
print("En Anchura: " + str(search.breadth_first_graph_search(ce).path()))
print("En Profundidad: " + str(search.depth_first_graph_search(ce).path()))
print("Branch & Bound: " + str(search.bab(ce).path()))
print("Branch & Bound con Subestimación: " + str(search.babsub(ce).path()))
print("====================================================================================")

"""
Result:
Nodos visitados:  43
En Anchura: [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node C>] : 86 + 98 + 85 + 101 + 138 = 508
Nodos visitados:  35
En Profundidad: [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node C>] : 86 + 98 + 85 + 101 + 138 = 508
Nodos visitados:  36
Branch & Bound: [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node C>] : 86 + 98 + 85 + 101 + 138 = 508
Nodos visitados:  8
Branch & Bound con Subestimación: [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node C>] : 86 + 98 + 85 + 101 + 138 = 508
"""

cs = search.GPSProblem('C', 'S', search.romania)
print("======================================[CASO_5]======================================")
print("En Anchura: " + str(search.breadth_first_graph_search(cs).path()))
print("En Profundidad: " + str(search.depth_first_graph_search(cs).path()))
print("Branch & Bound: " + str(search.bab(cs).path()))
print("Branch & Bound con Subestimación: " + str(search.babsub(cs).path()))
print("====================================================================================")

"""
Result:
Nodos visitados:  7
En Anchura: [<Node S>, <Node R>, <Node C>] : 80 + 146 = 226
Nodos visitados:  7
En Profundidad: [<Node S>, <Node F>, <Node B>, <Node P>, <Node C>] = 99 + 211 + 101 + 138 = 549
Nodos visitados:  6
Branch & Bound: [<Node S>, <Node R>, <Node C>] : 80 + 146 = 226
Nodos visitados:  3
Branch & Bound con Subestimación: [<Node S>, <Node R>, <Node C>]: 80 + 146 = 226
"""