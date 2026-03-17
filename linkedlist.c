#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

int read_nodes(struct Node *node)
{   
    if (node->next != NULL){
        printf("%d\n",read_nodes(node->next));
    };
    return node->data;

};

void main(){
    struct Node *snake_head = NULL;
    struct Node *snake_belly = NULL;
    struct Node *snake_butt = NULL; 

    snake_head = (struct Node *)malloc(sizeof(struct Node));
    snake_belly = (struct Node *)malloc(sizeof(struct Node));
    snake_butt = (struct Node *)malloc(sizeof(struct Node));

    snake_head->data = 6;
    snake_head->next = snake_belly;

    snake_belly->data = 7;
    snake_belly->next = snake_butt;

    snake_butt->data = 8;
    snake_butt->next = NULL;

    printf("%d\n",read_nodes(snake_head));

};
