## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定一个数组X和正整数K，请找出使表达式X[i] - x[i +1] … - X[i + K
1]，结果最接近于数组中位数的下标i，如果有多个i满足条件，请返回最大的i。  
其中，数组中位数:长度为N的数组，按照元素的值大小升序排列后，下标为N/2元素的值  
**补充说明:**

  1. 数组X的元素均为正整数;
  2. X的长度n取值范围: 2<= n <= 1000;
  3. K大于0且小于数组的大小;
  4. i的取值范围: 0 <=i < 1000;
  5. 题目的排序数组X[N]的中位数是X[N/2].

## 输入描述

无

## 输出描述

无

## 示例1

输入

    
    
    [50,50,2,3],2
    

输出

    
    
     1
    

说明

> 说明:  
>  1、中位数为50: [50,50,2,3]升序排序后变成[2,3,50,50]，中位数为下标4/2=2的元素50;  
>  2、计算结果为1: X[50,50,2,3]根据题目计算X[i] - …- X[i + K- 1]得出三个数  
>  0 (X[0]-X[1]= 50 -50) 、  
>  48 (X[1]-X[2] = 50 -2)  
>  -1 (X[2]-X[3]= 2-3) ，  
>  其中48最接近50，因此返回下标1

## 解题思路

这道题目要求我们找到一个数组中某个范围内的下标，使得该下标对应的计算结果最接近于数组的中位数。以下是题目的具体解释：

## 题目要点

  1. **输入与输出** :

     * 输入是一个数组 `X` 和一个正整数 `K`。
     * 输出是一个下标 `i`，该下标对应的计算结果最接近数组的中位数。
  2. **中位数的定义** :

     * 中位数是将数组元素按大小排序后，位于中间位置的元素。
     * 对于长度为 `N` 的数组，中位数是下标为 `N/2` 的元素（整除）。
  3. **计算表达式** :

     * 对于每个可能的下标 `i`，需要计算表达式：  
result = X [ i ] − X [ i \+ 1 ] − . . . − X [ i \+ K − 1 ] \text{result} =
X[i] - X[i+1] - ... - X[i+K-1] result=X[i]−X[i+1]−...−X[i+K−1]

     * 这个表达式计算的是从下标 `i` 开始的 `K` 个元素的差值。
  4. **寻找最接近中位数的结果** :

     * 对于每个计算出的结果，求出它与中位数的差的绝对值。
     * 找到差的绝对值最小的下标 `i`，如果有多个 `i`，则返回最大的 `i`。

## 示例分析

以示例 `X = [50, 50, 2, 3]` 和 `K = 2` 为例：

  1. **计算中位数** :

     * 排序后： `[2, 3, 50, 50]`，中位数为 `50`（下标为 `2` 的元素）。
  2. **计算结果** :

     * 对于 `i = 0`：  
result = X [ 0 ] − X [ 1 ] = 50 − 50 = 0 \text{result} = X[0] - X[1] = 50 - 50
= 0 result=X[0]−X[1]=50−50=0

     * 对于 `i = 1`：  
result = X [ 1 ] − X [ 2 ] = 50 − 2 = 48 \text{result} = X[1] - X[2] = 50 - 2
= 48 result=X[1]−X[2]=50−2=48

     * 对于 `i = 2`：  
result = X [ 2 ] − X [ 3 ] = 2 − 3 = − 1 \text{result} = X[2] - X[3] = 2 - 3 =
-1 result=X[2]−X[3]=2−3=−1

  3. **结果与中位数的比较** :

     * 计算结果 `0`、`48`、`-1` 与中位数 `50` 的差： 
       * `|0 - 50| = 50`
       * `|48 - 50| = 2`
       * `|-1 - 50| = 51`
     * `48` 是最接近 `50` 的，因此返回下标 `1`。

## Java

    
    
    import java.util.Arrays;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            String[] input_str = in.nextLine().replace("[","").replace("]","").split(",");
            int n = input_str.length - 1;
            int[] nums = new int[n];
            int k = Integer.valueOf(input_str[n]);
            for(int i=0; i<n; i++){
                nums[i] = Integer.valueOf(input_str[i]);
            }
    
            int[] sorted_nums = Arrays.copyOf(nums, n);
            Arrays.sort(sorted_nums);
            int median = sorted_nums[n/2];  // 计算中位数
    
            int minDiff = Integer.MAX_VALUE;  // 初始化最小差值为最大整数
            int result = -1;  // 初始化结果为-1
            for(int i=0; i<=n-k; i++){  // 遍历数组
                int count = nums[i];  // 初始化计数器为当前元素
                for(int j=i+1; j<i+k; j++){  // 计算表达式X[i] - x[i +1] ... - X[i + K  1]
                    count -= nums[j];
                }
                int diff = Math.abs(count - median);  // 计算当前差值
                if(diff < minDiff){  // 如果当前差值小于最小差值
                    minDiff = diff;  // 更新最小差值
                    result = i;  // 更新结果为当前下标
                } else if (diff == minDiff) {  // 如果当前差值等于最小差值
                    result = Math.max(result, i);  // 更新结果为最大的下标
                }
            }
    
            System.out.println(result);  // 输出结果
        }
    }
    

## Python

    
    
    input_str = input().replace("[", "").replace("]", "").split(",")
    
    # 计算输入数组的长度，n是数组的元素数量，最后一个元素为K
    n = len(input_str) - 1
    
    # 将前n个元素转换为整数，构建整数数组nums
    nums = [int(input_str[i]) for i in range(n)]
    
    # 将最后一个元素转换为整数，作为K的值
    k = int(input_str[n])
    
    # 创建nums的副本，并对副本进行排序以计算中位数
    sorted_nums = nums.copy()
    sorted_nums.sort()
    
    # 计算中位数：排序后下标为n//2的元素
    median = sorted_nums[n // 2]
    
    # 初始化最小差值为正无穷大，结果下标初始化为-1
    minDiff = float('inf')
    result = -1
    
    # 遍历所有可能的起始下标i，范围为0到n-k
    for i in range(n - k + 1):
        count = nums[i]  # 初始化count为当前下标的元素
        # 计算从i到i+k-1的元素的差值
        for j in range(i + 1, i + k):
            count -= nums[j]  # 依次减去下标j对应的元素
    
        # 计算当前count与中位数之间的绝对差值
        diff = abs(count - median)
    
        # 如果当前差值小于已知最小差值，则更新最小差值和结果下标
        if diff < minDiff:
            minDiff = diff
            result = i
        # 如果当前差值等于已知最小差值，则更新结果下标为较大的那个
        elif diff == minDiff:
            result = max(result, i)
    
    # 输出最终结果下标
    print(result)
    

## JavaScript

    
    
    const readline = require('readline');
    
    // 创建readline接口，设置输入输出流
    const rl = readline.createInterface({
      input: process.stdin,  
      output: process.stdout  
    });
    
    // 监听每一行输入
    rl.on('line', (input_str) => {
      // 移除输入字符串中的方括号
      input_str = input_str.replace("[", "").replace("]", "");
      
      // 将输入字符串按逗号分割，并转换为数字数组
      const input_arr = input_str.split(",").map(Number);
      
      // n是数组的长度减1（最后一个元素是K）
      const n = input_arr.length - 1;
      
      // nums数组包含前n个元素
      const nums = input_arr.slice(0, n);
      
      // k是数组中的最后一个元素，表示要计算的元素个数
      const k = input_arr[n];
    
      // 创建nums的副本并进行排序以计算中位数
      const sorted_nums = [...nums].sort((a, b) => a - b);
      
      // 计算中位数：排序后的中间元素
      const median = sorted_nums[Math.floor(n / 2)];
    
      // 初始化最小差值为JavaScript的安全整数最大值
      let minDiff = Number.MAX_SAFE_INTEGER;
      
      // 初始化结果下标为-1
      let result = -1;
      
      // 遍历所有可能的起始下标i，范围从0到n-k
      for (let i = 0; i <= n - k; i++) {
        let count = nums[i];  // 初始化count为当前下标的元素
        
        // 计算从i到i+k-1的元素差值
        for (let j = i + 1; j < i + k; j++) {
          count -= nums[j];  // 依次减去下标j对应的元素
        }
        
        // 计算当前count与中位数之间的绝对差值
        const diff = Math.abs(count - median);
        
        // 如果当前差值小于已知最小差值，则更新最小差值和结果下标
        if (diff < minDiff) {
          minDiff = diff;
          result = i;  // 更新结果下标为当前下标i
        } 
        // 如果当前差值等于已知最小差值，则更新结果下标为较大的那个
        else if (diff === minDiff) {
          result = Math.max(result, i);  // 保留较大的下标
        }
      }
    
      // 输出最终结果下标
      console.log(result);
      
      // 关闭readline接口
      rl.close();
    });
    

## C++

    
    
    #include <iostream>   
    #include <vector>     
    #include <algorithm>  
    #include <climits>   
    #include <sstream>   
    using namespace std;
    
    int main() {
        string input_str;   
        getline(cin, input_str);   
    
        // 移除字符串中的方括号 '[' 和 ']'
        input_str.erase(remove(input_str.begin(), input_str.end(), '['), input_str.end());
        input_str.erase(remove(input_str.begin(), input_str.end(), ']'), input_str.end());
    
        vector<string> input_vec;  // 声明一个字符串向量用于存储分割后的输入
        size_t pos = 0;  // 声明一个位置变量，用于查找逗号
        string token;    // 声明一个临时字符串，用于存储每个分割出的部分
    
        // 循环查找并分割字符串
        while ((pos = input_str.find(",")) != string::npos) {  // 找到逗号位置
            token = input_str.substr(0, pos);  // 获取逗号前的子字符串
            input_vec.push_back(token);  // 将子字符串添加到向量中
            input_str.erase(0, pos + 1);  // 移除已处理的部分
        }
        input_vec.push_back(input_str);  // 添加最后一个元素
    
        int n = input_vec.size() - 1;  // 计算有效元素的数量（最后一个元素是K）
        vector<int> nums;  // 声明一个整型向量用于存储数字
        for (int i = 0; i < n; i++) {
            nums.push_back(stoi(input_vec[i]));  // 将字符串转换为整数并添加到nums中
        }
        int k = stoi(input_vec[n]);  // 将最后一个元素转换为整数，作为K的值
    
        // 创建nums的副本并进行排序以计算中位数
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        int median = sorted_nums[n / 2];  // 计算中位数
    
        int minDiff = INT_MAX;  // 初始化最小差值为整数的最大值
        int result = -1;  // 初始化结果下标为-1
    
        // 遍历所有可能的起始下标i，范围从0到n-k
        for (int i = 0; i <= n - k; i++) {
            int count = nums[i];  // 初始化count为当前下标的元素
            
            // 计算从i到i+k-1的元素差值
            for (int j = i + 1; j < i + k; j++) {
                count -= nums[j];  // 依次减去下标j对应的元素
            }
            
            int diff = abs(count - median);  // 计算当前count与中位数之间的绝对差值
            
            // 如果当前差值小于已知最小差值，则更新最小差值和结果下标
            if (diff < minDiff) {
                minDiff = diff;
                result = i;  // 更新结果下标为当前下标i
            } 
            // 如果当前差值等于已知最小差值，则更新结果下标为较大的那个
            else if (diff == minDiff) {
                result = max(result, i);  // 保留较大的下标
            }
        }
    
        cout << result << endl;  // 输出最终结果下标
    
        return 0;  // 返回0，表示程序正常结束
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <limits.h>
    
    int compare(const void *a, const void *b) {
        return (*(int *)a - *(int *)b);  // 排序比较函数
    }
    
    int main() {
        char input_str[1000];  // 声明输入字符串
        fgets(input_str, sizeof(input_str), stdin);  // 读取一行输入
    
        // 去掉字符串中的方括号 '[' 和 ']'
        char *ptr = strchr(input_str, '[');
        while (ptr) {
            memmove(ptr, ptr + 1, strlen(ptr));  // 移除'['
            ptr = strchr(input_str, '[');
        }
        ptr = strchr(input_str, ']');
        while (ptr) {
            memmove(ptr, ptr + 1, strlen(ptr));  // 移除']'
            ptr = strchr(input_str, ']');
        }
    
        // 分割输入字符串
        int nums[100];  // 假设最大长度为100
        int n = 0, k = 0;
        char *token = strtok(input_str, ",");
        while (token) {
            if (token[0] != '\0') {
                if (n < 100) {
                    nums[n++] = atoi(token);  // 转换为整数并存入数组
                }
            }
            token = strtok(NULL, ",");
        }
        k = nums[n - 1];  // K的值是最后一个元素
        n--;  // 调整有效元素数量
    
        // 复制并排序数组以计算中位数
        int sorted_nums[100];
        memcpy(sorted_nums, nums, n * sizeof(int));
        qsort(sorted_nums, n, sizeof(int), compare);
        int median = sorted_nums[n / 2];  // 计算中位数
    
        int minDiff = INT_MAX;  // 初始化最小差值为最大整数
        int result = -1;  // 初始化结果为-1
    
        // 遍历数组
        for (int i = 0; i <= n - k; i++) {
            int count = nums[i];  // 初始化计数器为当前元素
            for (int j = i + 1; j < i + k; j++) {
                count -= nums[j];  // 计算当前表达式的值
            }
            int diff = abs(count - median);  // 计算当前差值
            if (diff < minDiff) {  // 如果当前差值小于最小差值
                minDiff = diff;  // 更新最小差值
                result = i;  // 更新结果为当前下标
            } else if (diff == minDiff) {  // 如果当前差值等于最小差值
                result = (result > i) ? result : i;  // 更新结果为最大的下标
            }
        }
    
        printf("%d\n", result);  // 输出结果
        return 0;  // 返回0，表示程序正常结束
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/52cdacecaa3903c21e49e1d8f9855591.png)

## 完整用例

### 用例1

    
    
    [50,50,2,3],2
    

### 用例2

    
    
    [1,2,3,4,5],2
    

### 用例3

    
    
    [10,20,30,40,50],3
    

### 用例4

    
    
    [100,200,300,400,500],4
    

### 用例5

    
    
    [5,10,15,20,25],2
    

### 用例6

    
    
    [1,2,3,4,5,6,7,8,9,10],4
    

### 用例7

    
    
    [1,3,5,7,9],2
    

### 用例8

    
    
    [1,1,1,1,1,1,1,1,1,1,1],3
    

### 用例9

    
    
    [9,8,7,6,5,4,3,2,1],3
    

### 用例10

    
    
    [5,5,5,5,5],2
    

