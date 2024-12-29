## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

明在玩一个数字加减游戏，只使用加法或者减法，将一个数字 s 变成数字 t。

每个回合，小明可以用当前的数字加上或减去一个数字。

现在有两种数字可以用来加减，分别为a，b（a != b），其中 b 没有使用次数限制。

请问小明最少可以用多少次 a，才能将数字 s 变成数字 t。

题目保证数字 s 一定能变成数字 t。

## 输入描述

输入的唯一一行包含四个正整数 s，t，a，b（1 ≤ s,t,a,b ≤ 10^5），并且a != b。

## 输出描述

#####

输出的唯一一行包含一个整数，表示最少需要使用多少次 a 才能将数字s变成数字 t

## 示例1

输入

    
    
    1 10 5 2
    

输出

    
    
    1
    

说明

> 初始值1加一次a变成6，然后加两次b变成10，因此a的使用次数为1

## 示例2

输入

    
    
    11 33 4 10
    

输出

    
    
    2
    

说明

> 11减两次a变成3，然后加三次b变成33，因此a的使用次数为2次

## 解题思路

### 题目解释

题目的主要目标是让玩家从一个起始数  s s s 通过多次加上或减去两个指定的数字  a a a 和  b b b 来变为另一个目标数  t t
t。其中，数字  b b b 的使用次数没有限制，但是我们需要尽量减少使用数字  a a a 的次数。

### 解题思路

为了解这个问题，我们需要关注两个核心目标：

  1. **确定数字 a a a 的最少使用次数：** 我们需要找到一种方式，使得使用  a a a 的次数最少。使用的次数可以是加  a a a 也可以是减  a a a，主要取决于  s s s 和  t t t 之间的差值与  a a a 和  b b b 的关系。

  2. **利用数字 b b b 来调整差值：** 由于  b b b 的使用次数没有限制，我们可以自由地加或减  b b b，以使  s s s 最终变为  t t t。

#### 具体步骤：

  * **计算差值：** 首先计算  s s s 和  t t t 之间的差  n n n，即  n = ∣ s − t ∣ n = |s - t| n=∣s−t∣。

  * **余数与模的关系：** 利用模运算来确定达到  t t t 需要  a a a 和  b b b 组合的方式。具体来说，考虑  n n n 除以  b b b 的余数，然后通过增加或减少  a a a 来调整这个余数，使其匹配  b b b 的倍数。

  * **循环检查：** 通过一个循环来尝试不同的  a a a 的使用次数（增加和减少），直到找到使  n n n 能够通过加上或减去  b b b 的倍数来达到 0 的方案。这个过程中，我们追踪  a a a 的使用次数。

  * **输出结果：** 得到能够使  s s s 变为  t t t 时  a a a 的最小使用次数。

#### 代码实现的逻辑：

  1. **初始化：** 读入四个数  s s s,  t t t,  a a a,  b b b。

  2. **计算绝对差值 n n n：** n = ∣ s − t ∣ n = |s - t| n=∣s−t∣。

  3. **计算 n n n 除以  b b b 的余数：** modValue1 = n % b \text{modValue1} = n \% b modValue1=n%b 和  modValue2 = ( b − modValue1 ) % b \text{modValue2} = (b - \text{modValue1}) \% b modValue2=(b−modValue1)%b。这两个值分别代表直接加到  n n n 或者通过减少到达一个  b b b 的倍数。

  4. **尝试不同的 a a a 使用次数：** 通过循环遍历尝试不同的  a a a 的使用次数，检查  ( a × i ) % b (a \times i) \% b (a×i)%b 是否等于  modValue1 \text{modValue1} modValue1 或  modValue2 \text{modValue2} modValue2，直到找到满足条件的最小的  i i i。

  5. **输出 i i i：** 输出  a a a 需要使用的最小次数  i i i。

通过这种方法，我们可以确保使用  a a a 的次数尽可能少，而  b b b 帮助调整余数以达到目标数  t t t。

## Java

    
    
    import java.util.Scanner;
    
     
    public class Main{
    
        public static void main(String[] args) {
         
            Scanner sc = new Scanner(System.in);
        
       
            String[] numbers = sc.nextLine().split(" ");
            
            // 解析输入的四个数字
            int s = Integer.parseInt(numbers[0]); // 第一个数字，起始值s
            int t = Integer.parseInt(numbers[1]); // 第二个数字，目标值t
            int a = Integer.parseInt(numbers[2]); // 第三个数字，增量a
            int b = Integer.parseInt(numbers[3]); // 第四个数字，模数b
            
            // 计算s和t的差的绝对值
            int n = Math.abs(s - t);
            // 计算n除以b的余数
            int modValue1 = n % b;
            // 计算b减去n除以b的余数后再模b，用于处理特殊情况
            int modValue2 = (b - modValue1) % b;
            
            int i = 0; // 初始化i，从0开始计算
            int tmpModValue; // 临时变量，用于存储中间计算结果
            
            // 循环，直到找到满足条件的i值
            while ((tmpModValue = (a * i) % b) != modValue1 && tmpModValue != modValue2) {
                i++; // 如果当前的tmpModValue不等于modValue1也不等于modValue2，i增加1
            }
            // 输出满足条件的最小i值
            System.out.println(i);
        }
    }
    
    

## Python

    
    
    # 读取输入的四个整数
    s, t, a, b = map(int, input().split())
    
    # 计算s和t的差的绝对值
    n = abs(s - t)
    
    # 计算n除以b的余数
    mod_value1 = n % b
    
    # 计算b减去n除以b的余数后再模b，用于处理特殊情况
    mod_value2 = (b - mod_value1) % b
    
    i = 0  # 初始化i，从0开始计算
    
    # 循环，直到找到满足条件的i值
    while (a * i) % b != mod_value1 and (a * i) % b != mod_value2:
        i += 1  # 如果当前余数不等于mod_value1和mod_value2，i增加1
    
    # 输出满足条件的最小i值
    print(i)
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    // 创建接口以便读取控制台输入
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
     
    rl.on('line', (input) => {
      // 将输入的数字转换为数组
      const [s, t, a, b] = input.split(' ').map(Number);
    
      // 计算s和t的差的绝对值
      const n = Math.abs(s - t);
    
      // 计算n除以b的余数
      const modValue1 = n % b;
    
      // 计算b减去n除以b的余数后再模b，用于处理特殊情况
      const modValue2 = (b - modValue1) % b;
    
      let i = 0;  // 初始化i，从0开始计算
    
      // 循环，直到找到满足条件的i值
      while ((a * i) % b !== modValue1 && (a * i) % b !== modValue2) {
        i++;  // 如果当前余数不等于modValue1和modValue2，i增加1
      }
    
      // 输出满足条件的最小i值
      console.log(i);
    
      rl.close(); // 关闭输入接口
    });
    
    

## C++

    
    
    #include <iostream>
    #include <cmath> // 包含数学库以便使用abs函数
    using namespace std;
    
    int main() {
        int s, t, a, b;
        
     
        cin >> s >> t >> a >> b;
    
        // 计算s和t的差的绝对值
        int n = abs(s - t);
    
        // 计算n除以b的余数
        int modValue1 = n % b;
    
        // 计算b减去n除以b的余数后再模b，用于处理特殊情况
        int modValue2 = (b - modValue1) % b;
    
        int i = 0; // 初始化i，从0开始计算
        int tmpModValue; // 临时变量，用于存储中间计算结果
    
        // 循环，直到找到满足条件的i值
        while ((tmpModValue = (a * i) % b) != modValue1 && tmpModValue != modValue2) {
            i++; // 如果当前余数不等于modValue1和modValue2，i增加1
        }
    
        // 输出满足条件的最小i值
        cout << i << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h> // 包含标准库以便使用abs函数
    
    int main() {
        int s, t, a, b;
        
     
        scanf("%d %d %d %d", &s, &t, &a, &b);
    
        // 计算s和t的差的绝对值
        int n = abs(s - t);
    
        // 计算n除以b的余数
        int modValue1 = n % b;
    
        // 计算b减去n除以b的余数后再模b，用于处理特殊情况
        int modValue2 = (b - modValue1) % b;
    
        int i = 0; // 初始化i，从0开始计算
        int tmpModValue; // 临时变量，用于存储中间计算结果
    
        // 循环，直到找到满足条件的i值
        while ((tmpModValue = (a * i) % b) != modValue1 && tmpModValue != modValue2) {
            i++; // 如果当前余数不等于modValue1和modValue2，i增加1
        }
    
        // 输出满足条件的最小i值
        printf("%d\n", i);
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    1 10 5 2
    

### 用例2

    
    
    11 33 4 10
    

### 用例3

    
    
    8 22 7 5
    

### 用例4

    
    
    8 50 9 4
    

### 用例5

    
    
    20 100 8 6
    

### 用例6

    
    
    13 40 3 7
    

### 用例7

    
    
    2 28 4 6
    

### 用例8

    
    
    9 81 10 7
    

### 用例9

    
    
    12 48 10 8
    

### 用例10

    
    
    7 100 12 9
    

