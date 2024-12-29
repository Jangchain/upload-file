## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 解题思路
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/531481147412447605047d39bc063274.png)

## 题目描述

> **给你一个整数 n，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 n 的** **最简** **分数。分数可以以**
> **任意** **顺序返回。**
>
> **示例 1：**
>  
>  
>     输入：n
>      = 2
>     输出：["1/2"]
>     解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
>  
>
> **示例 2：**
>  
>  
>     输入：n = 3
>     输出：["1/2","1/3","2/3"]
>  

## 解题思路

  1. **遍历所有可能的分母** ：从 2 开始到给定的最大值 n，因为分母为 1 时，分数就变成了 1，不符合最简分数的要求。

  2. **对每个分母遍历所有可能的分子** ：对于每个分母，分子的范围从 1 到该分母的前一个数字，保证分子始终小于分母。

  3. **判断分子和分母是否互质** ：使用最大公约数（GCD）算法来检查分子和分母的最大公约数。如果为 1，则分子和分母互质，即这两个数没有除 1 外的其他公约数。

  4. **生成最简分数** ：如果分子和分母互质，则将它们以分数的形式（“分子/分母”）转换为字符串，并添加到结果容器中。

## C++

    
    
     
    
    class Solution {
    public:
        std::vector<std::string> simplifiedFractions(int n) {
            std::vector<std::string> fractions;
            // 外层循环遍历所有可能的分母，从 2 开始到 n（包括 n），因为分母不能为 1（否则分数为 1，不符合题目要求）
            for (int denominator = 2; denominator <= n; denominator++) {
                // 内层循环遍历所有可能的分子，从 1 开始到分母减 1（不包括分母），保证分子总是小于分母
                for (int numerator = 1; numerator < denominator; numerator++) {
                    // 使用 gcd 函数判断分子和分母的最大公约数是否为 1，如果为 1 则说明此分数为最简分数
                    if (gcd(numerator, denominator) == 1) {
                        // 将最简分数以字符串形式添加到结果列表中
                        fractions.push_back(std::to_string(numerator) + "/" + std::to_string(denominator));
                    }
                }
            }
            return fractions;
        }
    
    private:
        int gcd(int a, int b) {
            // 循环直到 b 为 0，此时 a 就是最大公约数
            while (b != 0) {
                int temp = a % b;  // 计算 a 除以 b 的余数
                a = b;             // 将 b 赋值给 a
                b = temp;          // 将余数赋值给 b，继续循环
            }
            return a;
        }
    };
    

## Java

    
    
    public class Solution {
        /**
         * 此函数用于生成所有分母小于等于 n 的最简分数。
         * @param n 分数的最大分母
         * @return 返回一个包含所有最简分数的字符串列表
         */
        public List<String> simplifiedFractions(int n) {
            // 初始化结果列表，利用 (n-1) * (n/2) 预估可能的分数数量，这样可以减少动态数组扩容的性能损耗。
            List<String> fractions = new ArrayList<>((n - 1) * (n / 2));
            
            // 外层循环遍历所有可能的分母，从 2 开始到 n（包括 n），因为分母不能为 1（否则分数为 1，不符合题目要求）
            for (int denominator = 2; denominator <= n; denominator++) {
                // 内层循环遍历所有可能的分子，从 1 开始到分母减 1（不包括分母），保证分子总是小于分母
                for (int numerator = 1; numerator < denominator; numerator++) {
                    // 使用 gcd 函数判断分子和分母的最大公约数是否为 1，如果为 1 则说明此分数为最简分数
                    if (gcd(numerator, denominator) == 1) {
                        // 将最简分数以字符串形式添加到结果列表中
                        fractions.add(numerator + "/" + denominator);
                    }
                }
            }
            return fractions;
        }
    
        /**
         * 计算两个整数的最大公约数，使用辗转相除法（也称欧几里得算法）。
         * @param a 整数 a
         * @param b 整数 b
         * @return 返回 a 和 b 的最大公约数
         */
        private int gcd(int a, int b) {
            // 循环直到 b 为 0，此时 a 就是最大公约数
            while (b != 0) {
                int temp = a % b;  // 计算 a 除以 b 的余数
                a = b;             // 将 b 赋值给 a
                b = temp;          // 将余数赋值给 b，继续循环
            }
            return a;
        }
    }
    

## javaScript

    
    
    /**
     * @param {number} n
     * @return {string[]}
     */
    var simplifiedFractions = function(n) {
        const fractions = [];
        
        // 外层循环遍历所有可能的分母，从 2 开始到 n（包括 n）
        for (let denominator = 2; denominator <= n; denominator++) {
            // 内层循环遍历所有可能的分子，从 1 开始到分母减 1（不包括分母）
            for (let numerator = 1; numerator < denominator; numerator++) {
                // 使用 gcd 函数判断分子和分母的最大公约数是否为 1，如果为 1 则说明此分数为最简分数
                if (gcd(numerator, denominator) === 1) {
                    // 将最简分数以字符串形式添加到结果数组中
                    fractions.push(`${numerator}/${denominator}`);
                }
            }
        }
        return fractions;
    };
    
    /**
     * 计算两个整数的最大公约数，使用辗转相除法（欧几里得算法）。
     * @param {number} a 整数 a
     * @param {number} b 整数 b
     * @return {number} 返回 a 和 b 的最大公约数
     */
    function gcd(a, b) {
        // 循环直到 b 为 0，此时 a 就是最大公约数
        while (b !== 0) {
            let temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
    

## Python

    
    
    class Solution:
        def simplifiedFractions(self, n):
            """
            此函数用于生成所有分母小于等于 n 的最简分数。
            :param n: 分数的最大分母
            :return: 返回一个包含所有最简分数的字符串列表
            """
            # 初始化结果列表
            fractions = []
            
            # 外层循环遍历所有可能的分母，从 2 开始到 n（包括 n），因为分母不能为 1（否则分数为 1，不符合题目要求）
            for denominator in range(2, n + 1):
                # 内层循环遍历所有可能的分子，从 1 开始到分母减 1（不包括分母），保证分子总是小于分母
                for numerator in range(1, denominator):
                    # 使用 gcd 函数判断分子和分母的最大公约数是否为 1，如果为 1 则说明此分数为最简分数
                    if self.gcd(numerator, denominator) == 1:
                        # 将最简分数以字符串形式添加到结果列表中
                        fractions.append(f"{numerator}/{denominator}")
            
            return fractions
    
        def gcd(self, a, b):
            """
            计算两个整数的最大公约数，使用辗转相除法（也称欧几里得算法）。
            :param a: 整数 a
            :param b: 整数 b
            :return: 返回 a 和 b 的最大公约数
            """
            # 循环直到 b 为 0，此时 a 就是最大公约数
            while b != 0:
                a, b = b, a % b  # 计算 a 除以 b 的余数，并更新 a 和 b
            return a
    

