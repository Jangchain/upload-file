## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

部门组织绿岛骑行团建活动。租用公共双人自行车，每辆自行车最多坐两人，最大载重M。  
给出部门每个人的体重，请问最多需要租用多少双人自行车。

## 输入描述

第一行两个数字m、n，分别代表自行车限重，部门总人数。

第二行，n个数字，代表每个人的体重，体重都小于等于自行车限重m。

  * `0<m<=200`
  * `0<n<=1000000`

## 输出描述

最小需要的双人自行车数量。

## 示例1

输入

    
    
    3 4 
    3 2 2 1 
    
    

输出

    
    
    3          
    
    

说明

> ## 解题思路

#### 示例

**输入** ：

    
    
    3 4 
    3 2 2 1 
    

**输出** ：

    
    
    3
    

**解释** ：

  * 自行车的最大载重为 `3`，部门共有 `4` 个人，体重分别为 `[3, 2, 2, 1]`。
  * 为了使自行车的数量最少，可以将体重较轻的人和体重较重的人配对，使得他们共享一辆自行车： 
    * 第 1 辆车：体重为 `3` 的人独自乘坐（总重 `3`）。
    * 第 2 辆车：体重为 `2` 和 `1` 的人一起乘坐（总重 `3`）。
    * 第 3 辆车：另一个体重为 `2` 的人独自乘坐（总重 `2`）。

因此，最少需要 **3 辆双人自行车** 。

#### 解题思路

这道题的核心是要在满足最大载重的前提下，**将两个人尽量配对** ，以减少使用的自行车数量。可以采用**双指针** 的方法来解决问题：

  1. **对体重数组进行排序** ，从最轻到最重排列。
  2. 使用两个指针，一个指向体重最轻的人（左指针 `left`），一个指向体重最重的人（右指针 `right`）。
  3. 每次尝试将最轻的人（左指针）和最重的人（右指针）配对： 
     * 如果两个人的体重之和小于或等于 `M`，则他们可以共用一辆自行车，双指针同时向中间移动。
     * 如果两个人的体重之和超过 `M`，则最重的人独自使用一辆自行车，只移动右指针。
  4. 重复上述步骤，直到所有人都被分配到自行车上。
  5. 统计最少需要的自行车数量。

## Java

    
    
    import java.util.*;
    import java.util.stream.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            // 读取自行车限重和部门总人数，并按空格分割
            String[] firstLine = sc.nextLine().split(" ");
            int maxWeight = Integer.parseInt(firstLine[0]); // 自行车限重
            int numPeople = Integer.parseInt(firstLine[1]); // 部门总人数
    
            // 使用map将体重数据整行读取并转换为int数组
            int[] weights = Arrays.stream(sc.nextLine().split(" "))
                                  .mapToInt(Integer::parseInt)
                                  .toArray();
    
            // 排序体重数组
            Arrays.sort(weights);
    
            int bikeCount = 0;
            int lightest = 0;
            int heaviest = numPeople - 1;
    
            // 使用双指针进行配对
            while (lightest <= heaviest) {
                // 如果体重最轻和最重的两人能共乘一辆自行车
                if (weights[lightest] + weights[heaviest] <= maxWeight) {
                    lightest++;
                }
                // 无论是否配对，最重的人都需要单独使用一辆自行车
                heaviest--;
                bikeCount++;
            }
    
            // 输出最少需要的自行车数量
            System.out.println(bikeCount);
        }
    }
    

## Python

    
    
    # 导入必要的模块
    def main():
        # 读取自行车限重和部门总人数
        first_line = input().strip().split()
        max_weight = int(first_line[0])  # 自行车限重
        num_people = int(first_line[1])  # 部门总人数
    
        # 读取每个人的体重数据，转换为整数列表
        weights = list(map(int, input().strip().split()))
    
        # 对体重数组进行排序
        weights.sort()
    
        bike_count = 0  # 需要的自行车数量
        lightest = 0  # 最轻体重人员索引
        heaviest = num_people - 1  # 最重体重人员索引
    
        # 使用双指针算法进行配对
        while lightest <= heaviest:
            # 如果最轻和最重的两人能共用一辆自行车
            if weights[lightest] + weights[heaviest] <= max_weight:
                lightest += 1  # 最轻体重的人员已分配
            heaviest -= 1  # 最重体重的人员已分配
            bike_count += 1  # 分配一辆自行车
    
        # 输出最少需要的自行车数量
        print(bike_count)
    
    if __name__ == "__main__":
        main()
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.on('line', (input) => {
        const [maxWeight, numPeople] = input.split(' ').map(Number); // 自行车限重和部门总人数
        rl.on('line', (inputWeights) => {
            const weights = inputWeights.split(' ').map(Number); // 存储每个人的体重
    
            // 将体重从小到大排序
            weights.sort((a, b) => a - b);
    
            let bikeCount = 0; // 所需自行车数量
            let lightest = 0; // 指向体重最小的人的索引
            let heaviest = numPeople - 1; // 指向体重最大的人的索引
    
            // 当lightest小于等于heaviest时，说明还有人未配对
            while (lightest <= heaviest) {
                // 如果lightest和heaviest的体重之和小于等于自行车限重，则他们可以共享一辆自行车
                if (weights[lightest] + weights[heaviest] <= maxWeight) {
                    lightest++;
                }
                // 无论lightest和heaviest是否配对，heaviest都要向前移动
                heaviest--;
    
                // 每次循环都需要租用一辆自行车
                bikeCount++;
            }
    
            // 输出所需自行车数量
            console.log(bikeCount);
            rl.close();
        });
    });
    
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm> // std::sort
    
    using namespace std;
    
    int main() {
        // 读取自行车限重和部门总人数
        int maxWeight, numPeople;
        cin >> maxWeight >> numPeople;
    
        vector<int> weights(numPeople);
        
        // 读取每个人的体重
        for (int i = 0; i < numPeople; i++) {
            cin >> weights[i];
        }
    
        // 对体重数组进行排序
        sort(weights.begin(), weights.end());
    
        int bikeCount = 0; // 需要的自行车数量
        int lightest = 0;  // 最轻体重人员索引
        int heaviest = numPeople - 1; // 最重体重人员索引
    
        // 使用双指针算法进行配对
        while (lightest <= heaviest) {
            // 如果最轻和最重的两人能共用一辆自行车
            if (weights[lightest] + weights[heaviest] <= maxWeight) {
                lightest++; // 最轻体重的人员已分配
            }
            heaviest--; // 最重体重的人员已分配
            bikeCount++; // 分配一辆自行车
        }
    
        // 输出最少需要的自行车数量
        cout << bikeCount << endl;
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h> // qsort函数
    
    // 比较函数，用于qsort排序
    int compare(const void *a, const void *b) {
        return (*(int *)a - *(int *)b);
    }
    
    int main() {
        int maxWeight, numPeople;
    
        // 读取自行车限重和部门总人数
        scanf("%d %d", &maxWeight, &numPeople);
    
        int weights[numPeople];
    
        // 读取每个人的体重
        for (int i = 0; i < numPeople; i++) {
            scanf("%d", &weights[i]);
        }
    
        // 对体重数组进行排序
        qsort(weights, numPeople, sizeof(int), compare);
    
        int bikeCount = 0; // 需要的自行车数量
        int lightest = 0;  // 最轻体重人员索引
        int heaviest = numPeople - 1; // 最重体重人员索引
    
        // 使用双指针算法进行配对
        while (lightest <= heaviest) {
            // 如果最轻和最重的两人能共用一辆自行车
            if (weights[lightest] + weights[heaviest] <= maxWeight) {
                lightest++; // 最轻体重的人员已分配
            }
            heaviest--; // 最重体重的人员已分配
            bikeCount++; // 分配一辆自行车
        }
    
        // 输出最少需要的自行车数量
        printf("%d\n", bikeCount);
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/f9f192db11718872a4792a03cc8b085c.png)

### 完整用例

### 用例1

    
    
    3 4
    3 2 2 1
    

### 用例2

    
    
    100 5
    50 50 50 50 50
    

### 用例3

    
    
    200 4
    100 100 100 100
    

### 用例4

    
    
    100 3
    30 40 70
    

### 用例5

    
    
    150 6
    60 80 90 50 70 100
    

### 用例6

    
    
    200 2
    100 200
    

### 用例7

    
    
    100 7
    20 30 40 50 60 70 80
    

### 用例8

    
    
    150 5
    60 70 80 90 100
    

### 用例9

    
    
    100 8
    20 30 40 50 60 70 80 90
    

### 用例10

    
    
    100 6
    10 20 30 40 50 60
    

