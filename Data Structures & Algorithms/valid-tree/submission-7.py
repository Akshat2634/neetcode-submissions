class Solution:
    def dfs(self,adj,ans,visited,node):
        visited[node]= True
        ans.append(node)

        for num in adj[node]:
            if not visited[num]:
                self.dfs(adj,ans,visited,num)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        V= len(adj)
        visited = [False] * n
        ans = []

        self.dfs(adj,ans,visited,0)

        return len(ans)==n
