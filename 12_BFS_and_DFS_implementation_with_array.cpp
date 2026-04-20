#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void BFS(vector<vector<int>>& adj, int s) {
    vector<bool> visited(adj.size(), false);
    queue<int> q;
    visited[s] = true;
    q.push(s);

    cout << "BFS Traversal: ";
    while (!q.empty()) {
        int u = q.front();
        cout << u << " ";
        q.pop();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    cout << endl;
}

void DFSUtil(int u, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";
    for (int i = 0; i < adj[u].size(); i++)
        if (visited[adj[u][i]] == false)
            DFSUtil(adj[u][i], adj, visited);
}

void DFS(vector<vector<int>>& adj, int s) {
    vector<bool> visited(adj.size(), false);
    cout << "DFS Traversal: ";
    DFSUtil(s, adj, visited);
    cout << endl;
}

int main() {
    int V = 4;
    vector<vector<int>> adj(V);
    adj[0].push_back(1); adj[0].push_back(2);
    adj[1].push_back(2);
    adj[2].push_back(0); adj[2].push_back(3);
    adj[3].push_back(3);
    
    BFS(adj, 2);
    DFS(adj, 2);
    return 0;
}
