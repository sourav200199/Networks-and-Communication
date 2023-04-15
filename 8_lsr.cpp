#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout << "Enter the number of nodes: ";
    cin >> n;

    int d[n][n];
    cout << "Enter the distance matrix: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> d[i][j];
        }
    }

    int s;
    cout << "Enter the source node: ";
    cin >> s;

    int dist[n];
    bool visited[n] = {false};
    for (int i = 0; i < n; i++)
    {
        dist[i] = 999;
    }
    dist[s] = 0;

    for (int i = 0; i < n; i++)
    {
        int min = 999, u;
        for (int j = 0; j < n; j++)
        {
            if (visited[j] == false && dist[j] < min)
            {
                min = dist[j];
                u = j;
            }
        }
        visited[u] = true;
        for (int v = 0; v < n; v++)
        {
            if (visited[v] == false && d[u][v] != 0 && dist[u] + d[u][v] < dist[v])
            {
                dist[v] = dist[u] + d[u][v];
            }
        }
    }

    cout << "The shortest path from node " << char(s + 65) << " is:" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << char(s + 65) << " -> " << char(i + 65) << " : " << dist[i] << endl;
    }

    return 0;
}