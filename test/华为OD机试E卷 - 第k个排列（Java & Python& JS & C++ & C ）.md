## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定参数n，从1到n会有n个整数：1,2,3,…,n,这n个数字共有n!种排列。

按大小顺序升序列出所有排列的情况，并一一标记，

当n=3时,所有排列如下:

“123” “132” “213” “231” “312” “321”

给定n和k，返回第k个排列。

## 输入描述

  * 输入两行，第一行为n，第二行为k，
  * 给定n的范围是[1,9],给定k的范围是[1,n!]。

## 输出描述

输出排在第k位置的数字。

## 示例1

输入

    
    
    3
    3
    

输出

    
    
    213
    

说明

> 3的排列有123,132,213…,那么第三位置就是213

## 示例2

输入

    
    
    2
    2
    

输出

    
    
    21
    

说明

> 2的排列有12,21，那么第二位置的为21。

## 解题思路

## 常见的递归解法

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            int n, k;
            Vector<String> lines = new Vector<String>();
            Scanner scanner = new Scanner(System.in);
    
            // 读取 n 和 k
            n = scanner.nextInt();
            k = scanner.nextInt();
    
            // 如果 n 等于 1，则直接输出 1 并结束程序
            if (n == 1) {
                System.out.println("1");
                return;
            }
    
            // 初始化 nums 数组，存储 1 到 n 的整数
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = i + 1;
            }
    
            // 初始化结果列表
            List<String> result = new ArrayList<>();
    
            // 递归函数，用于生成所有排列
            generatePermutations(nums, "", result, k);
    
            // 对结果列表进行排序
            Collections.sort(result);
    
            // 输出第k个排列
            System.out.println(result.get(k - 1));
        }
    
        public static void generatePermutations(int[] nums, String current, List<String> result, int k) {
            // 如果数字数组为空，将当前结果添加到结果列表中
            if (nums.length == 0) {
                result.add(current);
                return;
            }
    
            // 遍历当前数字数组
            for (int i = 0; i < nums.length; i++) {
                // 取出一个数字
                int num = nums[i];
    
                // 创建新的数字数组，删除当前数字
                int[] newNums = new int[nums.length - 1];
                for (int j = 0; j < i; j++) {
                    newNums[j] = nums[j];
                }
                for (int j = i + 1; j < nums.length; j++) {
                    newNums[j - 1] = nums[j];
                }
    
                // 递归调用函数，传递更新后的数字数组和结果字符串
                generatePermutations(newNums, current + num, result, k);
    
                // 如果结果列表长度等于k，直接返回
                if (result.size() == k) {
                    return;
                }
            }
        }
    }
    
    

## Python

    
    
    n = int(input())
    k = int(input())
    
    
    if n == 1:
        print("1")
        exit()
    
    nums = [i+1 for i in range(n)]
    result = []
    
    def generatePermutations(nums, current, result, k):
        if len(nums) == 0:
            result.append(current)
            return
    
        for i in range(len(nums)):
            num = nums[i]
            newNums = nums[:i] + nums[i+1:]
            generatePermutations(newNums, current + str(num), result, k)
    
            if len(result) == k:
                return
    
    generatePermutations(nums, "", result, k)
    
    result.sort()
    print(result[k-1])
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on('line', (n) => {
      rl.on('line', (k) => {
        // 如果 n 等于 1，则直接输出 1 并结束程序
        if (n == 1) {
          console.log("1");
          rl.close();
          return;
        }
    
        // 初始化 nums 数组，存储 1 到 n 的整数
        let nums = [];
        for (let i = 0; i < n; i++) {
          nums.push(i + 1);
        }
    
        // 初始化结果列表
        let result = [];
    
        // 递归函数，用于生成所有排列
        generatePermutations(nums, "", result, k);
    
        // 对结果列表进行排序
        result.sort();
    
        // 输出第k个排列
        console.log(result[k - 1]);
    
        rl.close();
      });
    });
    
    function generatePermutations(nums, current, result, k) {
      // 如果数字数组为空，将当前结果添加到结果列表中
      if (nums.length === 0) {
        result.push(current);
        return;
      }
    
      // 遍历当前数字数组
      for (let i = 0; i < nums.length; i++) {
        // 取出一个数字
        let num = nums[i];
    
        // 创建新的数字数组，删除当前数字
        let newNums = nums.slice(0, i).concat(nums.slice(i + 1));
    
        // 递归调用函数，传递更新后的数字数组和结果字符串
        generatePermutations(newNums, current + num, result, k);
    
        // 如果结果列表长度等于k，直接返回
        if (result.length === k) {
          return;
        }
      }
    }
    
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    void generatePermutations(vector<int>& nums, string current, vector<string>& result, int k);
    
    int main() {
        int n, k;
        vector<string> lines;
        cin >> n >> k;
    
        if (n == 1) {
            cout << "1" << endl;
            return 0;
        }
    
        vector<int> nums(n);
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
    
        vector<string> result;
        generatePermutations(nums, "", result, k);
    
        sort(result.begin(), result.end());
    
        cout << result[k - 1] << endl;
    
        return 0;
    }
    
    void generatePermutations(vector<int>& nums, string current, vector<string>& result, int k) {
        if (nums.empty()) {
            result.push_back(current);
            return;
        }
    
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            vector<int> newNums(nums.size() - 1);
            copy(nums.begin(), nums.begin() + i, newNums.begin());
            copy(nums.begin() + i + 1, nums.end(), newNums.begin() + i);
    
            generatePermutations(newNums, current + to_string(num), result, k);
    
            if (result.size() == k) {
                return;
            }
        }
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    // 生成排列的递归函数
    void generatePermutations(int* nums, int numsSize, char* current, char** result, int* resultSize, int k) {
        // 如果数字数组为空，将当前结果添加到结果列表中
        if (numsSize == 0) {
            result[*resultSize] = (char*)malloc(strlen(current) + 1);
            strcpy(result[*resultSize], current);
            (*resultSize)++;
            return;
        }
    
        // 遍历当前数字数组
        for (int i = 0; i < numsSize; i++) {
            // 取出一个数字
            int num = nums[i];
    
            // 创建新的数字数组，删除当前数字
            int* newNums = (int*)malloc((numsSize - 1) * sizeof(int));
            for (int j = 0; j < i; j++) {
                newNums[j] = nums[j];
            }
            for (int j = i + 1; j < numsSize; j++) {
                newNums[j - 1] = nums[j];
            }
    
            // 更新结果字符串
            int newCurrentLen = strlen(current) + 10; // 分配足够大的空间
            char *newCurrent = (char*)malloc(newCurrentLen * sizeof(char));
            snprintf(newCurrent, newCurrentLen, "%s%d", current, num);
    
            // 递归调用函数，传递更新后的数字数组和结果字符串
            generatePermutations(newNums, numsSize - 1, newCurrent, result, resultSize, k);
    
            // 如果结果列表长度等于k，直接返回
            if (*resultSize == k) {
                free(newNums);
                free(newCurrent); // 避免内存泄漏
                return;
            }
    
            // 释放内存
            free(newNums);
            free(newCurrent); // 每次循环后释放newCurrent
        }
    }
    
    int compareStrings(const void* a, const void* b) {
        return strcmp(*(const char**)a, *(const char**)b);
    }
    
    int main() {
        int n, k;
    
        // 读取 n 和 k
        scanf("%d %d", &n, &k);
    
        // 如果 n 等于 1，则直接输出 1 并结束程序
        if (n == 1) {
            printf("1\n");
            return 0;
        }
    
        // 初始化 nums 数组，存储 1 到 n 的整数
        int* nums = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
    
        // 初始化结果列表
        char** result = (char**)malloc(100000000 * sizeof(char*));   
        int resultSize = 0;
    
        // 调用递归函数生成所有排列
        char current[100] = "";  // 初始的结果字符串为空
        generatePermutations(nums, n, current, result, &resultSize, k);
    
        // 对结果列表进行排序
        qsort(result, resultSize, sizeof(char*), compareStrings);
    
        // 输出第 k 个排列
        printf("%s\n", result[k - 1]);
    
        // 释放内存
        for (int i = 0; i < resultSize; i++) {
            free(result[i]);
        }
        free(result);
        free(nums);
    
        return 0;
    }
    

## 不用递归，用全排列

核心解题思路是**基于康托展开（Cantor Expansion）原理**
来解决排列组合问题。康托展开是一种将排列转换为字典序数（第几个排列）的方法，反之也可以用来根据字典序数反向推导出具体的排列。

#### 解题思路

  1. **理解排列的字典序** ：对于给定的整数 `n` 和 `k`，题目要求找到由 `[1, 2, ..., n]` 组成的所有排列中按字典序排列的第 `k` 个排列。字典序排列是将排列按数值大小进行排序。

  2. **分解问题** ：将排列问题分解为一系列位置选择的问题：

     * 首先确定排列的第一个数字，然后确定剩下数字的排列。
     * 通过除以某个数字的阶乘，可以找到这一位上的数字索引，接着更新 `k` 值并继续进行下一位的选择。
  3. **计算阶乘** ：使用阶乘来计算某个位置上的数字有多少种可能性。

     * 对于长度为 `n` 的数组，第一个数字确定后，剩下的 `n-1` 个数字有 `(n-1)!` 种排列方式。
     * 例如，对于 `[1, 2, 3]`，如果第一个数字是 `1`，那么剩余 `[2, 3]` 可以有 `2! = 2` 种排列。
  4. **确定每一位数字** ：通过计算 `(k-1) / (n-1)!` 来确定第一个数字的位置索引 `index`，然后从数字列表中删除已经选择的数字，并调整 `k` 为 `k % (n-1)!`，继续下一位的选择。

  5. **重复过程** ：这个过程从左到右一位一位确定，每一步都使用上述计算方法，直到所有位都确定。

#### 康托展开原理解析

以下通过一个例子详细讲解康托展开的原理：

例子：判断数字2143在集合{1, 2, 3, 4}的全排列中是第几大的排列？

##### 求解过程：

集合{1, 2, 3, 4}共有4个元素，因此总共有  4 ! = 24 4! = 24 4!=24
种排列方式。要计算2143在这些排列中所处的具体位置，我们可以通过以下步骤进行：

  1. **计算首位小于2的排列数** ：

     * 比2小的数字只有1。
     * 剩余的三个数字有  3 ! = 6 3! = 6 3!=6 种排列方式。
     * 因此，这部分排列的数量为  1 × 3 ! = 6 1 \times 3! = 6 1×3!=6。
  2. **计算首位为2、第二位小于1的排列数** ：

     * 第二位比1小的数字不存在。
     * 因此，这部分排列的数量为  0 × 2 ! = 0 0 \times 2! = 0 0×2!=0。
  3. **计算前两位为21、第三位小于4的排列数** ：

     * 第三位比4小的数字只有3。
     * 剩余的一个数字有  1 ! = 1 1! = 1 1!=1 种排列方式。
     * 因此，这部分排列的数量为  1 × 1 ! = 1 1 \times 1! = 1 1×1!=1。
  4. **计算前三位为214、第四位小于3的排列数** ：

     * 第四位比3小的数字不存在。
     * 因此，这部分排列的数量为  0 × 0 ! = 0 0 \times 0! = 0 0×0!=0。

##### 结果计算：

将以上各部分的结果相加，即可得到2143在全排列中的位置：

1 × 3 ! \+ 0 × 2 ! \+ 1 × 1 ! \+ 0 × 0 ! = 7 1 \times 3! + 0 \times 2! + 1
\times 1! + 0 \times 0! = 7 1×3!+0×2!+1×1!+0×0!=7

所以2143是第8大的排列。

##### 康托展开公式

通过上述例子，我们可以推导出康托展开的通用公式：

X = a [ n ] × ( n − 1 ) ! \+ a [ n − 1 ] × ( n − 2 ) ! \+ ⋯ \+ a [ i ] × ( i −
1 ) ! \+ ⋯ \+ a [ 2 ] × 1 ! \+ a [ 1 ] × 0 ! X = a[n] \times (n-1)! + a[n-1]
\times (n-2)! + \dots + a[i] \times (i-1)! + \dots + a[2] \times 1! + a[1]
\times 0! X=a[n]×(n−1)!+a[n−1]×(n−2)!+⋯+a[i]×(i−1)!+⋯+a[2]×1!+a[1]×0!

其中， a [ i ] a[i] a[i]表示原数第  i i i 位在当前未出现的元素中排在第几位（从0开始计数），并且满足  0 ≤ a [ i ] <
i 0 \leq a[i] < i 0≤a[i]<i（ 1 ≤ i ≤ n 1 \leq i \leq n 1≤i≤n）。

##### 康托逆展开

康托展开的逆过程称为康托逆展开，即对于某个集合的全排列，输入一个数字  k k k，返回对应的第  k k k 大排列。

## Java

    
    
    import java.util.ArrayList;
    import java.util.List;
    
    public class Main {
        public static String getPermutation(int n, int k) {
            // 初始化数字列表和阶乘表
            List<Integer> numbers = new ArrayList<>();
            int[] factorial = new int[n + 1];
            
            // 填充1到n的数字
            for (int i = 1; i <= n; i++) {
                numbers.add(i);
            }
            
            // 初始化阶乘表，factorial[0] = 1
            factorial[0] = 1;
            for (int i = 1; i <= n; i++) {
                factorial[i] = factorial[i - 1] * i;
            }
            
            // 调整k到0索引
            k--;
            StringBuilder result = new StringBuilder();
            
            // 从大到小确定每一位
            for (int i = n; i > 0; i--) {
                // 计算当前位数字索引
                int index = k / factorial[i - 1];
                result.append(numbers.get(index));
                
                // 移除已经选择的数字
                numbers.remove(index);
                
                // 更新k值
                k %= factorial[i - 1];
            }
            
            return result.toString();
        }
    
        public static void main(String[] args) {
            java.util.Scanner scanner = new java.util.Scanner(System.in);
            int n = scanner.nextInt();
            int k = scanner.nextInt();
            System.out.println(getPermutation(n, k));
        }
    }
    

## Python

    
    
    import math
    
    def get_permutation(n, k):
        # 初始化数字列表和阶乘表
        numbers = list(range(1, n+1))
        factorial = [1] * (n+1)
        
        # 预先计算所有阶乘值
        for i in range(2, n+1):
            factorial[i] = factorial[i-1] * i
        
        # 调整k到0索引
        k -= 1
        result = ""
        
        # 从大到小确定每一位
        for i in range(n, 0, -1):
            # 计算当前位数字索引
            index = k // factorial[i-1]
            result += str(numbers[index])
            
          
            
            # 更新k值
            k %= factorial[i-1]
        
        return result
    
     
    n = int(input())
    k = int(input())
    print(get_permutation(n, k))
    

## JavaScript

    
    
    function getPermutation(n, k) {
        // 初始化数字列表和阶乘表
        let numbers = Array.from({ length: n }, (_, i) => i + 1);
        let factorial = new Array(n + 1).fill(1);
    
        // 预先计算所有阶乘值
        for (let i = 2; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
    
        // 调整k到0索引
        k--;
        let result = '';
    
        // 从大到小确定每一位
        for (let i = n; i > 0; i--) {
            // 计算当前位数字索引
            let index = Math.floor(k / factorial[i - 1]);
            result += numbers[index];
    
            // 移除已经选择的数字
            numbers.splice(index, 1);
    
            // 更新k值
            k %= factorial[i - 1];
        }
    
        return result;
    }
    
    // 示例用法
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    readline.on('line', n => {
        readline.on('line', k => {
            console.log(getPermutation(parseInt(n), parseInt(k)));
            readline.close();
        });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    using namespace std;
    
    string getPermutation(int n, int k) {
        // 初始化数字列表和阶乘表
        vector<int> numbers;
        vector<int> factorial(n + 1, 1);
    
        // 填充1到n的数字
        for (int i = 1; i <= n; i++) {
            numbers.push_back(i);
        }
    
        // 预先计算所有阶乘值
        for (int i = 2; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
    
        // 调整k到0索引
        k--;
        string result;
    
        // 从大到小确定每一位
        for (int i = n; i > 0; i--) {
            // 计算当前位数字索引
            int index = k / factorial[i - 1];
            result += to_string(numbers[index]);
    
            // 移除已经选择的数字
            numbers.erase(numbers.begin() + index);
    
            // 更新k值
            k %= factorial[i - 1];
        }
    
        return result;
    }
    
    int main() {
        int n, k;
        cin >> n >> k;
        cout << getPermutation(n, k) << endl;
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    
    void getPermutation(int n, int k, char* result) {
        // 初始化数字列表和阶乘表
        int* numbers = (int*)malloc(n * sizeof(int));
        int* factorial = (int*)malloc((n + 1) * sizeof(int));
    
        // 填充1到n的数字
        for (int i = 0; i < n; i++) {
            numbers[i] = i + 1;
        }
    
        // 初始化阶乘表
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
    
        // 调整k到0索引
        k--;
        int index, pos = 0;
    
        // 从大到小确定每一位
        for (int i = n; i > 0; i--) {
            // 计算当前位数字索引
            index = k / factorial[i - 1];
            result[pos++] = numbers[index] + '0';  // 转换为字符保存
    
            // 移除已经选择的数字
            for (int j = index; j < n - 1; j++) {
                numbers[j] = numbers[j + 1];
            }
    
            // 更新k值
            k %= factorial[i - 1];
        }
        result[pos] = '\0';  // 添加字符串结束符
    
        // 释放动态分配的内存
        free(numbers);
        free(factorial);
    }
    
    int main() {
        int n, k;
        scanf("%d %d", &n, &k);
        char result[10];  // 假设n最大为9
        getPermutation(n, k, result);
        printf("%s\n", result);
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b0d8ff6d53693bfcf6e1605b507f3ae3.png)

#### 完整用例

##### 用例1

    
    
    3
    3
    

##### 用例2

    
    
    2
    2
    

##### 用例3

    
    
    4
    6
    

##### 用例4

    
    
    5
    1
    

##### 用例5

    
    
    6
    6
    

##### 用例6

    
    
    9
    362880
    

##### 用例7

    
    
    7
    5040
    

##### 用例8

    
    
    8
    40320
    

##### 用例9

    
    
    9
    362879
    

##### 用例10

    
    
    6
    720
    

