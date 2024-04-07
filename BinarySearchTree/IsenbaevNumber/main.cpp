#include <iostream>
#include <vector>

using namespace std;

struct Node{
    string key;
    string Name;
    Node* left = nullptr;
    Node* right = nullptr;
};

Node* createNode(string Name, string x){
    Node* newNode = new Node;
    newNode->key = x;
    newNode->Name = Name;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

Node* insertNode(Node* root, Node* x){
    if(root == nullptr){
        root = x;
    }
    else if(root->Name > x->Name){
        root->left = insertNode(root->left, x);
    }
    else if(root->Name < x->Name){
        root->right = insertNode(root->right, x);
    }
    return root;
}

Node* findValue(Node* root, string x){
    if(root == nullptr){
        return root;
    }
    else if(x < root->Name){
        return findValue(root->left, x);
    }
    else if(x > root->Name){
        return findValue(root->right, x);
    }else{
        return root;
    }
}

void assignValue(vector<Node*>& teamNode){
    bool checkIsa = false;
    for(size_t i = 0; i < teamNode.size(); ++i){
        if(teamNode[i]->Name == "Isenbaev"){
            checkIsa = true;
            break;
        }
    }
    if(checkIsa){
        for(size_t i = 0; i < teamNode.size(); ++i){
            if(teamNode[i]->Name != "Isenbaev"){
                teamNode[i]->key = "1";
            }else{
                teamNode[i]->key = "0";
            }
        }
    }else{
        for(size_t i = 0; i < teamNode.size(); ++i){
            teamNode[i]->key = "undefined";
        }
    }
}

void inorderTraversal(Node* root){
    if(root == nullptr){
        return;
    }
    inorderTraversal(root->left);
    cout << root->Name << " " << root->key << endl;
    inorderTraversal(root->right);
}

int main(){
    int T;
    cin >> T;
    string person;
    Node* root = nullptr;
    vector<Node*> teamNode;

    for(int i = 0; i < T; ++i){
        for(int j = 0; j < 3; ++j){
            cin >> person;
            Node* teamMember = createNode(person, "");
            teamNode.push_back(teamMember);
        }
        assignValue(teamNode);
        for(size_t i = 0; i < teamNode.size(); ++i){
            root = insertNode(root, teamNode[i]);
        }
        teamNode.clear(); // Clear the vector for the next iteration
    }

    cout << endl;

    inorderTraversal(root);

    // Free memory allocated for nodes
    // This is important to avoid memory leaks
    // Implement this if you're not using smart pointers
    // TODO: Implement memory deallocation
    
    return 0;
}
