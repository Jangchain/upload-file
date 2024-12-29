## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给你一个由 ‘0’ (空地)、‘1’ (银矿)、‘2’(金矿) 组成的的地图，矿堆只能由上下左右相邻的金矿或银矿连接形成。超出地图范围可以认为是空地。

假设银矿价值1，金矿价值2 ，请你找出地图中最大价值的矿堆并输出该矿堆的价值。

## 输入描述

地图元素信息如：

> 22220  
>  00000  
>  00000  
>  11111

  * 地图范围最大 300*300
  * 0 ≤ 地图元素 ≤ 2

## 输出描述

矿堆的最大价值

## 用例1

输入

    
    
    22220
    00000
    00000
    01111
    

输出

    
    
    8
    

说明

> ## 用例2

输入

    
    
    22220
    00020
    00010
    01111
    

输出

    
    
    15
    

说明

> ## 用例3

输入

    
    
    20000
    00020
    00000
    00111
    

输出

    
    
    3
    

说明

> ## 解题思路

这道题目要求在一个由 ‘0’、‘1’ 和 ‘2’ 组成的地图中找到最大价值的矿堆。具体来说：

#### 题意分析

  1. **地图元素** ：

     * ‘0’ 表示空地，没有价值。
     * ‘1’ 表示银矿，价值为 1。
     * ‘2’ 表示金矿，价值为 2。
  2. **矿堆的定义** ：

     * 矿堆由相邻的金矿和银矿组成，相邻指的是上下左右相连的单元格。
     * 每个矿堆的价值是其内部所有金矿和银矿的价值总和。
  3. **目标** ：

     * 计算并输出地图中所有矿堆中最大价值的矿堆。

#### 输入与输出

  * **输入** ：一个地图的字符串表示，每行代表地图的一行，字符之间不需要空格。
  * **输出** ：单个整数，表示最大矿堆的价值。

#### 示例解释

  * **示例 1** ：
    
        输入：
    22220
    00000
    00000
    01111
    输出：
    8
    

    * 这个地图中有一个金矿堆（包含四个 ‘2’）和一个银矿堆（包含五个 ‘1’）。金矿堆的价值是  2 \+ 2 \+ 2 \+ 2 = 8 2+2+2+2=8 2+2+2+2=8，银矿堆的价值是  1 \+ 1 \+ 1 \+ 1 \+ 1 = 5 1+1+1+1+1=5 1+1+1+1+1=5。所以，最大价值是 8。
  * **示例 2** ：
    
        输入：
    22220
    00020
    00010
    01111
    输出：
    15
    

    * 这个地图有多个金矿和银矿组成的矿堆。计算2+2+2+2+2+1+1+1+1=1，最大矿堆的价值为 15。
  * **示例 3** ：
    
        输入：
    20000
    00020
    00000
    00111
    输出：
    3
    

    * 在这个例子中，只有一个金矿和一个银矿形成的矿堆，其价值总和为 3。

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <queue>
    using namespace std;
    
    // 地图矩阵
    int map[100][100];
    
    // 上下左右，四个方向的偏移量
    int offsets[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    int main() {
        // 读入地图信息
        vector<string> lines;
        string line;
        while (getline(cin, line)) {
            lines.push_back(line);
        }
    
        // 构建地图矩阵
        int rows = lines.size();
        int cols = lines[0].size();
        for (int i = 0; i < rows; i++) {
            line = lines[i];
            for (int j = 0; j < cols; j++) {
                map[i][j] = line[j] - '0';
            }
        }
    
        // 记录最大矿堆价值
        int maxVal = 0;
    
        // 遍历地图矩阵
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
                if (map[i][j] > 0) {
                    queue<pair<int, int>> q;
                    q.push(make_pair(i, j));
    
                    int sum = 0;
    
                    while (!q.empty()) {
                        pair<int, int> pos = q.front();
                        q.pop();
                        int x = pos.first, y = pos.second;
    
                        sum += map[x][y];
                        map[x][y] = 0;
    
                        // 遍历四个方向
                        for (auto offset : offsets) {
                            int newX = x + offset[0];
                            int newY = y + offset[1];
    
                            // 如果新位置在地图范围内，且有矿，则加入队列中
                            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && map[newX][newY] > 0) {
                                q.push(make_pair(newX, newY));
                            }
                        }
                    }
    
                    // 更新最大矿堆价值
                    maxVal = max(maxVal, sum);
                }
            }
        }
    
        cout << maxVal << endl;
    
        return 0;
    }
    
    
    

## Java

    
    
    import java.util.ArrayList;
    import java.util.LinkedList;
    import java.util.Scanner;
    
    public class Main {
        // 地图矩阵
        static int[][] map;
    
        // 上下左右，四个方向的偏移量
        static int[][] offsets = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            // 读入地图信息
            ArrayList<String> lines = new ArrayList<>();
            while (sc.hasNextLine()) {
                lines.add(sc.nextLine());
            }
    
            // 构建地图矩阵
            int rows = lines.size();
            int cols = lines.get(0).length();
            map = new int[rows][cols];
            for (int i = 0; i < rows; i++) {
                String line = lines.get(i);
                for (int j = 0; j < cols; j++) {
                    map[i][j] = line.charAt(j) - '0';
                }
            }
    
            // 记录最大矿堆价值
            int maxVal = 0;
    
            // 遍历地图矩阵
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    // 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
                    if (map[i][j] > 0) {
                        LinkedList<int[]> stack = new LinkedList<>();
                        stack.add(new int[]{i, j});
    
                        int sum = 0;
    
                        while (!stack.isEmpty()) {
                            int[] pos = stack.removeLast();
                            int x = pos[0], y = pos[1];
    
                            sum += map[x][y];
                            map[x][y] = 0;
    
                            // 遍历四个方向
                            for (int[] offset : offsets) {
                                int newX = x + offset[0];
                                int newY = y + offset[1];
    
                                // 如果新位置在地图范围内，且有矿，则加入栈中
                                if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && map[newX][newY] > 0) {
                                    stack.add(new int[]{newX, newY});
                                }
                            }
                        }
    
                        // 更新最大矿堆价值
                        maxVal = Math.max(maxVal, sum);
                    }
                }
            }
    
            System.out.println(maxVal);
        }
    }
    
    
    

## javaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    // 地图矩阵
    let map;
    
    // 上下左右，四个方向的偏移量
    const offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let lines = [];
    rl.on('line', (line) => {
      lines.push(line);
    }).on('close', () => {
     // 构建地图矩阵
        const rows = lines.length;
        const cols = lines[0].length;
        map = new Array(rows);
        for (let i = 0; i < rows; i++) {
          map[i] = new Array(cols);
          const str = lines[i];
          for (let j = 0; j < cols; j++) {
            map[i][j] = parseInt(str.charAt(j));
          }
        }
    
        // 记录最大矿堆价值
        let maxVal = 0;
    
        // 遍历地图矩阵
        for (let i = 0; i < rows; i++) {
          for (let j = 0; j < cols; j++) {
            // 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
            if (map[i][j] > 0) {
              const stack = [];
              stack.push([i, j]);
    
              let sum = 0;
    
              while (stack.length > 0) {
                const pos = stack.pop();
                const x = pos[0], y = pos[1];
    
                sum += map[x][y];
                map[x][y] = 0;
    
                // 遍历四个方向
                for (const offset of offsets) {
                  const newX = x + offset[0];
                  const newY = y + offset[1];
    
                  // 如果新位置在地图范围内，且有矿，则加入栈中
                  if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && map[newX][newY] > 0) {
                    stack.push([newX, newY]);
                  }
                }
              }
    
              // 更新最大矿堆价值
              maxVal = Math.max(maxVal, sum);
            }
          }
        }
    
        console.log(maxVal);
        rl.close();
    })
    
    
    

## Python

    
    
    from collections import deque
    
    # 地图矩阵
    map = []
    
    # 上下左右，四个方向的偏移量
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 读入地图信息
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except:
            break
    
    # 构建地图矩阵
    rows = len(lines)
    cols = len(lines[0])
    map = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        line = lines[i]
        for j in range(cols):
            map[i][j] = int(line[j])
    
    # 记录最大矿堆价值
    maxVal = 0
    
    # 遍历地图矩阵
    for i in range(rows):
        for j in range(cols):
            # 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
            if map[i][j] > 0:
                stack = deque()
                stack.append((i, j))
    
                sum = 0
    
                while stack:
                    pos = stack.pop()
                    x, y = pos
    
                    sum += map[x][y]
                    map[x][y] = 0
    
                    # 遍历四个方向
                    for offset in offsets:
                        newX = x + offset[0]
                        newY = y + offset[1]
    
                        # 如果新位置在地图范围内，且有矿，则加入栈中
                        if newX >= 0 and newX < rows and newY >= 0 and newY < cols and map[newX][newY] > 0:
                            stack.append((newX, newY))
    
                # 更新最大矿堆价值
                maxVal = max(maxVal, sum)
    
    print(maxVal)
    
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>  // 包含此头文件
    #define MAX_SIZE 300
    
    // 地图矩阵
    int map[MAX_SIZE][MAX_SIZE];
    
    // 上下左右，四个方向的偏移量
    int offsets[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    int main() {
        char line[MAX_SIZE + 1];
        int rows = 0, cols = 0;
    
        // 读入地图信息
        while (fgets(line, sizeof(line), stdin) != NULL) {
            // 去掉换行符
            line[strcspn(line, "\n")] = 0;
            if (cols == 0) {
                cols = strlen(line);  // 获取列数
            }
            for (int j = 0; j < cols; j++) {
                map[rows][j] = line[j] - '0';  // 将字符转为整数
            }
            rows++;
        }
    
        // 记录最大矿堆价值
        int maxVal = 0;
    
        // 遍历地图矩阵
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
                if (map[i][j] > 0) {
                    int stack[MAX_SIZE * MAX_SIZE][2];  // 模拟栈
                    int stack_size = 0;  // 栈的当前大小
                    stack[stack_size][0] = i;  // 压入起始位置
                    stack[stack_size][1] = j;
                    stack_size++;
    
                    int sum = 0;
    
                    while (stack_size > 0) {
                        stack_size--;  // 先减少栈的大小
                        int x = stack[stack_size][0];  // 弹出栈顶元素
                        int y = stack[stack_size][1];
    
                        sum += map[x][y];
                        map[x][y] = 0;  // 标记为已访问
    
                        // 遍历四个方向
                        for (int k = 0; k < 4; k++) {
                            int newX = x + offsets[k][0];
                            int newY = y + offsets[k][1];
    
                            // 如果新位置在地图范围内，且有矿，则加入栈中
                            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && map[newX][newY] > 0) {
                                stack[stack_size][0] = newX;  // 压入新位置
                                stack[stack_size][1] = newY;
                                stack_size++;
                            }
                        }
                    }
    
                    // 更新最大矿堆价值
                    if (sum > maxVal) {
                        maxVal = sum;
                    }
                }
            }
        }
    
        printf("%d\n", maxVal);  // 输出最大矿堆价值
    
        return 0;
    }
    

![fengmian](https://i-blog.csdnimg.cn/blog_migrate/5f0b958970e6c0b7c34717431d93c2f8.png)

## 完整用例

### 用例1

    
    
    22220
    00000
    00000
    01111
    

### 用例2

    
    
    22220
    00020
    00010
    01111
    

### 用例3

    
    
    20000
    00020
    00000
    00111
    

### 用例4

    
    
    00000
    00000
    00000
    00000
    
    

### 用例5

    
    
    22222
    22222
    22222
    22222
    

### 用例6

    
    
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    2222222222
    

### 用例7

    
    
    2000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    0000000000
    

### 用例8

    
    
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    1111111111
    

### 用例9

    
    
    2222222222
    1111111111
    2222222222
    1111111111
    2222222222
    1111111111
    2222222222
    1111111111
    2222222222
    1111111111
    

### 用例10

    
    
    2222222222
    1111111111
    2222200000
    1111100000
    2222200000
    1111100000
    2222200000
    1111100000
    2222222222
    1111111111
    

