## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

  1. 单词中字母比较不区分大小写，两个单词先以第一个字母作为排序的基准，如果第一个字母相同，就用第二个字母为基准，如果第二个字母相同就以第三个字母为基准。依此类推，如果到某个字母不相同，字母顺序在前的那个单词顺序在前。
  2. 当一个短单词和一个长单词的开头部分都相同（即短单词是长单词从首字母开始的一部分），短单词顺序在前。
  3. 字母大小写不同的相同单词，只输出一次。

## 输入描述

无

## 输出描述

无

## 示例1

输入

    
    
    Hello hello world
    

输出

    
    
    Hello world
    

说明

> ## 示例2

输入

    
    
    i LOVE Cc I love CC Hello Hel Hellow
    

输出

    
    
    Cc Hel Hello Hellow i LOVE
    

说明

> ## 解题思路

去重排序

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String[] words = scanner.nextLine().split(" ");
            
            // 使用 TreeSet 以自定义比较器来排序和去重
            Set<String> uniqueWords = new TreeSet<>((a, b) -> {
                String lowerA = a.toLowerCase();
                String lowerB = b.toLowerCase();
                
                if (lowerA.startsWith(lowerB) && lowerA.length() > lowerB.length()) return 1;
                if (lowerB.startsWith(lowerA) && lowerB.length() > lowerA.length()) return -1;
                return lowerA.compareTo(lowerB);
            });
            
            // 添加所有单词到 TreeSet 自动排序并去重
            uniqueWords.addAll(Arrays.asList(words));
            
            // 输出结果
            StringJoiner sj = new StringJoiner(" ");
            for (String word : uniqueWords) {
                sj.add(word);
            }
            System.out.println(sj.toString());
        }
    }
    

## Python

    
    
    input_str = input()
    arr = input_str.split()
    
    # 对列表进行排序，忽略大小写，并优先将短单词排在前面
    arr.sort(key=lambda x: (x.lower(), len(x)))
    
    # 去重并保留第一个出现的大小写形式
    result = []
    seen = set()
    
    for word in arr:
        lower_word = word.lower()
        if lower_word not in seen:
            result.append(word)
            seen.add(lower_word)
    
    # 将结果列表以空格连接成字符串并输出
    print(" ".join(result))
    

## JavaScript

    
    
    const readline = require("readline");
    
    // 创建 readline 接口实例
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    
    // 监听每行输入
    rl.on("line", (line) => {
      const words = line.split(" ");
      console.log(sortAndDistinct(words));
    });
    
    // 排序和去重函数
    function sortAndDistinct(words) {
      // 排序：自定义比较规则，按字母顺序排序，不区分大小写，同时短单词在长单词前（如果是前缀）
      words.sort((a, b) => {
        const lowerA = a.toLowerCase();
        const lowerB = b.toLowerCase();
    
        if (lowerA.startsWith(lowerB) && lowerA.length > lowerB.length) return 1;
        if (lowerB.startsWith(lowerA) && lowerB.length > lowerA.length) return -1;
        return lowerA.localeCompare(lowerB);
      });
    
      const distinctWords = [];
      const seen = new Set();
    
      // 去重：忽略大小写的重复单词
      for (let word of words) {
        const lowerWord = word.toLowerCase();
        if (!seen.has(lowerWord)) {
          distinctWords.push(word);
          seen.add(lowerWord);
        }
      }
    
      return distinctWords.join(" ");
    }
    

## C++

    
    
    #include <iostream>
    #include <string>
    #include <vector>
    #include <algorithm>
    #include <sstream>
    #include <iterator>
    #include <unordered_set>
    using namespace std;
    
    // 自定义比较函数，先按字母顺序排序，再按长度优先
    bool compare(const string &a, const string &b) {
        string lowerA = a;
        string lowerB = b;
        // 转换为小写进行比较
        transform(lowerA.begin(), lowerA.end(), lowerA.begin(), ::tolower);
        transform(lowerB.begin(), lowerB.end(), lowerB.begin(), ::tolower);
        if (lowerA == lowerB) {
            return a.size() < b.size(); // 如果相同，短单词优先
        }
        return lowerA < lowerB; // 按字母顺序排序
    }
    
    int main() {
        string input;
        getline(cin, input);
    
        istringstream iss(input);
        vector<string> words((istream_iterator<string>(iss)), istream_iterator<string>());
    
        // 排序单词列表
        sort(words.begin(), words.end(), compare);
    
        // 去重，仅保留第一次出现的单词（忽略大小写）
        vector<string> result;
        unordered_set<string> seen;
    
        for (const auto &word : words) {
            string lowerWord = word;
            transform(lowerWord.begin(), lowerWord.end(), lowerWord.begin(), ::tolower);
            if (seen.find(lowerWord) == seen.end()) { // 如果没有出现过
                result.push_back(word);
                seen.insert(lowerWord);
            }
        }
    
        // 输出结果
        for (size_t i = 0; i < result.size(); ++i) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << endl;
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <ctype.h>
    
    #define MAX_WORDS 1000    // 假设最大单词数
    #define MAX_LENGTH 100    // 假设单词最大长度
    
    // 将字符串转换为小写
    void to_lowercase(char *str) {
        while (*str) {
            *str = tolower(*str);
            str++;
        }
    }
    
    // 比较函数，用于按字母顺序和长度排序
    int compare(const void *a, const void *b) {
        char *strA = *(char **)a;
        char *strB = *(char **)b;
        
        char lowerA[MAX_LENGTH], lowerB[MAX_LENGTH];
        strcpy(lowerA, strA);
        strcpy(lowerB, strB);
        to_lowercase(lowerA);
        to_lowercase(lowerB);
    
        int cmp = strcmp(lowerA, lowerB);
        if (cmp == 0) {
            return strlen(strA) - strlen(strB); // 如果相同，短单词优先
        }
        return cmp;
    }
    
    // 检查单词是否已经在结果数组中
    int is_duplicate(char *word, char **result, int result_size) {
        char lowerWord[MAX_LENGTH];
        strcpy(lowerWord, word);
        to_lowercase(lowerWord);
    
        for (int i = 0; i < result_size; i++) {
            char lowerResult[MAX_LENGTH];
            strcpy(lowerResult, result[i]);
            to_lowercase(lowerResult);
            if (strcmp(lowerWord, lowerResult) == 0) {
                return 1; // 找到重复
            }
        }
        return 0;
    }
    
    int main() {
        char input[5000];
        fgets(input, sizeof(input), stdin);
    
        // 分割输入字符串为单词
        char *words[MAX_WORDS];
        int word_count = 0;
        char *token = strtok(input, " \n");
        while (token != NULL && word_count < MAX_WORDS) {
            words[word_count] = strdup(token); // 复制单词
            word_count++;
            token = strtok(NULL, " \n");
        }
    
        // 排序单词
        qsort(words, word_count, sizeof(char *), compare);
    
        // 去重
        char *result[MAX_WORDS];
        int result_count = 0;
    
        for (int i = 0; i < word_count; i++) {
            if (!is_duplicate(words[i], result, result_count)) {
                result[result_count] = words[i];
                result_count++;
            } else {
                free(words[i]); // 释放重复单词的内存
            }
        }
    
        // 输出结果
        for (int i = 0; i < result_count; i++) {
            if (i > 0) printf(" ");
            printf("%s", result[i]);
            free(result[i]); // 输出后释放内存
        }
     
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/35dffa5459322f17fc46774dd91b127d.png)

## 完整用例

### 用例1

    
    
    Hello hello world
    

### 用例2

    
    
    i LOVE Cc I love CC Hello Hel Hellow
    

### 用例3

    
    
    aaa AaA aAa aaaaa
    

### 用例4

    
    
    Cat dog Dog cat CAT
    

### 用例5

    
    
    apple APPLE app App
    

### 用例6

    
    
    word words WORD Words wordy
    

### 用例7

    
    
    Alpha ALPHA alpha AlphaBeta ALPHABeta
    

### 用例8

    
    
    short shorter Shortest Short
    

### 用例9

    
    
    word Word woRD WORD wORd
    

### 用例10

    
    
    simple SIMPLE simplest SIMPlE simplest
    

