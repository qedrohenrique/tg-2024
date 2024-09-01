import networkx as nx
import random
from networkx import NetworkXNoCycle as NoCycle

def remove_circuit_edges(graph):
    while True:
        try:
            cycle = nx.find_cycle(graph, orientation='ignore')
            
            if cycle:
                edge_to_remove = cycle[0][:2]
                graph.remove_edge(*edge_to_remove)

                if not nx.is_connected(graph):
                    graph.add_edge(*edge_to_remove) 
                    break
            
        except NoCycle:
            break
    
    return graph

def generate_spanning_trees(G, k):
    T = remove_circuit_edges(G.copy())
    trees = [T.copy()]
    branches = list(T.edges())
    cords = []
    for edge in list(G.edges()):
        if edge not in branches:
            cords.append(edge)      

    for i in range(k-1):
      new_tree = T.copy()

      add_edge = cords[0]
      cords.remove(add_edge)

      new_tree.add_edge(*add_edge)
      
      cycle = nx.find_cycle(new_tree, orientation='ignore')
      cycle_edges = [(u, v) for u, v, _ in cycle]

      for u, v in cycle_edges: 
        nt = new_tree.copy()
        if not((u, v) == (add_edge[0], add_edge[1]) or (v, u) == (add_edge[0], add_edge[1])): # Se for qualquer aresta fora a corda adicionada
          nt.remove_edge(u, v)
          trees.append(nt.copy())
          if(len(trees) == k):
            return trees

    
    return trees

def generate_spanning_trees(G):
  T = remove_circuit_edges(G.copy())
  trees = [T.copy()]
  branches = list(T.edges())
  cords = []
  for edge in list(G.edges()):
      if edge not in branches:
          cords.append(edge)      


  for add_edge in cords:
    new_tree = T.copy()

    new_tree.add_edge(*add_edge)
    
    cycle = nx.find_cycle(new_tree, orientation='ignore')
    cycle_edges = [(u, v) for u, v, _ in cycle]

    for u, v in cycle_edges: 
      nt = new_tree.copy()
      if not((u, v) == (add_edge[0], add_edge[1]) or (v, u) == (add_edge[0], add_edge[1])): # Se for qualquer aresta fora a corda adicionada
        nt.remove_edge(u, v)
        trees.append(nt.copy())
    
  return trees

def distance_between_trees(T1, T2):
  dist = 0

  for u, v in list(T1.edges()):
    if (u, v) not in list(T2.edges()) and (v, u) not in list(T2.edges()):
      dist += 1

  return dist

def find_central_tree(trees):
  central_t = None
  min_d = 9999
  for t0 in trees:
    distances = []
    for ti in trees:
      distances.append(distance_between_trees(t0, ti))
    if max(distances) < min_d:
      min_d = max(distances)
      central_t = t0

  return central_t, min_d
