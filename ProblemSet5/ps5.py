# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Node: the source building and the destination building
# Edge: will contain the source and destination building, as well as the
# Total Distance and Outdoor Distance
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    g = WeightedDigraph()
    content = open(mapFilename, 'r')

    for line in content:
        line_list = line.split()

        source = int(line_list[0])
        if not g.hasNode(source):
            g.addNode(source)

        dest = int(line_list[1])
        if not g.hasNode(dest):
            g.addNode(dest)

        totaldist = float(line_list[2])
        outdoordist = float(line_list[3])

        edge = WeightedEdge(source, dest, totaldist, outdoordist)
        g.addEdge(edge)

    return g

    print "Loading map from file..."


# test
g = WeightedDigraph()
x = open('ProblemSet5/mit_map.txt', 'r')
x2 = x.readlines()
x3 = x2[0]
g.addNode(x3)
print g

# Q1
mitMap = load_map('ProblemSet5/mit_map.txt')
print mitMap
print isinstance(mitMap, Digraph)

# Q2
print isinstance(mitMap, WeightedDigraph)

#Q3
nodes = mitMap.nodes
print nodes
nodes = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 24, 26, 31, 32, 33, 34, 35, 36, 37, 38, 39, 46, 48, 50, 54, 56, 57, 62, 64, 66, 68, 76])

#Q4
edges = mitMap.edges
print edges
edges = {1: [[2, (75.0, 60.0)], [4, (80.0, 65.0)], [3, (36.0, 0.0)], [5, (32.0, 0.0)]], 2: [[6, (41.0, 0.0)], [14, (51.0, 0.0)], [4, (36.0, 0.0)], [10, (70.0, 50.0)], [3, (70.0, 50.0)], [1, (75.0, 60.0)]], 3: [[10, (32.0, 0.0)], [4, (60.0, 50.0)], [2, (70.0, 50.0)], [1, (36.0, 0.0)], [7, (25.0, 0.0)]], 4: [[12, (56.0, 0.0)], [8, (47.0, 0.0)], [2, (36.0, 0.0)], [10, (47.0, 0.0)], [3, (60.0, 50.0)], [1, (80.0, 65.0)]], 5: [[1, (32.0, 0.0)], [7, (20.0, 0.0)]], 6: [[8, (39.0, 0.0)], [2, (41.0, 0.0)]], 7: [[5, (20.0, 0.0)], [3, (25.0, 0.0)], [9, (20.0, 0.0)]], 8: [[16, (25.0, 0.0)], [6, (39.0, 0.0)], [4, (47.0, 0.0)]], 9: [[13, (40.0, 0.0)], [7, (20.0, 0.0)], [33, (29.0, 0.0)]], 10: [[4, (47.0, 0.0)], [2, (70.0, 50.0)], [3, (32.0, 0.0)], [13, (30.0, 0.0)]], 12: [[32, (100.0, 80.0)], [26, (30.0, 25.0)], [24, (33.0, 0.0)], [4, (56.0, 0.0)]], 13: [[24, (35.0, 30.0)], [39, (70.0, 50.0)], [31, (30.0, 25.0)], [10, (30.0, 0.0)], [9, (40.0, 0.0)]], 14: [[2, (51.0, 0.0)], [50, (50.0, 23.0)], [50, (25.0, 20.0)]], 16: [[56, (30.0, 0.0)], [32, (100.0, 50.0)], [26, (45.0, 0.0)], [8, (25.0, 0.0)]], 18: [[56, (35.0, 0.0)], [54, (20.0, 10.0)]], 24: [[13, (35.0, 30.0)], [26, (25.0, 20.0)], [34, (27.0, 0.0)], [12, (33.0, 0.0)]], 26: [[36, (34.0, 0.0)], [16, (45.0, 0.0)], [12, (30.0, 25.0)], [24, (25.0, 20.0)]], 31: [[13, (30.0, 25.0)], [37, (27.0, 0.0)]], 32: [[36, (70.0, 0.0)], [57, (30.0, 0.0)], [76, (80.0, 50.0)], [68, (110.0, 80.0)], [16, (100.0, 50.0)], [12, (100.0, 80.0)], [46, (90.0, 40.0)], [48, (80.0, 50.0)], [66, (70.0, 60.0)], [56, (80.0, 70.0)]], 33: [[35, (25.0, 0.0)], [9, (29.0, 0.0)]], 34: [[36, (25.0, 0.0)], [24, (27.0, 0.0)], [38, (25.0, 0.0)]], 35: [[37, (29.0, 0.0)], [33, (25.0, 0.0)]], 36: [[32, (70.0, 0.0)], [26, (34.0, 0.0)], [34, (25.0, 0.0)], [46, (80.0, 40.0)], [48, (100.0, 80.0)]], 37: [[39, (32.0, 0.0)], [31, (27.0, 0.0)], [35, (29.0, 0.0)]], 38: [[34, (25.0, 0.0)], [39, (34.0, 0.0)]], 39: [[37, (32.0, 0.0)], [13, (70.0, 50.0)]], 46: [[32, (90.0, 40.0)], [36, (80.0, 40.0)], [48, (25.0, 10.0)]], 48: [[32, (80.0, 50.0)], [36, (100.0, 80.0)], [46, (25.0, 10.0)]], 50: [[14, (50.0, 23.0)], [14, (25.0, 20.0)]], 54: [[56, (40.0, 30.0)], [66, (45.0, 35.0)], [18, (20.0, 10.0)], [62, (20.0, 10.0)], [14, (70.0, 60.0)], [50, (80.0, 70.0)]], 56: [[68, (80.0, 70.0)], [66, (40.0, 0.0)], [18, (35.0, 0.0)], [16, (30.0, 0.0)], [32, (80.0, 70.0)]], 57: [[32, (30.0, 0.0)]], 62: [[54, (20.0, 10.0)], [64, (30.0, 20.0)]], 64: [[62, (30.0, 20.0)]], 66: [[68, (51.0, 0.0)], [56, (40.0, 0.0)], [76, (130.0, 100.0)], [32, (70.0, 60.0)]], 68: [[32, (110.0, 80.0)], [76, (72.0, 30.0)], [66, (51.0, 0.0)], [56, (80.0, 70.0)]], 76: [[32, (80.0, 50.0)], [68, (72.0, 30.0)], [66, (130.0, 100.0)]]}


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def getDist(tempPath, digraph):
    totalDist = 0
    totalOutDist = 0
    for i in range(len(tempPath) - 1):
        source = tempPath[i]
        for dist in digraph.edges[source]:
            if tempPath[i+1] == dist[0]:
                totalDist =+ dist[1][0]
                totalOutDist += dist[1][1]

    return (totalDist, totalOutDist)


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    start = Node(start)
    end = Node(end)
    s = [[start]]
    shortest = None
    shortestTotal = float('inf')

    while len(s) != 0:
        tempPath = s.pop()
        lastNode = tempPath[len(tempPath) - 1]

        if lastNode == end:
            tempTotalDist, tempTotalOutDist = getDist(tempPath, digraph)
            if tempTotalDist < shortestTotal and tempTotalDist <= maxTotalDist and tempTotalOutDist <= maxDistOutdoors:
                shortest = tempPath
                shortestTotal = tempTotalDist

        for childNode in digraph.childrenOf(lastNode):
            if childNode not in tempPath:
                newPath = tempPath + [childNode]
                s.append(newPath)

    if shortest == None:
        raise ValueError('bruteForceSearch: No Path Found')
    else:
        return [str(x) for x in shortest]

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges


#     LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
