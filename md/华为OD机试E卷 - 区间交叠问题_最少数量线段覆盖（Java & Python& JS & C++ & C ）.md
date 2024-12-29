## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定坐标轴上的一组线段，线段的起点和终点均为整数并且长度不小于1，请你从中找到最少数量的线段，这些线段可以覆盖柱所有线段。

## 输入描述

第一行输入为所有线段的数量，不超过10000，后面每行表示一条线段，格式为"x,y"，x和y分别表示起点和终点，取值范围是[-105，105]。

## 输出描述

最少线段数量，为正整数

## 示例1

输入

    
    
    3
    1,4
    2,5
    3,6
    

输出

    
    
    2
    

说明

> ## 解题思路

题目的意思是要你找到一组线段，使得这些线段的数量最少，但能够完全覆盖给定的所有线段。每条线段由两个整数表示，分别为起点和终点，且保证长度不小于1（即起点小于终点）。

#### 示例分析

对于输入：

    
    
    3
    1,4
    2,5
    3,6
    

  * 线段1: 从1到4
  * 线段2: 从2到5
  * 线段3: 从3到6

可以看到，线段1覆盖了部分线段2，线段2又覆盖了部分线段3。实际上，你可以用两条线段来覆盖所有的线段，比如：

  1. 从1到6（覆盖所有线段）
  2. 从2到5（覆盖线段1和线段2）

但最优解是使用线段1（1到4）和线段3（3到6），因此输出为2。

## Java

    
    
    import java.util.Arrays;
    import java.util.LinkedList;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            int n = Integer.parseInt(sc.nextLine());
            int[][] ivs = new int[n][2]; // ivs: intervals
    
            for (int i = 0; i < n; i++) {
                String[] in = sc.nextLine().split(","); // in: input
                ivs[i][0] = Integer.parseInt(in[0]);
                ivs[i][1] = Integer.parseInt(in[1]);
            }
    
            // 排序：先按起点升序，再按终点升序
            Arrays.sort(ivs, (a, b) -> a[0] - b[0]);
    
            LinkedList<int[]> stk = new LinkedList<>(); // stk: stack
            stk.add(ivs[0]);
    
            for (int i = 1; i < ivs.length; i++) {
                int[] cur = ivs[i]; // cur: current interval
    
                while (true) {
                    if (stk.isEmpty()) {
                        stk.add(cur);
                        break;
                    }
    
                    int[] top = stk.getLast();
                    int s0 = top[0], e0 = top[1];
                    int s1 = cur[0], e1 = cur[1];
    
                    if (s1 > e0) { // 不重叠，直接加入
                        stk.add(cur);
                        break;
                    } else if (e1 <= e0) { // 当前范围完全被覆盖，无需操作
                        break;
                    } else if (s1 <= s0) { // 当前范围起点在栈顶前，调整栈顶
                        stk.removeLast();
                    } else { // 部分重叠，合并范围
                        stk.add(new int[]{e0, e1});
                        break;
                    }
                }
            }
    
            System.out.println(stk.size());
        }
    }
    

## Python

    
    
    # 输入处理
    n = int(input().strip())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().strip().split(','))
        intervals.append([start, end])
    
    # 按起点升序排序，若起点相同则按终点升序
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    stk = [intervals[0]]  # 使用列表模拟栈
    
    for i in range(1, len(intervals)):
        cur = intervals[i]
    
        while True:
            if not stk:  # 栈为空，直接加入
                stk.append(cur)
                break
    
            top = stk[-1]  # 获取栈顶元素
            t_start, t_end = top[0], top[1]
            c_start, c_end = cur[0], cur[1]
    
            if c_start > t_end:  # 不重叠，直接加入
                stk.append(cur)
                break
            elif c_end <= t_end:  # 当前范围完全被覆盖，无需操作
                break
            elif c_start <= t_start:  # 当前范围起点在栈顶前，调整栈顶
                stk.pop()
            else:  # 部分重叠，合并范围
                stk.append([t_end, c_end])
                break
    
    # 输出结果
    print(len(stk))
    

## JavaScript

    
    
     // 输入处理
    const readline = require('readline');
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let n;
    const intervals = [];
    
    rl.on('line', (line) => {
        if (n === undefined) {
            n = parseInt(line.trim());
        } else {
            const [start, end] = line.trim().split(',').map(Number);
            intervals.push([start, end]);
    
            if (intervals.length === n) {
                processIntervals();
                rl.close();
            }
        }
    });
    
    function processIntervals() {
        // 按起点升序排序，若起点相同则按终点升序
        intervals.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    
        const stk = [];  // 使用数组模拟栈
    
        for (let i = 0; i < intervals.length; i++) {
            const cur = intervals[i];
    
            while (true) {
                if (stk.length === 0) {  // 栈为空，直接加入
                    stk.push(cur);
                    break;
                }
    
                const top = stk[stk.length - 1];  // 获取栈顶元素
                const [t_start, t_end] = top;
                const [c_start, c_end] = cur;
    
                if (c_start > t_end) {  // 不重叠，直接加入
                    stk.push(cur);
                    break;
                } else if (c_end <= t_end) {  // 当前范围完全被覆盖，无需操作
                    break;
                } else if (c_start <= t_start) {  // 当前范围起点在栈顶前，调整栈顶
                    stk.pop();
                } else {  // 部分重叠，合并范围
                    stk.push([t_end, c_end]);
                    break;
                }
            }
        }
    
        // 输出结果
        console.log(stk.length);
    }
    
    

## C++

    
    
     #include <iostream>
    #include <vector>
    #include <algorithm>
    
    using namespace std;
    
    // 自定义比较函数，用于排序
    bool compare(const pair<int, int>& a, const pair<int, int>& b) {
        return (a.first < b.first) || (a.first == b.first && a.second < b.second);
    }
    
    int main() {
        int n;
        cin >> n;  // 输入数量
        vector<pair<int, int>> intervals(n);
    
        // 输入区间
        for (int i = 0; i < n; i++) {
            char comma;  // 用于读取逗号
            cin >> intervals[i].first >> comma >> intervals[i].second;
        }
    
        // 按起点升序排序，若起点相同则按终点升序
        sort(intervals.begin(), intervals.end(), compare);
    
        vector<pair<int, int>> stk;  // 使用向量模拟栈
    
        for (const auto& cur : intervals) {
            while (true) {
                if (stk.empty()) {  // 栈为空，直接加入
                    stk.push_back(cur);
                    break;
                }
    
                auto top = stk.back();  // 获取栈顶元素
                int t_start = top.first, t_end = top.second;
                int c_start = cur.first, c_end = cur.second;
    
                if (c_start > t_end) {  // 不重叠，直接加入
                    stk.push_back(cur);
                    break;
                } else if (c_end <= t_end) {  // 当前范围完全被覆盖，无需操作
                    break;
                } else if (c_start <= t_start) {  // 当前范围起点在栈顶前，调整栈顶
                    stk.pop_back();
                } else {  // 部分重叠，合并范围
                    stk.push_back({t_end, c_end});
                    break;
                }
            }
        }
    
        // 输出结果
        cout << stk.size() << endl;
        return 0;
    }
    
    

## C语言

    
    
     
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/caff9739150c9de3a3a9819625c5285b.png)

## 完整用例

### 用例1

    
    
    3
    1,2
    3,4
    5,6
    

### 用例2

    
    
    2
    1,5
    1,5
    

### 用例3

    
    
    3
    1,3
    2,5
    4,6
    

### 用例4

    
    
    4
    1,2
    2,3
    3,4
    4,5
    

### 用例5

    
    
    5
    1,4
    3,6
    2,5
    7,9
    8,10
    

### 用例6

    
    
    2
    1,2
    10,11
    

### 用例7

    
    
    6
    1,3
    2,4
    3,5
    6,8
    7,9
    8,10
    

### 用例8

    
    
    2
    1,10
    2,9
    

### 用例9

    
    
    4
    1,4
    2,6
    3,8
    5,7
    

### 用例10

    
    
    5
    1,3
    4,6
    2,5
    3,4
    5,7
    

