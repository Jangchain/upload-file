## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

A，B两个人玩一个数字比大小的游戏，在游戏前，两个人会拿到相同长度的两个数字序列，两个数字序列不相同的，且其中的数字是随机的。

A，B各自从数字序列中挑选出一个数字进行大小比较，赢的人得1分，输的人扣1分，相等则各自的分数不变。 用过的数字需要丢弃。

求A可能赢B的最大分数。

## 输入描述

输入数据的第1个数字表示数字序列的长度N，后面紧跟着两个长度为N的数字序列。

## 输出描述

A可能赢B的最大分数

## 示例1

输入

    
    
    3
    4 8 10
    3 6 4
    

输出

    
    
    3
    

说明

> 输入数据第1个数字表示数字序列长度为3，后面紧跟着两个长度为3的数字序列。  
>  序列A：4 8 10  
>  序列B：3 6 4  
>  A可以赢的最大分数是3。获得该分数的比大小过程可以是：  
>  1）A：4 B：3  
>  2）A：8 B：6  
>  3）A：10 B：4

## 解题思路

这道题可以采用贪心策略来解决。首先，将A和B的数字序列分别按照从小到大的顺序进行排序。然后，设置两个指针la和ra分别指向A序列的最左端和最右端，设置两个指针lb和rb分别指向B序列的最左端和最右端。

接下来，使用一个变量ans来记录A可能赢B的最大分数。开始循环，判断A序列的最大值和B序列的最大值的大小关系：

  * 如果A序列的最大值大于B序列的最大值，那么A可以选择最大值与B的最大值进行比较，A得1分，然后将指针向左移动一位。
  * 如果A序列的最大值小于B序列的最大值，那么A只能选择最小值与B的最大值进行比较，A扣1分，然后将指针向右移动一位。
  * 如果A序列的最大值等于B序列的最大值，那么需要进一步判断A序列的最小值和B序列的最小值的大小关系： 
    * 如果A序列的最小值大于B序列的最小值，那么A可以选择最小值与B的最小值进行比较，A得1分，然后将指针向右移动一位。
    * 如果A序列的最小值小于B序列的最小值，那么A只能选择最小值与B的最大值进行比较，A扣1分，然后将指针向右移动一位。

最后，返回变量ans即为A可能赢B的最大分数。

## Java

    
    
    import java.util.Arrays;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int n = scanner.nextInt();  // 输入数字序列的长度
            int[] A = new int[n];  // 输入A的数字序列
            int[] B = new int[n];  // 输入B的数字序列
    
            for (int i = 0; i < n; i++) {
                A[i] = scanner.nextInt();
            }
            for (int i = 0; i < n; i++) {
                B[i] = scanner.nextInt();
            }
    
            Arrays.sort(A);  // 将A的数字序列排序
            Arrays.sort(B);  // 将B的数字序列排序
            int used = B[0] - B[n-1];
            int res = 0;  // 初始化最大分数为0
    
            for (int i = 0; i < n; i++) {
                int j = 0;
                while (j < n) {
                    if (A[j] > B[i]) {  // 如果A的数字大于B的数字
                        A[j] = used;   // 用过了
                        res += 1;  // A得分加1
                        break;
                    }
                    if (j == n - 1 && A[j] == B[i]) {  // 如果A的数字和B的数字相等且已经遍历完A的数字序列
                        A[j] = used;  // 用过了
                        break;
                    }
                    j += 1;
                }
                if (j == n) {  // 如果j等于n，说明A的数字都小于等于B的数字，无法赢得更多分数
                    res -= (n - i);  // 分数减去剩余未比较的数字个数
                    break;
                }
            }
    
            System.out.println(res);  // 输出A可能赢B的最大分数
        }
    }
    

## Python

    
    
    n = int(input())  # 输入数字序列的长度
    A = list(map(int, input().split()))  # 输入A的数字序列
    B = list(map(int, input().split()))  # 输入B的数字序列
    
    A.sort()  # 将A的数字序列排序
    B.sort()  # 将B的数字序列排序
    used = B[0] - B[len(B)-1]
    res = 0  # 初始化最大分数为0
    
    for i in range(n):
        j = 0
        while j < n:
            if A[j] > B[i]:  # 如果A的数字大于B的数字
                A[j] = used   # 用过了
                res += 1  # A得分加1
                break
            if j == n - 1 and A[j] == B[i]:  # 如果A的数字和B的数字相等且已经遍历完A的数字序列
                A[j] = used  # 用过了
                break
            j += 1
        if j == n:  # 如果j等于n，说明A的数字都小于等于B的数字，无法赢得更多分数
            res -= (n - i)  # 分数减去剩余未比较的数字个数
            break
    
    print(res)  # 输出A可能赢B的最大分数
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on('line', (n) => {
      rl.on('line', (arrAStr) => {
        rl.on('line', (arrBStr) => {
          // 后面紧跟着两个长度为N的数字序列
          const arrA = arrAStr.split(' ').map(Number);
          const arrB = arrBStr.split(' ').map(Number);
    
          // 对两个数字序列进行排序
          arrA.sort((a, b) => a - b);
          arrB.sort((a, b) => a - b);
    
          // 初始化A和B的区间左右边界
          let leftA = 0;
          let rightA = n - 1;
          let leftB = 0;
          let rightB = n - 1;
    
          // 初始化答案为0
          let answer = 0;
    
          // 当A的区间左边界小于等于右边界时，进行循环
          while (leftA <= rightA) {
            // 如果A区间的最大值大于B区间的最大值
            if (arrA[rightA] > arrB[rightB]) {
              // A赢得这一轮比较，得1分
              answer += 1;
              // 更新A和B的区间右边界，即舍弃已使用的数字
              rightA--;
              rightB--;
            }
            // 如果A区间的最大值小于B区间的最大值
            else if (arrA[rightA] < arrB[rightB]) {
              // A输掉这一轮比较，扣1分
              answer -= 1;
              // 更新A和B的区间左边界，即舍弃已使用的数字
              leftA++;
              rightB--;
            }
            // 如果A区间的最大值等于B区间的最大值
            else {
              // 如果A区间的最小值大于B区间的最小值
              if (arrA[leftA] > arrB[leftB]) {
                // A赢得这一轮比较，得1分
                answer += 1;
                // 更新A和B的区间左边界，即舍弃已使用的数字
                leftA++;
                leftB++;
              }
              // 如果A区间的最小值小于等于B区间的最大值
              else {
                // 如果B区间的最大值大于A区间的最小值，A输掉这一轮比较，扣1分
                if (arrB[rightB] > arrA[leftA]) answer -= 1;
                // 更新A和B的区间左边界和右边界，即舍弃已使用的数字
                leftA++;
                rightB--;
              }
            }
          }
    
          // 输出A可能赢B的最大分数
          console.log(answer);
    
          rl.close();
        });
      });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    
    using namespace std;
    
    int main() {
        int n;
        cin >> n;  // 输入数字序列的长度
    
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];  // 输入A的数字序列
        }
    
        vector<int> B(n);
        for (int i = 0; i < n; i++) {
            cin >> B[i];  // 输入B的数字序列
        }
    
        sort(A.begin(), A.end());  // 将A的数字序列排序
        sort(B.begin(), B.end());  // 将B的数字序列排序
    
        int used = B[0] - B[B.size() - 1];
        int res = 0;  // 初始化最大分数为0
    
        for (int i = 0; i < n; i++) {
            int j = 0;
            while (j < n) {
                if (A[j] > B[i]) {  // 如果A的数字大于B的数字
                    A[j] = used;   // 用过了
                    res += 1;  // A得分加1
                    break;
                }
                if (j == n - 1 && A[j] == B[i]) {  // 如果A的数字和B的数字相等且已经遍历完A的数字序列
                    A[j] = used;  // 用过了
                    break;
                }
                j += 1;
            }
            if (j == n) {  // 如果j等于n，说明A的数字都小于等于B的数字，无法赢得更多分数
                res -= (n - i);  // 分数减去剩余未比较的数字个数
                break;
            }
        }
    
        cout << res << endl;  // 输出A可能赢B的最大分数
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    
    int cmp(const void *a, const void *b) {
        return (*(int *)a - *(int *)b;  // 用于排序的比较函数
    }
    
    int main() {
        int n;
        scanf("%d", &n);  // 输入数字序列的长度
    
        int *A = (int *)malloc(n * sizeof(int));  // 动态分配数组A
        int *B = (int *)malloc(n * sizeof(int));  // 动态分配数组B
    
        for (int i = 0; i < n; i++) {
            scanf("%d", &A[i]);  // 输入A的数字序列
        }
    
        for (int i = 0; i < n; i++) {
            scanf("%d", &B[i]);  // 输入B的数字序列
        }
    
        qsort(A, n, sizeof(int), cmp);  // 将A的数字序列排序
        qsort(B, n, sizeof(int), cmp);  // 将B的数字序列排序
    
        int res = 0;  // 初始化最大分数为0
        int j = 0;    // B序列的索引
    
        for (int i = 0; i < n; i++) {
            while (j < n && A[i] > B[j]) {  // 如果A的数字大于B的数字
                res += 1;  // A得分加1
                j++;  // B的数字使用
            }
        }
    
        res += (n - j);  // A可以赢得的分数加上B未使用的数字个数
    
        printf("%d\n", res);  // 输出A可能赢B的最大分数
    
        free(A);  // 释放动态分配的内存
        free(B);  // 释放动态分配的内存
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/60b4ed00df92392a58d9ad27257396c2.png)

#### 用例

##### 1

    
    
    3
    4 8 10
    3 6 4
    

##### 2

    
    
    4
    1 2 3 4
    5 6 7 8
    

##### 3

    
    
    5
    10 20 30 40 50
    5 15 25 35 45
    

##### 4

    
    
    3
    4 5 6
    6 7 8
    

##### 5

    
    
    6
    1 2 3 4 5 6
    6 7 8 9 10 11
    

##### 6

    
    
    4
    10 20 30 40
    40 30 20 10
    

##### 7

    
    
    2
    5 10
    15 20
    

##### 8

    
    
    3
    1 3 5
    2 4 6
    

##### 9

    
    
    4
    1 2 3 4
    4 3 2 1
    

##### 10

    
    
    2
    5 10
    10 5
    

#### 完整用例

##### 用例1

    
    
    3
    4 8 10
    3 6 4
    

##### 用例2

    
    
    4
    1 2 3 4
    5 6 7 8
    

##### 用例3

    
    
    5
    10 20 30 40 50
    5 15 25 35 45
    

##### 用例4

    
    
    3
    4 5 6
    6 7 8
    

##### 用例5

    
    
    6
    1 2 3 4 5 6
    6 7 8 9 10 11
    

##### 用例6

    
    
    4
    10 20 30 40
    40 30 20 10
    

##### 用例7

    
    
    2
    5 10
    15 20
    

##### 用例8

    
    
    3
    1 3 5
    2 4 6
    

##### 用例9

    
    
    4
    1 2 3 4
    4 3 2 1
    

##### 用例10

    
    
    2
    5 10
    10 5
    

