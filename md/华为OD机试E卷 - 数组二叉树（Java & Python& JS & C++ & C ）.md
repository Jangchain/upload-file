## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

二叉树也可以用数组来存储，给定一个数组，树的根节点的值存储在下标1，对于存储在下标N的节点，它的左子节点和右子节点分别存储在下标2*N和2*N+1，并且我们用值-1代表一个节点为空。

给定一个数组存储的二叉树，试求**从根节点到最小的叶子节点的路径** ，路径由节点的值组成。

## 输入描述

输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分隔。

注意第一个元素即为根节点的值，即数组的第N个元素对应下标N，下标0在树的表示中没有使用，所以我们省略了。

输入的树最多为7层。

## 输出描述

输出从根节点到最小叶子节点的路径上，各个节点的值，由空格分隔，用例保证最小叶子节点只有一个。

## 示例1

输入

    
    
    3 5 7 -1 -1 2 4
    

输出

    
    
    3 7 2
    

说明

> 最小叶子节点的路径为3 7 2。

## 示例2

输入

    
    
    5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
    

输出

    
    
    5 8 7 6
    

说明

> 最小叶子节点的路径为5 8 7 6，注意数组仅存储至最后一个非空节点，故不包含节点“7”右子节点的-1。

## 解题思路

题目的意思是要求你从一个用数组表示的二叉树中找到从根节点到最小叶子节点的路径，并输出该路径上所有节点的值。

  1. **二叉树的数组表示** ：

     * 二叉树的根节点存储在数组的下标1。
     * 对于存储在下标N的节点： 
       * 左子节点存储在下标 (2 \times N)
       * 右子节点存储在下标 (2 \times N + 1)
     * 节点值为-1表示该节点为空。
  2. **叶子节点的定义** ：

     * 叶子节点是没有任何子节点的节点。根据题目，要求找到最小的叶子节点，通常指的是值最小的叶子节点。
  3. **路径的表示** ：

     * 路径由节点的值组成，从根节点到目标叶子节点的顺序连接。

#### 示例分析

##### 示例1：

输入：

    
    
    3 5 7 -1 -1 2 4
    

  * 二叉树结构：

    
    
          3
         / \
        5   7
           / \
          2   4
    

  * 最小叶子节点是2，路径为3 → 7 → 2，输出：

    
    
    3 7 2
    

##### 示例2：

输入：

    
    
    5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
    

  * 二叉树结构：

    
    
          5
         / \
        9   8
             \
              7
               \
                6
    

  * 最小叶子节点是6，路径为5 → 8 → 7 → 6，输出：

    
    
    5 8 7 6
    

## Java

    
    
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Scanner;
    
    public class MinLeafPath {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);   
            String input = scanner.nextLine();  
            String[] inputArray = input.split(" ");  
            List<Integer> arr = new ArrayList<>(); 
    
            // 将输入的数字逐个提取到数组中
            for (String s : inputArray) {
                arr.add(Integer.parseInt(s));  // 将读取的字符串转为整数并添加到数组中
            }
    
            int n = arr.size() - 1;  // 获取数组的有效元素个数（不包括下标0）
            int min = Integer.MAX_VALUE;  // 初始化最小叶子节点的值为最大整数
            int minIdx = -1;  // 初始化最小叶子节点的索引为-1
    
            // 从数组的最后一个元素向前遍历
            for (int i = n; i >= 1; i--) {
                // 检查当前节点是否为叶子节点（无子节点）
                if (arr.get(i) != -1) {  // 仅处理有效节点
                    // 检查右子节点是否存在
                    if (i * 2 + 1 <= n && arr.get(i * 2 + 1) != -1) continue;
                    // 检查左子节点是否存在
                    if (i * 2 + 2 <= n && arr.get(i * 2 + 2) != -1) continue;
                    // 如果当前节点是叶子节点且其值小于当前最小值，则更新最小值和索引
                    if (min > arr.get(i)) {
                        min = arr.get(i);  // 更新最小值
                        minIdx = i;  // 更新最小叶子节点的索引
                    }
                }
            }
    
            List<Integer> path = new ArrayList<>();  // 存储从根节点到最小叶子节点的路径
            path.add(min);  // 将最小叶子节点的值添加到路径中
    
            // 从最小叶子节点向上追溯到根节点
            while (minIdx != 0) {
                int f = (minIdx - 1) / 2;  // 计算父节点的索引
                path.add(arr.get(f));  // 将父节点的值添加到路径中
                minIdx = f;  // 更新当前索引为父节点索引
            }
    
            // 反转路径，使其从根节点到叶子节点的顺序
            for (int i = path.size() - 1; i >= 0; i--) {
                System.out.print(path.get(i) + " ");  // 打印路径中的每个值
            }
            System.out.println();  // 打印换行符
        }
    }
    

## Python

    
    
    import queue  # 导入队列模块
    
    # 读入数组，使用空格分割的输入转换为整数列表
    arr = list(map(int, input().split()))
    n = len(arr) - 1  # 数组长度，减去 1 因为下标从 0 开始
    min_val = float('inf')  # 初始化最小值为无穷大
    min_idx = -1  # 初始化最小值的下标为 -1，表示未找到
    
    # 从后往前遍历数组
    for i in range(n, 0, -1):
        if arr[i] != -1:  # 当前节点不为空
            # 检查左子节点是否存在且不为空，若存在则跳过
            if i * 2 + 1 <= n and arr[i * 2 + 1] != -1:
                continue
            # 检查右子节点是否存在且不为空，若存在则跳过
            if i * 2 + 2 <= n and arr[i * 2 + 2] != -1:
                continue
            # 如果当前节点是叶子节点且值小于当前最小值，则更新最小值和最小值下标
            if min_val > arr[i]:
                min_val = arr[i]  # 更新最小值
                min_idx = i  # 更新最小值下标
    
    # 构造路径
    path = queue.deque()  # 使用双端队列来存储路径
    path.appendleft(min_val)  # 将最小值加入路径的前端
    
    # 从最小叶子节点向上遍历到根节点
    while min_idx != 0:  # 当最小值下标不为 0 时
        f = (min_idx - 1) // 2  # 计算父节点的下标
        path.appendleft(arr[f])  # 将父节点的值加入路径
        min_idx = f  # 更新当前下标为父节点下标
    
    # 输出结果，路径中的节点值以空格分隔
    print(' '.join(map(str, path)))
    

## JavaScript

    
    
    const readline = require('readline');   
    
     
    const rl = readline.createInterface({
      input: process.stdin,   
      output: process.stdout   
    });
    
    // 监听每一行输入
    rl.on('line', (input) => {
      // 将输入的字符串按空格分割，并将每个部分转换为数字，存储在数组 arr 中
      const arr = input.split(' ').map(Number);
      const n = arr.length - 1;  // 获取有效元素个数（不包括下标 0）
      let min = Infinity;  // 初始化最小叶子节点的值为无穷大
      let minIdx = -1;  // 初始化最小叶子节点的索引为 -1
    
      // 从数组的最后一个元素向前遍历
      for (let i = n; i >= 1; i--) {
        // 仅处理有效节点
        if (arr[i] !== -1) {
          // 检查右子节点是否存在
          if (i * 2 + 1 <= n && arr[i * 2 + 1] !== -1) continue;
          // 检查左子节点是否存在
          if (i * 2 + 2 <= n && arr[i * 2 + 2] !== -1) continue;
          // 如果当前节点是叶子节点且其值小于当前最小值，则更新最小值和索引
          if (min > arr[i]) {
            min = arr[i];  // 更新最小值
            minIdx = i;    // 更新最小叶子节点的索引
          }
        }
      }
    
      const path = [];  // 存储从根节点到最小叶子节点的路径
      path.unshift(min);  // 将最小叶子节点的值添加到路径的开头
    
      // 从最小叶子节点向上追溯到根节点
      while (minIdx !== 0) {
        const f = Math.floor((minIdx - 1) / 2);  // 计算父节点的索引
        path.unshift(arr[f]);  // 将父节点的值添加到路径的开头
        minIdx = f;  // 更新当前索引为父节点索引
      }
    
      // 打印路径中的所有节点值，以空格分隔
      console.log(path.join(' '));
    });
    

## C++

    
    
    #include <iostream>    
    #include <vector>     
    #include <sstream>     
    #include <algorithm>  
    #include <climits>     
    
    using namespace std;
    
    int main() {
        string input;   
        getline(cin, input);   
        stringstream ss(input);   
        vector<int> arr;   
        int num;  // 临时变量，用于存储读取的数字
    
        // 将输入的数字逐个提取到数组中
        while (ss >> num) {
            arr.push_back(num);  // 将读取的数字添加到数组中
        }
    
        int n = arr.size() - 1;  // 获取数组的有效元素个数（不包括下标0）
        int min = INT_MAX;  // 初始化最小叶子节点的值为最大整数
        int minIdx = -1;  // 初始化最小叶子节点的索引为-1
    
        // 从数组的最后一个元素向前遍历
        for (int i = n; i >= 1; i--) {
            // 检查当前节点是否为叶子节点（无子节点）
            if (arr[i] != -1) {  // 仅处理有效节点
                // 检查右子节点是否存在
                if (i * 2 + 1 <= n && arr[i * 2 + 1] != -1) continue;
                // 检查左子节点是否存在
                if (i * 2 + 2 <= n && arr[i * 2 + 2] != -1) continue;
                // 如果当前节点是叶子节点且其值小于当前最小值，则更新最小值和索引
                if (min > arr[i]) {
                    min = arr[i];  // 更新最小值
                    minIdx = i;    // 更新最小叶子节点的索引
                }
            }
        }
    
        vector<int> path;  // 存储从根节点到最小叶子节点的路径
        path.push_back(min);  // 将最小叶子节点的值添加到路径中
    
        // 从最小叶子节点向上追溯到根节点
        while (minIdx != 0) {
            int f = (minIdx - 1) / 2;  // 计算父节点的索引
            path.push_back(arr[f]);  // 将父节点的值添加到路径中
            minIdx = f;  // 更新当前索引为父节点索引
        }
    
        // 反转路径，使其从根节点到叶子节点的顺序
        reverse(path.begin(), path.end());
        
        // 输出路径的每个节点值
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] << " ";  // 打印路径中的每个值
        }
        cout << endl;  // 打印换行符
        return 0;  // 返回0表示程序正常结束
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>  // 添加此行以包含 strtok 函数
    #include <limits.h>
    
    int main() {
        char input[1000];  // 用于存储输入的字符串
        fgets(input, sizeof(input), stdin);  // 读取整行输入
    
        int arr[500];  // 假设数组最大容量为 500
        int n = 0;  // 数组有效元素个数
        char *token = strtok(input, " ");  // 分割字符串
    
        // 将输入的数字逐个提取到数组中
        while (token != NULL) {
            arr[n++] = atoi(token);  // 转换为整数并存储
            token = strtok(NULL, " ");  // 继续分割
        }
    
        int min = INT_MAX;  // 初始化最小叶子节点的值为最大整数
        int minIdx = -1;  // 初始化最小叶子节点的索引为 -1
    
        // 从数组的最后一个元素向前遍历
        for (int i = n - 1; i >= 1; i--) {
            // 检查当前节点是否为叶子节点（无子节点）
            if (arr[i] != -1) {  // 仅处理有效节点
                // 检查右子节点是否存在
                if (i * 2 + 1 < n && arr[i * 2 + 1] != -1) continue;
                // 检查左子节点是否存在
                if (i * 2 + 2 < n && arr[i * 2 + 2] != -1) continue;
                // 如果当前节点是叶子节点且其值小于当前最小值，则更新最小值和索引
                if (min > arr[i]) {
                    min = arr[i];  // 更新最小值
                    minIdx = i;    // 更新最小叶子节点的索引
                }
            }
        }
    
        int path[500];  // 存储从根节点到最小叶子节点的路径
        int pathSize = 0;  // 路径的有效长度
        path[pathSize++] = min;  // 将最小叶子节点的值添加到路径中
    
        // 从最小叶子节点向上追溯到根节点
        while (minIdx != 0) {
            int f = (minIdx - 1) / 2;  // 计算父节点的索引
            path[pathSize++] = arr[f];  // 将父节点的值添加到路径中
            minIdx = f;  // 更新当前索引为父节点索引
        }
    
        // 反转路径，使其从根节点到叶子节点的顺序
        for (int i = pathSize - 1; i >= 0; i--) {
            printf("%d ", path[i]);  // 打印路径中的每个值
        }
        printf("\n");  // 打印换行符
        return 0;  // 返回 0 表示程序正常结束
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/e91d0c8fcca605df7edb8710a0fd7981.png)

