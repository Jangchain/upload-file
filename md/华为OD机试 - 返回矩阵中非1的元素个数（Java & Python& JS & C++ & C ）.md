## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

存在一个m*n的二维数组，其成员取值范围为0，1，2。

其中值为1的元素具备同化特性，每经过1S，将上下左右值为0的元素同化为1。

而值为2的元素，免疫同化。

将数组所有成员随机初始化为0或2，再将矩阵的[0, 0]元素修改成1，在经过足够长的时间后求矩阵中有多少个元素是0或2（即0和2数量之和）。

## 输入描述

输入的前两个数字是矩阵大小。后面是数字矩阵内容。

## 输出描述

返回矩阵中非1的元素个数。

## 示例1

输入

    
    
    4 4
    0 0 0 0
    0 2 2 2
    0 2 0 0
    0 2 0 0
    

输出

    
    
    4 4
    0 0 0 0
    0 2 2 2
    0 2 0 0
    0 2 0 0
    

说明

> 输入数字前两个数字是矩阵大小。后面的数字是矩阵内容。
>
> 起始位置(0,0)被修改为1后，最终只能同化矩阵为：
>
> 1 1 1 1
>
> 1 2 2 2
>
> 1 2 0 0
>
> 1 2 0 0
>
> 所以矩阵中非1的元素个数为9

## 解题思路

题目的要求是模拟一个在二维数组中进行的“同化”过程。

  1. **二维数组的初始化** ：

     * 给定一个大小为  m × n m \times n m×n 的二维数组，每个元素的取值范围为 `0`、`1` 或 `2`。
     * 值为 `1` 的元素表示同化源，会将相邻的 `0` 元素同化为 `1`。
     * 值为 `2` 的元素对同化免疫，无法被同化。
  2. **同化过程** ：

     * 从矩阵的左上角元素 `[0, 0]` 开始，将其设为 `1`，作为初始同化源。
     * 在接下来的每秒钟内，所有为 `1` 的元素会尝试同化它的上、下、左、右相邻的 `0` 元素，将其变为 `1`。
     * `2` 元素则不会被同化，也不会对周围元素产生影响。
  3. **目标** ：

     * 经过足够长时间的同化过程后，矩阵中会有一部分元素被同化成 `1`，无法被同化的 `0` 和 `2` 元素将保持原状。
     * 最后，计算矩阵中非 `1` 元素的个数（即 `0` 和 `2` 的数量）。

## Java

    
    
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
    
            // 输入矩阵大小
            int rows = scanner.nextInt();
            int cols = scanner.nextInt();
    
            // 创建并初始化矩阵
            int[][] matrix = new int[rows][cols];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    matrix[i][j] = scanner.nextInt();
                }
            }
    
            // 标记数组，避免重复访问
            boolean[][] visited = new boolean[rows][cols];
    
            // 使用 DFS 从 (0, 0) 开始同化区域
            matrix[0][0] = 1; // 将起始点设为 1
            dfs(matrix, 0, 0, rows, cols, visited);
    
            // 计算非 1 元素的个数
            int nonAssimilatedCount = 0;
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    if (matrix[i][j] != 1) {
                        nonAssimilatedCount++;
                    }
                }
            }
    
            System.out.println(nonAssimilatedCount);
        }
    
        // DFS 方法
        private static void dfs(int[][] matrix, int x, int y, int rows, int cols, boolean[][] visited) {
            // 定义四个方向偏移量
            int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
            visited[x][y] = true; // 标记当前点为已访问
    
            for (int[] direction : directions) {
                int newX = x + direction[0];
                int newY = y + direction[1];
    
                // 检查新坐标是否在范围内、值为0，并且未被访问
                if (isValid(newX, newY, rows, cols, matrix, visited)) {
                    matrix[newX][newY] = 1; // 同化新坐标
                    dfs(matrix, newX, newY, rows, cols, visited); // 递归同化相连区域
                }
            }
        }
    
        // 辅助方法：检查坐标是否合法、矩阵值为0且未被访问
        private static boolean isValid(int x, int y, int rows, int cols, int[][] matrix, boolean[][] visited) {
            return x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] == 0 && !visited[x][y];
        }
    }
    
    

## Python

    
    
    def dfs(matrix, x, y, rows, cols, visited):
        # 定义四个方向偏移量：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited[x][y] = True  # 标记当前点为已访问
    
        for direction in directions:
            newX = x + direction[0]
            newY = y + direction[1]
    
            # 检查新坐标是否合法且未访问，且矩阵值为0
            if is_valid(newX, newY, rows, cols, matrix, visited):
                matrix[newX][newY] = 1  # 同化新坐标
                dfs(matrix, newX, newY, rows, cols, visited)  # 递归调用
    
    def is_valid(x, y, rows, cols, matrix, visited):
        # 检查坐标范围、矩阵值和访问状态
        return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0 and not visited[x][y]
    
    def main():
        # 输入矩阵大小
        rows, cols = map(int, input().split())
        # 初始化矩阵
        matrix = [list(map(int, input().split())) for _ in range(rows)]
    
        # 初始化标记数组，防止重复访问
        visited = [[False for _ in range(cols)] for _ in range(rows)]
    
        # 将起点设为1
        matrix[0][0] = 1
        dfs(matrix, 0, 0, rows, cols, visited)
    
        # 统计非1元素的数量
        non_assimilated_count = sum(1 for i in range(rows) for j in range(cols) if matrix[i][j] != 1)
        print(non_assimilated_count)
    
    if __name__ == "__main__":
        main()
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    function dfs(matrix, x, y, rows, cols, visited) {
        // 定义四个方向偏移量：上、下、左、右
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        visited[x][y] = true; // 标记当前点为已访问
    
        for (const [dx, dy] of directions) {
            const newX = x + dx;
            const newY = y + dy;
    
            // 检查新坐标是否合法且未访问，且矩阵值为0
            if (isValid(newX, newY, rows, cols, matrix, visited)) {
                matrix[newX][newY] = 1; // 同化新坐标
                dfs(matrix, newX, newY, rows, cols, visited); // 递归调用
            }
        }
    }
    
    function isValid(x, y, rows, cols, matrix, visited) {
        // 检查坐标范围、矩阵值和访问状态
        return x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] === 0 && !visited[x][y];
    }
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let input = [];
    rl.on('line', (line) => {
        input.push(line);
    }).on('close', () => {
        const [rows, cols] = input[0].split(' ').map(Number);
        const matrix = input.slice(1, rows + 1).map(row => row.split(' ').map(Number));
        const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
    
        // 将起点设为1
        matrix[0][0] = 1;
        dfs(matrix, 0, 0, rows, cols, visited);
    
        // 统计非1元素的数量
        let nonAssimilatedCount = 0;
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (matrix[i][j] !== 1) {
                    nonAssimilatedCount++;
                }
            }
        }
        console.log(nonAssimilatedCount);
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    using namespace std;
    
    void dfs(vector<vector<int>> &matrix, int x, int y, int rows, int cols, vector<vector<bool>> &visited) {
        // 定义四个方向偏移量：上、下、左、右
        int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        visited[x][y] = true; // 标记当前点为已访问
    
        for (int i = 0; i < 4; i++) {
            int newX = x + directions[i][0];
            int newY = y + directions[i][1];
    
            // 检查新坐标是否合法且未访问，且矩阵值为0
            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && matrix[newX][newY] == 0 && !visited[newX][newY]) {
                matrix[newX][newY] = 1; // 同化新坐标
                dfs(matrix, newX, newY, rows, cols, visited); // 递归调用
            }
        }
    }
    
    int main() {
        int rows, cols;
        cin >> rows >> cols;
    
        // 初始化矩阵
        vector<vector<int>> matrix(rows, vector<int>(cols));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cin >> matrix[i][j];
            }
        }
    
        // 初始化标记数组，防止重复访问
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
    
        // 将起点设为1
        matrix[0][0] = 1;
        dfs(matrix, 0, 0, rows, cols, visited);
    
        // 统计非1元素的数量
        int nonAssimilatedCount = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] != 1) {
                    nonAssimilatedCount++;
                }
            }
        }
    
        cout << nonAssimilatedCount << endl;
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdbool.h>
    
    void dfs(int matrix[][100], int x, int y, int rows, int cols, bool visited[][100]) {
        // 定义四个方向偏移量：上、下、左、右
        int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        visited[x][y] = true; // 标记当前点为已访问
    
        for (int i = 0; i < 4; i++) {
            int newX = x + directions[i][0];
            int newY = y + directions[i][1];
    
            // 检查新坐标是否合法且未访问，且矩阵值为0
            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && matrix[newX][newY] == 0 && !visited[newX][newY]) {
                matrix[newX][newY] = 1; // 同化新坐标
                dfs(matrix, newX, newY, rows, cols, visited); // 递归调用
            }
        }
    }
    
    int main() {
        int rows, cols;
        scanf("%d %d", &rows, &cols);
    
        // 初始化矩阵
        int matrix[100][100];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                scanf("%d", &matrix[i][j]);
            }
        }
    
        // 初始化标记数组，防止重复访问
        bool visited[100][100] = {false};
    
        // 将起点设为1
        matrix[0][0] = 1;
        dfs(matrix, 0, 0, rows, cols, visited);
    
        // 统计非1元素的数量
        int nonAssimilatedCount = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] != 1) {
                    nonAssimilatedCount++;
                }
            }
        }
    
        printf("%d\n", nonAssimilatedCount);
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/4fec7c37c086de4a3dec65dec800fb2d.png)

### 完整用例

### 用例1

    
    
    4 4
    0 0 0 0
    0 2 2 2
    0 2 0 0
    0 2 0 0
    

### 用例2

    
    
    3 3
    0 2 0
    0 0 0
    2 0 2
    

### 用例3

    
    
    5 5
    0 0 0 0 0
    0 2 2 2 0
    0 2 0 0 0
    0 2 0 0 0
    0 0 0 0 0
    

### 用例4

    
    
    2 2
    0 0
    0 2
    

### 用例5

    
    
    4 4
    0 0 0 0
    2 2 2 2
    0 0 0 0
    0 0 0 2
    

### 用例6

    
    
    3 4
    2 2 2 2
    2 0 0 2
    2 2 2 2
    

### 用例7

    
    
    4 5
    0 0 0 0 0
    0 2 2 0 0
    0 0 0 2 2
    0 0 0 0 0
    

### 用例8

    
    
    5 5
    0 0 0 0 0
    0 2 2 2 0
    0 2 0 2 0
    0 2 2 2 0
    0 0 0 0 0
    

### 用例9

    
    
    3 4
    2 2 2 2
    2 0 0 2
    2 2 2 2
    

### 用例10

    
    
    5 5
    2 2 2 2 2
    2 0 0 0 2
    2 0 2 0 2
    2 0 0 0 2
    2 2 2 2 2
    

