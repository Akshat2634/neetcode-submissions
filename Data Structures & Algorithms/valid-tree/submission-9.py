class Solution:
    def dfs(self,adj,visited,node,ans):
        visited[node] = True
        ans.append(node)

        for num in adj[node]:
            if not visited[num]:
                self.dfs(adj,visited,num,ans)
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # two conditions
        # should be connected 
        # n nodes and n-1 edges
        if n != len(edges)+1:
            return False

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            
            adj[v].append(u)
        
        v = len(adj)

        visited = [False] * n

        ans = []

        self.dfs(adj,visited,0,ans)

        return n == len(ans)



        