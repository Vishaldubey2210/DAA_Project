#include <iostream>
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
