## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

双十一众多商品进行打折销售，小明想购买自己心仪的一些物品，但由于受购买资金限制，所以他决定从众多心仪商品中购买三件，而且想尽可能的花完资金。

现在请你设计一个程序帮助小明计算尽可能花费的最大资金数额。

## 输入描述

输入第一行为一维整型数组M，数组长度小于100，数组元素记录单个商品的价格，单个商品价格小于1000。

输入第二行为购买资金的额度R，R小于100000。

输入格式是正确的，无需考虑格式错误的情况。

## 输出描述

输出为满足上述条件的最大花费额度。

如果不存在满足上述条件的商品，请返回-1。

## 示例1

输入

    
    
    23,26,36,27
    78
    

输出

    
    
    76
    

说明

> 金额23、26和27相加得到76，而且最接近且小于输入金额78。

## 示例2

输入

    
    
    23,30,40
    26
    

输出

    
    
    -1
    

说明

> 因为输入的商品，无法组合出来满足三件之和小于26.故返回-1。

## 解题思路

使用了**暴力搜索** 的方法来解决：

  1. **三重循环** :

     * 通过三个嵌套循环遍历所有可能的三件商品组合。
     * 第一个循环的索引 `i` 从 0 到 `goods.length - 3`，第二个循环的索引 `j` 从 `i + 1` 到 `goods.length - 2`，第三个循环的索引 `k` 从 `j + 1` 到 `goods.length - 1`。这种方式确保每次组合都是不同的三件商品。
  2. **总价计算与筛选** :

     * 在每次内层循环中，计算三件商品的总价 `tmp`。
     * 如果 `tmp` 小于或等于预算 `maxMoney`，则将其加入结果列表 `res`。
  3. **最大值查找** :

     * 如果结果列表 `res` 不为空，则遍历列表找出最大的总价并输出。
     * 如果 `res` 为空，说明没有找到合法的三件商品组合，输出 -1。

## Java

    
    
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            // 创建Scanner对象以读取输入
            Scanner scanner = new Scanner(System.in);
            
            // 读取商品价格输入并分割成字符串数组
            String[] goodsInput = scanner.nextLine().split(",");
            // 创建一个整型数组以存储商品价格
            int[] goods = new int[goodsInput.length];
            
            // 将字符串数组转换为整型数组
            for (int i = 0; i < goodsInput.length; i++) {
                goods[i] = Integer.parseInt(goodsInput[i]);
            }
            
            // 读取预算金额
            int maxMoney = Integer.parseInt(scanner.nextLine());
            // 创建一个列表以存储满足条件的总价
            List<Integer> res = new ArrayList<>();
            
            // 三重循环遍历所有可能的三件商品组合
            for (int i = 0; i < goods.length - 2; i++) {
                for (int j = i + 1; j < goods.length - 1; j++) {
                    for (int k = j + 1; k < goods.length; k++) {
                        // 计算当前三件商品的总价
                        int tmp = goods[i] + goods[j] + goods[k];
                        // 如果总价不超过预算，加入结果列表
                        if (tmp <= maxMoney) {
                            res.add(tmp);
                        }
                    }
                }
            }
            
            // 检查结果列表是否为空
            if (res.size() > 0) {
                // 找到结果列表中的最大值
                int max = res.get(0);
                for (int i = 1; i < res.size(); i++) {
                    if (res.get(i) > max) {
                        max = res.get(i);
                    }
                }
                // 输出最大总价
                System.out.println(max);
            } else {
                // 如果没有找到满足条件的组合，输出 -1
                System.out.println(-1);
            }
        }
    }
    

## Python

    
    
    import sys
    
    # 读取商品价格输入并用逗号分割
    goods_input = input().split(",")
    # 将输入的商品价格转换为整数列表
    goods = [int(x) for x in goods_input]
    # 读取预算金额
    max_money = int(input())
    # 用于存储满足条件的总价
    res = []
    
    # 三重循环遍历所有可能的三件商品组合
    for i in range(len(goods) - 2):
        for j in range(i + 1, len(goods) - 1):
            for k in range(j + 1, len(goods)):
                # 计算当前三件商品的总价
                tmp = goods[i] + goods[j] + goods[k]
                # 如果总价不超过预算，则加入结果列表
                if tmp <= max_money:
                    res.append(tmp)
    
    # 检查结果列表是否为空
    if len(res) > 0:
        # 找到结果列表中的最大总价
        max = res[0]
        for i in range(1, len(res)):
            if res[i] > max:
                max = res[i]
        # 输出最大总价
        print(max)
    else:
        # 如果没有找到满足条件的组合，输出 -1
        print(-1)
    

## JavaScript

    
    
    const readline = require('readline');
    
    // 创建读取接口
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    // 监听第一行输入（商品价格）
    rl.on('line', (goodsInput) => {
      // 将商品价格字符串分割并转换为数字数组
      const goods = goodsInput.split(',').map(Number);
      
      // 监听第二行输入（预算金额）
      rl.on('line', (maxMoneyInput) => {
        // 将预算金额转换为数字
        const maxMoney = Number(maxMoneyInput);
        // 用于存储满足条件的总价
        const res = [];
        
        // 三重循环遍历所有可能的三件商品组合
        for (let i = 0; i < goods.length - 2; i++) {
          for (let j = i + 1; j < goods.length - 1; j++) {
            for (let k = j + 1; k < goods.length; k++) {
              // 计算当前三件商品的总价
              const tmp = goods[i] + goods[j] + goods[k];
              // 如果总价不超过预算，加入结果数组
              if (tmp <= maxMoney) {
                res.push(tmp);
              }
            }
          }
        }
        
        // 检查结果数组是否为空
        if (res.length > 0) {
          // 找到结果数组中的最大值
          let max = res[0];
          for (let i = 1; i < res.length; i++) {
            if (res[i] > max) {
              max = res[i];
            }
          }
          // 输出最大总价
          console.log(max);
        } else {
          // 如果没有找到满足条件的组合，输出 -1
          console.log(-1);
        }
     
      });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <sstream>
    
    using namespace std;
    
    int main() {
        string input;
        // 读取一行输入（商品价格）
        getline(cin, input);
        stringstream ss(input);
        string token;
        vector<int> goods;
        
        // 通过逗号分割输入字符串并转换为整数，存入goods向量
        while (getline(ss, token, ',')) {
            goods.push_back(stoi(token));
        }
        
        int maxMoney;
        // 读取预算金额
        cin >> maxMoney;
        vector<int> res;
        
        // 三重循环遍历所有可能的三件商品组合
        for (int i = 0; i < goods.size() - 2; i++) {
            for (int j = i + 1; j < goods.size() - 1; j++) {
                for (int k = j + 1; k < goods.size(); k++) {
                    // 计算当前三件商品的总价
                    int tmp = goods[i] + goods[j] + goods[k];
                    // 如果总价不超过预算，加入结果向量
                    if (tmp <= maxMoney) {
                        res.push_back(tmp);
                    }
                }
            }
        }
        
        // 检查结果向量是否为空
        if (res.size() > 0) {
            int max = res[0];
            // 找到结果向量中的最大值
            for (int i = 1; i < res.size(); i++) {
                if (res[i] > max) {
                    max = res[i];
                }
            }
            // 输出最大总价
            cout << max << endl;
        } else {
            // 如果没有找到满足条件的组合，输出 -1
            cout << -1 << endl;
        }
        
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int main() {
        char input[1000];
        // 读取一行输入（商品价格）
        fgets(input, sizeof(input), stdin);
        
        int goods[100]; // 假设最多有100件商品
        int goodsCount = 0;
        
        // 通过逗号分割输入字符串并转换为整数，存入goods数组
        char *token = strtok(input, ",");
        while (token != NULL) {
            goods[goodsCount++] = atoi(token);
            token = strtok(NULL, ",");
        }
        
        int maxMoney;
        // 读取预算金额
        scanf("%d", &maxMoney);
        
        int res[100]; // 假设最多有100个结果
        int resCount = 0;
        
        // 三重循环遍历所有可能的三件商品组合
        for (int i = 0; i < goodsCount - 2; i++) {
            for (int j = i + 1; j < goodsCount - 1; j++) {
                for (int k = j + 1; k < goodsCount; k++) {
                    // 计算当前三件商品的总价
                    int tmp = goods[i] + goods[j] + goods[k];
                    // 如果总价不超过预算，加入结果数组
                    if (tmp <= maxMoney) {
                        res[resCount++] = tmp;
                    }
                }
            }
        }
        
        // 检查结果数组是否为空
        if (resCount > 0) {
            int max = res[0];
            // 找到结果数组中的最大值
            for (int i = 1; i < resCount; i++) {
                if (res[i] > max) {
                    max = res[i];
                }
            }
            // 输出最大总价
            printf("%d\n", max);
        } else {
            // 如果没有找到满足条件的组合，输出 -1
            printf("-1\n");
        }
        
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/601a32c70afd8b352fe2b88ebef7115d.png)

## 完整用例

### 用例1

10,20,30,45  
75

### 用例2

23,26,36,27  
78

### 用例3

23,30,40  
26

### 用例4

10,20,30,40,50  
100

### 用例5

5,10,15,20,25  
30

### 用例6

1,2,3,4,5  
7

### 用例7

100,200,300,400,500,600,700,800,900,1000  
1500

### 用例8

15,25,35,45,55  
100

### 用例9

50,60,70,80,90,100,110,120,130,140  
400

### 用例10

10,20,30,40,50,60,70,80,90,100  
500

