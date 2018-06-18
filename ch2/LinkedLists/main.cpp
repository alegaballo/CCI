#include <iostream>


class Node{

public: Node(int value): value(value){};
    Node *next = nullptr;
    int value;


    void appendToTail(int value){
        Node * end = new Node(value);
        Node *current = this;
        while (current->next){
            current = current->next;
        }
        current->next = end;
    }
};
void deleteDuplicates(Node* head);


void deleteDuplicates(Node * head) {
    Node * it = head;
    Node * prev = it;
    int freq[20];
    while(it){
        std::cout<<"IN DA LOOP\n";
        freq[it->value]++;
        if(freq[it->value]>1){
            prev->next = it->next;
            auto dead = it;
            delete(dead);
            it = prev;
        }
        else{
            prev = it;
        }
        it=it->next;

    }
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    Node n(5);
    n.appendToTail(9);
    n.appendToTail(5);
    n.appendToTail(9);
    n.appendToTail(9);
    n.appendToTail(9);
    n.appendToTail(7);
    n.appendToTail(7);
    n.appendToTail(5);
    n.appendToTail(5);
    n.appendToTail(7);
    n.appendToTail(7);


    Node * it = &n;
    while (it){
        std::cout<<it->value<<' ';
        it = it->next;
    }
    std::cout<<'\n';
    std::cout<<"time to cleanup\n";

    deleteDuplicates(&n);
    it = &n;
    while (it != nullptr){
        std::cout<<it->value <<' ';
        it = it->next;
    }
    return 0;
}