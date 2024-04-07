#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

struct Node{
    string key;
    int appear = 0;
    Node* left;
    Node* right;
};

Node* creatNode(string x){
    Node* newNode = new Node;
    newNode->key = x;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node* insertNode(Node* root, string x){

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

void createTree(Node* &root, vector<string> a){
    for(int i=0; i<a.size(); i++){
        root = insertNode(root, a[i]);
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

void Findcount(Node* root, string x){
    if(root == NULL){
        return;
    }
    else if(root->key > x){
        Findcount(root->left, x);
    }
    else if(root->key < x){
        Findcount(root->right, x);
    }
    else {
        root->appear += 1; // Update the appear variable of the current node
        Findcount(root->left, x); // Continue traversal in the left subtree
        Findcount(root->right, x); // Continue traversal in the right subtree
    }
}


void inorderTraversal(Node* root, int& max, string& penguin) {
    if (root == NULL) {
        return;
    }
    inorderTraversal(root->left, max, penguin);
    if (max <= root->appear) { // Use <= instead of <
        max = root->appear;
        penguin = root->key;
    }
    inorderTraversal(root->right, max, penguin);
}

int main(){
    Node* root = NULL;
    vector<string> penguinSet;
    string penguin;
    vector<string> species = {
        "Emperor Penguin", "Little Penguin", "Macaroni Penguin" 
    };

    int T;  
    cin >> T;
    cin.ignore();

    createTree(root, species);

    for(int i=0; i<T; i++){
        getline(cin, penguin);
        Findcount(root, penguin);
    }

    int max = -1;

    inorderTraversal(root, max, penguin);
    cout<< penguin << endl;
    
    return 0;
}
