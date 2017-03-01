"""Depth First Search in Python

Let's define G as our simple graph.

G = { 0 : [1, 2]     , 1 : [0, 3]     , 2 : [0, 3]     , 3 : [1, 2] }


G can be searched easily using a Depth-first algorithm (DFS). DFS can be pretty straight-forward (see implementation section).

You are called to:
1) Understand how the algorithm works. Try to run a few examples with print statements
2) See how recursion is used
3) Expand graph G with more nodes and run a few examples

Expansion of the algorithm
1) Rewrite the algorithm with NO recursion(!)
2) Iterate over all vertices, instead of using one root. 

Feel free to run your experiments under my code and submit when you believe it is ready"""

g1 = { 0 : set([1, 2]), 1 : set([0, 3]), 2 : set([0, 3]), 3 : set([1, 2]) }
g = {
'A': set(['B', 'C']),
'B': set(['A', 'D', 'E']),
'C': set(['A', 'F']),
'D': set(['B']),
'E': set(['B', 'F']),
'F': set(['C', 'E'])
}

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}


#EXAMPLE 1
#recursive DFS version

print("EXAMPLE 1")
def dfs_rec(adjLists, visited, v):
    visited[v] = True
    print(v, " ", end='')
    for w in adjLists[v]:
        if(not visited[w]):
            dfs_rec(adjLists, visited, w)
def dfs_v2(adjLists, s):
    visited = []
    n = len(adjLists)
    for i in range(n):
      visited.append(False)
    dfs_rec(adjLists, visited, s)

print(dfs_v2(g1, 0))

#EXAMPLE 2

print("\n")
print("EXAMPLE 2")

#Recursive depth first search from start
def recursive_dfs(graph, start, path=[]):
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

#Iterative depth first search from start
def iterative_dfs(graph, start, path=[]):
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path
  
print ('recursive dfs ', recursive_dfs(graph, 'A'))
print ('iterative dfs ', iterative_dfs(graph, 'A'))
