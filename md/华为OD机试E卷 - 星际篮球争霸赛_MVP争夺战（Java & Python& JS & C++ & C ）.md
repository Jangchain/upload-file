## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

在星球争霸篮球赛对抗赛中，最大的宇宙战队希望每个人都能拿到 MVP，MVP 的条件是单场最高分得分获得者。

可以并列所以宇宙战队决定在比赛中尽可能让更多队员上场，并且让所有得分的选手得分都相同，然而比赛过程中的每一分钟的得分都只能由某一个人包揽。

​

## 输入描述

输入第一行为一个数字 t ，表示为有得分的分钟数

  * 1 ≤ t ≤ 50

第二行为 t 个数字，代表每一分钟的得分 p

  * 1 ≤ p ≤ 50

## 输出描述

输出有得分的队员都是 MVP 时，最少得 MVP 得分。

## 示例1

输入

    
    
    9
    5 2 1 5 2 1 5 2 1
    

输出

    
    
    6
    

说明

>
>     一共 4 人得分，分别都是 6 分
>      5 + 1 ， 5 + 1 ， 5 + 1 ， 2 + 2 + 2
>  

## 解题思路

本题是可以归纳到：将数组划分为k个和相等的子集

可以在lettcode找到最原始的问题：698. 划分为k个相等的子集 - 力扣（LeetCode）

### 分析

首先第一个目标，将数组拆分，每个子数组的和相等。

比如[2,2,4] 拆分为[2,2] [4]

然后在所有的可能拆分条件下，子数组的和最小。

比如 [1,1,1,1] 可以拆分为[1] [1] [1] [1] 或 [1,1] [1,1]

明显最小的子数组元素之和是1.

## Java

    
    
    import java.util.Scanner;
    import java.util.Arrays;
    
    public class Main {
        public static void main(String[] args) {
            // 输入处理：读取元素个数和元素值，计算总和
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[] nums = new int[n];
            int sum = 0; // 保存所有元素的总和
            for (int i = 0; i < n; i++) {
                nums[i] = sc.nextInt();
                sum += nums[i];
            }
    
            // 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等
            for (int k = n; k > 0; k--) {
                // 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
                if (sum % k != 0) continue;
    
                int perSum = sum / k; // 每个子集的目标和
    
                // 对数组排序，确保较大元素在前，有助于提前剪枝
                Arrays.sort(nums);
    
                // 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
                if (nums[n - 1] > perSum) continue;
    
                // 使用动态规划判断是否可以分成 k 个子集
                int subsetCount = nums.length;
                boolean[] dp = new boolean[1 << subsetCount];  // dp[i] 表示是否能构成下标 i 的子集
                int[] curSum = new int[1 << subsetCount];      // curSum[i] 记录下标 i 对应的当前子集和
                dp[0] = true; // 初始化空集状态
    
                for (int i = 0; i < (1 << subsetCount); i++) {
                    if (!dp[i]) continue; // 如果当前子集状态不可行，跳过
                    for (int j = 0; j < subsetCount; j++) {
                        if ((i >> j & 1) != 0) continue; // 如果 nums[j] 已经在当前子集中使用，跳过
    
                        // 如果将 nums[j] 加入子集后超出目标和，跳过
                        if (curSum[i] + nums[j] > perSum) break;
    
                        int next = i | (1 << j); // 将 nums[j] 加入新的子集中
                        if (!dp[next]) {
                            curSum[next] = (curSum[i] + nums[j]) % perSum; // 更新新子集的和
                            dp[next] = true; // 标记新子集状态为可行
                        }
                    }
                }
    
                // 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
                if (dp[(1 << subsetCount) - 1]) {
                    System.out.println(perSum); // 输出每个子集的和
                    break;
                }
            }
    
            sc.close();
        }
    }
    

## Python

    
    
    # 输入处理：读取元素个数和元素值，计算总和
    n = int(input())  # 读取元素个数
    nums = list(map(int, input().split()))  # 读取所有元素并转换为整数列表
    sum_nums = sum(nums)  # 计算所有元素的总和
    
    # 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等
    for k in range(n, 0, -1):
        # 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
        if sum_nums % k != 0:
            continue
    
        per_sum = sum_nums // k  # 每个子集的目标和
    
        # 对数组排序，确保较大元素在前，有助于提前剪枝
        nums.sort()
    
        # 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
        if nums[-1] > per_sum:
            continue
    
        # 使用动态规划判断是否可以分成 k 个子集
        subset_count = len(nums)
        dp = [False] * (1 << subset_count)  # dp[i] 表示是否能构成下标 i 的子集
        cur_sum = [0] * (1 << subset_count)  # cur_sum[i] 记录下标 i 对应的当前子集和
        dp[0] = True  # 初始化空集状态
    
        for i in range(1 << subset_count):
            if not dp[i]:
                continue  # 如果当前子集状态不可行，跳过
            for j in range(subset_count):
                if (i >> j) & 1:
                    continue  # 如果 nums[j] 已经在当前子集中使用，跳过
    
                # 如果将 nums[j] 加入子集后超出目标和，跳过
                if cur_sum[i] + nums[j] > per_sum:
                    break
    
                next_subset = i | (1 << j)  # 将 nums[j] 加入新的子集中
                if not dp[next_subset]:
                    cur_sum[next_subset] = (cur_sum[i] + nums[j]) % per_sum  # 更新新子集的和
                    dp[next_subset] = True  # 标记新子集状态为可行
    
        # 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
        if dp[(1 << subset_count) - 1]:
            print(per_sum)  # 输出每个子集的和
            break
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    // 输入处理：读取元素个数和元素值，计算总和
    rl.on('line', (n) => {
        rl.on('line', (input) => {
            let nums = input.split(' ').map(Number);  // 将输入的元素转为整数数组
            let sum = nums.reduce((a, b) => a + b, 0);  // 计算数组元素总和
    
            // 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等
            for (let k = n; k > 0; k--) {
                // 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
                if (sum % k !== 0) continue;
    
                let perSum = Math.floor(sum / k);  // 每个子集的目标和
    
                // 对数组排序，确保较大元素在前，有助于提前剪枝
                nums.sort((a, b) => a - b);
    
                // 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
                if (nums[nums.length - 1] > perSum) continue;
    
                // 使用动态规划判断是否可以分成 k 个子集
                let subsetCount = nums.length;
                let dp = new Array(1 << subsetCount).fill(false);  // dp[i] 表示是否能构成下标 i 的子集
                let curSum = new Array(1 << subsetCount).fill(0);  // curSum[i] 记录下标 i 对应的当前子集和
                dp[0] = true;  // 初始化空集状态
    
                for (let i = 0; i < (1 << subsetCount); i++) {
                    if (!dp[i]) continue;  // 如果当前子集状态不可行，跳过
                    for (let j = 0; j < subsetCount; j++) {
                        if ((i >> j) & 1) continue;  // 如果 nums[j] 已经在当前子集中使用，跳过
    
                        // 如果将 nums[j] 加入子集后超出目标和，跳过
                        if (curSum[i] + nums[j] > perSum) break;
    
                        let next = i | (1 << j);  // 将 nums[j] 加入新的子集中
                        if (!dp[next]) {
                            curSum[next] = (curSum[i] + nums[j]) % perSum;  // 更新新子集的和
                            dp[next] = true;  // 标记新子集状态为可行
                        }
                    }
                }
    
                // 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
                if (dp[(1 << subsetCount) - 1]) {
                    console.log(perSum);  // 输出每个子集的和
                    break;
                }
            }
    
            rl.close();
        });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main()
    {
        /* 输入处理：读取元素个数和元素值，计算总和 */
        int n;
        cin >> n;
        vector<int> nums;
        int sum = 0; // 保存所有元素的总和
        for (int i = 0; i < n; i++)
        {
            int num;
            cin >> num;
            sum += num;
            nums.push_back(num);
        }
    
        /* 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等 */
        for (int k = n; k > 0; k--)
        {
            // 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
            if (sum % k != 0) continue;
    
            int perSum = sum / k; // 每个子集的目标和
    
            // 对数组排序，确保较大元素在前，有助于提前剪枝
            sort(nums.begin(), nums.end());
    
            // 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
            if (nums.back() > perSum) continue;
    
            /* 使用动态规划判断是否可以分成 k 个子集 */
            int subsetCount = nums.size();
            vector<bool> dp(1 << subsetCount, false);  // dp[i] 表示是否能构成下标集合为 i 的子集
            vector<int> curSum(1 << subsetCount, 0);   // curSum[i] 记录下标集合 i 对应的当前子集和
            dp[0] = true; // 初始化空集状态
    
            for (int i = 0; i < (1 << subsetCount); i++)
            {
                if (!dp[i]) continue; // 如果当前子集状态不可行，跳过
                for (int j = 0; j < subsetCount; j++)
                {
                    if ((i >> j) & 1) continue; // 如果 nums[j] 已经在当前子集中使用，跳过
    
                    // 如果将 nums[j] 加入子集后超出目标和，跳过
                    if (curSum[i] + nums[j] > perSum) break;
    
                    int next = i | (1 << j); // 将 nums[j] 加入新的子集中
                    if (!dp[next])
                    {
                        curSum[next] = (curSum[i] + nums[j]) % perSum; // 更新新子集的和
                        dp[next] = true; // 标记新子集状态为可行
                    }
                }
            }
    
            // 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
            if (dp[(1 << subsetCount) - 1])
            {
                cout << perSum << endl; // 输出每个子集的和
                break;
            }
        }
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <stdbool.h>
    
    // 比较函数，用于排序
    int compare(const void* a, const void* b) {
        return (*(int*)a - *(int*)b);
    }
    
    int main() {
        // 输入处理：读取元素个数和元素值，计算总和
        int n;
        scanf("%d", &n);
        int* nums = (int*)malloc(n * sizeof(int));
        int sum = 0; // 保存所有元素的总和
        for (int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
            sum += nums[i];
        }
    
        // 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等
        for (int k = n; k > 0; k--) {
            // 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
            if (sum % k != 0) continue;
    
            int perSum = sum / k; // 每个子集的目标和
    
            // 对数组排序，确保较大元素在前，有助于提前剪枝
            qsort(nums, n, sizeof(int), compare);
    
            // 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
            if (nums[n - 1] > perSum) continue;
    
            // 使用动态规划判断是否可以分成 k 个子集
            int subsetCount = n;
            bool* dp = (bool*)calloc(1 << subsetCount, sizeof(bool)); // dp[i] 表示是否能构成下标 i 的子集
            int* curSum = (int*)calloc(1 << subsetCount, sizeof(int)); // curSum[i] 记录下标 i 对应的当前子集和
            dp[0] = true; // 初始化空集状态
    
            for (int i = 0; i < (1 << subsetCount); i++) {
                if (!dp[i]) continue; // 如果当前子集状态不可行，跳过
                for (int j = 0; j < subsetCount; j++) {
                    if ((i >> j) & 1) continue; // 如果 nums[j] 已经在当前子集中使用，跳过
    
                    // 如果将 nums[j] 加入子集后超出目标和，跳过
                    if (curSum[i] + nums[j] > perSum) break;
    
                    int next = i | (1 << j); // 将 nums[j] 加入新的子集中
                    if (!dp[next]) {
                        curSum[next] = (curSum[i] + nums[j]) % perSum; // 更新新子集的和
                        dp[next] = true; // 标记新子集状态为可行
                    }
                }
            }
    
            // 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
            if (dp[(1 << subsetCount) - 1]) {
                printf("%d\n", perSum); // 输出每个子集的和
                break;
            }
    
            free(dp);
            free(curSum);
        }
    
        free(nums);
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    9
    5 2 1 5 2 1 5 2 1
    

### 用例2

    
    
    4
    10 10 10 10
    

### 用例3

    
    
    6
    3 3 3 3 6 6
    

### 用例4

    
    
    7
    8 7 1 8 7 1 8
    

### 用例5

    
    
    5
    2 3 4 5 6
    

### 用例6

    
    
    4
    12 8 4 4
    

### 用例7

    
    
    9
    8 8 8 8 4 4 4 4 4
    

### 用例8

    
    
    8
    1 2 3 4 5 6 7 8
    

### 用例9

    
    
    3
    10 15 20
    

### 用例10

    
    
    15
    1 2 1 2 1 2 1 2 1 2 1 2 1 2 1
    

