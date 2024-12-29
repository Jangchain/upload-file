## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

某组织举行会议，来了多个代表团同时到达，接待处只有一辆汽车，可以同时接待多个代表团，为了提高车辆利用率，请帮接待员计算可以坐满车的接待方案，输出方案数量。

约束:

  1. 一个团只能上一辆车，并且代表团人数 (代表团数量小于30，每个代表团人数小于30)小于汽车容量(汽车容量小于100)
  2. 需要将车辆坐满

## 输入描述

第一行 代表团人数，英文逗号隔开，代表团数量小于30，每个代表团人数小于30  
第二行 汽车载客量，汽车容量小于100

## 输出描述

坐满汽车的方案数量  
如果无解输出0

## 示例1

输入

    
    
    5,4,2,3,2,4,9
    10
    

输出

    
    
    4
    

说明

> 解释 以下几种方式都可以坐满车，所以，优先接待输出为4
>
> [2,3,5]
>
> [2,4,4]
>
> [2,3,5]
>
> [2,4,4]

## 解题思路

这道题的核心问题是一个经典的 **背包问题的变体** ，可以将其解释为“用指定人数的代表团正好坐满一辆汽车”的组合计数问题。以下是题意的详细解读：

* * *

### **题目要解决的问题**

  1. 有多个代表团，每个代表团的人数已知。
  2. 有一辆汽车，可以同时接待多个代表团，但汽车的总容量是固定的。
  3. **目标** ：计算有多少种不同的组合方式，可以使汽车的人数正好等于其容量。

* * *

### **约束和规则**

  1. **一个代表团只能上一辆车** ：代表团人数不能被拆分。
  2. **每种组合人数和必须刚好等于汽车容量** ：不能超载或少载。
  3. **代表团人数可以重复使用在不同组合中** ：例如 `[2, 3, 5]` 和 `[5, 3, 2]` 视为同一组合，但计算可能需要考虑到排列去重。

* * *

### **解题思路**

  1. **背包问题的核心思想** ：

     * 使用回溯法或动态规划（DP）找到所有使得和为 `汽车容量` 的组合。
     * 回溯法：遍历所有可能的子集，并检查是否满足条件。
     * 动态规划：通过记录状态来减少重复计算。
  2. **去重策略** ：

     * 可以先对输入的代表团人数排序，这样可以避免重复计算。
     * 排序后，用回溯法生成组合，确保相同组合不会多次计入结果。
  3. **输出结果** ：

     * 如果存在至少一种组合，则输出组合的总数量。
     * 如果没有符合条件的组合，则输出 `0`。

* * *

### **注意点**

  1. **重复代表团人数处理** ：

     * 输入可能包含重复人数，例如 `[2, 2, 3, 4]`。
     * 我们需要小心处理重复，确保每种组合只计入一次。
  2. **特殊情况** ：

     * 如果代表团人数总和小于汽车容量，直接输出 `0`。
     * 如果只有一个代表团人数等于汽车容量，那只有一种方案。

* * *

## Java

    
    
    import java.util.Arrays;
    import java.util.Scanner;
    
    public class Main {
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        // 读取代表团人数
        int[] groups = Arrays.stream(sc.nextLine().split(","))
                            .mapToInt(Integer::parseInt)
                            .toArray();
    
        // 读取汽车载客量
        int capacity =  sc.nextInt();
    
        // 初始化动态规划数组，dp[i]表示载客量为i时的方案数
        int[] dp = new int[capacity + 1];
        dp[0] = 1; // 载客量为0时，方案数为1（不接待任何代表团）
    
        // 代表团人数排序
        Arrays.sort(groups);
    
        // 动态规划转移
        for (int group : groups) {
           int diff = capacity - group; // group和capacity的差值
          for (int j = diff; j >= 0; j--) {
            dp[j + group] += dp[j]; // 转移方程：dp[j + group] += dp[j]，表示加上接待当前代表团后的方案数
          }
        }
    
        // 输出结果
        System.out.println(dp[capacity]);
      }
    }
    

## Python

    
    
    # 读取代表团人数
    groups = list(map(int, input().split(",")))
    
    # 读取汽车载客量
    capacity = int(input())
    
    # 初始化动态规划数组，dp[i]表示载客量为i时的方案数
    dp = [0] * (capacity + 1)
    
    
    dp[0] = 1  # 载客量为0时，方案数为1（不接待任何代表团）
    
    # 代表团人数排序
    groups.sort()
    
    # 动态规划转移
    for group in groups:
        diff = capacity - group  # group和capacity的差值
        for j in range(diff, -1, -1):
            dp[j + group] += dp[j]  # 转移方程：dp[j + group] += dp[j]，表示加上接待当前代表团后的方案数
    
    # 输出结果
    print(dp[capacity])
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on('line', (line1) => {
      const groups = line1.split(',').map(Number);
    
      rl.on('line', (line2) => {
        const capacity = parseInt(line2);
    
        const dp = new Array(capacity + 1).fill(0);
        dp[0] = 1;
    
        groups.sort((a, b) => a - b);
    
        for (const group of groups) {
          const diff = capacity - group;
          for (let j = diff; j >= 0; j--) {
            dp[j + group] += dp[j];
          }
        }
    
        console.log(dp[capacity]);
    
        rl.close();
      });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main() {
        // 读取代表团人数
        string input;
        getline(cin, input);
        vector<int> groups;
        size_t pos = 0;
        while ((pos = input.find(',')) != string::npos) {
            groups.push_back(stoi(input.substr(0, pos)));
            input.erase(0, pos + 1);
        }
        groups.push_back(stoi(input));
    
        // 读取汽车载客量
        int capacity;
        cin >> capacity;
    
        // 初始化动态规划数组，dp[i]表示载客量为i时的方案数
        vector<int> dp(capacity + 1, 0);
        dp[0] = 1; // 载客量为0时，方案数为1（不接待任何代表团）
    
        // 代表团人数排序
        sort(groups.begin(), groups.end());
    
        // 动态规划转移
        for (int group : groups) {
            int diff = capacity - group; // group和capacity的差值
            for (int j = diff; j >= 0; j--) {
                dp[j + group] += dp[j]; // 转移方程：dp[j + group] += dp[j]，表示加上接待当前代表团后的方案数
            }
        }
    
        // 输出结果
        cout << dp[capacity] << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    // 比较函数用于排序
    int cmp(const void *a, const void *b) {
        return (*(int *)a - *(int *)b);
    }
    
    int main() {
        char input[1024];  
        int capacity;
    
        // 读取代表团人数
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; // 去掉换行符
    
        // 将代表团人数解析为数组
        int groups[100];  
        int groupCount = 0;
        char *token = strtok(input, ",");
        while (token != NULL) {
            groups[groupCount++] = atoi(token);
            token = strtok(NULL, ",");
        }
    
        // 读取汽车载客量
        scanf("%d", &capacity);
    
        // 动态分配动态规划数组，dp[i]表示载客量为i时的方案数
        int *dp = (int *)calloc(capacity + 1, sizeof(int));
        if (dp == NULL) {
            printf("内存分配失败\n");
            return 1;
        }
    
        dp[0] = 1; // 载客量为0时，方案数为1
    
        // 对代表团人数进行排序
        qsort(groups, groupCount, sizeof(int), cmp);
    
        // 动态规划转移
        for (int i = 0; i < groupCount; i++) {
            int group = groups[i];
            for (int j = capacity - group; j >= 0; j--) {
                dp[j + group] += dp[j]; // 转移方程
            }
        }
    
        // 输出结果
        printf("%d\n", dp[capacity]);
    
        // 释放动态分配的内存
        free(dp);
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    5,4,2,3,2,4,9
    10
    

### 用例2

    
    
    1,1,1,1,1,1,1
    5
    

### 用例3

    
    
    10,10,10,10,10,10
    100
    

### 用例4

    
    
    2,3,4,5,6
    12
    

### 用例5

    
    
    1,2,3,4,5,6,7
    10
    

### 用例6

    
    
    10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10
    100
    

### 用例7

    
    
    5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    50
    

### 用例8

    
    
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
    30
    

### 用例9

    
    
    5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150
    150
    

### 用例10

    
    
    2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
    50
    

