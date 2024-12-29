## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

在第一人称射击游戏中，玩家通过键盘的A、S、D、W四个按键控制游戏人物分别向左、向后、向右、向前进行移动，从而完成走位。

假设玩家每按动一次键盘，游戏任务会向某个方向移动一步，如果玩家在操作一定次数的键盘并且各个方向的步数相同时，此时游戏任务必定会回到原点，则称此次走位为完美走位。

现给定玩家的走位（例如：`ASDA`），请通过更换其中一段连续走位的方式使得原走位能够变成一个完美走位。其中待更换的连续走位可以是相同长度的任何走位。

请返回待更换的连续走位的最小可能长度。

如果原走位本身是一个完美走位，则返回0。

​

## 输入描述

输入为由键盘字母表示的走位s，例如：`ASDA`

说明：

​ 1、走位长度 1 ≤ s.length ≤ 100000（也就是长度不一定是偶数）  
​ 2、s.length 是 4 的倍数  
​ 3、s中只含有’A’, ‘S’, ‘D’, ‘W’ 四种字符

## 输出描述

输出为待更换的连续走位的最小可能长度。

## 示例1

输入

    
    
    WASDAASD
    

输出

    
    
    1
    

说明

> 将第二个A替换为W，即可得到完美走位

## 示例2

输入

    
    
    AAAA
    

输出

    
    
    3
    

说明

> 将其中三个连续的A替换为WSD，即可得到完美走位

## 解题思路## 分析

完美走位是上下左右的次数一样的。如果不一样，我们需要在给定的走位中，找到一个**连续的字串** ，替换走位，是的走位完美。

题目要求，保持W,A,S,D字母个数平衡，即相等，如果不相等，可以从字符串中选取一段连续子串替换，来让字符串平衡。

比如：`WWWWAAAASSSS`

字符串长度12，W,A,S,D平衡的话，则每个字母个数应该是3个，而现在W,A,S各有4个，也就是说各超了1个。

因此我们应该从字符串中，**选取一段包含1个W，1个A，1个S的子串** ，来替换为D。

`WWWWAAAASSSS`

而符合这种要求的子串可能很多，我们需要找出其中最短的，即`**WAAAAS**`。

### 代码思路

  1. 首先，我们需要统计输入字符串中每个字符的出现次数。这可以通过遍历字符串并使用一个哈希表（字典）来实现。

  2. 然后，我们需要确定正整数序列的起始值。我们可以通过计算字符串长度除以序列长度来得到每个正整数的平均长度。然后，我们可以从10的（平均长度-1）次方开始，作为起始值。

  3. 接下来，我们需要使用滑动窗口的方法来寻找还原后的连续正整数序列。我们可以初始化两个指针，分别表示滑动窗口的左边界和右边界。同时，我们需要一个临时哈希表（字典）来存储当前滑动窗口内的字符出现次数。

  4. 在滑动窗口的过程中，我们需要不断更新左右边界的字符出现次数，并检查当前滑动窗口内的字符出现次数是否与输入字符串的字符出现次数匹配。如果匹配，说明我们找到了一个可能的连续正整数序列，此时我们可以更新结果变量。

  5. 当右边界超过字符串长度时，滑动窗口的过程结束。此时，结果变量中存储的就是还原后的连续正整数序列中的最小数字。

## Java

    
    
    import java.util.HashMap;
    import java.util.Scanner;
    
    public class Main {
    
        public static int minReplacementLength(String inputStr) {
            // 初始化方向键计数字典
            HashMap<Character, Integer> directionCount = new HashMap<>();
            directionCount.put('W', 0);
            directionCount.put('A', 0);
            directionCount.put('S', 0);
            directionCount.put('D', 0);
    
            // 统计输入字符串中每个方向键的出现次数
            for (char c : inputStr.toCharArray()) {
                directionCount.put(c, directionCount.get(c) + 1);
            }
    
            // 初始化左右指针和结果变量
            int left = 0;
            int right = 0;
            int minLength = inputStr.length();
    
            // 更新右指针对应的方向键计数
            directionCount.put(inputStr.charAt(0), directionCount.get(inputStr.charAt(0)) - 1);
    
            while (true) {
                // 计算当前最大方向键计数
                int maxCount = 0;
                for (int count : directionCount.values()) {
                    maxCount = Math.max(maxCount, count);
                }
    
                // 计算当前窗口长度和可替换的字符数
                int windowLength = right - left + 1;
                int replaceableChars = windowLength;
                for (int count : directionCount.values()) {
                    replaceableChars -= maxCount - count;
                }
    
                // 如果可替换字符数大于等于0且能被4整除，则更新结果变量
                if (replaceableChars >= 0 && replaceableChars % 4 == 0) {
                    minLength = Math.min(minLength, windowLength);
    
                    // 更新左指针并检查是否越界
                    if (left < inputStr.length()) {
                        directionCount.put(inputStr.charAt(left), directionCount.get(inputStr.charAt(left)) + 1);
                        left++;
                    } else {
                        break;
                    }
                } else {
                    // 更新右指针并检查是否越界
                    right++;
                    if (right >= inputStr.length()) {
                        break;
                    }
                    directionCount.put(inputStr.charAt(right), directionCount.get(inputStr.charAt(right)) - 1);
                }
            }
    
            return minLength;
        }
    
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String inputStr = scanner.nextLine();
            System.out.println(minReplacementLength(inputStr));
        }
    }
    
    
    
    

## Python

    
    
    def min_replacement_length(input_str):
        # 初始化方向键计数字典
        direction_count = {'W': 0, 'A': 0, 'S': 0, 'D': 0}
    
        # 统计输入字符串中每个方向键的出现次数
        for char in input_str:
            direction_count[char] += 1
    
        # 初始化左右指针和结果变量
        left = 0
        right = 0
        min_length = len(input_str)
    
        # 更新右指针对应的方向键计数
        direction_count[input_str[0]] -= 1
    
        while True:
            # 计算当前最大方向键计数
            max_count = max(direction_count.values())
    
            # 计算当前窗口长度和可替换的字符数
            window_length = right - left + 1
            replaceable_chars = window_length - sum(max_count - count for count in direction_count.values())
    
            # 如果可替换字符数大于等于0且能被4整除，则更新结果变量
            if replaceable_chars >= 0 and replaceable_chars % 4 == 0:
                min_length = min(min_length, window_length)
    
                # 更新左指针并检查是否越界
                if left < len(input_str):
                    direction_count[input_str[left]] += 1
                    left += 1
                else:
                    break
            else:
                # 更新右指针并检查是否越界
                right += 1
                if right >= len(input_str):
                    break
                direction_count[input_str[right]] -= 1
    
        return min_length
    
    
    if __name__ == "__main__":
        input_str = input()
        print(min_replacement_length(input_str))
    
    
    

## JavaScript

    
    
    function minReplacementLength(inputStr) {
        // 初始化方向键计数字典
        const directionCount = { W: 0, A: 0, S: 0, D: 0 };
    
        // 统计输入字符串中每个方向键的出现次数
        for (const c of inputStr) {
            directionCount[c]++;
        }
    
        // 初始化左右指针和结果变量
        let left = 0;
        let right = 0;
        let minLength = inputStr.length;
    
        // 更新右指针对应的方向键计数
        directionCount[inputStr[0]]--;
    
        while (true) {
            // 计算当前最大方向键计数
            const maxCount = Math.max(...Object.values(directionCount));
    
            // 计算当前窗口长度和可替换的字符数
            const windowLength = right - left + 1;
            let replaceableChars = windowLength;
            for (const count of Object.values(directionCount)) {
                replaceableChars -= maxCount - count;
            }
    
            // 如果可替换字符数大于等于0且能被4整除，则更新结果变量
            if (replaceableChars >= 0 && replaceableChars % 4 === 0) {
                minLength = Math.min(minLength, windowLength);
    
                // 更新左指针并检查是否越界
                if (left < inputStr.length) {
                    directionCount[inputStr[left]]++;
                    left++;
                } else {
                    break;
                }
            } else {
                // 更新右指针并检查是否越界
                right++;
                if (right >= inputStr.length) {
                    break;
                }
                directionCount[inputStr[right]]--;
            }
        }
    
        return minLength;
    }
    
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    readline.on('line', (inputStr) => {
        console.log(minReplacementLength(inputStr));
        readline.close();
    });
    
    
    

## C++

    
    
    #include <iostream>
    #include <string>
    #include <unordered_map>
    #include <algorithm>
    
    using namespace std;
    int min_replacement_length(const string &input_str) {
        // 初始化方向键计数字典
        unordered_map<char, int> direction_count = {{'W', 0}, {'A', 0}, {'S', 0}, {'D', 0}};
    
        // 统计输入字符串中每个方向键的出现次数
        for (char c : input_str) {
            direction_count[c]++;
        }
    
        // 初始化左右指针和结果变量
        int left = 0;
        int right = 0;
        int min_length = input_str.length();
    
        // 更新右指针对应的方向键计数
        direction_count[input_str[0]]--;
    
        while (true) {
            // 计算当前最大方向键计数
            int max_count = max({direction_count['W'], direction_count['A'], direction_count['S'], direction_count['D']});
    
            // 计算当前窗口长度和可替换的字符数
            int window_length = right - left + 1;
            int replaceable_chars = window_length;
            for (const auto &kv : direction_count) {
                replaceable_chars -= max_count - kv.second;
            }
    
            // 如果可替换字符数大于等于0且能被4整除，则更新结果变量
            if (replaceable_chars >= 0 && replaceable_chars % 4 == 0) {
                min_length = min(min_length, window_length);
    
                // 更新左指针并检查是否越界
                if (left < input_str.length()) {
                    direction_count[input_str[left]]++;
                    left++;
                } else {
                    break;
                }
            } else {
                // 更新右指针并检查是否越界
                right++;
                if (right >= input_str.length()) {
                    break;
                }
                direction_count[input_str[right]]--;
            }
        }
    
        return min_length;
    }
    
    int main() {
        string input_str;
        cin >> input_str;
        cout << min_replacement_length(input_str) << endl;
        return 0;
    }
    
    
    

## C语言

    
    
    #include <stdio.h>
    #include <string.h>
    #include <limits.h>
    
    // 用于计算字符频率的辅助函数
    void calculate_frequency(const char *s, int *freq) {
        for (int i = 0; s[i] != '\0'; i++) {
            freq[s[i]]++;
        }
    }
    
    // 主函数
    int main() {
        char s[100001];  // 假设输入长度最大为100000
        scanf("%s", s);  // 读取用户输入的走位字符串
    
        int n = strlen(s);  // 计算走位字符串的长度
        int required = n / 4;  // 每个方向的步数在完美走位中应当相等
    
        // 初始化各方向的步数频率统计
        int freq[256] = {0};  // 统计'A', 'S', 'D', 'W'出现的次数
        calculate_frequency(s, freq);  // 计算初始的频率
    
        // 如果已经是完美走位，则直接输出0
        if (freq['A'] == required && freq['S'] == required &&
            freq['D'] == required && freq['W'] == required) {
            printf("0\n");
            return 0;
        }
    
        // 初始化滑动窗口的左右边界和最小长度
        int left = 0, min_length = INT_MAX;
    
        // 滑动窗口的核心逻辑
        for (int right = 0; right < n; right++) {
            // 移动右边界，并减少对应字符的频率
            freq[s[right]]--;
    
            // 检查是否满足完美走位的条件
            while (freq['A'] <= required && freq['S'] <= required &&
                   freq['D'] <= required && freq['W'] <= required) {
                // 更新最小长度
                min_length = (right - left + 1) < min_length ? (right - left + 1) : min_length;
    
                // 移动左边界，并恢复对应字符的频率
                freq[s[left]]++;
                left++;
            }
        }
    
        // 输出最小替换长度
        printf("%d\n", min_length);
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    WASDAASD
    

### 用例2

    
    
    AAAA
    

### 用例3

    
    
    WASD
    

### 用例4

    
    
    WWWW
    

### 用例5

    
    
    WASDWASD
    

### 用例6

    
    
    WASDASDW
    

### 用例7

    
    
    WASDAAAD
    

### 用例8

    
    
    WASDSSSD
    

### 用例9

    
    
    WASDDDDD
    

### 用例10

    
    
    WASDWSWD
    

