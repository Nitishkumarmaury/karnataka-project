#include <stdio.h>
#include <stdbool.h>

#define N 4

bool isSafe(int queens[N], int row, int col) {
    for (int i = 0; i < row; i++) {
        if (queens[i] == col || queens[i] - i == col - row || queens[i] + i == col + row) {
            return false;
        }
    }
    return true;
}

void printSolution(int queens[N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (queens[i] == j)
                printf("Q ");
            else
                printf("_ ");
        }
        printf("\n");
    }
    printf("\n");
}

void solveNQueens(int queens[N], int row) {
    if (row == N) {
        printSolution(queens);
        return;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(queens, row, col)) {
            queens[row] = col;
            solveNQueens(queens, row + 1);
        }
    }
}

int main() {
    int queens[N] = {0};
    solveNQueens(queens, 0);
    return 0;
}