class Solution:
    def dfs(self,ans,visited,adj,node):
        ans.append(node)
        visited[node]=True

        for num in adj[node]:
            if not visited[num]:
                self.dfs(ans,visited,adj,num)


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)

        V = len(adj)
        visited = [False] * n
        ans = []

        self.dfs(ans,visited,adj,0)

        return len(ans)== n

        