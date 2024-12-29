## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定一个字符串s，s包括以空格分隔的若干个单词，请对s进行如下处理后输出：  
1、单词内部调整：对每个单词字母重新按字典序排序  
2、单词间顺序调整：

  * 统计每个单词出现的次数，并按次数降序排列
  * 次数相同，按单词长度升序排列
  * 次数和单词长度均相同，按字典升序排列

请输出处理后的字符串，每个单词以一个空格分隔

## 输入描述

一行字符串，每个字符取值范围：[a-zA-z0-9]以及空格，字符串长度范围：[1，1000]

## 输出描述

输出处理后的字符串，每个单词以一个空格分隔。

## 示例1

输入

    
    
    This is an apple
    

输出

    
    
    an is This aelpp
    

说明

> ## 示例2

输入

    
    
    My sister is in the house not in the yard
    

输出

    
    
    in in eht eht My is not adry ehosu eirsst
    

说明

> ## 解题思路

考察的是排序

  1. 对每个单词内部进行字典序排序
  2. 按照单词出现次数、单词长度、字典序升序排列

具体实现思路如下：

  1. 使用分割字符串，得到每个单词
  2. 对每个单词进行字典序排序，并存储到一个 List 中
  3. 统计每个单词出现的次数，并存储到一个 Map 中
  4. 使用 对 List 进行排序，排序规则如下： 
     * 次数不同，按照次数降序排列
     * 次数相同，长度不同，按照长度升序排列
     * 次数和长度都相同，按照字典序升序排列
  5. 输出处理后的字符串，每个单词以一个空格分隔

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();
            scanner.close();
    
            // 使用空格分割字符串
            String[] words = input.split(" "); // 分割字符串为单词
    
            // 对每个单词内部进行字典序排序
            for (int i = 0; i < words.length; i++) {
                char[] chars = words[i].toCharArray();
                Arrays.sort(chars);
                words[i] = new String(chars);
            }
    
            // 统计每个单词出现的次数
            Map<String, Integer> count = new HashMap<>();
            for (String word : words) {
                count.put(word, count.getOrDefault(word, 0) + 1);
            }
    
            // 进行排序（使用简单的冒泡排序代替 Collections.sort）
            for (int i = 0; i < words.length - 1; i++) {
                for (int j = 0; j < words.length - 1 - i; j++) {
                    // 进行比较
                    if (shouldSwap(words[j], words[j + 1], count)) {
                        // 交换
                        String temp = words[j];
                        words[j] = words[j + 1];
                        words[j + 1] = temp;
                    }
                }
            }
    
            // 输出处理后的字符串
            StringBuilder sb = new StringBuilder();
            for (String word : words) {
                sb.append(word).append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    
        // 判断是否需要交换两个单词
        private static boolean shouldSwap(String a, String b, Map<String, Integer> count) {
            if (!count.get(a).equals(count.get(b))) {
                // 次数不同，按照次数降序排列
                return count.get(a) < count.get(b);
            } else if (a.length() != b.length()) {
                // 次数相同，长度不同，按照长度升序排列
                return a.length() > b.length();
            } else {
                // 次数和长度都相同，按照字典序升序排列
                return a.compareTo(b) > 0;
            }
        }
    }
    

## Python

    
    
    import collections
    import functools
    
    input = input()
    words = input.split(" ")
    
    # 对每个单词内部进行字典序排序
    words = ["".join(sorted(word)) for word in words]
    
    # 统计每个单词出现的次数
    count = collections.Counter(words)
    
    # 按照要求排序
    words = sorted(words, key=functools.cmp_to_key(lambda a, b: count[b] - count[a] if count[a] != count[b] else len(a) - len(b) if len(a) != len(b) else -1 if a < b else 1))
    
    # 输出处理后的字符串
    output = " ".join(words)
    print(output)
    
    

## JavaScript

    
    
    const readline = require("readline");
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    
    rl.on("line", (input) => {
      const words = input.split(" ");
    
      // 对每个单词内部进行字典序排序
      const sortedWords = words.map((word) => word.split("").sort().join(""));
    
      // 统计每个单词出现的次数
      const count = sortedWords.reduce((acc, word) => {
        acc[word] = (acc[word] || 0) + 1;
        return acc;
      }, {});
    
      // 按照要求排序
      sortedWords.sort((a, b) => {
        if (count[b] !== count[a]) {
          return count[b] - count[a]; // 按出现次数降序
        }
        if (a.length !== b.length) {
          return a.length - b.length; // 按长度升序
        }
        return a < b ? -1 : 1; // 字典序升序
      });
    
      // 输出处理后的字符串
      console.log(sortedWords.join(" "));
      rl.close();
    });
    

## C++

    
    
    #include <iostream>
    #include <algorithm>
    #include <unordered_map>
    #include <sstream>
    #include <vector>
    
    using namespace std;
    
    int main() {
        // 读入字符串
        string input;
        getline(cin, input);
        // 使用 istringstream 分割字符串
        istringstream iss(input);
        string token;
        vector<string> words;
        while (getline(iss, token, ' ')) {
            // 对每个单词内部进行字典序排序
            sort(token.begin(), token.end());
            words.push_back(token);
        }
    
        // 统计每个单词出现的次数
        unordered_map<string, int> count;
        for (string word : words) {
            count[word]++;
        }
    
        // 按照要求排序
        sort(words.begin(), words.end(), [&](const string& a, const string& b) {
            if (count[a] != count[b]) {
                // 次数不同，按照次数降序排列
                return count[b] < count[a];
            } else if (a.length() != b.length()) {
                // 次数相同，长度不同，按照长度升序排列
                return a.length() < b.length();
            } else {
                // 次数和长度都相同，按照字典序升序排列
                return a < b;
            }
        });
    
        // 输出处理后的字符串
        ostringstream oss;
        for (string word : words) {
            oss << word << " ";
        }
        cout << oss.str() << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    #define MAX_WORDS 1000    // 定义最大单词数量
    #define MAX_LENGTH 100    // 定义单词的最大长度
    
    // 定义一个结构体，用于存储单词和其出现的次数
    typedef struct {
        char word[MAX_LENGTH]; // 存储单词
        int count;            // 存储单词出现的次数
    } WordCount;
    
    // 字母排序函数
    void sortString(char *str) {
        int length = strlen(str); // 获取字符串的长度
        // 使用 qsort 对字符串的字母进行排序
        qsort(str, length, sizeof(char), (int (*)(const void *, const void *)) strcmp);
    }
    
    // 比较函数，用于对 WordCount 结构体数组进行排序
    int compare(const void *a, const void *b) {
        WordCount *wordCountA = (WordCount *)a; // 将 void 指针转换为 WordCount 指针
        WordCount *wordCountB = (WordCount *)b; // 将 void 指针转换为 WordCount 指针
    
        // 先比较出现次数
        if (wordCountA->count != wordCountB->count) {
            return wordCountB->count - wordCountA->count; // 次数降序排列
        } else {
            // 如果出现次数相同，则比较单词长度
            int lenDiff = strlen(wordCountA->word) - strlen(wordCountB->word);
            if (lenDiff != 0) {
                return lenDiff; // 长度升序排列
            } else {
                return strcmp(wordCountA->word, wordCountB->word); // 字典序排序
            }
        }
    }
    
    int main() {
        char input[1000]; // 定义一个字符数组用于存储输入的字符串
        fgets(input, sizeof(input), stdin); // 从标准输入读取一行字符串
    
        // 处理单词的数组
        char *words[MAX_WORDS]; // 存储分割后的单词
        int wordCount = 0; // 记录总共的单词数量
    
        // 使用 strtok 函数分割单词，以空格和换行符为分隔符
        char *token = strtok(input, " \n");
        while (token != NULL) {
            char *sortedWord = malloc(MAX_LENGTH); // 动态分配内存存储排序后的单词
            strcpy(sortedWord, token); // 复制当前分割出的单词
            sortString(sortedWord); // 对单词内部进行字典序排序
            words[wordCount++] = sortedWord; // 将排序后的单词存入数组
            token = strtok(NULL, " \n"); // 继续分割下一个单词
        }
    
        // 统计每个单词出现的次数
        WordCount wordCounts[MAX_WORDS]; // 存储每个单词及其出现次数的数组
        int uniqueCount = 0; // 记录不同单词的数量
    
        // 遍历所有分割出的单词
        for (int i = 0; i < wordCount; i++) {
            int found = 0; // 标记是否找到了重复的单词
            // 检查当前单词是否已经存在于 wordCounts 数组中
            for (int j = 0; j < uniqueCount; j++) {
                if (strcmp(wordCounts[j].word, words[i]) == 0) {
                    wordCounts[j].count++; // 如果找到，增加计数
                    found = 1; // 标记已找到
                    break;
                }
            }
            // 如果没有找到该单词，则将其添加到 wordCounts 中
            if (!found) {
                strcpy(wordCounts[uniqueCount].word, words[i]); // 复制单词
                wordCounts[uniqueCount].count = 1; // 初始化计数为 1
                uniqueCount++; // 增加不同单词的计数
            }
        }
    
        // 按出现次数对单词进行排序
        qsort(wordCounts, uniqueCount, sizeof(WordCount), compare);
    
        // 输出结果
        for (int i = 0; i < uniqueCount; i++) {
            // 根据单词的出现次数输出每个单词
            for (int j = 0; j < wordCounts[i].count; j++) {
                printf("%s ", wordCounts[i].word);
            }
        }
        printf("\n"); // 输出换行
    
        // 释放动态分配的内存
        for (int i = 0; i < wordCount; i++) {
            free(words[i]); // 释放每个排序后单词的内存
        }
    
        return 0; // 程序结束
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/9c0bfdc1f9f6a8dbf4e8844b3529eccc.png)

## 完整用例

### 用例1

    
    
    This is an apple
    

### 用例2

    
    
    My sister is in the house not in the yard
    

### 用例3

    
    
    apple apple orange apple banana banana orange
    

### 用例4

    
    
    hello world hello code
    

### 用例5

    
    
    test test test example example code
    

### 用例6

    
    
    car bike plane car car bike
    

### 用例7

    
    
    apple banana cherry apple banana
    

### 用例8

    
    
    abcd efgh ijkl mnop qrst uvwx yz
    

### 用例9

    
    
    one two three four five six seven
    

### 用例10

    
    
    zoo zoo zebra zebra apple apple apple
    

