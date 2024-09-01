import networkx as nx
import re
from arvore_abrangencia import *
import matplotlib.pyplot as plt


# Criar um grafo vazio
G = nx.Graph()

agencias = [
  "RUA SANTA CLARA, 245", #
  "AVENIDA RUI BARBOSA, 2376", #
  "RUA RIACHUELO, 57",
  "AVENIDA ANDROMEDA, 1469", #
  "RUA SABARA, 30",
  "RUA EZEQUIEL ALVES GRACIANO, 140",
  "RUA QUINZE DE NOVEMBRO, 259",
  "AVENIDA DOUTOR NELSON D AVILA, 90",
  "RUA LOANDA, 895",
  "RUA GOIANIA, 15", #
]

pessoas_fisicas = [
  "RUA MATIAS PERES, 364",
  "RUA DA ALEGRIA, 39",
  "RUA CAPARAÓ, 370",
  "RUA ITUIUTABA, 50",
  "RUA PIMENTEIRAS, 322",
  "RUA CARVALHO DE ARAÚJO, 106 ",
  "RUA SAMUEL ANTÔNIO RODRIGUES, 197",
]

empresas = [
  "EMBRAER BRG. FARIA LIMA, 2170",
  "AKAER AV. CESARE MONSUETO GIULIO LATTES, 501",
  "DEDÉ CELLAV. ANDRÔMEDA, 654",
]

outros = [
  "UNESP AV. ENGENHEIRO FRANCISO JOSÉ LONGO, 777"
]

G.add_nodes_from(agencias)
G.add_nodes_from(pessoas_fisicas)
G.add_nodes_from(empresas)
G.add_nodes_from(outros)

for agencia in agencias:
  for pessoa in pessoas_fisicas:
    G.add_edge(agencia, pessoa)

for agencia in agencias:
  for empresa in empresas:
    G.add_edge(agencia, empresa)

for agencia in agencias:
  G.add_edge(agencia, outros[0])

def is_eulerian(G):
  for node in G.nodes():
    if G.degree(node) % 2 != 0:
      print(node)
      print(len(list(G.edges(node))))
      return False
  return True

def is_hamiltonian(G):
  n = len(list(G.nodes())) // 2
  for node in G.nodes():
    if G.degree(node) < n:
      print(node)
      return False
  return True

cut_value, (set1, set2) = nx.minimum_cut(G)

cut_edges = list(nx.edge_boundary(G, set1, set2))

print(cut_edges)

# print(is_hamiltonian(G))

# print(is_eulerian(G))

# trees = generate_spanning_trees(G)
# central_tree, dist = find_central_tree(trees)
# print(central_tree.edges(), dist)

# color_map = [ *(['skyblue']*10), *(['tab:red']*7), *(['tab:blue']*3), *(['tab:green']*1) ]

# options = {
#   "font_size": 16,
#   "node_size": 3000,
#   "linewidths": 3,
#   "width": 5,
#   "with_labels": True,
#   "node_color": color_map,
#   "node_size": 1000,
# }

# pos = nx.spring_layout(G, seed=7)

# plt.figure(figsize=(12, 12))
# nx.draw(central_tree, pos, **options)

# plt.show()