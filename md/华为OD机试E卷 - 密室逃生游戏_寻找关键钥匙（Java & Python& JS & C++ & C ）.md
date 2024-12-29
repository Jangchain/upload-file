## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小强正在参加《密室逃生》游戏，当前关卡要求找到符合给定 **密码K（升序的不重复小写字母组成）** 的箱子，并给出箱子编号，箱子编号为 1 ~ N 。

每个箱子中都有一个 **字符串s** ，字符串由大写字母、小写字母、数字、标点符号、空格组成，

需要在这些字符串中找到所有的字母，忽略大小写后排列出对应的密码串，并返回匹配密码的箱子序号。

提示：满足条件的箱子不超过1个。

## 输入描述

第一行为 key 的字符串，第二行为箱子 boxes，为数组样式，以空格分隔

  * 箱子 N 数量满足 1 ≤ N ≤ 10000
  * s 长度满足 0 ≤ s.length ≤ 50
  * 密码为仅包含小写字母的升序字符串，且不存在重复字母
  * 密码 K 长度1 ≤ K.length ≤ 26

##### 备注

箱子中字符拼出的字符串与密码的匹配忽略大小写，且要求与密码完全匹配，如：

> 密码 abc 匹配 aBc，但是密码 abc 不匹配 abcd

## 输出描述

返回对应箱子编号

如不存在符合要求的密码箱，则返回 -1

## 示例1

输入

    
    
    abc
    s,sdf134 A2c4b
    

输出

    
    
    2
    

说明

> 第2 个箱子中的 Abc ，符合密码 abc。

## 示例2

输入

    
    
    abc
    s,sdf134 A2c4bd 523[]
    

输出

    
    
    -1
    

说明

> 第2个箱子中的Abcd，与密码不完全匹配，不符合要求

## 解题思路

#### 题目解释

#### 歧义解释

  * **问题描述** ： 
    * 题目描述中的“第二行为箱子 `boxes`，为数组样式，以空格分隔”，这可能导致对输入的解析存在歧义。
    * 是否每个箱子本身可以包含空格？即一个箱子中的字符串 `s` 是否会包含内嵌的空格？
  * **歧义分析** ： 
    * 如果输入 `boxes` 是通过**空格分隔** 的字符串数组，是否需要处理箱子 `s` 内部的空格？
    * 例如，输入 `abc "de f" ghi`，这里的 `de f` 是一个单独的字符串还是两个分开的箱子？

关于空格，结合用例推测题意，应该是字符串s是不应该包含空格的，否则无法进行字符串分割。

##### **任务：**

  1. 提取箱子字符串 **s** 中的所有字母（忽略大小写）。
  2. 将提取出的字母转为小写，并按升序排列形成新的字符串。
  3. 检查该新字符串是否与密码 **K** 完全相同。
  4. 如果相同，则返回该箱子的编号；如果所有箱子都不匹配，则返回 **-1** 。

* * *

#### **输入描述**

  1. **第一行** ：密码字符串 `key`，只包含升序排列的不重复小写字母。
  2. **第二行** ：箱子字符串数组 `boxes`，以空格分隔，每个元素是箱子里的字符串。

* * *

#### **示例解析**

##### 示例 1：

**输入：**

    
    
    abc
    s,sdf134 A2c4b
    

**分析：**

  * 密码为：`abc`
  * 箱子字符串： 
    1. **第1个箱子** ：`s,sdf134` 提取字母 `sdf` → 转小写、排序：`dfs` ≠ `abc`
    2. **第2个箱子** ：`A2c4b` 提取字母 `A`, `c`, `b` → 转小写、排序：`abc` = `abc`

**输出：**

    
    
    2
    

##### 示例 2：

**输入：**

    
    
    abc
    s,sdf134 A2c4bd 523[]
    

**分析：**

  * 密码为：`abc`
  * 箱子字符串： 
    1. **第1个箱子** ：`s,sdf134` 提取字母：`sdf` → 排序：`dfs` ≠ `abc`
    2. **第2个箱子** ：`A2c4bd` 提取字母：`A`, `c`, `b`, `d` → 排序：`abcd` ≠ `abc`

**输出：**

    
    
    -1
    

* * *

#### **总结步骤**

  1. 提取箱子字符串中的所有字母，忽略非字母字符。
  2. 将提取的字母全部转为小写。
  3. 按字母升序排列。
  4. 比较生成的字符串与密码 **K** 是否完全一致。

## Java

    
    
    import java.util.Scanner;
    
    public class Main {
    
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String password = scanner.nextLine(); // 密码
            String[] boxes = scanner.nextLine().split(" "); // 盒子内容数组
            int result = -1; // 初始化结果为 -1
    
            // 遍历每个盒子
            for (int i = 0; i < boxes.length; i++) {
                String box = boxes[i].toLowerCase(); // 转小写
                StringBuilder extracted = new StringBuilder(); // 用于提取和存储字母
    
                // 提取并排序字母
                for (char c : box.toCharArray()) {
                    if (c >= 'a' && c <= 'z') {
                        extracted.append(c);
                    }
                }
    
                // 长度不同直接跳过
                if (extracted.length() != password.length()) {
                    continue;
                }
    
                // 排序提取的字母
                char[] chars = extracted.toString().toCharArray();
                java.util.Arrays.sort(chars);
    
                // 比较排序结果
                if (new String(chars).equals(password)) {
                    result = i + 1; // 更新结果为 1-based 索引
                    break;
                }
            }
    
            System.out.println(result); // 输出结果
        }
    }
    
    

## Python

    
    
    # 导入必要模块
    def main():
        # 读取输入的密码
        password = input().strip()  # 第一行输入为密码
        # 读取输入的盒子数组，按空格分割
        boxes = input().strip().split(" ")
        result = -1  # 初始化结果为 -1，表示未找到匹配项
    
        # 遍历每个盒子
        for i, box in enumerate(boxes):
            # 将盒子字符串转为小写
            lower_case = box.lower()
            # 提取盒子中的所有字母
            extracted = ''.join([c for c in lower_case if 'a' <= c <= 'z'])
    
            # 如果提取的字母数量与密码长度不同，直接跳过
            if len(extracted) != len(password):
                continue
    
            # 对提取的字母排序
            sorted_extracted = ''.join(sorted(extracted))
    
            # 如果排序后的结果与密码一致
            if sorted_extracted == password:
                result = i + 1  # 更新结果为当前盒子编号（从 1 开始）
                break  # 终止循环
    
        # 输出结果
        print(result)
    
    # 调用主函数
    if __name__ == "__main__":
        main()
    
    

## JavaScript

    
    
     
     
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    
        const inputLines = [];
        rl.on('line', (line) => {
            inputLines.push(line.trim());
            if (inputLines.length === 2) {
                rl.close(); // 只需要两行输入
            }
        });
    
        rl.on('close', () => {
            const password = inputLines[0]; // 第一行输入为密码
            const boxes = inputLines[1].split(" "); // 第二行输入为盒子字符串数组
            let result = -1; // 初始化结果为 -1
    
            // 遍历每个盒子
            for (let i = 0; i < boxes.length; i++) {
                const box = boxes[i].toLowerCase(); // 转为小写
                const extracted = box
                    .split('') // 将字符串拆分为字符数组
                    .filter((c) => c >= 'a' && c <= 'z') // 筛选出字母
                    .join(''); // 拼接为字符串
    
                // 如果提取的字母数量与密码长度不同，直接跳过
                if (extracted.length !== password.length) {
                    continue;
                }
    
                // 排序提取的字母
                const sortedExtracted = extracted.split('').sort().join('');
    
                // 如果排序结果与密码一致
                if (sortedExtracted === password) {
                    result = i + 1; // 更新结果为当前盒子编号（从 1 开始）
                    break; // 跳出循环
                }
            }
    
            console.log(result); // 输出结果
        });
     
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <cctype> // 用于tolower
    using namespace std;
    
    int main() {
        string password;
        getline(cin, password); // 读取第一行输入：密码
    
        string line;
        getline(cin, line); // 读取第二行输入：盒子字符串
    
        vector<string> boxes; // 存储所有盒子
        string temp;
        for (char c : line) {
            if (c == ' ') {
                if (!temp.empty()) boxes.push_back(temp);
                temp.clear();
            } else {
                temp.push_back(c);
            }
        }
        if (!temp.empty()) boxes.push_back(temp);
    
        int result = -1; // 初始化结果为 -1
    
        // 遍历每个盒子
        for (int i = 0; i < boxes.size(); i++) {
            string box = boxes[i];
            string extracted; // 用于存储提取的字母
    
            // 提取盒子中的字母并转换为小写
            for (char c : box) {
                if (isalpha(c)) {
                    extracted.push_back(tolower(c));
                }
            }
    
            // 如果提取的字母数量与密码长度不同，跳过
            if (extracted.size() != password.size()) {
                continue;
            }
    
            // 对提取的字母排序
            sort(extracted.begin(), extracted.end());
    
            // 排序后的结果与密码比较
            string sortedPassword = password;
            sort(sortedPassword.begin(), sortedPassword.end());
            if (extracted == sortedPassword) {
                result = i + 1; // 更新结果为当前盒子编号（从 1 开始）
                break; // 跳出循环
            }
        }
    
        cout << result << endl; // 输出结果
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>
    
    // 辅助函数：字符数组排序
    void sortString(char* str) {
        int n = strlen(str);
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (str[i] > str[j]) {
                    char temp = str[i];
                    str[i] = str[j];
                    str[j] = temp;
                }
            }
        }
    }
    
    int main() {
        char password[101];
        fgets(password, 101, stdin); // 读取第一行输入：密码
        password[strcspn(password, "\n")] = 0; // 去掉换行符
    
        char line[1001];
        fgets(line, 1001, stdin); // 读取第二行输入：盒子字符串
        line[strcspn(line, "\n")] = 0; // 去掉换行符
    
        char* boxes[100]; // 存储所有盒子
        int boxCount = 0;
    
        // 按空格分割盒子字符串
        char* token = strtok(line, " ");
        while (token != NULL) {
            boxes[boxCount++] = token;
            token = strtok(NULL, " ");
        }
    
        int result = -1; // 初始化结果为 -1
    
        // 遍历每个盒子
        for (int i = 0; i < boxCount; i++) {
            char* box = boxes[i];
            char extracted[101] = ""; // 提取的字母存储
            int k = 0;
    
            // 提取字母并转小写
            for (int j = 0; box[j] != '\0'; j++) {
                if (isalpha(box[j])) {
                    extracted[k++] = tolower(box[j]);
                }
            }
            extracted[k] = '\0';
    
            // 如果提取的字母数量与密码长度不同，跳过
            if (strlen(extracted) != strlen(password)) {
                continue;
            }
    
            // 对提取的字母排序
            sortString(extracted);
    
            // 对密码排序
            char sortedPassword[101];
            strcpy(sortedPassword, password);
            sortString(sortedPassword);
    
            // 比较排序后的结果
            if (strcmp(extracted, sortedPassword) == 0) {
                result = i + 1; // 更新结果为当前盒子编号（从 1 开始）
                break; // 跳出循环
            }
        }
    
        printf("%d\n", result); // 输出结果
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

### 完整用例

### 用例1

    
    
    abc
    s,sdf134 A2c4b
    

### 用例2

    
    
    abc
    s,sdf134 A2c4bd 523[]
    

### 用例3

    
    
    abcd
    AAbCcc12dddd dAcB!+? abcde efgh
    

### 用例4

    
    
    abcdef
    AAbCcc12dddd dAcB!+? abcde efgh
    

### 用例5

    
    
    a
    1 2 3 4 5
    

### 用例6

    
    
    mno
    MNO mn op qr st uv
    

### 用例7

    
    
    abc
    aAa bb cC abcCC
    

### 用例8

    
    
    xyz
    XY12 12X34Y56Z axy bz
    

### 用例9

    
    
    abc
    a,b,c ab c d e
    

### 用例10

    
    
    abc
    aabbcc a!b@c# aabc a1c
    

