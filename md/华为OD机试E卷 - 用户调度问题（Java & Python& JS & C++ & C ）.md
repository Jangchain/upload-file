## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

在通信系统中，一个常见的问题是对用户进行不同策略的调度，会得到不同的系统消耗和性能。

假设当前有n个待串行调度用户，每个用户可以使用A/B/C三种不同的调度策略，不同的策略会消耗不同的系统资源。请你根据如下规则进行用户调度，并返回总的消耗资源数。

规则：

  1. 相邻的用户不能使用相同的调度策略，例如，第1个用户使用了A策略，则第2个用户只能使用B或者C策略。

  2. 对单个用户而言，不同的调度策略对系统资源的消耗可以[归一化](https://so.csdn.net/so/search?q=%E5%BD%92%E4%B8%80%E5%8C%96&spm=1001.2101.3001.7020)后抽象为数值。例如，某用户分别使用A/B/C策略的系统消耗分别为15/8/17。

  3. 每个用户依次选择当前所能选择的对系统资源消耗最少的策略（局部最优），如果有多个满足要求的策略，选最后一个。

## 输入描述

第一行表示用户个数n

接下来每一行表示一个用户分别使用三个策略的系统消耗resA resB resC

###

## 输出描述

最优策略组合下的总的系统资源消耗数

## 示例1

输入

    
    
    3
    15 8 17
    12 20 9
    11 7 5
    

输出

    
    
    24
    

说明

> 1号用户使用B策略，2号用户使用C策略，3号用户使用B策略。系统资源消耗: 8 + 9 + 7 = 24。

## 解题思路

本题求的是**局部最优解** ，而不是全局最优解。

#### 为什么是局部最优解？

题目要求每个用户**依次选择当前所能选择的最小资源消耗策略** ，并且若有多个策略的资源消耗相同，则选择**最后一个策略**
。这种选择策略本身就是一个局部最优选择的过程：

  1. **每个用户的选择是独立的** ，只考虑该用户的策略和相邻用户的约束，不考虑整个调度序列的全局资源消耗。

  2. 每个用户根据**自己的当前状态** （即自己的三种选择的资源消耗）做出**局部最优选择** ：在当前可选的策略中，选择消耗最小的那个。如果有多个最小值，则选择最后一个（根据题意）。这一选择是**局部的最优** ，即在当下最有利的选择，但并不保证最终的整体系统资源消耗是最小的。

#### 举个例子：

考虑以下输入：

    
    
    3
    15 8 17
    12 20 9
    11 7 5
    

##### 第一位用户：

  * 资源消耗分别是：A=15, B=8, C=17。
  * 用户选择B，因为B的资源消耗是最小的（8）。此时做出了局部最优选择。

##### 第二位用户：

  * 资源消耗分别是：A=12, B=20, C=9。
  * 用户不能选择B（因为相邻用户已经选择了B），所以只能在A和C之间选择。此时选择C（因为9是最小的），这也是局部最优选择。

##### 第三位用户：

  * 资源消耗分别是：A=11, B=7, C=5。
  * 用户不能选择C（因为相邻用户已经选择了C），只能选择A和B。此时选择B（因为7比A的11小），做出了局部最优选择。

最终的选择是：

  * 用户1选择B（消耗8）
  * 用户2选择C（消耗9）
  * 用户3选择B（消耗7）

总消耗 = 8 + 9 + 7 = 24。

#### 全局最优和局部最优的差异：

  * **全局最优解** 会考虑整个序列的资源消耗，通过全局最优化的方法（例如动态规划、回溯等），寻找一个能最小化整个系统资源消耗的策略组合。这通常需要在选择每个用户策略时考虑后续的用户选择，以便找到最合适的全局策略。

  * **局部最优解** 仅考虑当前用户的选择，忽略后续用户可能会带来的影响。因此，它可能导致在某些情况下总资源消耗不一定是最小的，只能保证每一步选择是局部最优的。

## Java

    
    
    import java.util.Scanner;
    
    public class Main{
        public static void main(String[] args) {
            // 创建Scanner对象
            Scanner scanner = new Scanner(System.in);
            // 读取用户个数n
            int n = scanner.nextInt();
            // 创建n行3列的二维数组cost，用于存储每个用户使用三个策略的系统消耗resA resB resC
            int[][] cost = new int[n][3];
            // 读取每个用户使用三个策略的系统消耗resA resB resC
            for (int i = 0; i < n; i++) {
                cost[i][0] = scanner.nextInt();
                cost[i][1] = scanner.nextInt();
                cost[i][2] = scanner.nextInt();
            }
            // 调用findMinTotalCost方法，计算最优策略组合下的总的系统资源消耗数
            int result = findMinTotalCost(cost);
            // 输出最优策略组合下的总的系统资源消耗数
            System.out.println(result);
        }
    
        // 计算最优策略组合下的总的系统资源消耗数
        public static int findMinTotalCost(int[][] cost) {
            // 初始化最小总消耗为整数最大值
            int minTotalCost = Integer.MAX_VALUE;
            // 枚举第一个用户使用的调度策略
            for (int i = 0; i < 3; i++) {
                // 从第一个用户开始递归调用dfs方法，计算从第一个用户开始到最后一个用户结束的最小总消耗
                minTotalCost = Math.min(minTotalCost, dfs(cost, 0, i, 0));
            }
            // 返回最小总消耗
            return minTotalCost;
        }
    
        // 从第level个用户开始，枚举第level个用户使用的调度策略index，计算从第level个用户开始到最后一个用户结束的最小总消耗
        public static int dfs(int[][] cost, int level, int index, int totalCost) {
            // 如果已经遍历到最后一个用户，则返回当前总消耗
            if (level == cost.length) {
                return totalCost;
            }
            // 获取第level个用户使用三个策略的系统消耗resA resB resC
            int[] r = cost[level];
            // 初始化最小消耗为整数最大值
            int minCost = Integer.MAX_VALUE;
            // 枚举第level+1个用户使用的调度策略，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
            for (int i = 0; i < r.length; i++) {
                // 如果第level+1个用户使用的调度策略不等于第level个用户使用的调度策略，则递归调用dfs方法，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
                if (i != index) {
                    minCost = Math.min(minCost, dfs(cost, level + 1, i, totalCost + r[i]));
                }
            }
            // 返回从第level个用户开始到最后一个用户结束的最小总消耗
            return minCost;
        }
    }
    
    

## Python

    
    
    
    
    # 计算最优策略组合下的总的系统资源消耗数
    def findMinTotalCost(cost):
        # 初始化最小总消耗为整数最大值
        minTotalCost = float("inf")
        # 枚举第一个用户使用的调度策略
        for i in range(3):
            # 从第一个用户开始递归调用dfs方法，计算从第一个用户开始到最后一个用户结束的最小总消耗
            minTotalCost = min(minTotalCost, dfs(cost, 0, i, 0))
        # 返回最小总消耗
        return minTotalCost
    
    # 从第level个用户开始，枚举第level个用户使用的调度策略index，计算从第level个用户开始到最后一个用户结束的最小总消耗
    def dfs(cost, level, index, totalCost):
        # 如果已经遍历到最后一个用户，则返回当前总消耗
        if level == len(cost):
            return totalCost
        # 获取第level个用户使用三个策略的系统消耗resA resB resC
        r = cost[level]
        # 初始化最小消耗为整数最大值
        minCost = float("inf")
        # 枚举第level+1个用户使用的调度策略，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
        for i in range(len(r)):
            # 如果第level+1个用户使用的调度策略不等于第level个用户使用的调度策略，则递归调用dfs方法，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
            if i != index:
                minCost = min(minCost, dfs(cost, level + 1, i, totalCost + r[i]))
        # 返回从第level个用户开始到最后一个用户结束的最小总消耗
        return minCost
    n = int( input())
    # 创建n行3列的二维数组cost，用于存储每个用户使用三个策略的系统消耗resA resB resC
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    # 调用findMinTotalCost方法，计算最优策略组合下的总的系统资源消耗数
    result = findMinTotalCost(cost)
    # 输出最优策略组合下的总的系统资源消耗数
    print(result)
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    let n = 0;
    let cost = [];
    
    rl.on('line', (input) => {
      if (n === 0) {
        n = parseInt(input);
      } else {
        const arr = input.split(' ').map(Number);
        cost.push(arr);
        if (cost.length === n) {
          const result = findMinTotalCost(cost);
          console.log(result);
          rl.close();
        }
      }
    });
    
    // 计算最优策略组合下的总的系统资源消耗数
    function findMinTotalCost(cost) {
      // 初始化最小总消耗为整数最大值
      let minTotalCost = Number.MAX_SAFE_INTEGER;
      // 枚举第一个用户使用的调度策略
      for (let i = 0; i < 3; i++) {
        // 从第一个用户开始递归调用dfs方法，计算从第一个用户开始到最后一个用户结束的最小总消耗
        minTotalCost = Math.min(minTotalCost, dfs(cost, 0, i, 0));
      }
      // 返回最小总消耗
      return minTotalCost;
    }
    
    // 从第level个用户开始，枚举第level个用户使用的调度策略index，计算从第level个用户开始到最后一个用户结束的最小总消耗
    function dfs(cost, level, index, totalCost) {
      // 如果已经遍历到最后一个用户，则返回当前总消耗
      if (level === cost.length) {
        return totalCost;
      }
      // 获取第level个用户使用三个策略的系统消耗resA resB resC
      const r = cost[level];
      // 初始化最小消耗为整数最大值
      let minCost = Number.MAX_SAFE_INTEGER;
      // 枚举第level+1个用户使用的调度策略，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
      for (let i = 0; i < r.length; i++) {
        // 如果第level+1个用户使用的调度策略不等于第level个用户使用的调度策略，则递归调用dfs方法，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
        if (i !== index) {
          minCost = Math.min(minCost, dfs(cost, level + 1, i, totalCost + r[i]));
        }
      }
      // 返回从第level个用户开始到最后一个用户结束的最小总消耗
      return minCost;
    }
    
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <climits>
    #include <algorithm>
    using namespace std;
    
    int findMinTotalCost(vector<vector<int>>& cost);
    int dfs(vector<vector<int>>& cost, int level, int index, int totalCost);
    
    int main() {
        // 创建输入流对象
        istream& input = cin;
        // 读取用户个数n
        int n;
        input >> n;
        // 创建n行3列的二维数组cost，用于存储每个用户使用三个策略的系统消耗resA resB resC
        vector<vector<int>> cost(n, vector<int>(3));
        // 读取每个用户使用三个策略的系统消耗resA resB resC
        for (int i = 0; i < n; i++) {
            input >> cost[i][0] >> cost[i][1] >> cost[i][2];
        }
        // 调用findMinTotalCost方法，计算最优策略组合下的总的系统资源消耗数
        int result = findMinTotalCost(cost);
        // 输出最优策略组合下的总的系统资源消耗数
        cout << result << endl;
        return 0;
    }
    
    // 计算最优策略组合下的总的系统资源消耗数
    int findMinTotalCost(vector<vector<int>>& cost) {
        // 初始化最小总消耗为整数最大值
        int minTotalCost = INT_MAX;
        // 枚举第一个用户使用的调度策略
        for (int i = 0; i < 3; i++) {
            // 从第一个用户开始递归调用dfs方法，计算从第一个用户开始到最后一个用户结束的最小总消耗
            minTotalCost = min(minTotalCost, dfs(cost, 0, i, 0));
        }
        // 返回最小总消耗
        return minTotalCost;
    }
    
    // 从第level个用户开始，枚举第level个用户使用的调度策略index，计算从第level个用户开始到最后一个用户结束的最小总消耗
    int dfs(vector<vector<int>>& cost, int level, int index, int totalCost) {
        // 如果已经遍历到最后一个用户，则返回当前总消耗
        if (level == cost.size()) {
            return totalCost;
        }
        // 获取第level个用户使用三个策略的系统消耗resA resB resC
        vector<int>& r = cost[level];
        // 初始化最小消耗为整数最大值
        int minCost = INT_MAX;
        // 枚举第level+1个用户使用的调度策略，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
        for (int i = 0; i < r.size(); i++) {
            // 如果第level+1个用户使用的调度策略不等于第level个用户使用的调度策略，则递归调用dfs方法，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
            if (i != index) {
                minCost = min(minCost, dfs(cost, level + 1, i, totalCost + r[i]));
            }
        }
        // 返回从第level个用户开始到最后一个用户结束的最小总消耗
        return minCost;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <limits.h>
    
    #define MAX_USERS 1000  // 假设最多有 1000 个用户
    
    // 函数声明
    int findMinTotalCost(int cost[MAX_USERS][3], int n);
    int dfs(int cost[MAX_USERS][3], int level, int index, int totalCost, int n);
    
    int main() {
        int n;
        // 读取用户个数n
        scanf("%d", &n);
    
        // 创建二维数组cost，用于存储每个用户使用三个策略的系统消耗resA, resB, resC
        int cost[MAX_USERS][3];
        
        // 读取每个用户使用三个策略的系统消耗resA, resB, resC
        for (int i = 0; i < n; i++) {
            scanf("%d %d %d", &cost[i][0], &cost[i][1], &cost[i][2]);
        }
    
        // 调用findMinTotalCost方法，计算最优策略组合下的总的系统资源消耗数
        int result = findMinTotalCost(cost, n);
    
        // 输出最优策略组合下的总的系统资源消耗数
        printf("%d\n", result);
    
        return 0;
    }
    
    // 计算最优策略组合下的总的系统资源消耗数
    int findMinTotalCost(int cost[MAX_USERS][3], int n) {
        // 初始化最小总消耗为整数最大值
        int minTotalCost = INT_MAX;
    
        // 枚举第一个用户使用的调度策略
        for (int i = 0; i < 3; i++) {
            // 从第一个用户开始递归调用dfs方法，计算从第一个用户开始到最后一个用户结束的最小总消耗
            minTotalCost = (minTotalCost < dfs(cost, 0, i, 0, n)) ? minTotalCost : dfs(cost, 0, i, 0, n);
        }
    
        // 返回最小总消耗
        return minTotalCost;
    }
    
    // 从第level个用户开始，枚举第level个用户使用的调度策略index，计算从第level个用户开始到最后一个用户结束的最小总消耗
    int dfs(int cost[MAX_USERS][3], int level, int index, int totalCost, int n) {
        // 如果已经遍历到最后一个用户，则返回当前总消耗
        if (level == n) {
            return totalCost;
        }
    
        // 获取第level个用户使用三个策略的系统消耗resA, resB, resC
        int* r = cost[level];
    
        // 初始化最小消耗为整数最大值
        int minCost = INT_MAX;
    
        // 枚举第level+1个用户使用的调度策略，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
        for (int i = 0; i < 3; i++) {
            // 如果第level+1个用户使用的调度策略不等于第level个用户使用的调度策略，则递归调用dfs方法，计算从第level+1个用户开始到最后一个用户结束的最小总消耗
            if (i != index) {
                minCost = (minCost < dfs(cost, level + 1, i, totalCost + r[i], n)) ? minCost : dfs(cost, level + 1, i, totalCost + r[i], n);
            }
        }
    
        // 返回从第level个用户开始到最后一个用户结束的最小总消耗
        return minCost;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    3
    15 8 17
    12 20 9
    11 7 5
    

### 用例2

    
    
    4  
    10 15 20
    8 12 10
    9 7 6
    5 6 7
    

### 用例3

    
    
    2
    7 8 9
    6 10 5
    

### 用例4

    
    
    5
    5 10 15
    8 9 6
    7 12 11
    10 6 9
    9 7 10
    

### 用例5

    
    
    3
    20 15 10
    8 9 6
    12 11 10
    

### 用例6

    
    
    6
    5 6 7
    8 5 9
    6 8 10
    5 4 7
    8 6 5
    9 7 6
    

### 用例7

    
    
    4
    15 10 20
    9 11 7
    6 8 5
    10 12 11
    

### 用例8

    
    
    3
    8 9 7
    6 7 5
    5 6 4
    

### 用例9

    
    
    5
    9 8 7
    6 7 8
    5 6 7
    8 7 6
    7 6 5
    

### 用例10

    
    
    3
    20 15 10
    9 11 12
    10 8 6
    

