## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小明正在规划一个大型[数据中心](https://so.csdn.net/so/search?q=%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83&spm=1001.2101.3001.7020)机房，为了使得机柜上的机器都能正常满负荷工作，需要确保在每个机柜边上至少要有一个电箱。

为了简化题目，假设这个机房是一整排，M表示机柜，I表示间隔，请你返回这整排机柜，至少需要多少个电箱。 如果无解请返回 -1 。

​

## 输入描述

> cabinets = “MIIM”

### 备注:

其中 M 表示机柜，I 表示间隔

1 ≤ strlen(cabinets) ≤ 10000  
其中 cabinets[i] = ‘M’ 或者 'I‘

## 输出描述

> 2

表示至少需要2个电箱

## 示例1

输入

    
    
    MIIM
    

输出

    
    
    2
    

## 示例2

输入

    
    
    MIM
    

输出

    
    
    1
    

## 示例3

输入

    
    
    M
    

输出

    
    
    -1
    

## 示例4

输入

    
    
    MMM
    

输出

    
    
    -1
    

## 示例5

输入

    
    
    I
    

输出

    
    
    0
    

## 解题思路

这个题目的主要意图是计算在给定的机柜排列中，至少需要多少个电箱来保证所有机柜都能正常工作。

#### 示例分析

  * **示例 1** ：

    * 输入: `MIIM`
    * 布局: M（电箱放在这）I M（电箱放在这）I M
    * 可以放置 2 个电箱，分别在第一个和第三个机柜旁边。
    * 输出: `2`
  * **示例 2** ：

    * 输入: `MIM`
    * 布局: M（电箱放在这）I M
    * 可以放置 1 个电箱，在第一个机柜旁边即可。
    * 输出: `1`
  * **示例 3** ：

    * 输入: `M`
    * 只有一个机柜，没有间隔可供放置电箱。
    * 输出: `-1`（因为无法满足条件）。

好的，以下是结合稍微复杂用例的优化表达：

* * *

## 代码思路

本题的关键在于合理放置电箱，以确保每个机柜旁边至少有一个电箱。我们采用从左到右的遍历方式，并优先将电箱放在机柜的右侧。

#### 为什么优先放在右侧？

考虑以下示例：

    
    
    I M I M I
    

在这种情况下，如果将电箱放在第一个红色 `I` 的位置，只需一个电箱；而如果放在绿色 `I` 的位置，则需要两个电箱，显然不如前者经济。

再看一个稍复杂的例子：

    
    
    M I M I I M
    

从左到右遍历，遇到第一个 `M` 时，我们优先在其右侧（即第 `i + 1` 位置）放置电箱。接着，再遇到下一个 `M`，右侧同样可以放电箱。对于第三个
`M`，其右侧为 `I`，也可以放置电箱。

#### 特殊情况处理

在如下情况下：

    
    
    I M M I I
    

当遇到第一个 `M` 时，如果其右侧无法放电箱，则需要检查左侧，发现可以放电箱。之后再遇到第二个 `M`，其右侧为 `I`，可以继续放置电箱。

然而，如果出现以下情况：

    
    
    M M M
    

则无论从左侧还是右侧都无法放置电箱，因此应直接返回 `-1`。

#### 重要考虑

当机柜的右侧可以放电箱时，例如在第 `i` 个位置是机柜，第 `i + 1` 个位置是间隔，此时放置电箱后，我们是否还需考虑第 `i + 2` 个位置？

例如：

    
    
    M I M I
    

对于红色的 `M`，由于必然会有一个电箱，因此可以直接跳过 `i + 2` 和 `i + 3` 的位置，重新开始判断。

这种策略能有效减少不必要的判断，提升算法效率。通过优先放电箱并合理处理特殊情况，我们可以确保最小化所需电箱的数量。

## Java

    
    
    import java.util.Scanner;  
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);  
            String layout = scanner.nextLine();  // 读取机柜布局
            int len = layout.length(); // 获取机柜布局的长度
            int count = 0; // 初始化电箱数量为0
    
            // 遍历机柜布局的每一个字符
            for (int i = 0; i < len; i++) {
                // 如果当前字符是 'M'，表示这是一个机柜
                if (layout.charAt(i) == 'M') {
                    // 检查当前机柜的右侧是否有间隔 'I'
                    if (i + 1 < len && layout.charAt(i + 1) == 'I') {
                        count++; // 在右侧放置一个电箱
                        i += 2; // 跳过下一个间隔，继续检查后面的机柜
                    } 
                    // 检查当前机柜的左侧是否有间隔 'I'
                    else if (i - 1 >= 0 && layout.charAt(i - 1) == 'I') {
                        count++; // 在左侧放置一个电箱
                    } 
                    // 如果左右都没有间隔，无法放电箱
                    else {
                        count = -1; // 设置 count 为 -1 表示无解
                        break; // 退出循环
                    }
                }
            }
            // 输出结果：电箱数量或 -1 表示无解
            System.out.println(count); // 打印最终的电箱数量
        }
    }
    
    

## Python

    
    
    def main():
        # 读取机柜布局
        layout = input()
        length = len(layout)  # 获取机柜布局的长度
        count = 0  # 初始化电箱数量为0
    
        # 遍历机柜布局的每一个字符
        i = 0
        while i < length:
            # 如果当前字符是 'M'，表示这是一个机柜
            if layout[i] == 'M':
                # 检查当前机柜的右侧是否有间隔 'I'
                if i + 1 < length and layout[i + 1] == 'I':
                    count += 1  # 在右侧放置一个电箱
                    i += 2  # 跳过下一个间隔，继续检查后面的机柜
                # 检查当前机柜的左侧是否有间隔 'I'
                elif i - 1 >= 0 and layout[i - 1] == 'I':
                    count += 1  # 在左侧放置一个电箱
                # 如果左右都没有间隔，无法放电箱
                else:
                    count = -1  # 设置 count 为 -1 表示无解
                    break  # 退出循环
            i += 1
    
        # 输出结果：电箱数量或 -1 表示无解
        print(count)
    
    if __name__ == "__main__":
        main()
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    // 创建接口以读取输入
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    // 读取机柜布局
    rl.on('line', (layout) => {
        let len = layout.length; // 获取机柜布局的长度
        let count = 0; // 初始化电箱数量为0
    
        // 遍历机柜布局的每一个字符
        for (let i = 0; i < len; i++) {
            // 如果当前字符是 'M'，表示这是一个机柜
            if (layout[i] === 'M') {
                // 检查当前机柜的右侧是否有间隔 'I'
                if (i + 1 < len && layout[i + 1] === 'I') {
                    count++; // 在右侧放置一个电箱
                    i += 2; // 跳过下一个间隔，继续检查后面的机柜
                } 
                // 检查当前机柜的左侧是否有间隔 'I'
                else if (i - 1 >= 0 && layout[i - 1] === 'I') {
                    count++; // 在左侧放置一个电箱
                } 
                // 如果左右都没有间隔，无法放电箱
                else {
                    count = -1; // 设置 count 为 -1 表示无解
                    break; // 退出循环
                }
            }
        }
        // 输出结果：电箱数量或 -1 表示无解
        console.log(count); // 打印最终的电箱数量
    });
    
    

## C++

    
    
    #include <iostream>
    #include <string>
    
    using namespace std;
    
    int main() {
        string layout; // 存储机柜布局的字符串
        getline(cin, layout); // 读取机柜布局
        int len = layout.length(); // 获取机柜布局的长度
        int count = 0; // 初始化电箱数量为0
    
        // 遍历机柜布局的每一个字符
        for (int i = 0; i < len; i++) {
            // 如果当前字符是 'M'，表示这是一个机柜
            if (layout[i] == 'M') {
                // 检查当前机柜的右侧是否有间隔 'I'
                if (i + 1 < len && layout[i + 1] == 'I') {
                    count++; // 在右侧放置一个电箱
                    i += 2; // 跳过下一个间隔，继续检查后面的机柜
                } 
                // 检查当前机柜的左侧是否有间隔 'I'
                else if (i - 1 >= 0 && layout[i - 1] == 'I') {
                    count++; // 在左侧放置一个电箱
                } 
                // 如果左右都没有间隔，无法放电箱
                else {
                    count = -1; // 设置 count 为 -1 表示无解
                    break; // 退出循环
                }
            }
        }
        // 输出结果：电箱数量或 -1 表示无解
        cout << count << endl; // 打印最终的电箱数量
        return 0;
    }
    
    

## C语言

    
    
     #include <stdio.h>
    #include <string.h>
    
    int main() {
        char layout[10000]; // 存储机柜布局的字符串
        fgets(layout, sizeof(layout), stdin); // 读取机柜布局
        int len = strlen(layout) - 1; // 获取机柜布局的长度，减去换行符
        layout[len] = '\0'; // 去除换行符
        int count = 0; // 初始化电箱数量为0
    
        // 遍历机柜布局的每一个字符
        for (int i = 0; i < len; i++) {
            // 如果当前字符是 'M'，表示这是一个机柜
            if (layout[i] == 'M') {
                // 检查当前机柜的右侧是否有间隔 'I'
                if (i + 1 < len && layout[i + 1] == 'I') {
                    count++; // 在右侧放置一个电箱
                    i += 2; // 跳过下一个间隔，继续检查后面的机柜
                } 
                // 检查当前机柜的左侧是否有间隔 'I'
                else if (i - 1 >= 0 && layout[i - 1] == 'I') {
                    count++; // 在左侧放置一个电箱
                } 
                // 如果左右都没有间隔，无法放电箱
                else {
                    count = -1; // 设置 count 为 -1 表示无解
                    break; // 退出循环
                }
            }
        }
        // 输出结果：电箱数量或 -1 表示无解
        printf("%d\n", count); // 打印最终的电箱数量
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    MIIM
    

### 用例2

    
    
    MIM
    

### 用例3

    
    
    M
    

### 用例4

    
    
    MMM
    

### 用例5

    
    
    I
    

### 用例6

    
    
    IMIMI
    

### 用例7

    
    
    IIIMMMIII
    

### 用例8

    
    
    MMIMIMIM
    

### 用例9

    
    
    MIMIMMMIMIMIMIMI
    

### 用例10

    
    
    IMIMIMIMIMIIIIIM
    

