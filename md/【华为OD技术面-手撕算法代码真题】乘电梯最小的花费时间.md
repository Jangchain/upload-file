## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 输入
  * 输出
  * 用例1
  * 用例2
  * C++
  * Java
  * javaScript
  * Python

## 题目描述

某公司,每天早上都有很多人去坐电梯,每个人都可能到不同的楼层.同时电梯还有一个容量限制.电梯最多只能带K个人.电梯从第a层到第b层,会花费|a-b|的时间.  
现在有N个人，以及知道每个人想要去的地方，请问如何坐电梯，才能使每个人到达到他们对应的楼层，且所花费时间最少。电梯最后要回到第1层.

## 输入

对于每个输入,先输入两个整数N,K.表示有N个人,以及电梯的容量K.  
接下来一行,有N个整数,f1, f2, … , fn. 表示每个人要到达的地方.  
(1 <= N, K <= 2000, 1 <= fi <= 2000)

## 输出

输出最小的花费时间.

## 用例1

输入

    
    
    5 2
    3 5 2 4 1
    

输出

    
    
    12
    

## 用例2

输入

    
    
    4 1
    1 2 3 4
    

输出

    
    
    12
    

**测试用例1:**

  1. 按降序排列楼层列表：`[5, 4, 3, 2, 1]`。
  2. 根据电梯容量分组：`[[5, 4], [3, 2], [1]]`。
  3. 计算每次行程的时间成本（往返1楼）：`(5 - 1) * 2 + (3 - 1) * 2 + (1 - 1) * 2`。
  4. 计算时间成本总和：`8 + 4 + 0 = 12`。

测试用例1的最小时间成本估算：`12`

**测试用例2:**

  1. 由于电梯每次只能搭载一人，它将简单地将每个人带到他们的楼层然后返回。
  2. 计算每次行程的时间成本（往返1楼）：`(1 - 1) * 2 + (2 - 1) * 2 + (3 - 1) * 2 + (4 - 1) * 2`。
  3. 计算时间成本总和：`0 + 2 + 4 + 6`。

测试用例2的最小时间成本估算：`12`

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    
    int calculateMinTimeCost(std::vector<int> floors, int elevatorCapacity) {
        // 将楼层数组按降序排序
        std::sort(floors.begin(), floors.end(), std::greater<int>());
    
        int timeCost = 0;
        size_t i = 0;
        // 遍历楼层，每次最多搭载电梯容量的人数
        while (i < floors.size()) {
            // 当前行程中最高的楼层
            int highestFloor = floors[i];
            // 移动电梯容量或剩余人数（取较小值）
            i += std::min(elevatorCapacity, static_cast<int>(floors.size() - i));
            // 计算往返1楼的时间成本
            timeCost += (highestFloor - 1) * 2;
        }
    
        return timeCost;
    }
    
    int main() {
        // 测试用例1
        std::vector<int> floorsCase1 = {3, 5, 2, 4, 1};
        int elevatorCapacityCase1 = 2;
        int minCostCase = calculateMinTimeCost(floorsCase1, elevatorCapacityCase1);
        std::cout << minCostCase << std::endl;
    
        return 0;
    }
    

## Java

    
    
     
    
    import java.util.Arrays;
    import java.util.Collections;
    
    public class ElevatorOptimization {
        
        public static void main(String[] args) {
            // 测试用例1
            int[] floorsCase1 = {3, 5, 2, 4, 1};
            int elevatorCapacityCase1 = 2;
            int minCostCase  = calculateMinTimeCost(floorsCase1, elevatorCapacityCase1);
            System.out.println(minCostCase);
            
          
        }
    
        private static int calculateMinTimeCost(int[] floors, int elevatorCapacity) {
            // 将楼层数组按降序排序
            Integer[] sortedFloors = Arrays.stream(floors).boxed().toArray(Integer[]::new);
            Arrays.sort(sortedFloors, Collections.reverseOrder());
    
            int timeCost = 0;
            int i = 0;
            // 遍历楼层，每次最多搭载电梯容量的人数
            while (i < sortedFloors.length) {
                // 当前行程中最高的楼层
                int highestFloor = sortedFloors[i];
                // 移动电梯容量或剩余人数（取较小值）
                i += Math.min(elevatorCapacity, sortedFloors.length - i);
                // 计算往返1楼的时间成本
                timeCost += (highestFloor - 1) * 2;
            }
    
            return timeCost;
        }
    }
    

## javaScript

    
    
    function calculateMinTimeCost(floors, elevatorCapacity) {
        // 将楼层数组按降序排序
        floors.sort((a, b) => b - a);
    
        let timeCost = 0;
        let i = 0;
        // 遍历楼层，每次最多搭载电梯容量的人数
        while (i < floors.length) {
            // 当前行程中最高的楼层
            let highestFloor = floors[i];
            // 移动电梯容量或剩余人数（取较小值）
            i += Math.min(elevatorCapacity, floors.length - i);
            // 计算往返1楼的时间成本
            timeCost += (highestFloor - 1) * 2;
        }
    
        return timeCost;
    }
    
    // 测试用例1
    const floorsCase1 = [3, 5, 2, 4, 1];
    const elevatorCapacityCase1 = 2;
    const minCostCase = calculateMinTimeCost(floorsCase1, elevatorCapacityCase1);
    console.log(minCostCase);
    

## Python

    
    
    def calculate_min_time_cost(floors, elevator_capacity):
        # 将楼层数组按降序排序
        floors.sort(reverse=True)
    
        time_cost = 0
        i = 0
        # 遍历楼层，每次最多搭载电梯容量的人数
        while i < len(floors):
            # 当前行程中最高的楼层
            highest_floor = floors[i]
            # 移动电梯容量或剩余人数（取较小值）
            i += min(elevator_capacity, len(floors) - i)
            # 计算往返1楼的时间成本
            time_cost += (highest_floor - 1) * 2
    
        return time_cost
    
    # 测试用例1
    floors_case1 = [3, 5, 2, 4, 1]
    elevator_capacity_case1 = 2
    min_cost_case = calculate_min_time_cost(floors_case1, elevator_capacity_case1)
    print(min_cost_case)
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 输入
  * 输出
  * 用例1
  * 用例2
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/60398424d5147ca81166e00b60fd3e34.png)

