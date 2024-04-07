#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

struct Node {
    long long key;
    Node* left;
    Node* right;
};

Node* createNode(long long x) {
    Node* newNode = new Node;
    newNode->key = x;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node* insertNode(Node* root, long long x) {
    if (root == NULL) {
        root = createNode(x);
    }
    else if (x < root->key) {
        root->left = insertNode(root->left, x);
    }
    else if (x > root->key) {
        root->right = insertNode(root->right, x);
    }
    return root;
}

Node* createTree(const vector<long long>& a) {
    Node* root = NULL;
    for (long long i = 0; i < a.size(); i++) {
        root = insertNode(root, a[i]);
    }
    return root;
}

void deleteTree(Node* root) {
    if (root == NULL) {
        return;
    }

    deleteTree(root->left);
    deleteTree(root->right);
    delete(root);
}

bool find(Node* root, long long x) {
    if (root == NULL) {
        return false;
    }
    else if (root->key > x) {
        return find(root->left, x);
    }
    else if (root->key < x) {
        return find(root->right, x);
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int n, m;
        long long candy;
        cin >> n >> m;
        vector<long long> candies_1(n);
        unordered_set<long long> candySet;

        for (int j = 0; j < n; j++) {
            cin >> candy;
            candies_1[j] = candy;
            candySet.insert(candy);
        }

        for (int k = 0; k < m; k++) {
            cin >> candy;
            if (candySet.find(candy) != candySet.end()) {
                cout << "YES" << endl;
            }
            else {
                cout << "NO" << endl;
                candySet.insert(candy);
            }
        }

    }

    return 0;
}
