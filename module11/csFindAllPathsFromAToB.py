"""
Understand:
Input: graph = [[1, 2], [3],[3],[4],[]]
Output: [[0, 1, 3, 4], [0, 2, 3, 4]]

Plan:

"""

def csFindAllPathsFromAToB(graph):
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
