## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小明在学习二进制时，发现了一类不含 101的数，也就是：

将数字用二进制表示，不能出现 101 。  
现在给定一个整数区间 [l,r] ，请问这个区间包含了多少个不含 101 的数？

## 输入描述

输入的唯一一行包含两个正整数 l， r（ 1 ≤ l ≤ r ≤ 10^9）。

## 输出描述

输出的唯一一行包含一个整数，表示在 [l,r] 区间内一共有几个不含 101 的数。

## 示例1

输入

    
    
    1 10
    

输出

    
    
    8
    

说明

> 区间 [1,10] 内， 5 的二进制表示为 101 ，10的二进制表示为 1010 ，因此区间 [ 1 , 10 ] 内有 10−2=8 个不含
> 101的数。

## 示例2

输入

    
    
    10 20
    

输出

    
    
    7
    

说明

> 区间 [10,20] 内，满足条件的数字有 [12,14,15,16,17,18,19] 因此答案为 7。

## 解题思路

本题乍看是很简单的题目，直接进制转换，暴力法不就得了。但是你注意看范围是【1 ≤ l ≤ r ≤ 10^9】，暴力肯定会超时。这题使用的是数位DP

[数位dp总结 之 从入门到模板_wust_wenhao的博客-
CSDN博客](https://blog.csdn.net/wust_zzwh/article/details/52100392)

具体思路是从高位到低位逐位枚举，对于每一位，枚举它的取值，并根据前一位和前两位的值来判断是否符合条件。同时，使用记忆化数组来避免重复计算。

具体实现中，可以将数字转换为二进制数，然后递归处理每一位。递归函数中，p表示当前处理到的二进制位，limit表示当前位是否受到上限制，f表示记忆化数组，arr表示二进制数，pre表示前一位的值，prepre表示前两位的值。递归结束条件是处理完所有二进制位，此时返回1。在递归过程中，统计符合条件的数的个数，并使用记忆化数组避免重复计算。

## Java

    
    
    import java.util.*;
    
    public class Main {
    
        public static int dp(int num) {
            // 将数字转换为二进制数组
            List<Integer> binaryNums = new ArrayList<>();
            while (num > 0) {
                binaryNums.add(num % 2);  // 将最低位加入列表
                num /= 2;                 // 去掉最低位
            }
            Collections.reverse(binaryNums); // 反转数组，使二进制位从高位到低位排列
    
            // 初始化记忆化数组 binaryDp，用于存储已计算过的状态结果，避免重复计算
            int[][][] binaryDp = new int[binaryNums.size()][2][2];
    
            // 调用递归搜索函数开始计算
            return search(0, true, binaryDp, binaryNums, 0, 0);
        }
    
        public static int search(int p, boolean flag, int[][][] binaryDp, List<Integer> binaryNums, int pre, int prepre) {
            // 边界条件：如果已经处理完所有二进制位，返回 1，表示找到一个符合条件的数
            if (p == binaryNums.size()) {
                return 1;
            }
    
            // 如果当前状态已经计算过且没有上界限制，直接返回保存的结果
            if (!flag && binaryDp[p][pre][prepre] != 0) {
                return binaryDp[p][pre][prepre];
            }
    
            // 当前位的最大值。如果受上界限制，则取 binaryNums[p]；否则为 1
            int index = flag ? binaryNums.get(p) : 1;
            int count = 0;  // 记录符合条件的数的个数
    
            // 枚举当前位可能的值（0 或 1）
            for (int i = 0; i <= index; i++) {
                // 如果当前位的组合形成 "101" 模式（即 prepre=1, pre=0, 当前位 i=1），则跳过该情况
                if (i == 1 && pre == 0 && prepre == 1) {
                    continue;
                }
                // 递归处理下一位，更新 pre 和 prepre
                count += search(p + 1, flag && i == index, binaryDp, binaryNums, i, pre);
            }
    
            // 如果不受上界限制，将结果保存在记忆化数组 binaryDp 中
            if (!flag) {
                binaryDp[p][pre][prepre] = count;
            }
    
            return count;
        }
    
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int left = scanner.nextInt();  // 读取左边界
            int right = scanner.nextInt(); // 读取右边界
            scanner.close();
    
            // 计算区间 [left, right] 内不包含 "101" 模式的数的个数
            int result = dp(right) - dp(left - 1);
            System.out.println(result);
        }
    }
    

## Python

    
    
    def dp(num):
        # 将数字转化为二进制数组，bin(num)[2:] 将数字 num 转为二进制字符串并去掉 '0b' 前缀
        binaryNums = list(map(int, bin(num)[2:]))
        
        # 初始化记忆化数组 binaryDp，用来存储每个状态的计算结果，防止重复计算
        # binaryDp[p][pre][prepre] 表示在第 p 位，前一位 pre 和前两位 prepre 的状态下的结果
        # 其中 pre 和 prepre 的值为 0 或 1（即二进制数的一位），所以数组大小是 len(binaryNums) x 2 x 2
        binaryDp = [[[0] * 2 for _ in range(2)] for _ in range(len(binaryNums))]
    
        # 调用搜索函数，开始递归处理
        return search(0, True, binaryDp, binaryNums, 0, 0)
    
    def search(p, flag, binaryDp, binaryNums, pre, prepre):
        # 边界条件：如果已经处理完所有二进制位，返回 1，表示找到一个符合条件的数
        if p == len(binaryNums):
            return 1
    
        # 如果当前状态已经计算过，且没有上界限制，直接返回保存的结果
        if not flag and binaryDp[p][pre][prepre] != 0:
            return binaryDp[p][pre][prepre]
    
        # 当前位的最大值，flag 为 True 时，当前位的最大值为 binaryNums[p]；否则最大值为 1
        index = binaryNums[p] if flag else 1
        count = 0  # 用于计数符合条件的数的个数
    
        # 枚举当前位 i 的值，i 只能取 0 或 1
        for i in range(index + 1):
            # 如果当前位组成了 "101" 模式（即 prepre=1, pre=0, 当前位 i=1），跳过该情况
            if i == 1 and pre == 0 and prepre == 1:
                continue
            # 递归处理下一位，更新 pre 和 prepre，继续搜索下一个位
            count += search(p + 1, flag and i == index, binaryDp, binaryNums, i, pre)
    
        # 如果没有上界限制，则将结果保存在记忆化数组 binaryDp 中
        if not flag:
            binaryDp[p][pre][prepre] = count
    
        return count
    
    # 主函数部分
    left, right = map(int, input().split())  # 输入区间 [left, right]
    # 计算区间 [left, right] 内不包含 "101" 模式的数的个数
    print(dp(right) - dp(left - 1))
    

## JavaScript

    
    
    function dp(num) {
        // 将数字转化为二进制数组
        let binaryNums = [];
        while (num > 0) {
            // 将当前数字的最低位添加到 binaryNums 数组
            binaryNums.push(num % 2);
            // 右移一位，即除以 2 并取整
            num = Math.floor(num / 2);
        }
        // 因为上面的过程是从低位到高位，所以需要反转数组
        binaryNums.reverse();  
    
        // 初始化记忆化数组 binaryDp，用来记录中间结果，避免重复计算
        // binaryDp 的尺寸是 [binaryNums.length][2][2]，表示二进制位数 × 2 × 2
        // 用来表示前两位的值（pre 和 prepre）以及当前位的最大值约束
        let binaryDp = Array.from({ length: binaryNums.length }, () =>
            Array.from({ length: 2 }, () => Array(2).fill(0)) // 预填充为 0
        );
    
        // 调用 search 函数，开始递归搜索符合条件的数字
        return search(0, true, binaryDp, binaryNums, 0, 0);
    }
    
    function search(p, flag, binaryDp, binaryNums, pre, prepre) {
        // 边界条件：当所有二进制位都处理完时（p 等于二进制数位数），返回 1，表示找到一个符合条件的数
        if (p === binaryNums.length) {
            return 1;
        }
    
        // 如果当前状态已经计算过且没有上界限制，直接返回已经保存的结果，避免重复计算
        if (!flag && binaryDp[p][pre][prepre] !== 0) {
            return binaryDp[p][pre][prepre];
        }
    
        // 当前位的最大值
        // 如果 flag 为 true，当前位的值由二进制数组 binaryNums[p] 决定；否则，当前位最大为 1
        let index = flag ? binaryNums[p] : 1;
        let count = 0;  // 用于累加符合条件的数的个数
    
        // 枚举当前位的所有可能值（0 或 1）
        for (let i = 0; i <= index; i++) {
            // 如果出现 "101" 模式（即 prepre=1，pre=0，当前位 i=1），跳过该情况
            if (i === 1 && pre === 0 && prepre === 1) {
                continue;
            }
            // 递归调用 search，处理下一位，并累加符合条件的数的个数
            count += search(p + 1, flag && i === index, binaryDp, binaryNums, i, pre);
        }
    
        // 如果当前状态不再受到上界约束，保存当前计算结果到记忆化数组 binaryDp
        if (!flag) {
            binaryDp[p][pre][prepre] = count;
        }
    
        // 返回符合条件的数的个数
        return count;
    }
    
    // 使用 readline 模块来读取输入
    const readline = require('readline');
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    // 处理输入的每一行
    rl.on('line', (input) => {
      // 将输入的区间 [left, right] 转换为数字
      const [left, right] = input.split(' ').map(Number);
    
      // 计算区间 [left, right] 内不包含 "101" 模式的数的个数
      const count = dp(right) - dp(left - 1);
    
      // 输出计算结果
      console.log(count);
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    
    using namespace std;
    
    // 递归搜索函数，返回符合条件的数的个数
    // 参数说明：
    // - p：当前处理的二进制位位置
    // - flag：标记当前是否受上界限制
    // - binaryDp：记忆化数组，存储中间计算结果避免重复计算
    // - binaryNums：表示输入数字的二进制位数组
    // - pre：前一位的值
    // - prepre：前两位的值
    int search(int p, bool flag, vector<vector<vector<int>>>& binaryDp, const vector<int>& binaryNums, int pre, int prepre) {
        // 边界条件：当所有位都处理完时（即 p 等于二进制数位数），返回 1，表示找到一个符合条件的数
        if (p == binaryNums.size()) {
            return 1;
        }
    
        // 如果当前状态已经计算过，且没有上限限制，则直接返回保存的结果，避免重复计算
        if (!flag && binaryDp[p][pre][prepre] != 0) {
            return binaryDp[p][pre][prepre];
        }
    
        // 确定当前位可以取的最大值
        // 若 flag 为 true，当前位最大值为 binaryNums[p]，否则最大值为 1（因为不受上界约束）
        int index = flag ? binaryNums[p] : 1;
        int count = 0;  // 用于累加符合条件的数的个数
    
        // 枚举当前位的所有可能值（0 和 1）
        for (int i = 0; i <= index; i++) {
            // 若出现 "101" 模式（即 prepre=1，pre=0，当前位 i=1），跳过该情况
            if (i == 1 && pre == 0 && prepre == 1) {
                continue;
            }
            // 递归调用 search，处理下一位，并累加符合条件的数的个数
            count += search(p + 1, flag && i == index, binaryDp, binaryNums, i, pre);
        }
    
        // 如果当前状态不受上界限制，记录计算结果到记忆化数组 binaryDp，以便后续直接使用
        if (!flag) {
            binaryDp[p][pre][prepre] = count;
        }
    
        // 返回符合条件的数的个数
        return count;
    }
    
    // dp 函数，计算从 1 到 num 范围内不包含 "101" 二进制模式的数的个数
    int dp(int num) {
        // 将数字 num 转换为二进制表示并存入数组 binaryNums
        vector<int> binaryNums;
        while (num > 0) {
            binaryNums.push_back(num % 2);  // 取 num 的最低位
            num /= 2;  // 去掉最低位
        }
        // 由于结果是从低位到高位依次存入 binaryNums，因此需要将数组反转，以便从高位开始处理
        reverse(binaryNums.begin(), binaryNums.end());
    
        // 初始化记忆化数组 binaryDp，大小为二进制数位数 × 2 × 2，用于记录计算结果
        vector<vector<vector<int>>> binaryDp(binaryNums.size(), vector<vector<int>>(2, vector<int>(2, 0)));
    
        // 调用递归搜索函数 search，从第 0 位开始搜索，初始 flag 为 true，pre 和 prepre 为 0
        return search(0, true, binaryDp, binaryNums, 0, 0);
    }
    
    int main() {
        int left, right;
        // 读取输入区间 [left, right]
        cin >> left >> right;
    
        // 计算区间 [left, right] 内不包含 "101" 模式的数的个数
        // 结果为 dp(right) - dp(left - 1)，即右区间的符合数减去左区间前一位的符合数
        int result = dp(right) - dp(left - 1);
        cout << result << endl;  // 输出结果
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    // dp 函数，用于计算从 1 到 num 范围内不包含 "101" 二进制模式的数的个数
    int dp(int num) {
        // 将数字 num 转换为二进制存入数组 binaryNums
        int binaryNums[32];  // binaryNums 用于保存 num 的二进制表示，最多 32 位
        int binarySize = 0;  // binarySize 用于记录二进制数的位数
    
        // 将 num 转换为二进制，结果存入 binaryNums 数组
        while (num > 0) {
            binaryNums[binarySize++] = num % 2;  // 取 num 的最低位
            num /= 2;  // 去掉最低位
        }
    
        // 由于是从低位到高位依次添加到 binaryNums 中，因此需要反转数组
        for (int i = 0; i < binarySize / 2; i++) {
            int temp = binaryNums[i];
            binaryNums[i] = binaryNums[binarySize - 1 - i];
            binaryNums[binarySize - 1 - i] = temp;
        }
    
        // 初始化记忆化数组 binaryDp，用于存储中间结果
        // binaryDp[p][pre][prepre] 表示从第 p 位开始，前一位为 pre，前两位为 prepre 的状态下，不含 "101" 的个数
        int binaryDp[32][2][2];
        memset(binaryDp, 0, sizeof(binaryDp));  // 将所有位置初始化为 0
    
        // 调用递归搜索函数 search，从第 0 位开始搜索，初始 flag 为 1，pre 和 prepre 为 0
        return search(0, 1, binaryDp, binaryNums, binarySize, 0, 0);
    }
    
    // search 函数，用于递归搜索符合条件的二进制数
    // p：当前处理的位
    // flag：是否受上界限制
    // binaryDp：记忆化数组，存储中间结果以便重复使用
    // binaryNums：num 的二进制表示数组
    // binarySize：二进制位数
    // pre：前一位的值
    // prepre：前两位的值
    int search(int p, int flag, int binaryDp[32][2][2], int binaryNums[32], int binarySize, int pre, int prepre) {
        // 当处理到最高位时（p 等于 binarySize），说明已找到符合条件的数，返回 1
        if (p == binarySize) {
            return 1;
        }
    
        // 如果当前状态已经计算过且没有上限限制，直接返回存储的结果
        if (!flag && binaryDp[p][pre][prepre] != 0) {
            return binaryDp[p][pre][prepre];
        }
    
        // 根据 flag 确定当前位的取值范围
        // 如果 flag 为 1，当前位最大可取 binaryNums[p]；否则最大可取 1
        int index = flag ? binaryNums[p] : 1;
        int count = 0;  // 用于计数符合条件的数的个数
    
        // 枚举当前位可能的取值（0 或 1）
        for (int i = 0; i <= index; i++) {
            // 若出现 "101" 模式（即 prepre=1，pre=0，i=1），跳过该情况
            if (i == 1 && pre == 0 && prepre == 1) {
                continue;
            }
    
            // 递归调用 search 计算下一位，并累加符合条件的计数
            // flag && i == index 表示当前位受上界限制且取到最大值时，下一位的 flag 保持为 1
            count += search(p + 1, flag && i == index, binaryDp, binaryNums, binarySize, i, pre);
        }
    
        // 如果不受上限约束（flag 为 0），将结果存入记忆化数组 binaryDp
        if (!flag) {
            binaryDp[p][pre][prepre] = count;
        }
    
        return count;  // 返回符合条件的数的个数
    }
    
    int main() {
        int left, right;
        // 输入区间范围 [left, right]
        scanf("%d %d", &left, &right);
    
        // 计算区间 [left, right] 内不包含 "101" 模式的数的个数
        // 结果为 dp(right) 减去 dp(left - 1)
        int result = dp(right) - dp(left - 1);
        printf("%d\n", result);  // 输出结果
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/08aa3452b88e11a270e501e93c313fbc.png)

### 完整用例

### 用例1

    
    
    1 10
    

### 用例2

    
    
    10 20
    

### 用例3

    
    
    1 100
    

### 用例4

    
    
    50 100
    

### 用例5

    
    
    1 1000
    

### 用例6

    
    
    100 200
    

### 用例7

    
    
    1 500
    

### 用例8

    
    
    1000 2000
    

### 用例9

    
    
    999 1000
    

### 用例10

    
    
    10000 20000
    

