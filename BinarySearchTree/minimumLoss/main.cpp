#include <iostream>
#include <vector>
#include <algorithm>
#define INF 1e9

using namespace std;

struct Node{
    int key;
    Node* left;
    Node* right;
};

Node* creatNode(int x){
    Node* newNode = new Node;
    newNode->key = x;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node* insertNode(Node* root, int x){

    if(root == NULL){
        root = creatNode(x);
    }
    else if(x < root->key){
        root->left = insertNode(root->left, x); // Update left pointer
    }
    else if (x > root->key)
    {
        root->right = insertNode(root->right, x); // Update right pointer
    }
    // No need for an explicit condition for x == root->key

    return root;
}

void createTree(Node* &root, vector<int> a){
    for(int i=0; i<a.size(); i++){
        root = insertNode(root, a[i]);
    }
}

int size(Node* root){
    if(root == NULL){
        return 0;
    }
    else{
        return size(root->right) + 1 + size(root->left);
    }
}

void deleteTree(Node* root){
    if(root == NULL){
        return;
    }

    deleteTree(root->left);
    deleteTree(root->right);
    delete(root);
}

int main(){
    int n;
    cin >> n;
    int price;

    vector<int> prices;

    for(int i=0; i<n; i++){
        cin >> price;
        prices.push_back(price);
    }

    int min = INF;
    
    int buy;

    for(int i=0; i<prices.size(); i++){
        buy = prices[i];
        cout << min << endl;
        for(int j= i + 1; j < prices.size(); j++){
            if(prices[j] < buy){
                if(buy - prices[j] < min){
                    min = buy - prices[j];
                }
            }
        }
    }

    cout << min << endl;

    return 0;
}