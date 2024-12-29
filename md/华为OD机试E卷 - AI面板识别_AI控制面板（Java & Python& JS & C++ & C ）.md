## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

AI识别到面板上有N（1 ≤ N ≤ 100）个指示灯，灯大小一样，任意两个之间无重叠。

由于AI识别误差，每次别到的指示灯位置可能有差异，以4个坐标值描述AI识别的指示灯的大小和位置(左上角x1,y1，右下角x2,y2)，

请输出先行后列排序的指示灯的编号，排序规则：

  1. 每次在尚未排序的灯中挑选最高的灯作为的基准灯，
  2. 找出和基准灯属于同一行所有的灯进行排序。两个灯高低偏差不超过灯半径算同一行（即两个灯坐标的差 ≤ 灯高度的一半）。

​

## 输入描述

第一行为N，表示灯的个数  
接下来N行，每行为1个灯的坐标信息，格式为：

> 编号 x1 y1 2 y2

  * 编号全局唯一
  * 1 ≤ 编号 ≤ 100
  * 0 ≤ x1 < x2 ≤ 1000
  * 0 ≤ y1 < y2 ≤ 1000

## 输出描述

排序后的编号列表，编号之间以空格分隔

## 示例1

输入

    
    
    5
    1 0 0 2 2
    2 6 1 8 3
    3 3 2 5 4
    5 5 4 7 6
    4 0 4 2 6
    

输出

    
    
    1 2 3 4 5
    

说明

> ## 解题思路

题目的要求是将AI识别到的多个指示灯编号进行排序。排序需要遵循以下规则：

  1. **识别灯的位置** ：每个指示灯的坐标信息包含了左上角（x1, y1）和右下角（x2, y2），即灯的边界矩形。灯的位置定义由左上角y1的高度表示，即y1越小，灯越靠上。

  2. **排序的规则** ：排序应当按行顺序排列，具体方法是：

     * **行的定义** ：每次找出尚未排序的灯中最高的灯，作为基准灯，然后找出与该基准灯处于同一行的所有灯。
     * **同一行判定** ：如果两个灯的垂直位置差（y1之间的差）不超过灯高度的一半（高度为y2 - y1），则认为它们处于同一行。
     * **行内排序** ：在确定的同一行中，按列（即x1从小到大）顺序对灯排序。
  3. **输出格式** ：按照上面排序后的编号顺序输出编号，编号之间用空格分隔。

#### 示例解析

给定输入：

    
    
    5
    1 0 0 2 2
    2 6 1 8 3
    3 3 2 5 4
    5 5 4 7 6
    4 0 4 2 6
    

按照题意分析和排序步骤如下：

  * **步骤1** ：找到最高的灯，按y1值最小的灯“1”作为基准灯，判断其他灯是否在同一行。
  * **步骤2** ：找出在基准灯“1”同一行的所有灯，按列顺序（x1值）排序。
  * **重复步骤** ：依次挑选下一行的基准灯，重复同样的过程，直到排序所有灯。

最终输出结果为：

    
    
    1 2 3 4 5
    

## Java

    
    
    import java.util.PriorityQueue;
    import java.util.Comparator;
    import java.util.Scanner;
    import java.util.StringJoiner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int n = Integer.parseInt(sc.nextLine()); // 灯的数量
            PriorityQueue<Light> pqY = new PriorityQueue<>(Comparator.comparingInt(l -> l.y)); // 按y坐标排序
    
            // 读取灯的数据并添加到优先队列
            for (int i = 0; i < n; i++) {
                String[] data = sc.nextLine().split(" "); // 使用 split 分割输入行
                int id = Integer.parseInt(data[0]);
                int x1 = Integer.parseInt(data[1]);
                int y1 = Integer.parseInt(data[2]);
                int x2 = Integer.parseInt(data[3]);
                int y2 = Integer.parseInt(data[4]);
                int cx = (x1 + x2) / 2; // 中心x坐标
                int cy = (y1 + y2) / 2; // 中心y坐标
                int rad = (x2 - x1) / 2; // 半径
                pqY.offer(new Light(id, cx, cy, rad));
            }
    
            StringJoiner result = new StringJoiner(" ");
            PriorityQueue<Light> pqX = new PriorityQueue<>(Comparator.comparingInt(l -> l.x)); // 按x坐标排序
    
            while (!pqY.isEmpty()) {
                Light ref = pqY.poll(); // 当前基准灯
                pqX.offer(ref); // 添加基准灯到当前行
    
                // 查找并添加同一行的灯
                while (!pqY.isEmpty() && Math.abs(pqY.peek().y - ref.y) <= ref.r) {
                    pqX.offer(pqY.poll());
                }
    
                // 输出当前行的灯编号
                while (!pqX.isEmpty()) {
                    result.add(String.valueOf(pqX.poll().id)); // 按x坐标顺序输出同一行的灯编号
                }
            }
    
            System.out.println(result.toString()); // 输出结果
        }
    }
    
    class Light {
        int id;
        int x;
        int y;
        int r;
    
        public Light(int id, int x, int y, int r) {
            this.id = id;
            this.x = x;
            this.y = y;
            this.r = r;
        }
    }
    
    

## Python

    
    
    import sys
    from math import floor
    
    class Light:
        def __init__(self, id, x, y, r):
            self.id = id
            self.x = x
            self.y = y
            self.r = r
    
    # 按 y 坐标排序的比较函数
    def y_comparator(light):
        return light.y
    
    # 按 x 坐标排序的比较函数
    def x_comparator(light):
        return light.x
    
    def main():
        input_lines = sys.stdin.read().strip().split("\n")
        n = int(input_lines[0])  # 灯的数量
        pqY = []  # 按 y 坐标排序的灯队列
    
        # 读取每个灯的坐标
        for i in range(1, n + 1):
            id, x1, y1, x2, y2 = map(int, input_lines[i].split())
            cx = floor((x1 + x2) / 2)  # 中心 x 坐标
            cy = floor((y1 + y2) / 2)  # 中心 y 坐标
            rad = floor((x2 - x1) / 2)  # 半径
            pqY.append(Light(id, cx, cy, rad))
    
        # 按 y 坐标排序
        pqY.sort(key=y_comparator)
    
        result = []
        pqX = []  # 按 x 坐标排序的灯队列
    
        while pqY:
            ref = pqY.pop(0)  # 当前行的基准灯
            pqX.append(ref)  # 将基准灯添加到当前行
    
            # 查找并添加同一行的灯
            i = 0
            while i < len(pqY) and abs(pqY[i].y - ref.y) <= ref.r:
                pqX.append(pqY.pop(i))
            
            # 按 x 坐标排序
            pqX.sort(key=x_comparator)
    
            # 输出当前行的灯编号
            while pqX:
                result.append(str(pqX.pop(0).id))
    
        print(" ".join(result))  # 输出最终结果
    
    if __name__ == "__main__":
        main()
    
    

## JavaScript

    
    
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    class Light {
        constructor(id, x, y, r) {
            this.id = id;
            this.x = x;
            this.y = y;
            this.r = r;
        }
    }
    
    // 按 y 坐标排序的比较函数
    const yComparator = (a, b) => a.y - b.y;
    // 按 x 坐标排序的比较函数
    const xComparator = (a, b) => a.x - b.x;
    
    const input = [];
    rl.on('line', (line) => {
        input.push(line.trim());
    }).on('close', () => {
        const n = parseInt(input[0], 10); // 灯的数量
        const pqY = []; // 按 y 坐标排序的灯队列
    
        // 读取每个灯的坐标
        for (let i = 1; i <= n; i++) {
            const [id, x1, y1, x2, y2] = input[i].split(" ").map(Number);
            const cx = Math.floor((x1 + x2) / 2); // 中心 x 坐标
            const cy = Math.floor((y1 + y2) / 2); // 中心 y 坐标
            const rad = Math.floor((x2 - x1) / 2); // 半径
            pqY.push(new Light(id, cx, cy, rad));
        }
    
        pqY.sort(yComparator); // 按 y 坐标排序
    
        const result = [];
        const pqX = []; // 按 x 坐标排序的灯队列
    
        while (pqY.length > 0) {
            const ref = pqY.shift(); // 当前行的基准灯
            pqX.push(ref); // 将基准灯添加到当前行
    
            // 查找并添加同一行的灯
            let i = 0;
            while (i < pqY.length && Math.abs(pqY[i].y - ref.y) <= ref.r) {
                pqX.push(pqY[i]);
                pqY.splice(i, 1); // 移除当前灯
            }
    
            // 按 x 坐标排序
            pqX.sort(xComparator);
    
            // 输出当前行的灯编号
            while (pqX.length > 0) {
                result.push(pqX.shift().id.toString());
            }
        }
    
        console.log(result.join(" ")); // 输出最终结果
    });
    
    

## C++

    
    
    #include <iostream>
    #include <queue>
    #include <vector>
    #include <cmath>
    #include <string>
    #include <sstream>
    using namespace std;
    
    // 灯对象结构体，包含 id, x 坐标, y 坐标 和 半径 r
    struct Light {
        int id, x, y, r;
        Light(int id, int x, int y, int r) : id(id), x(x), y(y), r(r) {}
    };
    
    // y 坐标排序的比较器
    struct CompareY {
        bool operator()(const Light& a, const Light& b) {
            return a.y > b.y;
        }
    };
    
    // x 坐标排序的比较器
    struct CompareX {
        bool operator()(const Light& a, const Light& b) {
            return a.x > b.x;
        }
    };
    
    int main() {
        int n;
        cin >> n; // 读取灯的数量
        priority_queue<Light, vector<Light>, CompareY> pqY; // 按 y 坐标排序的优先队列
    
        // 读取灯的数据并添加到优先队列
        for (int i = 0; i < n; ++i) {
            int id, x1, y1, x2, y2;
            cin >> id >> x1 >> y1 >> x2 >> y2;
            int cx = (x1 + x2) / 2; // 中心 x 坐标
            int cy = (y1 + y2) / 2; // 中心 y 坐标
            int rad = (x2 - x1) / 2; // 半径
            pqY.push(Light(id, cx, cy, rad)); // 将灯对象加入到 y 坐标优先队列
        }
    
        stringstream result;
        priority_queue<Light, vector<Light>, CompareX> pqX; // 按 x 坐标排序的优先队列
    
        // 处理每一行灯
        while (!pqY.empty()) {
            Light ref = pqY.top();
            pqY.pop();
            pqX.push(ref);
    
            // 查找并添加同一行的灯
            while (!pqY.empty() && abs(pqY.top().y - ref.y) <= ref.r) {
                pqX.push(pqY.top());
                pqY.pop();
            }
    
            // 输出当前行的灯编号
            while (!pqX.empty()) {
                result << pqX.top().id << " ";
                pqX.pop();
            }
        }
    
        cout << result.str() << endl; // 输出最终结果
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <math.h>
    
    #define MAX_LIGHTS 1000 // 假设最多有 1000 盏灯
    
    // 定义灯的结构体，包含 id, x 坐标, y 坐标 和 半径 r
    typedef struct {
        int id;
        int x;
        int y;
        int r;
    } Light;
    
    // 按 y 坐标排序的比较函数，用于 qsort
    int compareByY(const void *a, const void *b) {
        return ((Light *)a)->y - ((Light *)b)->y;
    }
    
    // 按 x 坐标排序的比较函数，用于 qsort
    int compareByX(const void *a, const void *b) {
        return ((Light *)a)->x - ((Light *)b)->x;
    }
    
    int main() {
        int n; // 灯的数量
        Light lights[MAX_LIGHTS]; // 存储灯的数组
        Light rowLights[MAX_LIGHTS]; // 存储同一行的灯
    
        // 读取灯的数量
        scanf("%d", &n);
    
        // 读取每个灯的数据
        for (int i = 0; i < n; i++) {
            int id, x1, y1, x2, y2;
            scanf("%d %d %d %d %d", &id, &x1, &y1, &x2, &y2);
    
            int cx = (x1 + x2) / 2; // 计算中心 x 坐标
            int cy = (y1 + y2) / 2; // 计算中心 y 坐标
            int rad = (x2 - x1) / 2; // 计算半径 r
    
            lights[i] = (Light){id, cx, cy, rad}; // 将灯信息存入数组
        }
    
        // 对灯数组按 y 坐标排序
        qsort(lights, n, sizeof(Light), compareByY);
    
        int result[MAX_LIGHTS]; // 存储结果灯的 ID 的数组
        int resultIndex = 0;    // 结果数组的索引
    
        int i = 0;
        while (i < n) {
            int rowCount = 0; // 当前行灯的数量
    
            Light ref = lights[i]; // 基准灯
            rowLights[rowCount++] = ref; // 将基准灯添加到当前行
            i++;
    
            // 查找并添加同一行的灯（基于 y 坐标和半径范围判断）
            while (i < n && abs(lights[i].y - ref.y) <= ref.r) {
                rowLights[rowCount++] = lights[i];
                i++;
            }
    
            // 对当前行的灯按 x 坐标排序
            qsort(rowLights, rowCount, sizeof(Light), compareByX);
    
            // 按顺序将当前行的灯编号添加到结果
            for (int j = 0; j < rowCount; j++) {
                result[resultIndex++] = rowLights[j].id;
            }
        }
    
        // 输出所有灯的编号
        for (int i = 0; i < resultIndex; i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    5
    1 0 0 2 2
    2 6 1 8 3
    3 3 2 5 4
    5 5 4 7 6
    4 0 4 2 6
    

### 用例2

    
    
    4
    1 0 0 3 3
    2 4 1 7 4
    3 8 5 10 7
    4 1 5 3 7
    

### 用例3

    
    
    6
    1 1 1 4 4
    2 2 5 5 8
    3 7 7 9 9
    4 0 10 3 13
    5 4 5 6 8
    6 8 10 11 13
    

### 用例4

    
    
    3
    1 0 0 2 2
    2 3 0 5 2
    3 6 1 8 3
    

### 用例5

    
    
    7
    1 0 0 2 2
    2 3 0 5 2
    3 6 0 8 2
    4 1 3 4 6
    5 5 3 8 6
    6 2 7 5 10
    7 6 7 9 10
    

### 用例6

    
    
    4
    1 0 0 4 4
    2 5 0 9 4
    3 10 0 14 4
    4 0 5 4 9
    

### 用例7

    
    
    8
    1 0 0 3 3
    2 4 1 7 4
    3 1 4 3 6
    4 5 5 8 8
    5 2 7 4 10
    6 6 9 9 12
    7 0 10 3 13
    8 4 13 6 16
    

### 用例8

    
    
    5
    1 1 1 3 3
    2 2 2 4 4
    3 5 5 7 7
    4 8 8 10 10
    5 6 6 9 9
    

### 用例9

    
    
    6
    1 0 0 2 2
    2 3 0 5 2
    3 1 3 3 5
    4 4 3 6 5
    5 2 6 4 8
    6 5 6 7 8
    

### 用例10

    
    
    7
    1 1 1 5 5
    2 6 1 10 5
    3 11 1 15 5
    4 2 6 6 10
    5 7 6 11 10
    6 12 6 16 10
    7 0 11 4 15
    

