#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter no. of nodes: ";
    cin >> n;
    
    int cost[n][n], next_node[n][n];
    cout << "Enter the cost matrix: " << endl;
    
    // If there is no direct path, then the cost is infinity (= INT_MAX)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
            next_node[i][j] = j;
        }
    }
    
    // Calculating the updated table as well as the next node table
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (cost[i][k] + cost[k][j] < cost[i][j]) {
                    cost[i][j] = cost[i][k] + cost[k][j];
                    next_node[i][j] = next_node[i][k];
                }
            }
        }
    }
    
    int x;
    cout << "Enter the source vertex: ";
    cin >> x;
    
    // Printing the shortest paths from the source vertex
    cout << "The shortest paths from vertex " << char(x+65) << " are:" << endl;
    for (int i = 0; i < n; i++) {
        cout << char(x+65) << " -> " << char(i+65) << ": " << cost[x][i] << endl;
    }
    
    return 0;
}
