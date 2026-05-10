#include <stdlib.h>
#include <stdio.h>

void list_print(int* list, size_t length){
    for (size_t i = 0; i < length; i++){
        printf(" %d ", list[i]);
    };
    printf("\n");
}

int* fibonacci(size_t n){
    int *list = malloc(n * sizeof(int));
    if (list == NULL) return NULL;

    if (n > 0){
        list[0] = 1;
    };
    if (n > 1){
        list[1] = 1;
    };

    for (size_t i = 2; i < n; i++){
        list[i] = list[i-1] + list[i-2];
    };

    return list;
}

int main(){

    size_t n = 10;
    int *fibonacci_output = fibonacci(n);

    list_print(fibonacci_output, n);

    free(fibonacci_output);
    return 0;
}
