#include <stdio.h>

char create_board(){
    return char [8]{char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},
                    char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"},char [8]{"░", "░", "░", "░", "░", "░", "░", "░"}}
}

void display_board(char board[]){
    char t[] = ""
    for (int i = 0; i < (sizeof(board)-1); i++){
        t = ""
        for (int j = 0; j < (sizeof(board)-1); j++){
            t += (" "+string(board[i][j]))
        printf (t)
        }
    }
    printf (" ")
}

char add_queen(int position[],char area[]){
    int y = position[0]
    int x = position[1]
    for (int i = 0; i < (sizeof(area)-1-y); i++){
        area[y+i][x] = char "█"
    }
    for (int i = 0; i < (sizeof(area)-1-y); i++){
        if (0 <= x+i < sizeof(area)-1 and 0 <= y+i < sizeof(area)-1){
            area[y+i][x+i] = "█" 
        }
        if (0 <= x-i < sizeof(area)-1 and 0 <= y+i < sizeof(area)-1){
            area[y+i][x-i] = "█" 
        }
    }
    area[y][x] = char "♛"

    return area
}:

int find_queens(char board=make_board(),int queens=0,int positions=[]){
    printf ("placed"+str(positions))
    display_board(board)
    if (queens == len(board)){
        return int position
    }; else{
        for (int i = 0; i < (sizeof(board)-1); i++){
            int multiverse = []
            if (board[queens][i] =="░"){
                universe = find_queens(add_queen((queens,i),(copy.deepcopy(board))),queens+1,copy.deepcopy(positions)+[(queens,i)])
            }
            if (int universe != None){
                multiverse.append(universe)
            }
           
        if (len(multiverse) != 0){
            return multiverse[0]
        }
    }
    printf ("goback")
}
