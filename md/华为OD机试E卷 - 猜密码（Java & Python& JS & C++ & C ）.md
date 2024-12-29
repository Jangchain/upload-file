## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小杨申请了一个保密柜，但是他忘记了密码。只记得密码都是数字，而且所有数字都是不[重复的](https://so.csdn.net/so/search?q=%E9%87%8D%E5%A4%8D%E7%9A%84&spm=1001.2101.3001.7020)。

请你根据他记住的数字范围和密码的最小数字数量，帮他算下有哪些可能的组合，**规则如下** ：

  1. 输出的组合都是从可选的数字范围中选取的，且不能重复；
  2. 输出的密码数字要按照从小到大的顺序排列，密码组合需要按照字母顺序，从小到大的顺序排序。
  3. 输出的每一个组合的数字的数量要大于等于密码最小数字数量；
  4. 如果可能的组合为空，则返回“None”

## 输入描述

输入的第一行是可能的密码数字列表，数字间以半角逗号分隔  
输入的第二行是密码最小数字数量

  * 

## 输出描述

可能的密码组合，每种组合显示成一行，每个组合内部的数字以半角逗号分隔，从小到大的顺序排列。

输出的组合间需要按照字典序排序。  
比如：2,3,4放到2,4的前面

##### 备注

字典序是指按照单词出现在字典的顺序进行排序的方法，比如：

  * a排在b前
  * a排在ab前
  * ab排在ac前
  * ac排在aca前

## 示例1

输入

    
    
    2,3,4
    2
    

输出

    
    
    2,3
    2,3,4
    2,4
    3,4
    

说明

> 最小密码数量是两个，可能有三种组合：  
>  2,3  
>  2,4  
>  3,4
>
> 三个密码有一种：  
>  2,3,4

## 示例2

输入

    
    
    2,0
    1
    

输出

    
    
    0
    0,2
    2
    

说明

> 可能的密码组合，一个的有两种:  
>  0  
>  2  
>  两个的有一个:  
>  0,2

## 解题思路

这道题目是一个关于密码组合的问题，要求从给定的数字列表中选取不重复的数字来形成密码。这些组合需要满足以下条件：

  1. **无重复数字** ：每个组合内的数字必须是唯一的，不能重复出现。
  2. **排序规则** ： 
     * 组合内的数字需要按照从小到大的顺序排列。
     * 组合之间按照字典序排序。字典序类似于单词在字典中的排序，例如组合 `2,3` 排在 `2,4` 前面，因为 `3` 小于 `4`。
  3. **数字数量限制** ：每个组合中的数字数量不能少于给定的最小数字数量。

#### 示例解释

**示例 1** :  
输入为数字列表 `2,3,4` 和最小数字数量 `2`。

  * 这意味着需要形成的密码组合中至少需要有两个数字。
  * 可能的组合是： 
    * 两个数字的组合：`2,3`、`2,4`、`3,4`
    * 三个数字的组合：`2,3,4`
  * 按照字典序输出结果。

**示例 2** :  
输入为数字列表 `2,0` 和最小数字数量 `1`。

  * 最小数字数量为 `1`，所以可以有一个数字的组合也可以有两个数字的组合。
  * 可能的组合是： 
    * 一个数字的组合：`0`、`2`
    * 两个数字的组合：`0,2`
  * 按照字典序输出结果。

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void dfs(List<String> nums, int index, int level, List<String> path, List<String> res) {
            if (path.size() >= level) { // 当路径长度达到level时，记录路径
                StringBuilder combination = new StringBuilder();
                for (int i = 0; i < path.size(); i++) {
                    if (i > 0) combination.append(","); // 数字之间用逗号分隔
                    combination.append(path.get(i));
                }
                res.add(combination.toString());
            }
            if (path.size() == nums.size()) return; // 路径长度达到nums长度时退出
    
            for (int i = index; i < nums.size(); i++) { // 枚举数字
                path.add(nums.get(i));
                dfs(nums, i + 1, level, path, res); // 递归搜索
                path.remove(path.size() - 1);
            }
        }
    
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            String line = sc.nextLine(); // 读入数字列表
            int level = sc.nextInt(); // 读入最小数字数量
    
            List<String> nums = new ArrayList<>();
            String delimiter = ",";
            StringTokenizer st = new StringTokenizer(line, delimiter);
            while (st.hasMoreTokens()) { // 分割数字列表
                nums.add(st.nextToken());
            }
            Collections.sort(nums); // 排序
    
            List<String> res = new ArrayList<>();
            List<String> path = new ArrayList<>();
            dfs(nums, 0, level, path, res);
    
            if (!res.isEmpty()) {
                for (String s : res) {
                    System.out.println(s);
                }
            } else {
                System.out.println("None");
            }
        }
    }
    
    

## Python

    
    
    def dfs(nums, index, level, path, res):
        if len(path) >= level:  # 当路径长度达到level时，记录路径
            combination = ",".join(path)  # 数字之间用逗号分隔
            res.append(combination)
        if len(path) == len(nums):  # 路径长度达到nums长度时退出
            return
    
        for i in range(index, len(nums)):  # 枚举数字
            path.append(nums[i])
            dfs(nums, i + 1, level, path, res)  # 递归搜索
            path.pop()
    
    def main():
        nums = input().split(',')  # 读取数字列表
        nums.sort()  # 排序
        level = int(input())  # 读取最小数字数量
    
        res = []
        path = []
        dfs(nums, 0, level, path, res)
    
        if res:
            for combination in res:
                print(combination)
        else:
            print("None")
    
    if __name__ == "__main__":
        main()
    
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    function dfs(nums, index, level, path, res) {
      if (path.length >= level) { // 当路径长度达到level时，记录路径
        let combination = "";
        for (let i = 0; i < path.length; i++) {
          if (i > 0) combination += ","; // 数字之间用逗号分隔
          combination += path[i];
        }
        res.push(combination);
      }
      if (path.length == nums.length) return; // 路径长度达到nums长度时退出
    
      for (let i = index; i < nums.length; i++) { // 枚举数字
        path.push(nums[i]);
        dfs(nums, i + 1, level, path, res); // 递归搜索
        path.pop();
      }
    }
    
    rl.on('line', (line) => {
      const nums = line.split(',').sort(); // 排序
      rl.once('line', (level) => {
        level = parseInt(level);
        const res = [];
        const path = [];
        dfs(nums, 0, level, path, res);
    
        if (res.length) {
          for (let i = 0; i < res.length; i++) {
            console.log(res[i]);
          }
        } else {
          console.log("None");
        }
    
        rl.close();
      });
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    void dfs(vector<string>& nums, int index, int level, vector<string>& path, vector<string>& res) {
        if (path.size() >= level) { // 当路径长度达到level时，记录路径
            string combination = "";
            for (int i = 0; i < path.size(); i++) {
                if (i > 0) combination += ","; // 数字之间用逗号分隔
                combination += path[i];
            }
            res.push_back(combination);
        }
        if (path.size() == nums.size()) return; // 路径长度达到nums长度时退出
    
        for (int i = index; i < nums.size(); i++) { // 枚举数字
            path.push_back(nums[i]);
            dfs(nums, i + 1, level, path, res); // 递归搜索
            path.pop_back();
        }
    }
    
    int main() {
        string line;
        getline(cin, line); // 读入数字列表
        int level;
        cin >> level; // 读入最小数字数量
    
        vector<string> nums;
        string delimiter = ",";
        size_t pos = 0;
        string token;
        while ((pos = line.find(delimiter)) != string::npos) { // 分割数字列表
            token = line.substr(0, pos);
            nums.push_back(token);
            line.erase(0, pos + delimiter.length());
        }
        nums.push_back(line);
        sort(nums.begin(), nums.end()); // 排序
    
        vector<string> res;
        vector<string> path;
        dfs(nums, 0, level, path, res);
    
        if (res.size()) {
            for (int i = 0; i < res.size(); i++) {
                cout << res[i] << endl;
            }
        } else {
            cout << "None" << endl;
        }
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    #define MAX_NUMS 100
    #define MAX_LENGTH 10
    
    void swap(char** a, char** b) {
        char* temp = *a;
        *a = *b;
        *b = temp;
    }
    
    int compare(const void* a, const void* b) {
        return strcmp(*(const char**)a, *(const char**)b);
    }
    
    void dfs(char* nums[], int num_size, int index, int level, char* path[], int path_size, char** res, int* res_size) {
        if (path_size >= level) { // 当路径长度达到level时，记录路径
            char* combination = malloc(MAX_NUMS * MAX_LENGTH * sizeof(char));
            combination[0] = '\0';
            for (int i = 0; i < path_size; i++) {
                if (i > 0) strcat(combination, ",");
                strcat(combination, path[i]);
            }
            res[*res_size] = combination;
            (*res_size)++;
        }
        if (path_size == num_size) return;
    
        for (int i = index; i < num_size; i++) { // 枚举数字
            path[path_size] = nums[i];
            dfs(nums, num_size, i + 1, level, path, path_size + 1, res, res_size);
        }
    }
    
    int main() {
        char line[1024];
        if (!fgets(line, 1024, stdin)) return 1;
        line[strcspn(line, "\n")] = 0; // Remove newline character
    
        int level;
        scanf("%d", &level);
    
        char* nums[MAX_NUMS];
        int num_size = 0;
        char* token = strtok(line, ",");
        while (token != NULL) {
            nums[num_size] = malloc((strlen(token) + 1) * sizeof(char));
            strcpy(nums[num_size], token);
            num_size++;
            token = strtok(NULL, ",");
        }
        qsort(nums, num_size, sizeof(char*), compare);
    
        char* path[MAX_NUMS];
        char* res[MAX_NUMS * MAX_NUMS];
        int res_size = 0;
        dfs(nums, num_size, 0, level, path, 0, res, &res_size);
    
        if (res_size > 0) {
            for (int i = 0; i < res_size; i++) {
                printf("%s\n", res[i]);
                free(res[i]);
            }
        } else {
            printf("None\n");
        }
    
        for (int i = 0; i < num_size; i++) {
            free(nums[i]);
        }
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

