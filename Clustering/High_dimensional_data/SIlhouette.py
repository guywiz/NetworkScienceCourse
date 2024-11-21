import math
from tulip import *

def euclidean_dist(graph, node, other_nodes):
    '''
    computes the euclidean distance, based on layout 2d positions,
    from a given node to all other nodes in the graph
    '''
    return {n: (graph['viewLayout'][node] - graph['viewLayout'][n]).norm() for n in other_nodes}

def graph_dist(graph, node, other_nodes):
    '''
    computes the graph distance from a given node to all other nodes in the graph
    '''
    max_dist = graph.getIntegerProperty('max_dist')
    tlp.maxDistance(graph, node, max_dist, tlp.UNDIRECTED)
    return {n: max_dist[n] for n in other_nodes}
    
def silhouette(graph, node, community_prop, which_dist=graph_dist):
    '''
    computes the silhouette score of a given node in a graph
    given a community structure
    and a distance function
    '''

    # maps cluster index to clusters (subgraphs)
    cluster_map = {community_prop[sub.getOneNode()]: sub for sub in graph.getSubGraphs()}

    a_cluster = cluster_map[community_prop[node]]
    a = sum(which_dist(graph, node, a_cluster.getNodes()).values()) / (a_cluster.numberOfNodes() - 1)
    min_b = math.inf
    for community_index, community in cluster_map.items():
        if community_index != community_prop[node]:
            b = sum(which_dist(graph, node, community.getNodes()).values()) / (community.numberOfNodes())
            if b < min_b:
                min_b = b
    return (min_b - a)/max(min_b, a)

def main(graph):
    community_prop = graph.getDoubleProperty('community')
    params = tlp.getDefaultPluginParameters('Louvain', graph)
    params['result'] = community_prop
    graph.applyDoubleAlgorithm('Louvain', community_prop, params)
    params = tlp.getDefaultPluginParameters('Equal Value', graph)
    params['property'] = community_prop
    graph.applyAlgorithm('Equal Value', params)
    
    silhouette_g_dist_prop = graph.getDoubleProperty('silhouette_g_dist')
    silhouette_e_dist_prop = graph.getDoubleProperty('silhouette_e_dist')
    for n in graph.getNodes():
        silhouette_g_dist_prop[n] = silhouette(graph, n, community_prop)
        silhouette_e_dist_prop[n] = silhouette(graph, n, community_prop, euclidean_dist)


    
