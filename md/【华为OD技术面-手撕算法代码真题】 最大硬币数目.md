#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * C++
  * Java
  * javaScript
  * Python

## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

## 题目描述

> 有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：
>
>   * 每一轮中，你将会选出 **任意** 3 堆硬币（不一定连续）。
>   * Alice 将会取走硬币数量最多的那一堆。
>   * 你将会取走硬币数量第二多的那一堆。
>   * Bob 将会取走最后一堆。
>   * 重复这个过程，直到没有更多硬币。
>

>
> 给你一个整数数组 `piles` ，其中 `piles[i]` 是第 `i` 堆中硬币的数目。
>
> 返回你可以获得的最大硬币数目。
>
> **示例 1：**
>  
>  
>     输入：piles = [2,4,1,2,7,8]
>     输出：9
>     解释：选出 (2, 7, 8) ，Alice 取走 8 枚硬币的那堆，你取走 7 枚硬币的那堆，Bob 取走最后一堆。
>     选出 (1, 2, 4) , Alice 取走 4 枚硬币的那堆，你取走 2 枚硬币的那堆，Bob 取走最后一堆。
>     你可以获得的最大硬币数目：7 + 2 = 9.
>     考虑另外一种情况，如果选出的是 (1, 2, 8) 和 (2, 4, 7) ，你就只能得到 2 + 4 = 6 枚硬币，这不是最优解。
>  
>
> **示例 2：**
>  
>  
>     输入：piles = [2,4,5]
>     输出：4
>  
>
> **示例 3：**
>  
>  
>     输入：piles = [9,8,7,6,5,1,2,3,4]
>     输出：18
>  
>
> **提示：**
>
>   * `3 <= piles.length <= 10^5`
>   * `piles.length % 3 == 0`
>   * `1 <= piles[i] <= 10^4`
>

## C++

    
    
    class Solution {
    public:
        /**
         * 计算你在分配硬币过程中可以获得的最大硬币数目。
         * 分配硬币的规则是：每轮你选择任意 3 堆硬币，然后按照从大到小的顺序，分别由 Alice、你和 Bob 各自选择一堆。
         * Alice 总是选择最多的那一堆硬币，你选择第二多的，Bob 选择第三多的。重复该过程直到没有更多硬币。
         * 本函数计算你可以获得的最大硬币数目。
         * 
         * @param piles - 包含硬币数目的向量，每个元素代表一堆硬币的数量。
         * @return int - 你可以获得的最大硬币数目。
         */
        int maxCoins(vector<int>& piles) {
            sort(piles.begin(), piles.end()); // 对硬币堆进行升序排序
            
            int length = piles.size(); // 数组的长度，即堆的总数
            int rounds = length / 3; // 分 3 堆为一组，所以一共需要进行的轮数为总长度除以 3
            int coins = 0; // 用于累计你获得的硬币总数
            int index = length - 2; // 开始的索引设定为倒数第二个元素，因为这是每组中的第二大堆
            
            // 进行多轮选择，每轮选择 3 堆硬币
            for (int i = 0; i < rounds; i++) {
                coins += piles[index]; // 你在每轮中获得第二多的那一堆硬币
                index -= 2; // 每完成一轮，索引需要向前移动两位，以选择下一组的第二多硬币
            }
            
            // 返回你所获得的最大硬币数目
            return coins;
        }
    };
    

## Java

    
    
    class Solution {
        /**
         * 计算你在分配硬币过程中可以获得的最大硬币数目。
         * 分配硬币的规则是：每轮你选择任意 3 堆硬币，然后按照从大到小的顺序，分别由 Alice、你和 Bob 各自选择一堆。
         * Alice 总是选择最多的那一堆硬币，你选择第二多的，Bob 选择第三多的。重复该过程直到没有更多硬币。
         * 本函数计算你可以获得的最大硬币数目。
         * 
         * @param piles - 包含硬币数目的数组，每个元素代表一堆硬币的数量。
         * @return int - 你可以获得的最大硬币数目。
         */
        public int maxCoins(int[] piles) {
            Arrays.sort(piles); // 对硬币堆进行排序
            
            int length = piles.length; // 数组的长度，即堆的总数
            int rounds = length / 3; // 分 3 堆为一组，所以一共需要进行的轮数为总长度除以 3
            int coins = 0; // 用于累计你获得的硬币总数
            int index = length - 2; // 开始的索引设定为倒数第二个元素，因为这是每组中的第二大堆
            
            // 进行多轮选择，每轮选择 3 堆硬币
            for (int i = 0; i < rounds; i++) {
                coins += piles[index]; // 你在每轮中获得第二多的那一堆硬币
                index -= 2; // 每完成一轮，索引需要向前移动两位，以选择下一组的第二多硬币
            }
            
            // 返回你所获得的最大硬币数目
            return coins;
        }
    }
    

## javaScript

    
    
    /**
     * 给定一个包含 3n 堆硬币的数组，计算你在分配硬币过程中可以获得的最大硬币数目。
     * 分配硬币的规则是：每轮你选择任意 3 堆硬币，然后按照从大到小的顺序，分别由 Alice、你和 Bob 各自选择一堆。
     * Alice 总是选择最多的那一堆硬币，你选择第二多的，Bob 选择第三多的。重复该过程直到没有更多硬币。
     * 本函数计算你可以获得的最大硬币数目。
     *
     * @param {number[]} piles - 包含硬币数目的数组，每个元素代表一堆硬币的数量。
     * @return {number} - 你可以获得的最大硬币数目。
     */
    var maxCoins = function(piles) {
        // 先对数组进行升序排序，以方便选择最大的堆。
        piles.sort((a, b) => a - b);
        
        // 数组的长度，即堆的总数。
        const length = piles.length;
    
        // 分 3 堆为一组，所以一共需要进行的轮数为总长度除以 3。
        const rounds = Math.floor(length / 3);
    
        // 用于累计你获得的硬币总数。
        let coins = 0;
    
        // 开始的索引设定为倒数第二个元素，因为这是每组中的第二大堆。
        let index = length - 2;
    
        // 进行多轮选择，每轮选择 3 堆硬币。
        for (let i = 0; i < rounds; i++) {
            // 你在每轮中获得第二多的那一堆硬币。
            coins += piles[index];
    
            // 每完成一轮，索引需要向前移动两位，以选择下一组的第二多硬币。
            index -= 2;
        }
    
        // 返回你所获得的最大硬币数目。
        return coins;
    };
    

## Python

    
    
    class Solution:
        def maxCoins(self, piles: List[int]) -> int:
            n = len(piles) # 获取堆的总数
            piles.sort() # 对堆进行排序
            return sum(piles[n // 3 :: 2]) # 返回你可以获得的最大硬币数目
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/c98271d3c8a9c618fe43222034119f4a.png)

