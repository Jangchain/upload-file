![doutub_gif](https://i-blog.csdnimg.cn/blog_migrate/e9413fcd109f2f3d7297192eab0c0b2a.gif)

## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

大家好！今天我给大家推荐一份备受赞誉的华为OD技术面试手撕算法代码真题。 所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 题目
  * 用例
  *     * 示例 1：
    * 示例 2：
    * 示例 3：
  * 提示：
  * 题解 - 动态规划
  * Java
  * C++代码：
  * Python代码：
  * JavaScript代码：

## 题目

​ 给你一个字符串，现在你需要将它进行分割，使得每个子串都是回文，求最少需要分割的次数。

​ 例如，对于字符串 “abaedaba”，至少需要进行三次切分，将它切分为 {“aba”, “e”, “d”, “aba”} 才能使得每个子串都是回文。

## 用例

### 示例 1：

输入：s = “aab”  
输出：1  
解释：只需一次分割就可将 s 分割成 [“aa”,“b”] 这样两个回文子串。

### 示例 2：

输入：s = “a”  
输出：0

### 示例 3：

输入：s = “ab”  
输出：1

## 提示：

    
    
    1 <= s.length <= 2000
    s 仅由小写英文字母组成
    

## 题解 - 动态规划

我们设定 f[i] 代表字符串前缀 s[0…i] 的最少分割次数。为了得出 f[i] 的值，我们可以尝试枚举 s[0…i]
分割出的最后一个回文串，这样我们就可以写出状态转移方程：

f[i] = min {f[j]} + 1 (0 ≤ j < i)，其中 s[j+1…i] 是一个回文串。

这意味着我们枚举最后一个回文串的起始位置 j+1，保证 s[j+1…i] 是一个回文串，那么 f[i] 就可以从 f[j] 转移而来，附加 1
次额外的分割次数。

需要注意的是，我们在上面的状态转移方程中，还少考虑了一种情况，即 s[0…i] 本身就是一个回文串。此时其不需要进行任何分割，即：f[i] = 0。

那么我们如何知道 s[j+1…i] 或者 s[0…i] 是否为回文串呢？我们可以使用预处理方法，将字符串 s 的每个子串是否为回文串预先计算出来，即：

设 g(i,j) 表示 s[i…j] 是否为回文串，那么有状态转移方程：

g(i,j) = True, 当 i ≥ j  
g(i,j) = g(i+1,j−1) ∧ (s[i]=s[j]), 其他情况

其中 ∧ 表示逻辑与运算，即 s[i…j] 为回文串，当且仅当其为空串（i>j），其长度为 1（i=j），或者首尾字符相同且 s[i+1…j−1]
为回文串。

这样一来，我们只需要 O(1) 的时间就可以判断任意 s[i…j] 是否为回文串了。通过动态规划计算出所有的 f 值之后，最终的答案即为 f[n−1]，其中
n 是字符串 s 的长度。

## Java

    
    
    import java.util.Arrays;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            // 创建Scanner对象用于获取用户输入
            Scanner scanner = new Scanner(System.in);
            // 读取用户输入的字符串
            String s = scanner.nextLine();
            // 调用minCut方法计算最小分割次数
            int result =  minCut(s);
            // 输出结果
            System.out.println(result);
        }
    
        public static int minCut(String s) {
            // 获取字符串长度
            int n = s.length();
            // 创建二维布尔数组，用于存储字符串的每个子串是否为回文串
            boolean[][] g = new boolean[n][n];
            for (int i = 0; i < n; ++i) {
                // 初始化二维布尔数组，假设所有子串都是回文串
                Arrays.fill(g[i], true);
            }
    
            // 通过动态规划计算出字符串的每个子串是否为回文串
            for (int i = n - 1; i >= 0; --i) {
                for (int j = i + 1; j < n; ++j) {
                    g[i][j] = s.charAt(i) == s.charAt(j) && g[i + 1][j - 1];
                }
            }
    
            // 创建数组，用于存储字符串的前缀的最少分割次数
            int[] f = new int[n];
            // 初始化数组，假设所有前缀的最少分割次数都是最大值
            Arrays.fill(f, Integer.MAX_VALUE);
            for (int i = 0; i < n; ++i) {
                // 如果字符串的前缀是回文串，那么最少分割次数为0
                if (g[0][i]) {
                    f[i] = 0;
                } else {
                    // 否则，通过动态规划计算出最少分割次数
                    for (int j = 0; j < i; ++j) {
                        if (g[j + 1][i]) {
                            f[i] = Math.min(f[i], f[j] + 1);
                        }
                    }
                }
            }
    
            // 返回字符串的最少分割次数
            return f[n - 1];
        }
    }
    
    
    
    
    

## C++代码：

    
    
    #include <iostream>
    #include <vector>
    #include <string>
    #include <algorithm>
    #include <climits>
    
    using namespace std;
    
    // 计算最小分割次数的函数
    int minCut(string s) {
        int n = s.size();
        vector<vector<bool>> g(n, vector<bool>(n, true));
        vector<int> f(n);
    
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 1; j < n; ++j) {
                g[i][j] = (s[i] == s[j]) && g[i + 1][j - 1];
            }
        }
    
        for (int i = 0; i < n; ++i) {
            if (g[0][i]) {
                f[i] = 0;
            } else {
                f[i] = INT_MAX;
                for (int j = 0; j < i; ++j) {
                    if (g[j + 1][i]) {
                        f[i] = min(f[i], f[j] + 1);
                    }
                }
            }
        }
    
        return f[n - 1];
    }
    
    int main() {
        string s;
        // 读取用户输入的字符串
        getline(cin, s);
        // 调用minCut方法计算最小分割次数
        int result = minCut(s);
        // 输出结果
        cout << result << endl;
    
        return 0;
    }
    
    

## Python代码：

    
    
    # 计算最小分割次数的函数
    def minCut(s):
        n = len(s)
        g = [[True] * n for _ in range(n)]
        f = [0] * n
    
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = s[i] == s[j] and g[i + 1][j - 1]
    
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                f[i] = float('inf')
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
    
        return f[n - 1]
    
    # 读取用户输入的字符串
    s = input('')
    # 调用minCut方法计算最小分割次数
    result = minCut(s)
    # 输出结果
    print(result)
    
    
    

## JavaScript代码：

    
    
    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    // 计算最小分割次数的函数
    function minCut(s) {
      const n = s.length;
      const g = Array.from({ length: n }, () => Array(n).fill(true));
      const f = new Array(n).fill(0);
    
      for (let i = n - 1; i >= 0; --i) {
        for (let j = i + 1; j < n; ++j) {
          g[i][j] = s[i] === s[j] && g[i + 1][j - 1];
        }
      }
    
      for (let i = 0; i < n; ++i) {
        if (g[0][i]) {
          f[i] = 0;
        } else {
          f[i] = Number.MAX_SAFE_INTEGER;
          for (let j = 0; j < i; ++j) {
            if (g[j + 1][i]) {
              f[i] = Math.min(f[i], f[j] + 1);
            }
          }
        }
      }
    
      return f[n - 1];
    }
    
    readline.on('line', (s) => {
      const result = minCut(s);
      console.log(result);
      readline.close();
    });
    
    
    
    

