## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

静态扫描可以快速识别源代码的缺陷，静态扫描的结果以扫描报告作为输出：

1、文件扫描的成本和文件大小相关，如果文件大小为N，则扫描成本为N个[金币](https://so.csdn.net/so/search?q=%E9%87%91%E5%B8%81&spm=1001.2101.3001.7020)

2、扫描报告的缓存成本和文件大小无关，每缓存一个报告需要M个金币

3、扫描报告缓存后，后继再碰到该文件则不需要扫描成本，直接获取缓存结果

给出源代码文件标识序列和文件大小序列，求解采用合理的缓存策略，最少需要的金币数。

## 输入描述

第一行为缓存一个报告金币数M，L<= M <= 100

第二行为文件标识序列：F1,F2,F3,…,Fn。

第三行为文件大小序列：S1,S2,S3,…,Sn。

备注：

  * 1 <= N <= 10000
  * 1 <= Fi <= 1000
  * 1 <= Si <= 10

## 备注：

  * 采用合理的缓存策略，需要的最少金币数

## 输出描述

可以被两方都到达的聚餐地点数量，行末无空格。

## 示例1

输入

    
    
    5
    1 2 2 1 2 3 4
    1 1 1 1 1 1 1
    

输出

    
    
    7
    

说明

> 7

## 示例2

输入

    
    
    5
    2 2 2 2 2 5 2 2 2
    3 3 3 3 3 1 3 3 3
    

输出

    
    
    9
    

说明

> ## 解题思路

简单的贪心题，对于每一种大小的文件，需要判断的是 **每次都重新扫描的成本** 和 **扫描一次加上缓存的成本** ，选择其中最小的即可。

## Java

    
    
    import java.util.HashMap;
    import java.util.Map;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            
            // 获取输入的缓存金币数
            int m = scanner.nextInt();
            scanner.nextLine(); // 读取行结束符
            
            // 获取文件标识序列
            String[] fileIdStrs = scanner.nextLine().split(" ");
            // 获取文件大小序列
            String[] fileSizeStrs = scanner.nextLine().split(" ");
            
            // 使用 HashMap 存储每个文件的总扫描成本和文件大小
            Map<Integer, Integer> scanCosts = new HashMap<>();
            Map<Integer, Integer> sizes = new HashMap<>();
    
            // 遍历文件标识和文件大小
            for (int i = 0; i < fileIdStrs.length; i++) {
                int fileId = Integer.parseInt(fileIdStrs[i]);
                int fileSize = Integer.parseInt(fileSizeStrs[i]);
                
                // 初始化文件大小
                sizes.putIfAbsent(fileId, fileSize);
                // 累加扫描成本
                scanCosts.put(fileId, scanCosts.getOrDefault(fileId, 0) + fileSize);
            }
    
            int totalCost = 0;
    
            // 计算每个文件的最小成本
            for (int fileId : scanCosts.keySet()) {
                int scanCost = scanCosts.get(fileId);
                int size = sizes.get(fileId);
                // 选择最小成本
                totalCost += Math.min(scanCost, size + m);
            }
    
            // 输出总成本
            System.out.println(totalCost);
        }
    }
    

## Python

    
    
    # 获取输入的缓存金币数和文件标识序列、文件大小序列
    m = int(input())
    file_ids = list(map(int, input().split()))
    file_sizes = list(map(int, input().split()))
    
    # 使用字典存储每个文件的总扫描成本和缓存成本
    costs = {}
    
    # 遍历文件标识列表，统计每个文件的总扫描成本
    for file_id, file_size in zip(file_ids, file_sizes):
        if file_id not in costs:
            costs[file_id] = {'scan_cost': 0, 'size': file_size}
        
        costs[file_id]['scan_cost'] += file_size
    
    total_cost = 0
    
    # 计算每个文件的最小成本
    for file_id, cost_info in costs.items():
        scan_cost = cost_info['scan_cost']
        size = cost_info['size']
        
        # 选择扫描所有出现的该文件或缓存的最低成本
        total_cost += min(scan_cost, size + m)
    
    print(total_cost)
    

## JavaScript

    
    
    const readline = require('readline');
    // 创建readline接口实例
    const rl = readline.createInterface({
      input: process.stdin, // 输入流
      output: process.stdout // 输出流
    });
    
    let m, f_str, s_str;
    // 监听input事件，读取输入数据
    rl.on('line', (input) => {
      // 判断输入的是哪一行数据
      if (!m) {
        m = parseInt(input.trim()); // 缓存一个报告金币数M
      } else if (!f_str) {
        f_str = input.trim(); // 文件标识序列
      } else if (!s_str) {
        s_str = input.trim(); // 文件大小序列
        rl.close(); // 读取完数据，关闭接口实例
      }
    });
    
    // 监听close事件，计算最少需要的金币数
    rl.on('close', () => {
      const f = f_str.split(' ').map(Number); // 将文件标识序列转换为数字数组
      const s = s_str.split(' ').map(Number); // 将文件大小序列转换为数字数组
      const count = new Map(); // 存储文件标识出现的次数
      const size = new Map(); // 存储文件标识对应的文件大小
      for (let i = 0; i < f.length; i++) {
        const k = f[i]; // 获取文件标识
        count.set(k, (count.get(k) || 0) + 1); // 统计文件标识出现的次数
        if (!size.has(k)) {
          size.set(k, s[i]); // 记录文件标识对应的文件大小
        }
      }
      let ans = 0; // 最少需要的金币数
      for (const [k, v] of count.entries()) {
        ans += Math.min(v * size.get(k), size.get(k) + m); // 计算每个文件标识需要的金币数，取最小值
      }
      console.log(ans); // 输出最少需要的金币数
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <unordered_map>
    #include <algorithm>
    
    using namespace std;
    
    int main() {
        int m;
        cin >> m; // 获取缓存金币数
    
        // 文件标识和文件大小序列
        vector<int> fileIds, fileSizes;
        int fileId, fileSize;
    
        // 读取文件标识
        while (cin >> fileId) {
            fileIds.push_back(fileId);
            if (cin.get() == '\n') break; // 检测到换行停止输入
        }
    
        // 读取文件大小
        for (int i = 0; i < fileIds.size(); i++) {
            cin >> fileSize;
            fileSizes.push_back(fileSize);
        }
    
        // 使用哈希表存储扫描成本和文件大小
        unordered_map<int, int> scanCosts, sizes;
    
        // 遍历文件标识和文件大小
        for (int i = 0; i < fileIds.size(); i++) {
            scanCosts[fileIds[i]] += fileSizes[i]; // 累加扫描成本
            sizes[fileIds[i]] = fileSizes[i]; // 存储文件大小
        }
    
        int totalCost = 0;
    
        // 计算每个文件的最小成本
        for (const auto& entry : scanCosts) {
            int id = entry.first;
            int scanCost = entry.second;
            int size = sizes[id];
            totalCost += min(scanCost, size + m); // 选择最小成本
        }
    
        cout << totalCost << endl; // 输出总成本
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    
    #define MAX_FILES 1000 // 假设最大文件数
    
    int main() {
        int m; // 缓存金币数
        scanf("%d", &m); // 读取缓存金币数
    
        int file_ids[MAX_FILES]; // 存储文件标识
        int file_sizes[MAX_FILES]; // 存储文件大小
        int scan_costs[MAX_FILES] = {0}; // 存储每个文件的扫描成本，初始化为0
        int size[MAX_FILES] = {0}; // 存储每个文件的大小，初始化为0
        int count = 0; // 文件计数
    
        // 读取文件标识
        while (scanf("%d", &file_ids[count]) != EOF) {
            count++; // 增加文件计数
            if (getchar() == '\n') break; // 检测到换行停止输入
        }
    
        // 读取文件大小
        for (int i = 0; i < count; i++) {
            scanf("%d", &file_sizes[i]); // 读取文件大小
        }
    
        // 遍历文件标识和大小，计算扫描成本
        for (int i = 0; i < count; i++) {
            int file_id = file_ids[i]; // 获取文件标识
            int file_size = file_sizes[i]; // 获取文件大小
    
            // 更新扫描成本和文件大小
            scan_costs[file_id] += file_size; // 累加扫描成本
            size[file_id] = file_size; // 更新文件大小
        }
    
        int total_cost = 0; // 总成本初始化为0
    
        // 计算每个文件的最小成本
        for (int i = 0; i < MAX_FILES; i++) {
            if (scan_costs[i] > 0) { // 如果该文件存在
                // 计算最小成本，选择扫描成本和大小加上金币数的最小值
                total_cost += (scan_costs[i] < size[i] + m) ? scan_costs[i] : (size[i] + m);
            }
        }
    
        printf("%d\n", total_cost); // 输出总成本
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/62a51e10ad939e48a8af364d5755e057.png)

### 完整用例

### 用例1

    
    
    5
    1 2 2 1 2 3 4
    1 1 1 1 1 1 1
    

### 完整用例

### 用例2

    
    
    5
    2 2 2 2 2 5 2 2 2
    3 3 3 3 3 1 3 3 3
    

### 完整用例

### 用例3

    
    
    10
    1 1 2 2 3
    2 2 3 3 4
    

### 完整用例

### 用例4

    
    
    20
    1 2 3 4
    5 5 5 5
    

### 完整用例

### 用例5

    
    
    15
    1 1 1 2 3
    1 1 1 2 2
    

### 完整用例

### 用例6

    
    
    25
    1 2 3 4 5
    1 2 3 4 5
    

### 完整用例

### 用例7

    
    
    5
    1 2 2 3 3 4
    3 3 3 3 3 3
    

### 完整用例

### 用例8

    
    
    30
    1 1 1 2 2 2 3 3 3
    2 2 2 1 1 1 3 3 3
    

### 完整用例

### 用例9

    
    
    50
    1 2 2 3 3 4
    1 1 1 1 1 1
    

### 完整用例

### 用例10

    
    
    40
    1 1 1 1 1 1 1 1
    5 5 5 5 5 5 5 5
    

