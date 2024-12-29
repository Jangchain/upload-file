## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

Linux操作系统有多个发行版，distrowatch.com提供了各个发行版的资料。这些发行版互相存在关联，例如Ubuntu基于Debian开发，而Mint又基于Ubuntu开发，那么我们认为Mint同Debian也存在关联。

发行版集是一个或多个相关存在关联的操作系统发行版，集合内不包含没有关联的发行版。

给你一个 n * n 的矩阵 isConnected，其中 isConnected[i][j] = 1 表示第 i 个发行版和第 j 个发行版直接关联，而
isConnected[i][j] = 0 表示二者不直接相连。

返回最大的发行版集中发行版的数量。

## 输入描述

第一行输入发行版的总数量N，

之后每行表示各发行版间是否直接相关

#### 备注

1 ≤ N ≤ 200

## 输出描述

输出最大的发行版集中发行版的数量

## 示例1

输入

    
    
    4
    1 1 0 0
    1 1 1 0
    0 1 1 0
    0 0 0 1
    

输出

    
    
    3
    

说明

> Debian(1)和Unbuntu(2)相关
>
> Mint(3)和Ubuntu(2)相关，
>
> EeulerOS(4)和另外三个都不相关，
>
> 所以存在两个发行版集，发行版集中发行版的数量分别是3和1，所以输出3

## 解题思路

####

##### 详细分析：

  1. **输入矩阵说明** ：

     * `isConnected[i][j] = 1` 表示第 `i` 个发行版和第 `j` 个发行版之间有直接关联。
     * `isConnected[i][j] = 0` 表示第 `i` 和第 `j` 发行版没有直接关联。
     * 矩阵对角线上的元素 `isConnected[i][i] = 1`，表示每个发行版与自己关联。
  2. **发行版集的定义** ：

     * 发行版集是由一个或多个互相关联的发行版组成的群体。发行版直接或间接关联都算在一个发行版集中，例如 `A` 和 `B` 关联，`B` 和 `C` 关联，那么 `A`、`B` 和 `C` 都属于同一个发行版集。
  3. **问题目标** ：

     * 找出发行版集中最大的那个，输出其中发行版的数量。

#### 示例解析：

##### 示例 1：

输入：

    
    
    4
    1 1 0 0
    1 1 1 0
    0 1 1 0
    0 0 0 1
    

解释：

  * 发行版1和发行版2直接相关（`isConnected[0][1] = 1` 和 `isConnected[1][0] = 1`）。
  * 发行版2和发行版3直接相关（`isConnected[1][2] = 1` 和 `isConnected[2][1] = 1`）。
  * 因此，发行版1、2、3形成了一个互相关联的发行版集（连通分量）。
  * 发行版4没有和其他发行版相关联，形成一个独立的发行版集。

两个发行版集分别是：

  * 发行版集1：包含发行版1、2、3（数量为3）。
  * 发行版集2：仅包含发行版4（数量为1）。

因此，最大的发行版集包含3个发行版，输出结果为 `3`。

#### 思路：

这个问题可以看作**图的连通分量问题** ，我们需要找出图中所有的连通分量，并且返回最大的连通分量的节点数。

#### 步骤：

这个问题可以看作**图的连通分量问题** ，我们需要找出图中所有的连通分量，并且返回最大的连通分量的节点数。可以使用**深度优先搜索（DFS）**或**
广度优先搜索（BFS）**来遍历图，查找所有连通分量。

  1. **矩阵视作图的邻接矩阵** ：

     * `isConnected[i][j] = 1` 表示节点 `i` 和节点 `j` 之间有边（直接关联）。
  2. **遍历矩阵** ：

     * 便利所有节点，找到所有互相关联的节点（即同一连通分量的节点）。
  3. **记录每个连通分量的大小** ：

     * 对每个连通分量进行遍历时，计数其包含的节点数量，最终返回最大的连通分量。

## Java

    
    
    import java.util.*;
    
    class Main {
        public static void main(String[] args) {
            // 处理输入
            Scanner scanner = new Scanner(System.in);
            int numOfVersions = scanner.nextInt();  // 版本数量
    
            int[][] matrix = new int[numOfVersions][numOfVersions];   // 版本信息矩阵
            for (int i = 0; i < numOfVersions; i++) {
                for (int j = 0; j < numOfVersions; j++) {
                    matrix[i][j] = scanner.nextInt();    // 将每行版本信息存储在 matrix 中
                }
            }
    
            // 记录是否访问过的版本
            boolean[] visited = new boolean[numOfVersions];
            int maxGroupSize = 0;   // 最大关联版本数量
    
            // 遍历所有节点
            for (int i = 0; i < numOfVersions; i++) {
                if (!visited[i]) {   // 如果当前节点尚未访问
                    int groupSize = dfs(matrix, visited, i);   // 深度优先搜索找到连通分量的大小
                    maxGroupSize = Math.max(maxGroupSize, groupSize);   // 更新最大连通分量的大小
                }
            }
    
            System.out.println(maxGroupSize);   // 输出最大连通分量的大小
        }
    
        // 深度优先搜索
        public static int dfs(int[][] matrix, boolean[] visited, int node) {
            visited[node] = true;   // 标记当前节点为已访问
            int size = 1;   // 当前连通分量的大小，包含当前节点
    
            for (int i = 0; i < matrix.length; i++) {
                // 如果节点 i 与当前节点直接相连，且尚未访问
                if (matrix[node][i] == 1 && !visited[i]) {
                    size += dfs(matrix, visited, i);   // 递归搜索连通节点
                }
            }
    
            return size;
        }
    }
    

## Python

    
    
    # 处理输入
    def main():
        num_of_versions = int(input())  # 读取版本数量
    
        # 创建版本信息矩阵
        matrix = []
        for _ in range(num_of_versions):
            row = list(map(int, input().split()))
            matrix.append(row)
    
        # 创建访问记录数组
        visited = [False] * num_of_versions
        max_group_size = 0  # 最大关联版本数量
    
        # 遍历所有节点
        for i in range(num_of_versions):
            if not visited[i]:  # 如果当前节点尚未访问
                group_size = dfs(matrix, visited, i)  # 深度优先搜索找到连通分量的大小
                max_group_size = max(max_group_size, group_size)  # 更新最大连通分量的大小
    
        print(max_group_size)  # 输出最大连通分量的大小
    
    # 深度优先搜索
    def dfs(matrix, visited, node):
        visited[node] = True  # 标记当前节点为已访问
        size = 1  # 当前连通分量的大小，包含当前节点
    
        for i in range(len(matrix)):
            # 如果节点 i 与当前节点直接相连，且尚未访问
            if matrix[node][i] == 1 and not visited[i]:
                size += dfs(matrix, visited, i)  # 递归搜索连通节点
    
        return size
    
    if __name__ == "__main__":
        main()
    

## JavaScript

    
    
    // 处理输入
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let numOfVersions = 0;
    let matrix = [];
    let currentLine = 0;
    
    // 读取输入
    rl.on('line', (line) => {
        if (currentLine === 0) {
            numOfVersions = parseInt(line);  // 读取版本数量
        } else {
            matrix.push(line.trim().split(' ').map(Number));  // 读取每行并转换为整数数组
        }
        currentLine++;
    
        // 当读取到最后一行时处理逻辑
        if (currentLine > numOfVersions) {
            rl.close();
    
            // 创建访问记录数组
            let visited = new Array(numOfVersions).fill(false);
            let maxGroupSize = 0;  // 最大关联版本数量
    
            // 遍历所有节点
            for (let i = 0; i < numOfVersions; i++) {
                if (!visited[i]) {  // 如果当前节点尚未访问
                    let groupSize = dfs(matrix, visited, i);  // 深度优先搜索找到连通分量的大小
                    maxGroupSize = Math.max(maxGroupSize, groupSize);  // 更新最大连通分量的大小
                }
            }
    
            console.log(maxGroupSize);  // 输出最大连通分量的大小
        }
    });
    
    // 深度优先搜索
    function dfs(matrix, visited, node) {
        visited[node] = true;  // 标记当前节点为已访问
        let size = 1;  // 当前连通分量的大小，包含当前节点
    
        for (let i = 0; i < matrix.length; i++) {
            // 如果节点 i 与当前节点直接相连，且尚未访问
            if (matrix[node][i] === 1 && !visited[i]) {
                size += dfs(matrix, visited, i);  // 递归搜索连通节点
            }
        }
    
        return size;
    }
    

## C++

    
    
    #include <iostream>
    #include <vector>
    using namespace std;
    
    // 深度优先搜索
    int dfs(vector<vector<int>>& matrix, vector<bool>& visited, int node) {
        visited[node] = true;  // 标记当前节点为已访问
        int size = 1;  // 当前连通分量的大小，包含当前节点
    
        for (int i = 0; i < matrix.size(); i++) {
            // 如果节点 i 与当前节点直接相连，且尚未访问
            if (matrix[node][i] == 1 && !visited[i]) {
                size += dfs(matrix, visited, i);  // 递归搜索连通节点
            }
        }
    
        return size;
    }
    
    int main() {
        int numOfVersions;
        cin >> numOfVersions;  // 读取版本数量
    
        // 创建版本信息矩阵
        vector<vector<int>> matrix(numOfVersions, vector<int>(numOfVersions));
        for (int i = 0; i < numOfVersions; i++) {
            for (int j = 0; j < numOfVersions; j++) {
                cin >> matrix[i][j];  // 读取每个元素
            }
        }
    
        // 创建访问记录数组
        vector<bool> visited(numOfVersions, false);
        int maxGroupSize = 0;  // 最大关联版本数量
    
        // 遍历所有节点
        for (int i = 0; i < numOfVersions; i++) {
            if (!visited[i]) {  // 如果当前节点尚未访问
                int groupSize = dfs(matrix, visited, i);  // 深度优先搜索找到连通分量的大小
                maxGroupSize = max(maxGroupSize, groupSize);  // 更新最大连通分量的大小
            }
        }
    
        cout << maxGroupSize << endl;  // 输出最大连通分量的大小
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdbool.h>
    
    // 深度优先搜索
    int dfs(int matrix[][200], bool visited[], int numOfVersions, int node) {
        visited[node] = true;  // 标记当前节点为已访问
        int size = 1;  // 当前连通分量的大小，包含当前节点
    
        for (int i = 0; i < numOfVersions; i++) {
            // 如果节点 i 与当前节点直接相连，且尚未访问
            if (matrix[node][i] == 1 && !visited[i]) {
                size += dfs(matrix, visited, numOfVersions, i);  // 递归搜索连通节点
            }
        }
    
        return size;
    }
    
    int main() {
        int numOfVersions;
        scanf("%d", &numOfVersions);  // 读取版本数量
    
        // 创建版本信息矩阵
        int matrix[200][200];  // 假设最多200个版本，满足题目限制
        for (int i = 0; i < numOfVersions; i++) {
            for (int j = 0; j < numOfVersions; j++) {
                scanf("%d", &matrix[i][j]);  // 读取每个元素
            }
        }
    
        // 创建访问记录数组
        bool visited[200] = {false};  // 初始化为未访问
        int maxGroupSize = 0;  // 最大关联版本数量
    
        // 遍历所有节点
        for (int i = 0; i < numOfVersions; i++) {
            if (!visited[i]) {  // 如果当前节点尚未访问
                int groupSize = dfs(matrix, visited, numOfVersions, i);  // 深度优先搜索找到连通分量的大小
                if (groupSize > maxGroupSize) {
                    maxGroupSize = groupSize;  // 更新最大连通分量的大小
                }
            }
        }
    
        printf("%d\n", maxGroupSize);  // 输出最大连通分量的大小
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/9cdb5c8d2298f96a67debabee2936c57.png)

## 完整用例

### 用例1

    
    
    4
    1 1 0 0
    1 1 1 0
    0 1 1 0
    0 0 0 1
    

### 用例2

    
    
    5
    1 1 0 0 0
    1 1 1 0 0
    0 1 1 1 0
    0 0 1 1 0
    0 0 0 0 1
    

### 用例3

    
    
    3
    1 0 0
    0 1 0
    0 0 1
    

### 用例4

    
    
    6
    1 1 0 0 0 0
    1 1 0 0 0 0
    0 0 1 1 0 0
    0 0 1 1 0 0
    0 0 0 0 1 1
    0 0 0 0 1 1
    

### 用例5

    
    
    4
    1 1 0 1
    1 1 0 0
    0 0 1 1
    1 0 1 1
    

### 用例6

    
    
    2
    1 0
    0 1
    

### 用例7

    
    
    7
    1 1 0 0 0 0 0
    1 1 1 0 0 0 0
    0 1 1 1 0 0 0
    0 0 1 1 1 0 0
    0 0 0 1 1 1 0
    0 0 0 0 1 1 1
    0 0 0 0 0 1 1
    

### 用例8

    
    
    5
    1 0 0 0 0
    0 1 0 0 0
    0 0 1 0 0
    0 0 0 1 0
    0 0 0 0 1
    

### 用例9

    
    
    3
    1 1 1
    1 1 1
    1 1 1
    

### 用例10

    
    
    5
    1 1 1 0 0
    1 1 0 0 0
    1 0 1 0 0
    0 0 0 1 1
    0 0 0 1 1
    

