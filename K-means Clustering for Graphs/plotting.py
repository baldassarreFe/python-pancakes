import numpy as np
import pydot as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from colour import Color

def toLetter(node):
    return chr(ord('A') + node)
toLetters = np.vectorize(toLetter)

## Plot directed graph, note that edges will overlap
def plotFromAdj(adj, nodeLabels=None, nodeValues=None, path=None, nodesToHighlight=[]):
    graph = pd.Dot(graph_type='digraph',rankdir="LR")
    N = adj.shape[0]
    nodes = range(N)

    nodeColors = ["#ebebe0" if node not in nodesToHighlight else Color("lightgreen").get_hex_l() for node in nodes]
    nodeValues = [""]*N if nodeValues is None else list(map("[{0}]".format, nodeValues))
    nodeLabels = nodeLabels if nodeLabels is not None else [toLetter(node) + nodeValues[node] for node in nodes]

    for node in nodes:
        graph.add_node(pd.Node(node, fontsize=20, style="filled", fillcolor=nodeColors[node], label=nodeLabels[node]))

    pathEdges={}
    if path is not None:
        pathEdges = dict(zip(
            zip(path[:-1], path[1:]),
            [color.get_hex_l() for color in Color("darkred").range_to(Color("gold"), len(path)-1)]
        ))

    for i in nodes:
        for j in nodes:
            if adj[i,j]>0:
                e = pd.Edge(i,j,label=str(adj[i,j]),fontsize=15,arrowhead="vee")
                if (i,j) in pathEdges:
                    e.set_color(pathEdges[(i,j)])
                    e.set_penwidth(2.5)
                graph.add_edge(e)

    graph.write_png('temp.png')
    img = mpimg.imread('temp.png')

    dpi = 80
    margin = 0.09 # (9% of the width/height of the figure...)
    xpixels, ypixels = img.shape[0],img.shape[1]
    # Make a figure big enough to accomodate an axis of xpixels by ypixels as well as the ticklabels, etc...
    figsize = (1 + margin) * ypixels / dpi, (1 + margin) * xpixels / dpi
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])
    ax.imshow(img, interpolation="none")
    plt.show()

## EXAMPLE GRAPH
if __name__ == '__main__':
    adj = np.array([
        [0,10,-1,1],
        [12,0,3,-1],
        [2,5,0,-1],
        [2,5,-1,0]
    ])
    nodeValues = [1,2,3,4]
    nodesToHighlight=[0,1,2]
    path = [0, 1, 2, 1, 0]
    plotFromAdj(adj,nodeValues=nodeValues, path=path, nodesToHighlight=nodesToHighlight)
