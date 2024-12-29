## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

书籍的长、宽都是整数对应(l,w)。如果书A的长宽度都比B长宽大时，则允许将B排列放在A上面。

现在有一组规格的书籍，书籍叠放时要求书籍不能做旋转，请计算最多能有多少个规格书籍能叠放在一起。

​

## 输入描述

输入：books = [[20,16],[15,11],[10,10],[9,10]]

说明：总共4本书籍，第一本长度为20宽度为16；第二本书长度为15宽度为11，依次类推，最后一本书长度为9宽度为10.

## 输出描述

输出：3

说明: 最多3个规格的书籍可以叠放到一起, 从下到上依次为: [20,16],[15,11],[10,10]

## 示例1

输入

    
    
    [[20,16],[15,11],[10,10],[9,10]]
    

输出

    
    
    3
    

说明

> ## 解题思路

## Java

    
    
    import java.util.*;
    
    public class Main {
      public static void main(String[] args) {
     
        Scanner sc = new Scanner(System.in);
    
     
        String input = sc.nextLine();
    
        // 去掉字符串的首尾方括号，并按书籍分隔符 "],[" 分割，生成每本书的字符串数组
        String[] bookStrings = input.substring(1, input.length() - 1).split("(?<=]),(?=\\[)");
        
        // 定义二维数组存储所有书的长宽信息
        Integer[][] books = new Integer[bookStrings.length][];
        
        // 遍历每本书的字符串，将其转换为长度和宽度的整数数组
        for (int i = 0; i < bookStrings.length; i++) {
            // 去掉当前书的方括号，并按逗号分割
            String[] bookValues = bookStrings[i].substring(1, bookStrings[i].length() - 1).split(",");
            books[i] = new Integer[bookValues.length];
            
            // 将分割后的字符串转换为整数并存入书籍数组
            for (int j = 0; j < bookValues.length; j++) {
                books[i][j] = Integer.parseInt(bookValues[j]);
            }
        }
    
        // 按照书的长度从小到大排序，如果长度相同，则按宽度从大到小排序
        Arrays.sort(books, Comparator.comparing((Integer[] arr) -> arr[0])
            .thenComparing((Integer[] arr) -> -arr[1]));
    
        // 提取所有书籍的宽度，准备计算最长不下降子序列
        int[] widths = Arrays.stream(books).mapToInt(book -> book[1]).toArray();
    
        // 定义一个数组用于保存最长不下降子序列（LIS）
        int[] lis = new int[widths.length];
        int len = 0; // 用于记录 LIS 的长度
    
        // 遍历所有书籍的宽度，使用二分查找优化 LIS 计算
        for (int i = 0; i < widths.length; i++) {
            // 使用二分查找确定宽度插入 LIS 的位置
            int idx = Arrays.binarySearch(lis, 0, len, widths[i]);
            
            // 如果找不到合适位置，binarySearch 返回负数，需转换为插入位置
            if (idx < 0) {
                idx = -(idx + 1); // 二分查找返回负数时转换为插入位置
            }
    
            // 更新 LIS，若插入位置是当前长度 len 位置，表示找到了新的子序列元素，增加 len
            lis[idx] = widths[i];
            if (idx == len) {
                len++; // 子序列长度增加
            }
        }
    
        // 输出最长不下降子序列的长度，即最大可以叠放的书籍数量
        System.out.println(len);
      }
    }
    

## Python

    
    
    import sys   
    import bisect   
    
    # 读取用户输入的书籍数据，假设输入形如 [[20,16],[21,15],[22,14]]
    books = eval(input())  # eval 将输入的字符串转化为实际的 Python 数据结构（二维列表）
    
    # 对书籍列表按照书的长度从小到大排序，如果长度相同则按照宽度从大到小排序
    books.sort(key=lambda x: (x[0], -x[1]))  
    # lambda 函数 x[0] 表示按长度排序，x[1] 前面的负号表示宽度按照降序排列
    
    # 提取所有书籍的宽度，生成一个列表
    widths = list(map(lambda x: x[1], books))  # 使用 map 提取每本书的宽度并转换为列表
    
    # 初始化最长不下降子序列（LIS），首先将第一个宽度值放入 LIS 列表
    lis = [widths[0]]
    
    # 遍历所有书籍的宽度，从第二本书开始
    for i in range(1, len(widths)):
        # 如果当前书的宽度大于 LIS 列表中的最后一个元素，则将其追加到 LIS 中
        if widths[i] > lis[-1]:
            lis.append(widths[i])
        # 如果当前书的宽度小于 LIS 列表中的第一个元素，替换第一个元素
        elif widths[i] < lis[0]:
            lis[0] = widths[i]
        # 否则，使用二分查找找到第一个大于或等于当前宽度的位置，并替换它
        else:
            idx = bisect.bisect_left(lis, widths[i])
            lis[idx] = widths[i]
    
    # 输出 LIS 的长度，即可以叠放的最多书籍数量
    print(len(lis))
    

## JavaScript

    
    
    const readline = require('readline');
    
     
    const rl = readline.createInterface({
      input: process.stdin,  
      output: process.stdout  
    });
    
     
    rl.on('line', (input) => {
     
      // 按照 "],[" 分割每本书的信息
      const books = input.substring(1, input.length - 1)
        .split(/(?<=]),(?=\[)/) // 使用正则表达式分割书本
        .map(s => s.substring(1, s.length - 1) // 去掉每本书的内部方括号
          .split(',') // 按逗号分隔长度和宽度
          .map(Number)); // 将字符串转换为数字
    
      // 按照书籍的长度从小到大排序，如果长度相同，则按宽度从大到小排序
      books.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
    
      // 提取书籍的宽度，准备计算最长不下降子序列
      const widths = books.map(book => book[1]);
    
      // 初始化 LIS（Longest Increasing Subsequence, 最长不下降子序列）的数组
      const lis = [widths[0]]; // 以第一本书的宽度作为起点
    
      // 遍历所有书籍的宽度，从第二本书开始
      for (let i = 1; i < widths.length; i++) {
        // 如果当前书的宽度大于 LIS 的最后一个元素，直接追加到 LIS 中
        if (widths[i] > lis[lis.length - 1]) {
          lis.push(widths[i]);
        } 
        // 如果当前书的宽度小于 LIS 的第一个元素，替换第一个元素
        else if (widths[i] < lis[0]) {
          lis[0] = widths[i];
        } 
        // 否则，找到 LIS 中第一个大于或等于当前宽度的位置，进行替换
        else {
          const idx = lis.findIndex(w => w >= widths[i]);
          lis[idx] = widths[i];
        }
      }
    
      // 输出 LIS 的长度，即最大可以叠放的书籍数量
      console.log(lis.length);
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    
    using namespace std;
    
    int main() {
        // 获取用户输入的一行数据
        string input;
        getline(cin, input);
    
        vector<vector<int>> books;
        size_t pos = 1; // 初始化位置，跳过输入的第一个字符 '['
    
        // 解析输入字符串，提取每本书的长和宽
        while (pos < input.size() - 1) { // 当遍历到输入的倒数第二个字符时停止
            size_t end = input.find("],", pos); // 查找每本书的结束位置
            if (end == string::npos) { // 如果没找到 "],", 则说明已经到最后一本书
                end = input.size() - 1; // 将结束位置设置为输入字符串的倒数第一个字符 ']'
            }
            // 截取表示一本书的字符串，例如 "[20,16]"
            string book_str = input.substr(pos, end - pos + 1);
            pos = end + 2; // 更新 pos，跳过 "],"
    
            vector<int> book;
            size_t book_pos = 1; // 初始化为1，跳过书字符串的第一个字符 '['
            // 解析书的长度和宽度
            while (book_pos < book_str.size() - 1) {
                size_t book_end = book_str.find(",", book_pos); // 找到书的宽度与长度的分隔符 ","
                if (book_end == string::npos) { // 如果没找到分隔符，则表示当前数字是宽度
                    book_end = book_str.size() - 1;
                }
                // 提取长度或宽度的数字字符串，并将其转换为整数
                string num_str = book_str.substr(book_pos, book_end - book_pos);
                book_pos = book_end + 1; // 更新位置，跳过逗号 ","
                book.push_back(stoi(num_str)); // 将数字添加到书的向量中
            }
            // 将解析出的书的长宽向量添加到 books 数组中
            books.push_back(book);
        }
    
        // 对书籍进行排序
        // 先按照长度升序排序，如果长度相同，则按宽度降序排列
        sort(books.begin(), books.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] == b[0] ? b[1] < a[1] : a[0] < b[0]; // 如果长度相等，按宽度降序排列
        });
    
        // 提取所有书的宽度，方便之后寻找最长不下降子序列
        vector<int> widths;
        for (vector<int>& book : books) {
            widths.push_back(book[1]); // 仅保留每本书的宽度
        }
    
        // 寻找宽度的最长不下降子序列(LIS)，使用二分查找优化
        vector<int> lis;
        int len = 0; // 记录最长子序列的长度
        for (int i = 0; i < widths.size(); i++) {
            // 找到当前宽度应该插入的位置，保持宽度不下降
            int idx = lower_bound(lis.begin(), lis.end(), widths[i]) - lis.begin();
            if (idx == len) {
                // 如果插入的位置等于当前 LIS 的长度，说明找到了一个新的更大的宽度，直接添加
                lis.push_back(widths[i]);
                len++; // 增加最长子序列的长度
            } else {
                // 否则，用当前宽度替换掉对应位置的值，以保持 LIS 的最小值
                lis[idx] = widths[i];
            }
        }
    
        // 输出最长不下降子序列的长度，也就是最多可以叠放的书籍数量
        cout << len << endl;
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    // 用于书籍存储的结构体，每本书包含长度和宽度
    typedef struct {
        int length;
        int width;
    } Book;
    
    // 比较函数，用于 qsort 排序书籍
    // 先按长度升序，如果长度相同则按宽度降序
    int compare(const void* a, const void* b) {
        Book* bookA = (Book*)a;
        Book* bookB = (Book*)b;
        if (bookA->length == bookB->length) {
            return bookB->width - bookA->width; // 宽度降序
        }
        return bookA->length - bookB->length; // 长度升序
    }
    
    // 二分查找优化，寻找插入点
    int lower_bound(int* lis, int len, int target) {
        int left = 0, right = len;
        while (left < right) {
            int mid = (left + right) / 2;
            if (lis[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    int main() {
        // 获取用户输入的一行数据
        char input[1000]; // 假设输入不会超过1000字符
        fgets(input, sizeof(input), stdin);
    
        Book books[100]; // 假设最多有100本书
        int bookCount = 0; // 记录书的数量
    
        char* pos = input + 1; // 跳过输入的第一个字符 '['
        // 解析输入字符串，提取每本书的长和宽
        while (*pos != ']') { // 当遇到输入的倒数第二个字符停止
            int length, width;
            sscanf(pos, "[%d,%d]", &length, &width); // 解析出一本书的长和宽
            books[bookCount].length = length;
            books[bookCount].width = width;
            bookCount++;
    
            // 移动到下一本书的位置，跳过当前的 "],"
            pos = strstr(pos, "],");
            if (pos) {
                pos += 2; // 跳过 "],"
            } else {
                break; // 到达最后一本书
            }
        }
    
        // 对书籍进行排序，先按长度升序，如果长度相同则按宽度降序
        qsort(books, bookCount, sizeof(Book), compare);
    
        // 提取所有书的宽度，方便之后寻找最长不下降子序列
        int widths[100]; // 宽度数组
        for (int i = 0; i < bookCount; i++) {
            widths[i] = books[i].width;
        }
    
        // 寻找宽度的最长不下降子序列(LIS)，使用二分查找优化
        int lis[100]; // LIS 数组
        int len = 0; // 记录最长子序列的长度
    
        for (int i = 0; i < bookCount; i++) {
            // 找到当前宽度应该插入的位置，保持宽度不下降
            int idx = lower_bound(lis, len, widths[i]);
            if (idx == len) {
                // 如果插入位置等于当前 LIS 的长度，说明找到了一个新的更大的宽度
                lis[len++] = widths[i];
            } else {
                // 否则，用当前宽度替换掉对应位置的值，以保持 LIS 的最小值
                lis[idx] = widths[i];
            }
        }
    
        // 输出最长不下降子序列的长度，也就是最多可以叠放的书籍数量
        printf("%d\n", len);
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    [[1,1],[2,2],[3,3],[4,4]]
    

### 用例2

    
    
    [[1,1],[2,2],[2,2],[3,3]]
    

### 用例3

    
    
    [[1,1],[2,2],[2,2],[2,2]]
    

### 用例4

    
    
    [[1,1],[2,2],[3,3],[1,2]]
    

### 用例5

    
    
    [[1,1],[2,2],[3,3],[2,1]]
    

### 用例6

    
    
    [[20,16],[15,11],[10,10],[9,10],[8,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2],[1,1]]
    

### 用例7

    
    
    [[20,16],[15,11],[10,10],[9,10],[8,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2],[2,2]]
    

### 用例8

    
    
    [[20,16],[15,11],[10,10],[9,10],[8,8],[7,7],[6,6],[5,5],[4,4],[4,4],[4,4],[4,4]]
    

### 用例9

    
    
    [[20,16],[15,11],[10,10],[9,10],[8,8],[7,7],[6,6],[5,5],[5,5],[5,5],[5,5],[5,5]]
    

### 用例10

    
    
    [[20,16],[15,11],[10,10],[9,10],[8,8],[7,7],[6,6],[6,6],[6,6],[6,6],[6,6],[6,6]]
    

