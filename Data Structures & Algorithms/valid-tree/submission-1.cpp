class Solution {
public:

    void dfs(vector<vector<int>> &adj,vector<int> &ans,vector<int> &visited, int node){
        ans.push_back(node);
        visited[node]=1;

        for(auto i:adj[node]){
            if(!visited[i]){
                dfs(adj,ans,visited,i);
            }
        }
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        if(n-1 != edges.size()){
            return false;
        }

        vector<vector<int>> adj(n);

        for(auto edge: edges){
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> visited(adj.size(),0);
        vector<int> ans;

        dfs(adj, ans, visited, 0);
        return ans.size()==n;



    }
};
