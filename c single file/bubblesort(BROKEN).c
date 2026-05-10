#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

//UTIL LINKED LIST LIBRARY START

struct Node {
    int val;
    struct Node* next;
};

void display_list(struct Node* list){
    struct Node* n = list;
    printf("[");
    while (n){
        printf("%d,",n->val);
        n = n->next;
    }
    printf("NULL]");
}

struct Node* append(int val, struct Node* next) {
    struct Node* n = malloc(sizeof(struct Node));
    n->val = val;
    n->next = next;

    return n;
}

int of(struct Node* list, size_t index) {
    struct Node* n = list;
    for (size_t i = 0; i < index; i++) {
        assert(n != NULL);
        n = n->next;
    }

    return n->val;
}

size_t length(struct Node* list){
    struct Node* n = list;
    size_t length = 0;
    while (n){
        n = n->next;
        length++;
    }

    return length;
}

void concat_list(struct Node* list_a,struct Node* list_b) {
    struct Node* n = list_a;
    while (n->next){
        n = n->next;

    }

    n->next = list_b;
}

int max(struct Node* list){
    struct Node* n = list;
    int max = n->val;
    while (n){
        if (n->val > max){
            max = n->val;
        }
        n = n->next;

    }

    return max;
}

int min(struct Node* list){
    struct Node* n = list;
    int min = n->val;
    while (n){
        if (n->val < min){
            min = n->val;
        }
        n = n->next;

    }

    return min;
}

struct Node* split_list(struct Node* list, size_t split_at){
    struct Node* new_list = list;
    struct Node* prev = NULL;
    for (size_t i = 0; i < split_at; i++){
        prev = new_list;
        new_list = new_list->next;
    }

    if (prev) {
        prev->next = NULL;
    }
    
    return new_list;
    
}

struct Node* swap(struct Node* list, size_t a, size_t b){
    //shit code, replace later
    struct Node* cut_left = list;
    struct Node* cut_a = split_list(cut_left, a);
    struct Node* cut_mid = split_list(cut_a, 1);
    struct Node* cut_b = split_list(cut_mid, b - a - 1);
    struct Node* cut_right = split_list(cut_b, 1);

    printf("left");  display_list(cut_left);
    printf(" a");     display_list(cut_a);
    printf(" mid");   display_list(cut_mid);
    printf(" b");     display_list(cut_b);
    printf(" right"); display_list(cut_right);
    printf("\r\n");

    concat_list(cut_a,cut_right);
    concat_list(cut_mid,cut_a);
    concat_list(cut_b,cut_mid);
    concat_list(cut_left,cut_b);
    return cut_left;
}

struct Node* bubble_sort(struct Node* list){
    size_t n = length(list);
    for(size_t j = 0; j < n; j++){
        struct Node* head = list;
        for(size_t i = 0; i < n-1; i++){
            if(of(list,i) > of(list,i+1)){
                list = swap(list,i,i+1);
            }
        }
    }
    return list;
}


void info_list(struct Node* list){
    printf("List Info\r\n");
    printf("\r\n");
    printf(" ~ List ");
    display_list(list);
    printf("\r\n");
    printf(" ~ Max of list %d \r\n", max(list));
    printf(" ~ Min of list %d \r\n", min(list));
    printf("\r\n");
}

//UTIL LINKED LIST LIBRARY END




int main(void) {
    struct Node* my_list = append(7,append(4,append(3,append(2,append(8,append(5,append(1,NULL)))))));

    info_list(my_list);

    my_list = bubble_sort(my_list);

    info_list(my_list);

}
