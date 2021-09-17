#include<iostream>
using namespace std;


class node{
    public:
    int data;
    struct node *next;
    struct node *prev;

    node(int val){
        data =val;
        next = NULL; 
        prev = NULL;

    }
};

node linkedlist(node* head , int val){
    node* newnode = new node(val);
    if(head == NULL){
        head = newnode;
        return head;
    }

    node* current = head;
    while(current->next != NULL){
        current = current->next;
    }
    current->next = newnode;
    newnode->prev = current;
    return head;
}



int main(){

    node* head = NULL;
    head = linkedlist(head, 1);
    head = linkedlist(head, 2);
    head = linkedlist(head, 3);
    head = linkedlist(head, 4);
    head = linkedlist(head, 5);

    node* current = head;
    while(current != NULL){
        cout<<current->data<<" ";
        current = current->next;
    }
    cout<<endl;
    return 0;
}

