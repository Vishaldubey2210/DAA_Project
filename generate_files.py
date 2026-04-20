import os

files_content = {
    "01_A_Insertion_sort.cpp": """#include <iostream>
using namespace std;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, n);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
""",
    "02_Bubble_Sort.cpp": """#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
""",
    "03_A_Merge_sort.cpp": """#include <iostream>
#include <vector>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int i = 0; i < n2; i++) R[i] = arr[m + 1 + i];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
""",
    "03_B_Linear_search.cpp": """#include <iostream>
using namespace std;

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}

int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int x = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = linearSearch(arr, n, x);
    if(result == -1) cout << "Element is not present in array";
    else cout << "Element is present at index " << result;
    return 0;
}
""",
    "04_A_Quicksort.cpp": """#include <iostream>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
""",
    "04_B_Binary_search.cpp": """#include <iostream>
using namespace std;

int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x) return m;
        if (arr[m] < x) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int x = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = binarySearch(arr, 0, n - 1, x);
    if(result == -1) cout << "Element is not present in array";
    else cout << "Element is present at index " << result;
    return 0;
}
""",
    "05_Strassen_Matrix_multiplication.cpp": """#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<int>> Matrix;

Matrix add(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

Matrix sub(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

// Strassen's matrix multiplication (simple base case version for demonstration)
Matrix strassen(Matrix A, Matrix B) {
    int n = A.size();
    if (n == 1) {
        return {{A[0][0] * B[0][0]}};
    }
    
    int newSize = n / 2;
    Matrix A11(newSize, vector<int>(newSize)), A12(newSize, vector<int>(newSize));
    Matrix A21(newSize, vector<int>(newSize)), A22(newSize, vector<int>(newSize));
    Matrix B11(newSize, vector<int>(newSize)), B12(newSize, vector<int>(newSize));
    Matrix B21(newSize, vector<int>(newSize)), B22(newSize, vector<int>(newSize));

    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            A11[i][j] = A[i][j]; A12[i][j] = A[i][j + newSize];
            A21[i][j] = A[i + newSize][j]; A22[i][j] = A[i + newSize][j + newSize];
            B11[i][j] = B[i][j]; B12[i][j] = B[i][j + newSize];
            B21[i][j] = B[i + newSize][j]; B22[i][j] = B[i + newSize][j + newSize];
        }
    }

    Matrix M1 = strassen(add(A11, A22), add(B11, B22));
    Matrix M2 = strassen(add(A21, A22), B11);
    Matrix M3 = strassen(A11, sub(B12, B22));
    Matrix M4 = strassen(A22, sub(B21, B11));
    Matrix M5 = strassen(add(A11, A12), B22);
    Matrix M6 = strassen(sub(A21, A11), add(B11, B12));
    Matrix M7 = strassen(sub(A12, A22), add(B21, B22));

    Matrix C11 = add(sub(add(M1, M4), M5), M7);
    Matrix C12 = add(M3, M5);
    Matrix C21 = add(M2, M4);
    Matrix C22 = add(sub(add(M1, M3), M2), M6);

    Matrix C(n, vector<int>(n));
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            C[i][j] = C11[i][j]; C[i][j + newSize] = C12[i][j];
            C[i + newSize][j] = C21[i][j]; C[i + newSize][j + newSize] = C22[i][j];
        }
    }
    return C;
}

int main() {
    Matrix A = {{1, 2}, {3, 4}};
    Matrix B = {{5, 6}, {7, 8}};
    Matrix C = strassen(A, B);
    for (int i = 0; i < C.size(); i++) {
        for (int j = 0; j < C.size(); j++) cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}
""",
    "06_Finding_Maximum_and_Minimum.cpp": """#include <iostream>
using namespace std;

struct Pair { int min, max; };

struct Pair getMinMax(int arr[], int n) {
    struct Pair minmax;
    int i;
    
    if (n == 1) {
        minmax.max = arr[0];
        minmax.min = arr[0];
        return minmax;
    }

    if (arr[0] > arr[1]) {
        minmax.max = arr[0];
        minmax.min = arr[1];
    } else {
        minmax.max = arr[1];
        minmax.min = arr[0];
    }

    for (i = 2; i < n; i++) {
        if (arr[i] > minmax.max) minmax.max = arr[i];
        else if (arr[i] < minmax.min) minmax.min = arr[i];
    }

    return minmax;
}

int main() {
    int arr[] = {1000, 11, 445, 1, 330, 3000};
    int arr_size = 6;
    struct Pair minmax = getMinMax(arr, arr_size);
    cout << "Minimum element is " << minmax.min << endl;
    cout << "Maximum element is " << minmax.max << endl;
    return 0;
}
""",
    "06_A_Convex_Hull_problem.cpp": """#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct Point {
    int x, y;
};

int orientation(Point p, Point q, Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;  // colinear
    return (val > 0) ? 1 : 2; // clock or counterclock wise
}

void convexHull(Point points[], int n) {
    if (n < 3) return;

    vector<Point> hull;
    int l = 0;
    for (int i = 1; i < n; i++)
        if (points[i].x < points[l].x)
            l = i;

    int p = l, q;
    do {
        hull.push_back(points[p]);
        q = (p + 1) % n;
        for (int i = 0; i < n; i++) {
           if (orientation(points[p], points[i], points[q]) == 2)
               q = i;
        }
        p = q;
    } while (p != l);

    for (int i = 0; i < hull.size(); i++)
        cout << "(" << hull[i].x << ", " << hull[i].y << ")" << endl;
}

int main() {
    Point points[] = {{0, 3}, {2, 2}, {1, 1}, {2, 1}, {3, 0}, {0, 0}, {3, 3}};
    int n = sizeof(points)/sizeof(points[0]);
    convexHull(points, n);
    return 0;
}
""",
    "07_A_Huffman_coding_Using_Greedy.cpp": """#include <iostream>
#include <queue>
using namespace std;

struct MinHeapNode {
    char data;
    unsigned freq;
    MinHeapNode *left, *right;
    MinHeapNode(char data, unsigned freq) {
        left = right = NULL;
        this->data = data;
        this->freq = freq;
    }
};

struct compare {
    bool operator()(MinHeapNode* l, MinHeapNode* r) {
        return (l->freq > r->freq);
    }
};

void printCodes(struct MinHeapNode* root, string str) {
    if (!root) return;
    if (root->data != '$') cout << root->data << ": " << str << "\\n";
    printCodes(root->left, str + "0");
    printCodes(root->right, str + "1");
}

void HuffmanCodes(char data[], int freq[], int size) {
    struct MinHeapNode *left, *right, *top;
    priority_queue<MinHeapNode*, vector<MinHeapNode*>, compare> minHeap;
    for (int i = 0; i < size; ++i)
        minHeap.push(new MinHeapNode(data[i], freq[i]));
    while (minHeap.size() != 1) {
        left = minHeap.top(); minHeap.pop();
        right = minHeap.top(); minHeap.pop();
        top = new MinHeapNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        minHeap.push(top);
    }
    printCodes(minHeap.top(), "");
}

int main() {
    char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    int freq[] = { 5, 9, 12, 13, 16, 45 };
    int size = sizeof(arr) / sizeof(arr[0]);
    HuffmanCodes(arr, freq, size);
    return 0;
}
""",
    "07_B_Knapsack_using_greedy.cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int value, weight;
    Item(int value, int weight) : value(value), weight(weight) {}
};

bool cmp(struct Item a, struct Item b) {
    double r1 = (double)a.value / (double)a.weight;
    double r2 = (double)b.value / (double)b.weight;
    return r1 > r2;
}

double fractionalKnapsack(int W, struct Item arr[], int n) {
    sort(arr, arr + n, cmp);
    int curWeight = 0;
    double finalvalue = 0.0;

    for (int i = 0; i < n; i++) {
        if (curWeight + arr[i].weight <= W) {
            curWeight += arr[i].weight;
            finalvalue += arr[i].value;
        } else {
            int remain = W - curWeight;
            finalvalue += arr[i].value * ((double)remain / (double)arr[i].weight);
            break;
        }
    }
    return finalvalue;
}

int main() {
    int W = 50; 
    Item arr[] = { { 60, 10 }, { 100, 20 }, { 120, 30 } };
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Maximum value we can obtain = " << fractionalKnapsack(W, arr, n);
    return 0;
}
""",
    "08_Tree_Traversals.cpp": """#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *left, *right;
    Node(int data) {
        this->data = data;
        left = right = NULL;
    }
};

void printPreorder(struct Node* node) {
    if (node == NULL) return;
    cout << node->data << " ";
    printPreorder(node->left);
    printPreorder(node->right);
}

void printInorder(struct Node* node) {
    if (node == NULL) return;
    printInorder(node->left);
    cout << node->data << " ";
    printInorder(node->right);
}

void printPostorder(struct Node* node) {
    if (node == NULL) return;
    printPostorder(node->left);
    printPostorder(node->right);
    cout << node->data << " ";
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Preorder traversal: "; printPreorder(root); cout << endl;
    cout << "Inorder traversal: "; printInorder(root); cout << endl;
    cout << "Postorder traversal: "; printPostorder(root); cout << endl;
    
    return 0;
}
""",
    "09_Longest_common_subsequence.cpp": """#include <iostream>
#include <vector>
using namespace std;

int lcs(string X, string Y, int m, int n) {
    int L[m + 1][n + 1];
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) L[i][j] = 0;
            else if (X[i - 1] == Y[j - 1]) L[i][j] = L[i - 1][j - 1] + 1;
            else L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }
    return L[m][n];
}

int main() {
    string S1 = "AGGTAB";
    string S2 = "GXTXAYB";
    int m = S1.length();
    int n = S2.length();
    cout << "Length of LCS is " << lcs(S1, S2, m, n);
    return 0;
}
""",
    "10_N_queens_problem.cpp": """#include <iostream>
#include <vector>
using namespace std;

#define N 4

void printSolution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << (board[i][j] ? "Q " : ". ");
        cout << "\\n";
    }
}

bool isSafe(int board[N][N], int row, int col) {
    for (int i = 0; i < col; i++)
        if (board[row][i]) return false;
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return false;
    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j]) return false;
    return true;
}

bool solveNQUtil(int board[N][N], int col) {
    if (col >= N) return true;
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            if (solveNQUtil(board, col + 1)) return true;
            board[i][col] = 0; 
        }
    }
    return false;
}

int main() {
    int board[N][N] = { {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0} };
    if (!solveNQUtil(board, 0)) {
        cout << "Solution does not exist";
        return 0;
    }
    printSolution(board);
    return 0;
}
""",
    "11_Travelling_salesman_problem.cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define V 4

int travllingSalesmanProblem(int graph[][V], int s) {
    vector<int> vertex;
    for (int i = 0; i < V; i++)
        if (i != s) vertex.push_back(i);

    int min_path = 1e9;
    do {
        int current_pathweight = 0;
        int k = s;
        for (int i = 0; i < vertex.size(); i++) {
            current_pathweight += graph[k][vertex[i]];
            k = vertex[i];
        }
        current_pathweight += graph[k][s];
        min_path = min(min_path, current_pathweight);
    } while (next_permutation(vertex.begin(), vertex.end()));

    return min_path;
}

int main() {
    int graph[][V] = { { 0, 10, 15, 20 },
                       { 10, 0, 35, 25 },
                       { 15, 35, 0, 30 },
                       { 20, 25, 30, 0 } };
    int s = 0;
    cout << "Minimum TSP distance: " << travllingSalesmanProblem(graph, s) << endl;
    return 0;
}
""",
    "12_BFS_and_DFS_implementation_with_array.cpp": """#include <iostream>
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
""",
    "13_Randomized_quick_sort.cpp": """#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

int partition_r(int arr[], int low, int high) {
    srand(time(NULL));
    int random = low + rand() % (high - low);
    swap(arr[random], arr[high]);
    return partition(arr, low, high);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition_r(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}
""",
    "14_String_matching_algorithms.cpp": """#include <iostream>
#include <string>
using namespace std;

void naiveMatch(string pat, string txt) {
    int M = pat.length();
    int N = txt.length();

    for (int i = 0; i <= N - M; i++) {
        int j;
        for (j = 0; j < M; j++)
            if (txt[i + j] != pat[j])
                break;
        if (j == M)
            cout << "Pattern found at index " << i << endl;
    }
}

int main() {
    string txt = "AABAACAADAABAAABAA";
    string pat = "AABA";
    cout << "Naive String Matching:" << endl;
    naiveMatch(pat, txt);
    return 0;
}
""",
    "15_Discussion_real_time_problem.cpp": """#include <iostream>
using namespace std;

int main() {
    cout << "=== Discussion over analyzing a real-time problem ===" << endl;
    cout << "Problem Context: Food Delivery Optimization" << endl;
    cout << "Challenges:" << endl;
    cout << "1. Shortest path finding (can use Dijkstra/A* algorithm)" << endl;
    cout << "2. Optimizing multiple drop-offs (Travelling Salesman Problem / Greedy heuristics)" << endl;
    cout << "3. Resource allocation & scheduling (Dynamic Programming)" << endl;
    cout << "\\nConclusion: Various DAA concepts like Greedy strategies and Graphs directly solve real-world logistical challenges." << endl;
    return 0;
}
"""
}

# Write files to root folder map
for file_name, code in files_content.items():
    path = os.path.join(".", file_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Created {file_name}")

