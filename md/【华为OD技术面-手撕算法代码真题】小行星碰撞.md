## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 注意
  * 题目描述
  * 用例
  * 题解
  * C++
  * Java
  * javaScript
  * Python

## 注意

**本题leetcode原题**

## 题目描述

给定一个整数数组 `asteroids`，表示在同一行的小行星。

对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。

找出碰撞后剩下的所有小行星。碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。如果两颗小行星大小相同，则两颗小行星都会爆炸。两颗移动方向相同的小行星，永远不会发生碰撞。

## 用例

**示例 1：**

    
    
    输入：asteroids = [5,10,-5]
    输出：[5,10]
    解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
    

**示例 2：**

    
    
    输入：asteroids = [8,-8]
    输出：[]
    解释：8 和 -8 碰撞后，两者都发生爆炸。
    

**示例 3：**

    
    
    输入：asteroids = [10,2,-5]
    输出：[10]
    解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
    

**提示：**

  * `2 <= asteroids.length <= 104`
  * `-1000 <= asteroids[i] <= 1000`
  * `asteroids[i] != 0`

## 题解

<https://leetcode.cn/problems/asteroid-collision/solutions/>

## C++

    
    
    class Solution {
    public:
        vector<int> asteroidCollision(vector<int>& asteroids) {
            vector<int> st; // 定义一个 vector 来模拟栈，用于存储当前存活的小行星
            for (auto aster : asteroids) { // 遍历每个小行星
                bool alive = true; // 标记当前小行星是否存活
                while (alive && aster < 0 && !st.empty() && st.back() > 0) {
                    // 当当前小行星向左移动，栈非空，且栈顶小行星向右移动时，可能发生碰撞
                    alive = st.back() < -aster; // 判断栈顶小行星是否会被当前小行星销毁
                    if (st.back() <= -aster) { // 如果栈顶小行星的大小不超过当前小行星的大小
                        st.pop_back(); // 移除栈顶小行星，表示其被销毁
                    }
                }
                if (alive) {
                    st.push_back(aster); // 如果当前小行星存活，则将其加入栈中
                }
            }
            return st; // 返回栈中剩余的小行星，即为碰撞后存活的小行星
        }
    };
    

## Java

    
    
    class Solution {
        public int[] asteroidCollision(int[] asteroids) {
            Deque<Integer> stack = new ArrayDeque<Integer>(); // 使用双端队列作为栈，存储当前存活的小行星
            for (int aster : asteroids) { // 遍历每个小行星
                boolean alive = true; // 标记当前小行星是否存活
                while (alive && aster < 0 && !stack.isEmpty() && stack.peek() > 0) {
                    // 当当前小行星向左移动，栈非空，且栈顶小行星向右移动时，可能发生碰撞
                    alive = stack.peek() < -aster; // 判断栈顶小行星是否会被当前小行星销毁
                    if (stack.peek() <= -aster) { // 如果栈顶小行星的大小不超过当前小行星的大小
                        stack.pop(); // 移除栈顶小行星，表示其被销毁
                    }
                }
                if (alive) {
                    stack.push(aster); // 如果当前小行星存活，则将其加入栈中
                }
            }
            int size = stack.size(); // 获取栈的大小，即存活小行星的数量
            int[] ans = new int[size]; // 创建结果数组
            for (int i = size - 1; i >= 0; i--) { // 填充结果数组
                ans[i] = stack.pop(); // 将栈中小行星依次取出，赋值给结果数组
            }
            return ans; // 返回结果数组
        }
    }
    

## javaScript

    
    
    // 定义小行星碰撞函数
    var asteroidCollision = function(asteroids) {
        const stack = []; // 使用栈来保存当前存活的小行星
        // 遍历每一个小行星
        for (const aster of asteroids) {
            let alive = true; // 假设当前小行星初始状态为存活
            // 当当前小行星向左移动，并且栈不为空，且栈顶小行星向右移动时，可能会发生碰撞
            while (alive && aster < 0 && stack.length > 0 && stack[stack.length - 1] > 0) {
                // 判断当前小行星的大小是否大于栈顶小行星的大小
                alive = stack[stack.length - 1] < -aster; // 如果是，则当前小行星存活，否则被销毁
                // 如果栈顶小行星的大小小于等于当前小行星的大小，则栈顶小行星被销毁
                if (stack[stack.length - 1] <= -aster) {
                    stack.pop();
                }
            }
            // 如果当前小行星存活，则将其加入栈中
            if (alive) {
                stack.push(aster);
            }
        }
        // 根据栈的大小创建结果数组
        const size = stack.length;
        const ans = new Array(size).fill(0);
        // 将栈中的小行星逆序填入结果数组
        for (let i = size - 1; i >= 0; i--) {
            ans[i] = stack.pop();
        }
        // 返回结果数组
        return ans;
    };
    

## Python

    
    
    class Solution:
        def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            st = [] # 使用列表作为栈来保存当前存活的小行星
            # 遍历每一个小行星
            for aster in asteroids:
                alive = True # 假设当前小行星初始状态为存活
                # 当当前小行星向左移动，并且栈不为空，且栈顶小行星向右移动时，可能会发生碰撞
                while alive and aster < 0 and st and st[-1] > 0:
                    # 判断当前小行星的大小是否大于栈顶小行星的大小
                    alive = st[-1] < -aster # 如果是，则当前小行星存活，否则被销毁
                    # 如果栈顶小行星的大小小于等于当前小行星的大小，则栈顶小行星被销毁
                    if st[-1] <= -aster:
                        st.pop()
                # 如果当前小行星存活，则将其加入栈中
                if alive:
                    st.append(aster)
            # 返回栈中剩余的小行星，即为碰撞后存活的小行星
            return st
    

#### 文章目录

  * 华为OD面试真题精选
  * 注意
  * 题目描述
  * 用例
  * 题解
  * C++
  * Java
  * javaScript
  * Python

![fengmian](https://i-blog.csdnimg.cn/blog_migrate/394971cb01fca8d138a4e44d4aeabcf2.png)

