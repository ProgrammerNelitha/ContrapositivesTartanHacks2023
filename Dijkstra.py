def dijkstraAlgorithm(G, s, f):
    # make all distances in G infinite
    dist = {}
    prev = {}
    Q = []
    vertices = G.getVertices()
    rooms = [vertices[i].getName() for i in range(len(vertices))]
    for room in rooms:
        dist[room] = float('inf')
        prev[room] = None
        Q.append(room)
    dist[s] = 0

    while len(Q) > 0:
        u = min(dist, key=dist.get)
        if u == f:
            break
        Q.pop()
        
        node = G.findNode(u)
        neighbors = node.getNeighbors()

        for v in neighbors:
            v_name = v.getName()
            alt = dist[u] + G.getEdge(u,v)
            if alt < dist[v_name]:
                dist[v_name] = alt
                prev[v_name] = u

    return dist, prev