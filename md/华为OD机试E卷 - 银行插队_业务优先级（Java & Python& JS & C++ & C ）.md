## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

某银行将客户分为了若干个优先级， 1 级最高， 5 级最低，当你需要在银行办理业务时，优先级高的人随时可以插队到优先级低的人的前面。

现在给出一个人员到来和银行办理业务的时间序列，请你在每次银行办理业务时输出客户的编号。

如果同时有多位优先级相同且最高的客户，则按照先来后到的顺序办理。

## 输入描述

输入第一行是一个正整数 n ,表示输入的序列中的事件数量。(1 ≤ n ≤ 500)

接下来有 n 行，每行第一个字符为 a 或 p 。

当字符为 a 时，后面会有两个的正整数 num 和 x ,表示到来的客户编号为 num ,优先级为 x ;

当字符为 p 时，表示当前优先级最高的客户去办理业务。

###

## 输出描述

输出包含若干行，对于每个 p ， 输出一行，仅包含一个正整数 num , 表示办理业务的客户编号。

## 示例1

输入

    
    
    4
    a 1 3
    a 2 2
    a 3 2
    p
    

输出

    
    
    2
    

说明

> ## 解题思路

首先要看懂题目！

输入N行 每行代表一个事件，如果是p的话则办理业务，此时输出一个客户编号。可以下面的的用例：

    
    
    8
    a 1 3
    a 2 2
    a 3 2
    p
    a 4 3
    a 5 1
    a 6 2
    p
    

这里有8个事件，每四个人进行一波办理业务，最后输出的结果是【 2，5 】

遇到第一个p，开始给前面三个人办理业务，明显2号优先级最高，输出2

遇到第二个p，开始给前面的2+3=5个人办理业务，明显5号优先级最高，输出5

这里的数量级别很小，只有(1 ≤ n ≤ 500)；我们只需要使用list加上for循环就可以了。

一个二维数组的结构

    
    
    [
        级别1 ：[]
        级别2 ：[]
    .....
    
    ]
    

## Java

    
    
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();
    
            // 客户列表，按照优先级从高到低分别为a[1]~a[5]
            List<List<Integer>> customers = new ArrayList<>();
            for (int i = 0; i < 6; i++){
                customers.add(new ArrayList<>());
            }
    
            // 处理每个操作
            for (int i = 0; i < n; i++) {
                String op = in.next();
                if (op.equals("a")) { // 添加客户
                    int id = in.nextInt();
                    int priority = in.nextInt();
                    customers.get(priority).add(id); // 将客户添加到对应优先级的列表中
                } else { // 处理下一个客户
                    for (int j = 1; j <= 5; j++) { // 从高到低依次遍历客户列表
                        if (!customers.get(j).isEmpty()) { // 如果该优先级的客户列表不为空
                            System.out.println(customers.get(j).remove(0)); // 输出该客户的编号，并从列表中删除
                            break; // 处理完一个客户后结束循环
                        }
                    }
                }
            }
        }
    }
    
    

## Python

    
    
    customers = [[] for _ in range(6)] # 客户列表，按照优先级从高到低分别为customers[1]~customers[5]
    n = int(input())
    
    # 处理每个操作
    for i in range(n):
        op = input().split()
        if op[0] == "a": # 添加客户
            id = int(op[1])
            priority = int(op[2])
            customers[priority].append(id) # 将客户添加到对应优先级的列表中
        else: # 处理下一个客户
            for j in range(1, 6): # 从高到低依次遍历客户列表
                if customers[j]: # 如果该优先级的客户列表不为空
                    print(customers[j].pop(0)) # 输出该客户的编号，并从列表中删除
                    break # 处理完一个客户后结束循环
    
    

## JavaScript

    
    
    const readline = require('readline');
    
     
    const rl = readline.createInterface({
      input: process.stdin,  
      output: process.stdout  
    });
    
     
    let n;
    let customers = Array.from({length: 6}, () => []);
     
    rl.on('line', (line) => {
      // 如果n未定义，则将输入的第一行赋值给n
      if (!n) {
        n = parseInt(line);
      } else {
        // 否则将输入的每一行按空格分割并赋值给op、id和priority
        const [op, id, priority] = line.split(' ');
        // 如果op为'a'，则将id插入到对应的priority的二维数组中
        if (op === 'a') {
          customers[priority].push(parseInt(id));
        } else {
          // 否则遍历优先级1~5的二维数组，找到第一个非空数组并输出其第一个元素，然后将其删除
          for (let j = 1; j <= 5; j++) {
            if (customers[j].length > 0) {
              console.log(customers[j][0]);
              customers[j].shift();
              break;
            }
          }
        }
      }
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    using namespace std;
    
    int main() {
        int n;
        cin >> n;
    
        // 客户列表，按照优先级从高到低分别为a[1]~a[5]
        vector<vector<int>> customers(6);
    
        // 处理每个操作
        for (int i = 0; i < n; i++) {
            char op;
            cin >> op;
            if (op == 'a') { // 添加客户
                int id, priority;
                cin >> id >> priority;
                customers[priority].push_back(id); // 将客户添加到对应优先级的列表中
            } else { // 处理下一个客户
                for (int j = 1; j <= 5; j++) { // 从高到低依次遍历客户列表
                    if (!customers[j].empty()) { // 如果该优先级的客户列表不为空
                        cout << customers[j][0] << endl; // 输出该客户的编号
                        customers[j].erase(customers[j].begin()); // 从列表中删除该客户
                        break; // 处理完一个客户后结束循环
                    }
                }
            }
        }
    
        return 0;
    }
    
    

## C语言

    
    
     #include <stdio.h>
    
    #define MAX_PRIORITY 5
    #define MAX_CUSTOMERS 500
    
    // 定义二维数组存储客户列表，分别为每个优先级的队列，和每个优先级的客户计数
    int customers[MAX_PRIORITY + 1][MAX_CUSTOMERS];
    int customer_count[MAX_PRIORITY + 1] = {0};
    
    int main() {
        int n;
        scanf("%d", &n);
    
        // 处理每个操作
        for (int i = 0; i < n; i++) {
            char op;
            int id, priority;
            scanf(" %c", &op); // 读取操作符
            
            if (op == 'a') { // 添加客户
                scanf("%d %d", &id, &priority);
                int count = customer_count[priority];
                customers[priority][count] = id; // 添加客户到对应优先级的队列
                customer_count[priority]++;      // 更新该优先级的客户数量
            } else if (op == 'p') { // 处理业务
                // 从最高优先级开始查找
                for (int j = 1; j <= MAX_PRIORITY; j++) {
                    if (customer_count[j] > 0) { // 该优先级的客户列表不为空
                        printf("%d\n", customers[j][0]); // 输出客户编号
                        // 移除该客户，将剩下的客户向前移动
                        for (int k = 1; k < customer_count[j]; k++) {
                            customers[j][k - 1] = customers[j][k];
                        }
                        customer_count[j]--; // 更新该优先级的客户数量
                        break;
                    }
                }
            }
        }
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    4
    a 1 3
    a 2 2
    a 3 2
    p
    

### 用例2

    
    
    6
    a 1 3
    a 2 4
    p
    a 3 2
    a 4 5
    p
    

### 用例3

    
    
    5
    a 1 5
    a 2 4
    p
    a 3 5
    p
    

### 用例4

    
    
    7
    a 1 2
    a 2 3
    a 3 2
    a 4 5
    p
    p
    p
    

### 用例5

    
    
    8
    a 1 1
    a 2 1
    p
    a 3 1
    p
    p
    a 4 2
    p
    

### 用例6

    
    
    6
    a 1 3
    a 2 3
    a 3 4
    p
    p
    p
    

### 用例7

    
    
    8
    a 1 3
    a 2 3
    a 3 4
    p
    p
    a 4 5
    p
    p
    

### 用例8

    
    
    6
    a 1 1
    p
    a 2 2
    p
    a 3 1
    p
    

### 用例9

    
    
    10
    a 1 2
    a 2 3
    p
    a 3 3
    a 4 4
    p
    p
    p
    a 5 5
    p
    

### 用例10

    
    
    8
    a 1 5
    a 2 4
    p
    p
    a 3 3
    a 4 5
    p
    p
    

