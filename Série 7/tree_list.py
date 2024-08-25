def is_tree(graph):
    V = len(graph)
    visited = [False] * V
    
    def dfs(v, parent):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if not dfs(neighbor, v):  # Continua percorrendo o grafo
                    return False
            elif neighbor != parent: # Se um vizinho já foi visitado, e não é o pai, então há um ciclo
                return False
        return True
    
    # |E| =  |V| - 1
    num_edges = sum(len(neighbors) for neighbors in graph) // 2
    if num_edges != V - 1:
        return False
    
    # Acíclico
    if not dfs(0, -1):
        return False
    
    # Conexo
    if not all(visited):
        return False
    
    return True

graph = [
    [1, 2],  # Vértice 0 conectado a 1 e 2
    [0, 3, 4],  # Vértice 1 conectado a 0, 3, 4
    [0],  # Vértice 2 conectado a 0
    [1],  # Vértice 3 conectado a 1
    [1, 2]   # Vértice 4 conectado a 1 e 2
]

print(is_tree(graph))
