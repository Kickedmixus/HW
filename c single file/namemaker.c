#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    const char *names[5];
    names[0] = "John";
    names[1] = "Kevin";
    names[2] = "Phil";
    names[3] = "Greg";
    names[4] = "Steven";

    const char *endings[5];
    endings[0] = " the great";
    endings[1] = " the stinky";
    endings[2] = " the yummy";
    endings[3] = " the agile";
    endings[4] = " the red";

    srand(time(NULL)); 

    int random1 = (rand() % 5);
    int random2 = (rand() % 5);

    printf("%s%s \n",names[random1],endings[random2]);

};
