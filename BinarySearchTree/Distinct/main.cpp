#include <iostream>
#include <vector>

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
    int T;
    cin >> T;
    
    int n,x, n1;
    vector<int> arr;
    int SIZE = 0;
    Node* root;

    for(int i=0; i<T; i++){
        root = NULL;
        cin >> n >> x;

        for(int i=0; i<n; i++){
            cin >> n1;
            arr.push_back(n1);
        }
    
        createTree(root, arr);

        SIZE = size(root);  

        if(SIZE == x){
            cout << "Good" << endl;
        }else if(SIZE < x){
            cout << "Bad" << endl;
        }else {
            cout << "Average" << endl;
        }     

        deleteTree(root);
        arr.clear();
    }


    return 0;
}