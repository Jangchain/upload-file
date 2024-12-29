## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定一个长度为n的整型数组，表示一个选手在n轮内可选择的牌面分数。选手基于规则选牌，

请计算所有轮结束后其可以获得的最高总分数。

**选择规则如下：**

  1. 在每轮里选手可以选择获取该轮牌面，则其总分数加上该轮牌面分数，为其新的总分数。
  2. 选手也可不选择本轮牌面直接跳到下一轮，此时将当前总分数还原为3轮前的总分数，若当前轮次小于等于3（即在第1、2、3轮选择跳过轮次），则总分数置为0。
  3. 选手的初始总分数为0，且必须依次参加每一轮

​

## 输入描述

第一行为一个小写逗号分割的字符串，表示n轮的牌面分数，1<= n <=20。

分数值为整数，-100 <= 分数值 <= 100。

不考虑格式问题。

## 输出描述

所有轮结束后选手获得的最高总分数。

## 示例1

输入

    
    
    1,-5,-6,4,3,6,-2
    

输出

    
    
    11
    

说明

> ## 解题思路

这个题目要求解的是在一系列轮次中如何选择分数以最大化总分，同时考虑到特定的规则制约选择过程。

##### 规则

  1. **选择牌面** ：若选手选择获取当前轮的牌面分数，则该轮分数加到总分上。
  2. **跳过选择** ： 
     * **跳到下一轮** ：如果选手跳过当前轮，那么他的总分数会回到3轮前的总分数。特别地，如果当前是前三轮（第1、2、3轮），总分将被置为0。
  3. **初始总分为0** ：选手开始时没有分数。
  4. **必须依次参加每轮** ：选手不能跳过轮次，只能选择是否获取分数。

##### 目标

计算在所有轮次结束后，选手可以获得的最高总分数。

#### 示例说明

  * 输入的分数数组为 `[1, -5, -6, 4, 3, 6, -2]`。
  * 考虑最优策略为： 
    * **第1轮选择分数1** ：总分为1。
    * **第2轮跳过** ：由于在前三轮内，总分重置为0。
    * **第3轮跳过** ：总分仍为0。
    * **第4轮选择分数4** ：总分从0变为4。
    * **第5轮选择分数3** ：总分从4变为7。
    * **第6轮选择分数6** ：总分从7变为13。
    * **第7轮跳过** ：总分回到第4轮的总分4。
    * 选择这些分数后，最后总分为11。

## Java

    
    
    import java.util.Scanner;
    import java.util.TreeMap;
    
    public class Main {
      public static void main(String[] args) {
        // 创建 Scanner 对象，用于读取用户输入
        Scanner scanner = new Scanner(System.in);
    
        // 读取一行输入的牌面分数，输入为逗号分隔的字符串
        String line = scanner.nextLine();
    
        // 将输入字符串按逗号分割成字符串数组
        String[] numStrArray = line.split(",");
    
        // 使用 TreeMap 记录每一轮结束时的最大总分
        TreeMap<Integer, Integer> map = new TreeMap<>();
    
        // 初始化最大总分为 0
        int maxScore = 0;
    
        // 遍历所有轮次的分数
        for (int m = 0, size = numStrArray.length; m < size; m++) {
          // 将当前轮次的字符串分数转换为整数
          int num = Integer.parseInt(numStrArray[m]);
    
          // 处理前三轮的特殊情况
          if (m < 3) {
            if (m == 0) {
              // 如果是第一轮，最大总分为当前轮分数与 0 之间的较大值
              maxScore = Math.max(0, num);
            } else {
              // 如果是第二或第三轮，总分为前一轮的总分加上当前轮分数，结果和 0 比较取较大值
              maxScore = Math.max(0, (maxScore + num));
            }
          } else {
            // 从第四轮开始，总分为当前轮分数加上前一轮总分，或者 3 轮前的总分中较大的那个
            maxScore = Math.max((maxScore + num), map.get(m - 2));
          }
    
          // 记录当前轮结束后的最大总分，存入 map
          map.put(m + 1, maxScore);
        }
    
        // 输出最终的最大总分
        System.out.print(maxScore);
      }
    }
    
    

## Python

    
    
    import sys
    
    line = input()
    numStrArray = line.split(",")
    map = {}
    maxScore = 0
    for m in range(len(numStrArray)):
        num = int(numStrArray[m])
        if m < 3:
            if m == 0:
                maxScore = max(0, num)
            else:
                maxScore = max(0, (maxScore + num))
        else:
            maxScore = max((maxScore + num), map[m - 2])
        map[m + 1] = maxScore
    sys.stdout.write(str(maxScore))
    
    

## JavaScript

    
    
    const readline = require('readline');
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on("line", (line) => {
      const numStrArray = line.split(",");
      const map = new Map();
      let maxScore = 0;
      for (let m = 0, size = numStrArray.length; m < size; m++) {
        const num = parseInt(numStrArray[m]);
        if (m < 3) {
          if (m === 0) {
            maxScore = Math.max(0, num);
          } else {
            maxScore = Math.max(0, (maxScore + num));
          }
        } else {
          maxScore = Math.max((maxScore + num), map.get(m - 2));
        }
        map.set(m + 1, maxScore);
      }
      console.log(maxScore);
      rl.close();
    });
    
    

## C++

    
    
    #include <iostream>
    #include <sstream>
    #include <map>
    using namespace std;
    
    int main() {
      string line;
      getline(cin, line);
      stringstream ss(line);
      string numStr;
      map<int, int> map;
      int maxScore = 0;
      int m = 0;
      while (getline(ss, numStr, ',')) {
        int num = stoi(numStr);
        if (m < 3) {
          if (m == 0) {
            maxScore = max(0, num);
          } else {
            maxScore = max(0, (maxScore + num));
          }
        } else {
          maxScore = max((maxScore + num), map[m - 2]);
        }
        map[m + 1] = maxScore;
        m++;
      }
      cout << maxScore;
      return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int max(int a, int b) {
        return a > b ? a : b;
    }
    
    int main() {
        // 定义数组存储轮次分数
        int map[20] = {0}; // 用于存储每一轮的最大总分数
        int maxScore = 0;  // 初始化最大分数为0
        char line[100];    // 存储输入字符串
        int nums[20];      // 存储分割后的整数数组
        int size = 0;      // 记录轮次个数
        
        // 读取输入的字符串
        fgets(line, 100, stdin);
    
        // 将输入字符串按逗号分割并转换为整数
        char *token = strtok(line, ",");
        while (token != NULL) {
            nums[size++] = atoi(token);
            token = strtok(NULL, ",");
        }
    
        // 计算每一轮的最大分数
        for (int m = 0; m < size; m++) {
            int num = nums[m];
    
            // 前三轮的特殊处理
            if (m < 3) {
                if (m == 0) {
                    maxScore = max(0, num); // 第一轮的分数和0进行比较
                } else {
                    maxScore = max(0, maxScore + num); // 第二、三轮是当前总分加分数，与0比较
                }
            } else {
                // 第四轮及之后，最大总分为当前总分加上当前轮的分数或三轮前的分数
                maxScore = max(maxScore + num, map[m - 2]);
            }
    
            // 存储当前轮的最大总分
            map[m + 1] = maxScore;
        }
    
        // 输出最终最大总分
        printf("%d\n", maxScore);
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

#### 完整用例

##### 用例1

    
    
    1,-5,-6,4,3,6,-2
    

##### 用例2

    
    
    1,2,3,4,5,6,7,8,9,10
    

##### 用例3

    
    
    -1,-2,-3,-4,-5
    

##### 用例4

    
    
    0,0,0,0,0
    

##### 用例5

    
    
    100,100,100,100,100
    

##### 用例6

    
    
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    

##### 用例7

    
    
    10,20,30,40,50,60,70,80,90,100,90,80,70,60,50,40,30,20,10,0
    

##### 用例8

    
    
    -1,0,1,-2,0,2,-3,0,3,-4,0,4,-5,0,5,-6,0,6,-7,0
    

##### 用例9

    
    
    10,-20,30,-40,50,-60,70,-80,90,-100,110,-120,130,-140,150,-160,170,-180,190,-200
    

##### 用例10

    
    
    -10,-20,-30,-40,-50,-60,-70,-80,-90,-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,0
    

