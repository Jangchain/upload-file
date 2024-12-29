## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

在一条笔直的公路上安装了N个路灯，从位置0开始安装，路灯之间间距固定为100米。  
每个路灯都有自己的照明半径，请计算第一个路灯和最后一个路灯之间，无法照明的区间的长度和。

## 输入描述

第一行为一个数N，表示路灯个数，1<=N<=100000  
第二行为N个空格分隔的数，表示路灯的照明半径，1<=照明半径<=100000*100

## 输出描述

第一个路灯和最后一个路灯之间，无法照明的区间的长度和

## 示例1

输入

    
    
    2
    50 50
    

输出

    
    
    0
    

说明

> 路灯1覆盖0-50，路灯2覆盖50-100，路灯1和路灯2之间(0米-100米)无未覆盖的区间。

## 示例2

输入

    
    
    4
    50 70 20 70
    

输出

    
    
    20
    

说明

> 输入说明：  
>  路灯1 覆盖0-50  
>  路灯2 覆盖30-170  
>  路灯3 覆盖180-220  
>  路灯4 覆盖230-370  
>  输出说明  
>  [170,180],[220,230]，两个未覆盖的区间，总里程为20

##

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[][] lights = new int[n][2];
            for (int i = 0; i < n; i++) {
                int radius = sc.nextInt();
                int left = Math.max(i * 100 - radius, 0);
                int right = radius + i * 100;
                lights[i][0] = left;
                lights[i][1] = right;
            }
            List<int[]> intervals = new ArrayList<>();
            int start = lights[0][0];
            int end = lights[0][1];
            for (int i = 1; i < n; i++) {
                if (lights[i][0] > end) {
                    intervals.add(new int[]{start, end});
                    start = lights[i][0];
                    end = lights[i][1];
                } else {
                    end = Math.max(end, lights[i][1]);
                }
            }
            intervals.add(new int[]{start, end});
            int from = intervals.get(0)[1];
            int gap = 0;
            for (int i = 1; i < intervals.size(); i++) {
                int to = intervals.get(i)[0];
                gap += to - from;
                from = intervals.get(i)[1];
            }
            System.out.println(gap);
        }
    }
    

## Python

    
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        tmp = arr[i]
        l = max(i * 100 - tmp, 0)
        r = tmp + i * 100
        arr[i] = [l, r]
    
    start, end = arr[0]
    res = []
    
    for i in range(n):
        if arr[i][0] > end:
            res.append([start, end])
            start, end = arr[i]
        else:
            end = max(end, arr[i][1])
    
    res.append([start, end])
    
    start = res[0][1]
    gap = 0
    
    for i in range(1, len(res)):
        end = res[i][0]
        gap += end - start
        start = res[i][1]
    
    print(gap)
    

## JavaScript

    
    
    const readline = require("readline");
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    
    const lines = [];
    rl.on("line", (line) => {
      lines.push(line);
    
      if (lines.length === 2) {
        let n = lines[0] - 0;
        let arr = lines[1]
          .split(" ")
          .slice(0, n)
          .map((ele, idx) => {
            return [idx * 100 - ele < 0 ? 0 : idx * 100 - ele, ele - 0 + idx * 100];
          })
          .sort((a, b) => a[0] - b[0]);
    
        let gap = 0;
        let [start, end] = arr[0];
        for (let i = 1; i < arr.length; i++) {
          if (arr[i][0] > end) {
            gap += arr[i][0] - end;
            [start, end] = arr[i];
          } else {
            end = Math.max(end, arr[i][1]);
          }
        }
    
        console.log(gap);
    
        lines.length = 0;
      }
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main() {
       // 路灯数量
    int n;
        cin >> n;
        // 存储每个路灯的左右边界
        vector<vector<int>> lights(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            // 输入路灯的照明半径
            int radius;
            cin >> radius;
            // 计算路灯的左右边界
            int left = max(i * 100 - radius, 0);
            int right = radius + i * 100;
            lights[i] = {left, right};
        }
        // 存储不连续的区间
        vector<vector<int>> intervals;
        // 记录当前区间的左右边界
        int start = lights[0][0];
        int end = lights[0][1];
        for (int i = 1; i < n; i++) {
            if (lights[i][0] > end) {
                intervals.push_back({start, end});
                start = lights[i][0];
                end = lights[i][1];
            } else {
                end = max(end, lights[i][1]);
            }
        }
        intervals.push_back({start, end});
        // 计算不连续的区间的长度和
        int from = intervals[0][1];
        int gap = 0;
        for (int i = 1; i < intervals.size(); i++) {
            int to = intervals[i][0];
            gap += to - from;
            from = intervals[i][1];
        }
        cout << gap << endl;
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <limits.h>
    
    #define MAX_LIGHTS 100 // 假设最多有 100 个路灯
    
    int main() {
        // 路灯数量
        int n;
        scanf("%d", &n); // 输入路灯数量
    
        // 存储每个路灯的左右边界
        int lights[MAX_LIGHTS][2]; // 二维数组存储左右边界
    
        for (int i = 0; i < n; i++) {
            // 输入路灯的照明半径
            int radius;
            scanf("%d", &radius);
            // 计算路灯的左右边界
            int left = (i * 100 - radius > 0) ? (i * 100 - radius) : 0; // 左边界，确保不小于0
            int right = radius + i * 100; // 右边界
            lights[i][0] = left; // 存储左边界
            lights[i][1] = right; // 存储右边界
        }
    
        // 存储不连续的区间
        int intervals[MAX_LIGHTS][2]; // 存储不连续区间的数组
        int intervalCount = 0; // 不连续区间计数
    
        // 记录当前区间的左右边界
        int start = lights[0][0];
        int end = lights[0][1];
    
        for (int i = 1; i < n; i++) {
            if (lights[i][0] > end) {
                // 如果当前灯的左边界大于当前区间的右边界，表示不连续
                intervals[intervalCount][0] = start; // 存储当前区间的起始位置
                intervals[intervalCount][1] = end; // 存储当前区间的结束位置
                intervalCount++; // 增加区间计数
    
                // 更新为新区间
                start = lights[i][0];
                end = lights[i][1];
            } else {
                // 更新当前区间的右边界
                end = (end > lights[i][1]) ? end : lights[i][1]; // 取较大值
            }
        }
        // 存储最后一个区间
        intervals[intervalCount][0] = start;
        intervals[intervalCount][1] = end;
        intervalCount++; // 增加区间计数
    
        // 计算不连续的区间的长度和
        int from = intervals[0][1]; // 初始化从第一个区间的右边界开始
        int gap = 0; // 不连续长度和初始化为0
    
        for (int i = 1; i < intervalCount; i++) {
            int to = intervals[i][0]; // 当前区间的左边界
            gap += to - from; // 计算间隙长度
            from = intervals[i][1]; // 更新当前右边界
        }
    
        printf("%d\n", gap); // 输出不连续的区间长度和
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/c5b50d409081a57013db82417f32cc1f.png)

## 完整用例

### 用例1

    
    
    2
    50 50
    

### 用例2

    
    
    4
    50 70 20 70
    

### 用例3

    
    
    3
    100 50 100
    

### 用例4

    
    
    5
    10 20 30 40 50
    

### 用例5

    
    
    6
    150 150 150 150 150 150
    

### 用例6

    
    
    3
    100 0 100
    

### 用例7

    
    
    4
    100 10 10 100
    

### 用例8

    
    
    4  
    30 40 50 60  
    

### 用例9

    
    
    3  
    200 50 200  
    

### 用例10

    
    
    3  
    30 20 30  
    

